# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "dnspython>=2.6",
# ]
# ///
"""
DNS / auth audit — execute step.

Checks every sending domain against the four records the skill requires
(reference.md §6) plus two defects the manual Notion workflow kept missing:
an over-budget SPF chain, and stray Lync/Skype SRV records copy-pasted from
the Microsoft 365 setup guide.

Read-only. Queries public DNS only. Touches nothing at any provider.

Usage:
    uv run execute.py acme.com acmehq.com
    uv run execute.py --file domains.txt
    uv run execute.py --file domains.txt --csv dns_audit.csv

Exit code: 0 = no FAIL, 2 = at least one FAIL (usable as a launch gate).
"""

import argparse
import csv
import sys

import dns.resolver

# ── Configuration ────────────────────────────────────────────────

RESOLVER = dns.resolver.Resolver()
RESOLVER.lifetime = RESOLVER.timeout = 6.0

# Google, Microsoft, and common vendor DKIM selectors.
SELECTORS = [
    "google", "selector1", "selector2", "default", "k1", "s1", "s2",
    "mail", "dkim", "smtp", "key1", "em", "mandrill", "zoho",
]

SPF_LOOKUP_LIMIT = 10          # RFC 7208 §4.6.4
GT_DMARC_STANDARD = "reject"   # reference.md §6

ICON = {"PASS": "  [PASS]", "WARN": "  [WARN]", "FAIL": "  [FAIL]"}


# ── Helpers ──────────────────────────────────────────────────────

def q(name, rtype):
    """Query DNS, returning a list of unquoted strings. Never raises."""
    try:
        return [
            r.to_text().strip('"').replace('" "', "")
            for r in RESOLVER.resolve(name, rtype)
        ]
    except Exception:
        return []


def spf_lookups(record, depth=0, seen=None):
    """Count DNS-lookup-consuming mechanisms per RFC 7208. Limit is 10."""
    if seen is None:
        seen = set()
    if depth > 5:
        return 0
    n = 0
    for tok in record.split():
        t = tok.lower()
        if t.startswith(("include:", "redirect=")):
            n += 1
            tgt = t.split(":", 1)[-1] if t.startswith("include:") else t.split("=", 1)[-1]
            if tgt not in seen:
                seen.add(tgt)
                for sub in q(tgt, "TXT"):
                    if sub.startswith("v=spf1"):
                        n += spf_lookups(sub, depth + 1, seen)
        elif t in ("a", "mx", "ptr") or t.startswith(("a:", "mx:", "ptr:", "exists:")):
            n += 1
    return n


def classify_mx(mx_records):
    """Map MX hostnames to a sending/receiving provider (PR #29 logic)."""
    j = " ".join(mx_records).lower()
    if "google" in j:
        return "Google"
    if "outlook" in j or "protection.outlook" in j:
        return "Microsoft"
    if "mimecast" in j:
        return "Mimecast (SEG)"
    if "pphosted" in j or "ppe-hosted" in j:
        return "Proofpoint (SEG)"
    if "barracuda" in j:
        return "Barracuda (SEG)"
    if "zoho" in j:
        return "Zoho"
    return "Other/unknown"


# ── Audit ────────────────────────────────────────────────────────

def audit(domain):
    rows = []

    def row(dim, verdict, detail):
        rows.append((dim, verdict, detail))

    # MX + provider classification
    mx = q(domain, "MX")
    if not mx:
        row("MX", "FAIL", "no MX record — domain cannot receive mail")
        provider = "none"
    else:
        provider = classify_mx(mx)
        row("MX", "PASS", f"{len(mx)} record(s) -> {provider}")

    # SPF: exactly one record, inside the lookup budget
    spf = [t for t in q(domain, "TXT") if t.lower().startswith("v=spf1")]
    if len(spf) == 0:
        row("SPF", "FAIL", "no SPF record")
    elif len(spf) > 1:
        row("SPF", "FAIL", f"{len(spf)} SPF records — RFC allows exactly 1, both are ignored")
    else:
        n = spf_lookups(spf[0])
        verdict = "PASS" if n <= SPF_LOOKUP_LIMIT else "FAIL"
        row("SPF", verdict, f"1 record, {n}/{SPF_LOOKUP_LIMIT} DNS lookups | {spf[0][:70]}")

    # DKIM across known selectors
    found = []
    for s in SELECTORS:
        hit = False
        for rec in q(f"{s}._domainkey.{domain}", "TXT"):
            if "v=dkim1" in rec.lower() or "p=" in rec:
                found.append(s)
                hit = True
                break
        if not hit and q(f"{s}._domainkey.{domain}", "CNAME"):
            found.append(f"{s}(CNAME)")
    if found:
        row("DKIM", "PASS", f"selector(s): {', '.join(found)}")
    else:
        row("DKIM", "WARN",
            f"no DKIM on {len(SELECTORS)} known selectors — may use a custom one, verify in the provider UI")

    # DMARC + policy strength against the GT standard
    dm = [t for t in q("_dmarc." + domain, "TXT") if t.lower().startswith("v=dmarc1")]
    if not dm:
        row("DMARC", "FAIL", "no DMARC record")
    else:
        pol = next(
            (p.split("=", 1)[1].strip() for p in dm[0].split(";") if p.strip().startswith("p=")),
            "?",
        )
        if pol == GT_DMARC_STANDARD:
            row("DMARC", "PASS", f"p={pol} (GT standard)")
        elif pol in ("none", "quarantine"):
            row("DMARC", "WARN",
                f"p={pol} — GT standard is p=reject; p=none is a short verification phase only")
        else:
            row("DMARC", "FAIL", f"unparseable policy: {dm[0][:60]}")

    # Stray Lync/Skype SRV — copy-pasted from the M365 setup guide, never needed for cold email
    lync = q("_sip._tls." + domain, "SRV") + q("_sipfederationtls._tcp." + domain, "SRV")
    row("SRV-hygiene", "FAIL" if lync else "PASS",
        f"stray Lync/Skype SRV present: {lync}" if lync else "no stray Lync/Skype SRV")

    return provider, rows


# ── Main ─────────────────────────────────────────────────────────

def main():
    ap = argparse.ArgumentParser(description="Audit MX/SPF/DKIM/DMARC/SRV for sending domains.")
    ap.add_argument("domains", nargs="*", help="Domains to audit")
    ap.add_argument("--file", help="Text file with one domain per line")
    ap.add_argument("--csv", default="dns_audit.csv", help="CSV audit trail (default: dns_audit.csv)")
    args = ap.parse_args()

    domains = list(args.domains)
    if args.file:
        with open(args.file) as fh:
            domains += [ln.strip() for ln in fh if ln.strip() and not ln.startswith("#")]
    if not domains:
        ap.error("no domains given — pass them as arguments or with --file")

    print("=" * 68)
    print("DNS / AUTH AUDIT")
    print(f"{len(domains)} domain(s) · read-only · public DNS only")
    print("=" * 68)

    out_rows = []
    worst = 0
    totals = {"PASS": 0, "WARN": 0, "FAIL": 0}

    for d in domains:
        provider, rows = audit(d)
        fails = sum(1 for _, v, _ in rows if v == "FAIL")
        warns = sum(1 for _, v, _ in rows if v == "WARN")
        flag = "FAIL" if fails else ("WARN" if warns else "PASS")
        totals[flag] += 1

        print(f"\n[{flag}]  {d}   [{provider}]")
        for dim, v, detail in rows:
            print(f"{ICON[v]} {dim:12} {detail}")
            out_rows.append({"domain": d, "provider": provider,
                             "dimension": dim, "verdict": v, "detail": detail})

        worst = max(worst, 2 if fails else 1 if warns else 0)

    with open(args.csv, "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["domain", "provider", "dimension", "verdict", "detail"])
        w.writeheader()
        w.writerows(out_rows)

    print("\n" + "=" * 68)
    print(f"SUMMARY: {totals['PASS']} pass · {totals['WARN']} warn · {totals['FAIL']} fail")
    print(f"Audit trail: {args.csv}")
    if totals["FAIL"]:
        print("A FAIL on MX, SPF or DMARC is launch-blocking. Fix before going live.")
    print("=" * 68)

    sys.exit(2 if worst == 2 else 0)


if __name__ == "__main__":
    main()

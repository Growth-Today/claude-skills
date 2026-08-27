# /// script
# requires-python = ">=3.10"
# dependencies = ["dnspython"]
# ///
"""
Gate tests for execute.py — no network.

Every case stubs DNS and asserts what the launch gate does with it. Run this
after any change to the verdict logic. The point is that "the script ran and
printed something reasonable" is not evidence; these are.

    uv run test_gate.py
"""

import sys
import execute

CLEAN = {
    ("d.test", "MX"): (["10 aspmx.l.google.com."], "ok"),
    ("d.test", "TXT"): (["v=spf1 include:_spf.google.com ~all"], "ok"),
    ("google._domainkey.d.test", "TXT"): (["v=DKIM1; k=rsa; p=MIIBIjANBg"], "ok"),
    ("_dmarc.d.test", "TXT"): (["v=DMARC1; p=reject; rua=mailto:x@d.test"], "ok"),
}

CASES = [
    ("clean domain", {}, "PASS", 0),
    ("DMARC p=quarantine",
     {("_dmarc.d.test", "TXT"): (["v=DMARC1; p=quarantine"], "ok")}, "WARN", 2),
    ("DMARC missing",
     {("_dmarc.d.test", "TXT"): ([], "empty")}, "FAIL", 2),
    ("DKIM missing",
     {("google._domainkey.d.test", "TXT"): ([], "empty")}, "FAIL", 2),
    ("DKIM revoked (empty p=)",
     {("google._domainkey.d.test", "TXT"): (["v=DKIM1; k=rsa; p="], "ok")}, "FAIL", 2),
    ("null MX",
     {("d.test", "MX"): (["0 ."], "ok")}, "FAIL", 2),
    ("no MX", {("d.test", "MX"): ([], "empty")}, "FAIL", 2),
    ("two SPF records",
     {("d.test", "TXT"): (["v=spf1 a ~all", "v=spf1 mx ~all"], "ok")}, "FAIL", 2),
    ("TXT lookup timed out",
     {("d.test", "TXT"): ([], "error")}, "FAIL", 2),
    ("stray Lync SRV only",
     {("_sip._tls.d.test", "SRV"): (["0 0 443 sipdir.online.lync.com."], "ok")}, "WARN", 0),
]


def run(case_overrides):
    table = dict(CLEAN)
    table.update(case_overrides)
    execute.q_status = lambda n, rt: table.get((n, rt), ([], "empty"))
    execute.q = lambda n, rt: execute.q_status(n, rt)[0]

    _, rows = execute.audit("d.test")
    fails = any(v == "FAIL" for _, v, _ in rows)
    warns = any(v == "WARN" for _, v, _ in rows)
    blocked = any(dim in execute.BLOCKING and v != "PASS" for dim, v, _ in rows)
    flag = "FAIL" if fails else ("WARN" if warns else "PASS")
    return flag, (2 if (fails or blocked) else 0)


def main():
    bad = 0
    print(f"{'case':<28} {'verdict':<8} {'exit':<5} result")
    print("-" * 60)
    for name, overrides, want_flag, want_exit in CASES:
        flag, code = run(overrides)
        ok = (flag, code) == (want_flag, want_exit)
        bad += not ok
        print(f"{name:<28} {flag:<8} {code:<5} "
              f"{'ok' if ok else f'FAILED (wanted {want_flag}/{want_exit})'}")
    print("-" * 60)
    print(f"{len(CASES) - bad}/{len(CASES)} passed")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

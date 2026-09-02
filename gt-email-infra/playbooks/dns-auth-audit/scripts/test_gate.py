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


def lockstep():
    """The Python MX table and the Clay formula must classify the same providers.

    They are maintained in two places by two different people. Diffing them here
    is cheaper than finding out from a client's routing.
    """
    import re
    from pathlib import Path

    clay_file = (Path(__file__).resolve().parents[3]
                 / ".claude" / "skills" / "campaign-building" / "gt-SKILL.md")
    text = clay_file.read_text()
    block = text.split("A null MX")[1].split("```")[0]
    clay = [n for n in re.findall(r'\?\s*"([a-z-]+)"', block)
            if n not in ("other", "no-email")]
    py = [n for n, _, _ in execute.MX_PROVIDERS]

    missing_clay = [n for n in py if n not in clay]
    missing_py = [n for n in clay if n not in py]
    ok = not missing_clay and not missing_py
    print(f"\nMX provider lockstep: python {len(py)} · clay {len(clay)} · "
          f"{'in step' if ok else f'DIVERGED (clay missing {missing_clay}, python missing {missing_py})'}")
    return ok


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
    if not lockstep():
        bad += 1
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())

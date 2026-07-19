#!/usr/bin/env python3
"""Fail when the public organization policy drifts from canonical routes/copy."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
profile = (ROOT / "profile" / "README.md").read_text(encoding="utf-8")
support = (ROOT / "SUPPORT.md").read_text(encoding="utf-8")
security = (ROOT / "SECURITY.md").read_text(encoding="utf-8")
readme = (ROOT / "README.md").read_text(encoding="utf-8")

required = {
    "profile support route": (profile, "https://veripsa.com/support"),
    "profile security route": (profile, "https://veripsa.com/security/disclosure"),
    "support no-SLA wording": (support, "does not offer a contractual support SLA today"),
    "support target wording": (support, "within a few business days"),
    "security subject prefix": (security, "[SECURITY]"),
    "license index entry": (readme, "[`LICENSE`](./LICENSE)"),
}
for label, (body, needle) in required.items():
    if needle not in body:
        raise SystemExit(f"missing invariant: {label}: {needle!r}")

for forbidden in (
    "domain%20verified",
    "img.shields.io/badge/status-",
    "within **2 business days**",
    "[security]",
):
    corpus = "\n".join((profile, support, security))
    if forbidden in corpus:
        raise SystemExit(f"stale or self-asserted public claim remains: {forbidden!r}")

print("public organization policy invariants verified")

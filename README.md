> **STAGING — not yet published.** This directory holds the content that will become the public **GetVeripsa/.github** repository. GitHub surfaces files from an org's `.github` repository as the **org-wide default** (for example, `SECURITY.md` is shown on every GetVeripsa repo that doesn't ship its own). Review here first; publish later.

# GetVeripsa/.github (planned public repository)

This repo will hold the **org-level GitHub configuration** for the [GetVeripsa](https://github.com/GetVeripsa) organization — security policy, code of conduct, support pointers, and the org profile README.

It **does not contain product code.** Veripsa's product (the Core App and the platform) lives in private repositories.

## What goes here

| File | Purpose |
| --- | --- |
| `SECURITY.md` | Org-default security policy. How to report a vulnerability, expected response time, scope. |
| `CODE_OF_CONDUCT.md` | Org-default code of conduct (Contributor Covenant 2.1). |
| `SUPPORT.md` | Where users go for help. Points to `veripsa.com/support` and `/docs`. |
| `FUNDING.yml` | Explicit "no funding links" — Veripsa does not accept donations or sponsorship. Comments only; no entries. |
| `profile/README.md` | The org profile README rendered at `github.com/GetVeripsa`. |

## How GitHub uses these files

When a repository in the GetVeripsa org **does not** ship its own `SECURITY.md` / `CODE_OF_CONDUCT.md` / `SUPPORT.md`, GitHub will show the one from this `.github` repository instead. The `profile/README.md` is rendered on the organization's landing page.

## Publishing checklist (for the PO)

1. Create the public repo `GetVeripsa/.github` on GitHub.
2. Copy the files in this directory (except this `README.md`) into the root of that repo.
3. Verify by opening any GetVeripsa repo's **Security** tab — the policy should appear.
4. Verify the org page at `https://github.com/GetVeripsa` shows the profile README.

## Honesty rules these files follow

- No "100%", "guarantees", "prevents", "always", "never misses".
- No internal mechanism details, no roadmap claims, no engine internals.
- Customer / metric claims: none. Honest empty states only.
- `support@veripsa.com` is the single contact. Security reports go to the same address with subject prefix `[SECURITY]`; conduct reports use `[CONDUCT]`. We can split into dedicated addresses once volume warrants it.

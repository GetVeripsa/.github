# Veripsa

[![veripsa.com](https://img.shields.io/badge/veripsa.com-domain%20verified-blue)](https://veripsa.com)
[![Made in Japan](https://img.shields.io/badge/made%20in-Japan-red)](https://veripsa.com)
[![License: MIT (public assets)](https://img.shields.io/badge/license-MIT%20(public%20assets)-green)](https://github.com/GetVeripsa/veripsa-changelog/blob/main/LICENSE)
[![Status](https://img.shields.io/badge/status-veripsa.com%2Fstatus-lightgrey)](https://veripsa.com/status)

**Pre-merge cross-PR collision control.** When several pull requests are open at once — especially with AI coding agents and people working the same repository in parallel — changes that look independent can collide on `main`. Git surfaces only *textual* conflicts, and only at merge time. Veripsa compares the open PRs against each other and against `main` **before anyone merges**, looking past filenames at how the pieces of the repository actually relate.

Veripsa is **one GitHub App**. Install it on a repository and it posts a check run and a single PR comment on every PR push. There is no per-agent setup; the same install covers humans and AI coding agents alike. **Advisory by default** — your branch-protection policy decides what's required to merge.

## Try Veripsa Core in 10 minutes

→ **<https://veripsa.com/try>** — the guided walkthrough: install on a test repo, open two PRs that touch the same call path, and see the check run and the PR comment land before either one merges.

## What it is, honestly

- **Advisory by default.** Veripsa posts a check and a comment; your branch-protection policy decides what's required.
- **Acknowledging is not an approval.** When a material coupling is flagged, the `veripsa-ack` label records that someone *saw* the specific coupling and chose to proceed deliberately. Veripsa does not assert your change is correct. Reviewers and CI still decide what merges.
- **Pre-merge, cross-PR.** Looks at the set of open PRs together, not just the current one.
- **Structural, not filename.** Reasons about the repository as a whole — so it can surface coupling a folder heuristic and Git both miss.
- **Content-free.** Only paths, symbol names, line ranges, edges, and counts cross the wire. Source files do not.

## What it is not

- Not a merge queue.
- Not an AI code reviewer.
- Not a replacement for tests, CI, or branch protection.

## Honest scope today

- **Within-repo, same-branch coordination only.** Cross-repo / within-org coordination is on the roadmap and not a shipped claim.
- **Same-owner only.** All coordinated PRs must be on a repository owned by the installing GitHub account.
- **Branch-protection gating requires a paid GitHub plan** on private repositories. On free private repos, Veripsa stays advisory.
- **Language coverage varies.** The percentage of PR file paths the extractor recognizes is reported per installation.
- **No customer case studies yet.** Effect claims (rework hours saved, cycle-time impact) require a deployed A/B over real PRs over time; that evidence does not exist yet.

## Featured projects

The Veripsa product lives in private repositories. The public repos here are the surfaces integrators and reviewers need.

| Repo | What it is |
| --- | --- |
| [`veripsa-changelog`](https://github.com/GetVeripsa/veripsa-changelog) | User-visible changes to Veripsa Core, grouped by date. |
| [`veripsa-webhook-spec`](https://github.com/GetVeripsa/veripsa-webhook-spec) | The integration contract — which GitHub events the App subscribes to, the shape of the check run and PR comment, and the semantics of the `veripsa-ack` label. |
| [`.github`](https://github.com/GetVeripsa/.github) | Org-wide GitHub defaults — security policy, code of conduct, support pointers, and this profile. |

## Recent improvements

→ **<https://veripsa.com/whats-new>** — what changed in the last few weeks, in plain English. The dated entries are in the [`veripsa-changelog`](https://github.com/GetVeripsa/veripsa-changelog) repo.

## Get started

- **Install** the Veripsa Core App on GitHub. The free tier covers public repos and small private repos; no account required to start.
- **Docs:** <https://veripsa.com/docs>
- **Pricing:** <https://veripsa.com>
- **Status:** <https://veripsa.com/status>
- **Trust Center:** <https://veripsa.com/trust>
- **Security disclosure:** <https://veripsa.com/security/disclosure>

## This organization

- **GetVeripsa** is the organization that publishes the Veripsa Core GitHub App.
- Product code is in private repositories. The public surface here is the App listing and the three repos above.
- For support: <https://veripsa.com/support> or **support@veripsa.com**.
- For vulnerability reports: see [SECURITY.md](https://github.com/GetVeripsa/.github/blob/main/SECURITY.md) or the canonical process at <https://veripsa.com/security/disclosure>.

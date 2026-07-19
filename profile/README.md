# Veripsa

[![veripsa.com](https://img.shields.io/badge/veripsa.com-domain%20verified-blue)](https://veripsa.com)
[![Made in Japan](https://img.shields.io/badge/made%20in-Japan-red)](https://veripsa.com)
[![Status](https://img.shields.io/badge/status-veripsa.com%2Fstatus-lightgrey)](https://veripsa.com/status)

**GitHub-native pre-merge traffic control for parallel coding agents.** Veripsa
helps teams notice when open pull requests may need a safer landing order
before `main` changes.

Install Veripsa Core once as a GitHub App. It keeps a native GitHub check—and,
when useful, at most one managed PR comment—current automatically; humans and
agents use the same repository installation. Veripsa is advisory by default—
your branch-protection policy decides what is required to merge.

## Start here

| Need | Link |
| --- | --- |
| Try the guided demo | <https://veripsa.com/try> |
| Understand the product | <https://veripsa.com/how-it-works> |
| Product docs | <https://veripsa.com/docs> |
| Data handling and trust | <https://veripsa.com/trust> |
| Recent improvements | <https://veripsa.com/whats-new> |
| Service status | <https://veripsa.com/status> |

## Public repositories

There are three intentional public surfaces:

| Repository | Purpose |
| --- | --- |
| [`veripsa-webhook-spec`](https://github.com/GetVeripsa/veripsa-webhook-spec) | Public integration contract, permissions/events, output schemas, ACK semantics, and data handling. |
| [`ai-pr-collision-lab`](https://github.com/GetVeripsa/ai-pr-collision-lab) | Small maintained repository for trying a two-PR landing-order scenario. |
| [`.github`](https://github.com/GetVeripsa/.github) | Organization profile, security policy, support routes, and canonical links. |

The Core engine and hosted platform remain private. The public surfaces explain
what data crosses the boundary and what users can observe, not how Veripsa
decides internally.

## Product boundaries

- Veripsa is not a merge queue or an AI code reviewer.
- It does not replace tests, CI, branch protection, or human review.
- Source file and diff bodies are not retained or displayed by Veripsa Core.
- Today coordination is within one repository; cross-repository coordination
  is not a current product claim.

Support: <https://veripsa.com/support>
Security reports: <https://veripsa.com/security/disclosure>

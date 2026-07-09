# Veripsa

[![veripsa.com](https://img.shields.io/badge/veripsa.com-domain%20verified-blue)](https://veripsa.com)
[![Made in Japan](https://img.shields.io/badge/made%20in-Japan-red)](https://veripsa.com)
[![License: MIT (public assets)](https://img.shields.io/badge/license-MIT%20(public%20assets)-green)](https://github.com/GetVeripsa/veripsa-changelog/blob/main/LICENSE)
[![Status](https://img.shields.io/badge/status-veripsa.com%2Fstatus-lightgrey)](https://veripsa.com/status)

**GitHub-native pre-merge traffic control for AI coding agents.** Veripsa helps teams notice when open pull requests may need a safer landing order before `main` changes.

Veripsa Core is a GitHub App. Install it on a repository and it posts a check run plus a PR comment on covered pull requests. There is no per-agent setup; the same install covers humans and AI coding agents alike. It is **advisory by default** — your branch-protection policy decides what is required to merge.

## Start here

| Need | Link |
| --- | --- |
| Try the product without risking your own repo | <https://veripsa.com/try> |
| Understand the product in plain English | <https://veripsa.com/how-it-works> |
| Decide whether it fits your team | <https://veripsa.com/fit> |
| Docs | <https://veripsa.com/docs> |
| Share / quote Veripsa safely | <https://veripsa.com/share> |
| 日本語の共有キット | <https://veripsa.com/ja/share> |
| Status | <https://veripsa.com/status> |
| Trust Center | <https://veripsa.com/trust> |
| GitHub discovery index | [`DISCOVERY.md`](https://github.com/GetVeripsa/.github/blob/main/DISCOVERY.md) |

## What it is, honestly

- **Pre-merge traffic control.** Veripsa gives teams a warning before a risky landing order turns into a `main` problem.
- **Built for parallel AI-agent work.** Humans and AI coding agents can be active in the same repository without each agent needing a separate setup.
- **Advisory by default.** Veripsa posts a check and a comment; your branch-protection policy decides what is required.
- **Content-free by design.** Source file bodies are not stored or displayed. Veripsa is not a code-review surface.
- **GitHub-native.** The experience lives where teams already make merge decisions: pull requests, checks, labels, and branch protection.

## What it is not

- Not a merge queue.
- Not an AI code reviewer.
- Not a replacement for tests, CI, branch protection, or human review.
- Not a guarantee that every conflict or defect disappears.

## Featured public repos

The Veripsa product code lives in private repositories. The public repos here are the surfaces integrators, reviewers, and curators need.

| Repo | What it is |
| --- | --- |
| [`veripsa-changelog`](https://github.com/GetVeripsa/veripsa-changelog) | User-visible changes to Veripsa Core, grouped by date. |
| [`veripsa-webhook-spec`](https://github.com/GetVeripsa/veripsa-webhook-spec) | Public integration notes for GitHub events, check output, and `veripsa-ack`. |
| [`veripsa-roadmap`](https://github.com/GetVeripsa/veripsa-roadmap) | Public roadmap notes and scope boundaries. |
| [`veripsa-examples`](https://github.com/GetVeripsa/veripsa-examples) | Example material for understanding Veripsa in small repos. |
| [`ai-pr-collision-lab`](https://github.com/GetVeripsa/ai-pr-collision-lab) | Small public lab for AI-agent PR collision examples. |
| [`.github`](https://github.com/GetVeripsa/.github) | Org-wide GitHub defaults, security policy, support pointers, and this profile. |

## Feeds and discovery

- GitHub discovery index: [`DISCOVERY.md`](https://github.com/GetVeripsa/.github/blob/main/DISCOVERY.md)
- Blog RSS: <https://veripsa.com/blog/feed.xml>
- Blog JSON Feed: <https://veripsa.com/blog/feed.json>
- LLM discovery file: <https://veripsa.com/llms.txt>
- Recent improvements: <https://veripsa.com/whats-new>
- Share kit: <https://veripsa.com/share>
- Japanese share kit: <https://veripsa.com/ja/share>

## Get started

- **Install** the Veripsa Core App on GitHub. Free access covers public repos and small private repos; no credit card is required to start.
- **Docs:** <https://veripsa.com/docs>
- **Fit check:** <https://veripsa.com/fit>
- **Pricing / free access:** <https://veripsa.com/pricing>
- **Security disclosure:** <https://veripsa.com/security/disclosure>

## This organization

- **GetVeripsa** publishes the Veripsa Core GitHub App and public review/discovery materials.
- Product code is private. Public repositories are intentionally scoped to trust, docs, examples, changelog, and integration notes.
- For support: <https://veripsa.com/support> or **support@veripsa.com**.
- For vulnerability reports: see [SECURITY.md](https://github.com/GetVeripsa/.github/blob/main/SECURITY.md) or the canonical process at <https://veripsa.com/security/disclosure>.

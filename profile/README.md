# Veripsa

**GitHub-native pre-merge PR traffic control for parallel coding agents.**
Veripsa helps teams notice when open pull requests may need collision or
landing-order attention before `main` changes.

Install Veripsa Core once as a GitHub App. It keeps a native GitHub check—and,
when useful, at most one managed PR comment—current automatically; humans and
agents use the same repository installation. Veripsa is advisory by default—
branch protection or rulesets decide what is required to merge.

## Start here

| Need | Link |
| --- | --- |
| Try the guided demo | <https://veripsa.com/try> |
| Understand the product | <https://veripsa.com/how-it-works> |
| See a collision walkthrough | <https://veripsa.com/collision> |
| Product docs | <https://veripsa.com/docs> |
| Data handling and trust | <https://veripsa.com/trust> |
| Recent improvements | <https://veripsa.com/whats-new> |
| Live service status | <https://veripsa.com/status> |
| Support | <https://veripsa.com/support> |

## Public repositories

There are three intentional public surfaces:

| Repository | Purpose |
| --- | --- |
| [`veripsa-webhook-spec`](https://github.com/GetVeripsa/veripsa-webhook-spec) | Versioned public integration contract, permissions/events, output schemas, acknowledgement semantics, and data handling. |
| [`ai-pr-collision-lab`](https://github.com/GetVeripsa/ai-pr-collision-lab) | Maintained repository for trying a two-PR landing-order scenario. |
| [`.github`](https://github.com/GetVeripsa/.github) | Organization profile, security policy, support routes, and canonical links. |

The Core engine and hosted platform remain private. The public surfaces explain
what data crosses the boundary and what users can observe, not how Veripsa
decides internally.

## Product boundaries

- Current coordination is between open pull requests within one repository.
- The four base traffic signals are Clear, Heads up, Wait in line, and Unknown.
- A material coupling may add Paused as an acknowledgement control overlay; it
  is not a fifth traffic verdict.
- Veripsa works alongside merge queues, AI code reviewers, tests, CI, branch
  protection, and human review.
- Source file and diff bodies are not retained or displayed by Veripsa Core.

- Support: <https://veripsa.com/support>
- Security reports: <https://veripsa.com/security/disclosure>

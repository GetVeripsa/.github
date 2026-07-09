# Recommended public repository metadata

This file tracks the GitHub repository descriptions and topics that should be set manually in GitHub Settings. The current connector can edit repository files, but it does not expose repository description/topic mutations.

## Organization-wide topic set

Use these topics where relevant:

```text
ai-agents
github-app
pull-requests
devtools
ci-cd
code-review-workflow
branch-protection
agentic-coding
software-engineering
merge-safety
```

Avoid topics that overstate the product:

```text
merge-queue
ai-code-reviewer
autonomous-code-review
security-scanner
```

## Repository descriptions

| Repo | Recommended description |
| --- | --- |
| `GetVeripsa/.github` | Org profile, security, support, and discovery materials for Veripsa. |
| `GetVeripsa/veripsa-changelog` | User-visible changes to Veripsa Core, the GitHub App for AI-agent PR traffic control. |
| `GetVeripsa/veripsa-roadmap` | Public roadmap and scope boundaries for Veripsa Core. |
| `GetVeripsa/veripsa-webhook-spec` | Public integration contract for Veripsa GitHub checks, comments, labels, and schemas. |
| `GetVeripsa/veripsa-examples` | Worked examples for using Veripsa Core on GitHub pull requests. |
| `GetVeripsa/ai-pr-collision-lab` | Maintained sandbox repository for trying Veripsa on parallel AI-agent PR scenarios. |
| `RollNuts/veripsa-live-demo` | Historical public Veripsa PR-pair demo; maintained sandbox lives at GetVeripsa/ai-pr-collision-lab. |
| `RollNuts/ai-pr-collision-lab` | User fork of the Veripsa AI PR collision lab; see GetVeripsa/ai-pr-collision-lab for the maintained sandbox. |

## Per-repo topic suggestions

### `GetVeripsa/veripsa-webhook-spec`

```text
ai-agents
github-app
pull-requests
webhooks
json-schema
typescript
devtools
agentic-coding
```

### `GetVeripsa/ai-pr-collision-lab`

```text
ai-agents
github-app
pull-requests
sandbox
python
pytest
agentic-coding
devtools
```

### `GetVeripsa/veripsa-examples`

```text
ai-agents
github-app
pull-requests
examples
documentation
devtools
agentic-coding
```

### `GetVeripsa/veripsa-changelog`

```text
ai-agents
github-app
changelog
pull-requests
devtools
```

### `GetVeripsa/veripsa-roadmap`

```text
ai-agents
github-app
roadmap
pull-requests
devtools
```

## Canonical links to include in repo websites when GitHub allows it

- Product: https://veripsa.com
- Try: https://veripsa.com/try
- Share kit: https://veripsa.com/share
- Japanese share kit: https://veripsa.com/ja/share
- Discovery: https://veripsa.com/llms.txt

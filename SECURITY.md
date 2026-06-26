# Security Policy

Thanks for helping keep Veripsa users safe. This is the **org-default** policy for every public and private repository in the [GetVeripsa](https://github.com/GetVeripsa) organization. Individual repositories may publish a more specific policy that supersedes this one.

The full, canonical disclosure process is at **<https://veripsa.com/security/disclosure>**. The short version follows.

## How to report a vulnerability

Email **support@veripsa.com** with the subject line starting `[SECURITY]`, including:

- A description of the issue.
- The component you believe is affected (the **Veripsa Core GitHub App**, **veripsa.com**, or this org's tooling).
- Steps to reproduce, a proof of concept, or an exploit chain if you have one.
- Your name or handle so we can credit you, if you'd like to be credited.

> Veripsa is a small team. Security reports are routed off the same `support@veripsa.com` inbox using the `[SECURITY]` subject prefix — please use it so the report is triaged ahead of general support. We will split into a dedicated `security@` address once volume warrants it.

Please **do not** open a public GitHub issue, public discussion, or public PR for a suspected security issue.

## What to expect

- **Acknowledgement:** within **2 business days** of receipt.
- **Initial triage:** within **5 business days** — we will tell you whether the report appears valid, what we believe the severity is, and what the next step is.
- **Status updates:** at least every **7 days** while a report is open.
- **Coordinated disclosure:** we work with reporters on a public disclosure timeline once a fix is shipped. Default target is **90 days** from report to public disclosure; we negotiate shorter or longer based on severity and complexity.
- **Credit:** with your permission, we credit reporters in the public disclosure note.

## Scope

In scope:

- The **Veripsa Core GitHub App** (the App installed on customer repositories from the GetVeripsa org).
- **veripsa.com** — the marketing, account, and billing surfaces operated by Veripsa.
- Repositories inside the [GetVeripsa](https://github.com/GetVeripsa) organization that this default policy covers.

Out of scope:

- **Third-party services** that Veripsa uses as subprocessors (e.g. the hosting provider, the payment processor, the email provider). These have their own coordinated disclosure programs. Please report directly to them. If you believe a Veripsa configuration of a third-party service is at fault, that **is** in scope — please tell us.
- **Social engineering** of Veripsa staff, physical attacks, and denial-of-service tests against production.
- **GitHub itself** — please use <https://bounty.github.com/>.
- Findings that require a **pre-compromised** developer machine or a **pre-compromised GitHub account** of a Veripsa user.

## Safe harbor

If you make a good-faith effort to comply with this policy, we will:

- Not pursue or support legal action against you for your research.
- Work with you to understand and resolve the issue quickly.
- Recognize your contribution if you'd like public credit.

Good faith includes: not accessing or modifying other users' data beyond what is necessary to demonstrate the issue, not degrading Veripsa's service for other users, and giving us reasonable time to fix the issue before public disclosure.

## What this policy is not

- It is **not** a bug bounty program. Veripsa does not currently pay cash rewards for vulnerability reports. We will say so if and when that changes.
- It is **not** a substitute for the canonical process at <https://veripsa.com/security/disclosure>, which is the authoritative reference.

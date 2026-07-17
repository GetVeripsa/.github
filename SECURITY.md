# Security Policy

Thanks for helping keep Veripsa users safe. This is the **org-default** policy
for GetVeripsa repositories that inherit it. An individual repository may
publish a more specific policy that supersedes this one.

The full, canonical disclosure process is at **<https://veripsa.com/security/disclosure>**. The short version follows.

## How to report a vulnerability

Email **support@veripsa.com** with the subject line starting `[SECURITY]`, including:

- A description of the issue.
- The component you believe is affected (the **Veripsa Core GitHub App**, **veripsa.com**, or this org's tooling).
- Steps to reproduce, a proof of concept, or an exploit chain if you have one.
- Your name or handle so we can credit you, if you'd like to be credited.

> Security reports are routed from `support@veripsa.com` using the `[SECURITY]`
> subject prefix. Please use it so the report is triaged ahead of general support.

Please **do not** open a public GitHub issue, public discussion, or public PR for a suspected security issue.

## What to expect

Response targets, scope, safe-harbor terms, and coordinated-disclosure details
live on the [canonical disclosure page](https://veripsa.com/security/disclosure).
They are maintained there so this org default cannot drift into a conflicting
promise. Veripsa handles reports on a best-effort basis and credits reporters
with their permission.

## Scope

In scope:

- The **Veripsa Core GitHub App** (the App installed on customer repositories from the GetVeripsa org).
- **veripsa.com** — the marketing and account surfaces operated by Veripsa.
- Repositories inside the [GetVeripsa](https://github.com/GetVeripsa) organization that this default policy covers.

Out of scope:

- **Third-party services** that Veripsa uses as subprocessors (e.g. the hosting provider). These have their own coordinated disclosure programs. Please report directly to them. If you believe a Veripsa configuration of a third-party service is at fault, that **is** in scope — please tell us.
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

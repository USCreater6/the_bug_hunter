# 01 — The Hunt Loop

Run this loop for every candidate bug. Never skip a step. "Done" is defined for each.

## 1. Policy review
Confirm the asset is in scope and the bug class is paid (not excluded). Note any rate/tool limits.
**Done when:** you can name the in-scope asset and quote the reward band for this severity.

## 2. Hypothesis
Write one sentence: *"If I change X, the server will wrongly do Y."*
**Done when:** the sentence names a specific parameter/endpoint and a specific wrong behaviour.

## 3. Minimal test
Make the **smallest single change** that would prove or disprove the hypothesis, on your own accounts/data, by hand in Repeater.
**Done when:** you sent exactly one changed request and captured the response.

## 4. Manual validation
Reproduce it **2 more times**. Rule out caching, your own session confusion, or a coincidence. Confirm expected-vs-observed behaviour.
**Done when:** 3 independent reproductions, and you can explain *why* the server behaves this way.

## 5. Evidence
Capture the request/response pair and a short screen recording or screenshots. **Redact** cookies, tokens, and any personal data.
**Done when:** evidence shows the full repro and contains zero secrets.

## 6. Report draft
Fill `04_REPORT_TEMPLATE.md`. Run `03_TRIAGE_GATE.md`. **You** decide whether to submit.
**Done when:** the draft passes the triage gate and you have consciously chosen to submit or shelve it.

---

### Scaling to "10 tasks" safely (Phase C version)
You don't need 10 unattended agents. You get the same coverage by running this loop once per **vulnerability class**, one at a time:

IDOR/access-control · authentication · session · SSRF · CSRF · open redirect · business-logic · file upload · info disclosure · API/GraphQL.

Each class is a "task". Claude copilots each. This is what Phase B later automates as read-only code review — the loop stays the same.

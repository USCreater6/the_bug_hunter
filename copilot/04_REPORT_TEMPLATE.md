# 04 — Report Template

Fill every section. Keep it short and factual. Paste into the program's submission form only after `03_TRIAGE_GATE.md` passes and you have decided to submit.

---

**Title:** `<Vuln class> on <asset> allows <impact in a few words>`

**Affected asset:** `<exact in-scope URL / endpoint / app>`

**Severity (your assessment):** `<Low / Medium / High / Critical>` — match it to demonstrated impact, not potential.

**Prerequisites:**
`<accounts, roles, or conditions needed — e.g. two standard user accounts, both created by me>`

**Steps to reproduce (minimal):**
1. `<step>`
2. `<step>`
3. `<step>`
Keep it to the fewest steps that reproduce the issue.

**Expected vs observed:**
- Expected: `<what the server should do>`
- Observed: `<what it actually did>`

**Impact:**
`<concrete harm: who is affected, what data/action, scale. No inflation.>`

**Evidence:**
`<attached: redacted request/response, screenshots or short video. No cookies/tokens/PII.>`

**Suggested remediation (where justified):**
`<the fix in 1–3 sentences, e.g. enforce server-side authorization check on <object> before returning it>`

---

> Do not invent evidence. Do not submit automatically. One finding per report unless the program says otherwise.

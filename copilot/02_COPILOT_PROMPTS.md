# 02 — Copilot Prompts

Paste these into a Claude chat at the matching step. Claude explains, reviews, and drafts.
**Claude does not send live requests to a third-party target. You execute every action yourself.**

Fill the `<...>` placeholders. Redact cookies/tokens before pasting anything captured.

---

## Step 1 — Policy review
```
Here is a bug-bounty program policy I pasted below. I want to test <asset> for <bug class>.
1) Is <asset> explicitly in scope?
2) Is <bug class> excluded or non-qualifying?
3) What is the reward band for this severity?
4) Any rules on automated tools or rate limits I must follow?
Answer only from the text I pasted. If it's not in the text, say "not stated".
<paste policy text>
```

## Step 2 — Hypothesis stress-test
```
My hypothesis: "If I change <X>, the server will wrongly do <Y>."
Poke holes in it. What would make this NOT a vulnerability? What's the smallest single
request that would prove or disprove it? What's the most likely benign explanation?
```

## Step 3 — Read a captured request
```
Explain this HTTP request/response. What does each header and parameter do?
Which single field is worth changing to test my hypothesis, and why?
(Cookies/tokens redacted.)
<paste redacted request/response>
```

## Step 4 — Validate, don't fool myself
```
I changed <field> from <a> to <b> and got <result>. I reproduced it 3 times.
Could this be caching, my own session, or a coincidence rather than a real auth/logic flaw?
What would confirm it's real? What would rule it out?
```

## Step 5 — Exclusion & duplicate check
```
For program <name>, is <finding in one line> a known exclusion or commonly non-qualifying issue?
Answer only from the policy text below; flag anything that reads like an exclusion.
<paste exclusions section>
```

## Step 6 — Report draft & impact review
```
Draft a report from these notes using title / asset / prerequisites / steps / impact / remediation.
Keep impact factual — do not inflate severity. Tell me if the impact is too weak to be worth submitting.
<paste your notes + redacted evidence summary>
```

---

### What NOT to ask Claude to do
- "Scan <site> for me" — no.
- "Send these requests to <live third-party target>" — no.
- "Find bugs in <company> automatically" — no.
Those cross authorization. Claude will refuse and you'd risk a ban. Keep Claude in the explain/review/draft seat.

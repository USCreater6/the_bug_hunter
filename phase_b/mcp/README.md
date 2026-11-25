# Phase B MCP server (scaffold)

A **read-only** code-review server for the cloud VM. The skills in `phase_b/skills/`
already work in Claude today — this server is for when you provision the VM
(Phase B at scale). Don't run it on the 8GB laptop.

## What it does
Four read-only tools: `review_source`, `triage_program`, `gen_test_plan`,
`draft_report`. It reads source files under an allowlisted root and returns
structured analysis. It is pinned to `claude-opus-5-5`.

## What it never does
No network traffic, no running target code, no live testing, no auto-submit.
`review_source` refuses any path outside `scope.json`'s `allowed_roots`.

## Setup (on the VM, later)
1. `pip install -r requirements.txt`
2. `cp scope.example.json scope.json` and edit `allowed_roots` to repos you may read.
3. Register `server.py` as an MCP server in your client.

## Status
Scaffold. `review_source` is a real lightweight pattern reviewer; the other three
return structured templates the review skills fill. Deep analysis is done by the
Claude skills, not by this server.

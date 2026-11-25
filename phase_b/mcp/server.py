#!/usr/bin/env python3
"""the_bug_hunter Phase B - read-only code-review MCP server (scaffold).

Runs on the authorized cloud VM (not needed for the skills, which work now).
READ-ONLY: it reads source files under an allowlisted root and returns structured
analysis. It NEVER sends network traffic, runs target code, or tests a live
third-party system. AI reasoning is pinned to claude-opus-5-5 with no fallback.
"""
from __future__ import annotations
import json
import os
import re
import pathlib

from mcp.server.fastmcp import FastMCP  # pip install mcp  (see requirements.txt)

MODEL = "claude-opus-5-5"  # pinned; no fallback to any other model
mcp = FastMCP("the_bug_hunter-review")


# --- scope lock: only paths under an allowlisted root may be read ---
def _load_scope() -> dict:
    cfg = os.environ.get("TBH_SCOPE", str(pathlib.Path(__file__).with_name("scope.json")))
    try:
        return json.loads(pathlib.Path(cfg).read_text())
    except Exception:
        return {"allowed_roots": [], "note": "no scope.json - nothing is reviewable until you add one"}


SCOPE = _load_scope()


def _in_scope(path: str) -> bool:
    rp = pathlib.Path(path).resolve()
    for root in SCOPE.get("allowed_roots", []):
        try:
            rp.relative_to(pathlib.Path(root).resolve())
            return True
        except ValueError:
            continue
    return False


# --- lightweight, local-only, read-only pattern reviewer ---
PATTERNS = [
    ("injection",       r"cursor\.execute\([^,]*%|execute\(\s*f['\"]|\bquery\s*\+\s*request\b"),
    ("deserialization", r"pickle\.loads|yaml\.load\((?!.*Loader)|\beval\(|\bexec\("),
    ("ssrf",            r"requests\.(get|post)\([^)]*\b(url|target|host|endpoint)\b"),
    ("path-traversal",  r"open\([^)]*\b(request|input|param|filename)\b"),
    ("secrets",         r"(api_key|secret|password|token)\s*=\s*['\"][^'\"]{8,}['\"]"),
]


@mcp.tool()
def review_source(path: str) -> dict:
    """Read ONE in-scope source file; return pattern-based candidate findings.
    Read-only. Each candidate is a hypothesis to validate by hand, not a confirmed bug."""
    if not _in_scope(path):
        return {"error": "out of scope", "path": path, "allowed_roots": SCOPE.get("allowed_roots", [])}
    text = pathlib.Path(path).read_text(errors="replace")
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        for cls, pat in PATTERNS:
            if re.search(pat, line):
                out.append({"class": cls, "line": i, "code": line.strip()[:160],
                            "confidence": "low",
                            "validate_by": "manual review + ONE test by the human"})
    return {"path": path, "candidates": out, "model": MODEL,
            "note": "read-only; validate every candidate by hand before treating it as a finding"}


@mcp.tool()
def triage_program(policy_text: str) -> dict:
    """Summarize a pasted program policy. Fill ONLY from policy_text; unknown -> 'not stated'."""
    return {"instructions": "answer only from policy_text; silence on scanners = 'not stated' = restrictive",
            "fields": ["in_scope", "paid_classes", "exclusions", "automation_rules",
                       "rate_limits", "eligibility", "worth_it"], "model": MODEL}


@mcp.tool()
def gen_test_plan(hypothesis: str, target: str) -> dict:
    """Produce a MANUAL test plan. Never executes anything; the human runs it."""
    return {"hypothesis": hypothesis, "target": target, "execution": "human-only",
            "template": ["preconditions", "minimal_test", "expected", "bug_if",
                         "evidence", "stop_conditions", "request_budget"], "model": MODEL}


@mcp.tool()
def draft_report(finding_json: str) -> dict:
    """Draft a report from a VALIDATED finding. Never auto-submits."""
    try:
        finding = json.loads(finding_json)
    except Exception:
        return {"error": "finding_json must be JSON"}
    return {"draft_fields": ["title", "asset", "severity", "prereqs", "steps",
                             "expected_observed", "impact", "evidence", "remediation"],
            "submit": "human-only", "model": MODEL, "finding": finding}


if __name__ == "__main__":
    mcp.run()

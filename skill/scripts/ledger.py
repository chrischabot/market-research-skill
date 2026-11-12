#!/usr/bin/env python3
"""Check and render the run ledger of a market-research workspace.

The lead keeps <workspace>/run.json as the single record of what the run
planned, what was done and what was left. This script validates that record
against the files on disk and prints the status table for the run log.

    ledger.py check <workspace>     exit 0 when the ledger and files agree
    ledger.py table <workspace>     print the stage table as Markdown

It reads only; it never changes the workspace. Passing the check proves the
ledger is consistent with the files, not that the research is good.
Python 3.8 or later, standard library only.
"""

import json
import re
import sys
from pathlib import Path

RUN_STATUSES = {"in_progress", "complete", "incomplete"}
DEPTHS = {"quick", "standard", "deep"}
UNIT_STATUSES = {
    "planned",      # decided on, not started
    "in_progress",  # an agent has it
    "done",         # output written and accepted by the lead
    "thin",         # output accepted with a recorded gap
    "blocked",      # could not be done; note says why
    "deferred",     # left out by depth or budget; note says why
    "stale",        # an input changed after it was written
    "dropped",      # removed from the run on purpose
}
NEEDS_NOTE = {"thin", "blocked", "deferred", "stale", "dropped"}
WRITTEN = {"done", "thin"}
OPEN = {"planned", "in_progress", "stale"}

# Roles whose documents must be sourced from pages opened during the run.
EVIDENCE_ROLES = {
    "market-analyst",
    "competitor-scout",
    "competitor-profiler",
    "growth-researcher",
    "feedback-researcher",
}
# Roles whose documents describe our own product.
PRODUCT_ROLES = {"component-analyst", "product-writer"}
MIN_LINKS = 3
MIN_FEEDBACK_QUOTES = 3

LINK = re.compile(r"https?://[^\s)>\]]+")
MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
QUOTE = re.compile(r"[\"“][^\"”\n]{12,}[\"”]")
LABELS = ("Today", "Intended", "Possible", "Open")


def load(workspace):
    path = workspace / "run.json"
    if not path.is_file():
        raise SystemExit(f"no run.json in {workspace}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        raise SystemExit(f"run.json is not valid JSON: {err}")


def safe_relative(value):
    """A workspace-relative path that cannot escape the workspace."""
    if not isinstance(value, str) or not value.strip():
        return False
    parts = Path(value).parts
    return not Path(value).is_absolute() and ".." not in parts


def check_output(workspace, unit, rel, errors, warnings):
    uid = unit["id"]
    path = workspace / rel
    if not path.is_file():
        errors.append(f"{uid}: status {unit['status']} but {rel} does not exist")
        return
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        errors.append(f"{uid}: {rel} is empty")
        return
    head = text.lstrip().splitlines()[:12]
    if not head[0].startswith("# "):
        errors.append(f"{uid}: {rel} does not begin with a title")
    if not any(line.startswith("Product:") for line in head):
        errors.append(f"{uid}: {rel} has no 'Product:' header line")

    role = unit.get("role", "")
    if role in EVIDENCE_ROLES:
        links = len(set(LINK.findall(text)))
        if links < MIN_LINKS:
            errors.append(
                f"{uid}: {rel} cites {links} link(s); an evidence document "
                f"needs at least {MIN_LINKS}"
            )
    if role == "feedback-researcher" and unit["status"] == "done":
        quotes = len(QUOTE.findall(text))
        if quotes < MIN_FEEDBACK_QUOTES:
            warnings.append(
                f"{uid}: {rel} has {quotes} quotation(s); mark the unit thin "
                f"if users really said this little"
            )
    if role in PRODUCT_ROLES and not any(label in text for label in LABELS[1:]):
        warnings.append(
            f"{uid}: {rel} never says Intended, Possible or Open; check that "
            f"it is not written entirely as present fact"
        )
    if rel == "landscape.md" or rel.startswith("strategy/"):
        for target in MD_LINK.findall(text):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            if not resolved.exists():
                errors.append(f"{uid}: {rel} links to {target}, which does not exist")


def check(workspace):
    errors, warnings = [], []
    run = load(workspace)

    for field in ("product", "depth", "status", "started", "updated", "units"):
        if field not in run:
            errors.append(f"run.json is missing '{field}'")
    if errors:
        return errors, warnings

    if run["depth"] not in DEPTHS:
        errors.append(f"depth '{run['depth']}' is not one of {sorted(DEPTHS)}")
    if run["status"] not in RUN_STATUSES:
        errors.append(f"status '{run['status']}' is not one of {sorted(RUN_STATUSES)}")
    if run["status"] == "incomplete" and not run.get("incomplete_reason"):
        errors.append("an incomplete run must state incomplete_reason")

    budget = run.get("budget")
    started = run.get("agents_started", 0)
    if budget is not None:
        if not isinstance(budget, int) or budget < 1:
            errors.append("budget must be a positive whole number or null")
        elif isinstance(started, int) and started > budget:
            errors.append(f"agents_started ({started}) exceeds the budget ({budget})")

    units = run["units"]
    if not isinstance(units, list) or not units:
        errors.append("units must be a non-empty list")
        return errors, warnings

    seen, claimed = set(), {}
    for index, unit in enumerate(units):
        uid = unit.get("id") if isinstance(unit, dict) else None
        if not uid:
            errors.append(f"unit {index} has no id")
            continue
        if uid in seen:
            errors.append(f"duplicate unit id '{uid}'")
        seen.add(uid)

        status = unit.get("status")
        if status not in UNIT_STATUSES:
            errors.append(f"{uid}: status '{status}' is not one of {sorted(UNIT_STATUSES)}")
            continue
        stage = unit.get("stage")
        if not isinstance(stage, int) or not 1 <= stage <= 7:
            errors.append(f"{uid}: stage must be a whole number from 1 to 7")
        if not unit.get("role"):
            errors.append(f"{uid}: no role")
        if status in NEEDS_NOTE and not str(unit.get("note", "")).strip():
            errors.append(f"{uid}: status {status} needs a note saying why")

        outputs = unit.get("outputs") or []
        if not outputs and unit.get("role") not in ("coverage-critic",):
            errors.append(f"{uid}: no outputs listed")
        for rel in outputs:
            if not safe_relative(rel):
                errors.append(f"{uid}: output '{rel}' must be a path inside the workspace")
                continue
            if rel in claimed and status != "dropped":
                errors.append(f"{uid}: {rel} is also claimed by {claimed[rel]}")
            claimed.setdefault(rel, uid)
            if status in WRITTEN:
                check_output(workspace, unit, rel, errors, warnings)

    if run["status"] == "complete":
        unfinished = [u["id"] for u in units if u.get("status") in OPEN]
        if unfinished:
            errors.append(
                "run is marked complete but these units are still open: "
                + ", ".join(unfinished)
            )

    competitors = workspace / "competitors"
    if competitors.is_dir():
        for path in sorted(competitors.glob("*.md")):
            rel = path.relative_to(workspace).as_posix()
            if rel not in claimed:
                warnings.append(f"{rel} is on disk but no unit in the ledger lists it")

    return errors, warnings


def table(workspace):
    run = load(workspace)
    lines = [
        "| Stage | Unit | Role | Status | Outputs | Note |",
        "|-------|------|------|--------|---------|------|",
    ]
    units = sorted(run.get("units", []), key=lambda u: (u.get("stage", 0), u.get("id", "")))
    for unit in units:
        outputs = ", ".join(f"`{o}`" for o in unit.get("outputs") or [])
        note = str(unit.get("note", "")).replace("|", "/").replace("\n", " ")
        lines.append(
            f"| {unit.get('stage', '')} | {unit.get('id', '')} | {unit.get('role', '')} "
            f"| {unit.get('status', '')} | {outputs} | {note} |"
        )
    counts = {}
    for unit in units:
        counts[unit.get("status")] = counts.get(unit.get("status"), 0) + 1
    summary = ", ".join(f"{count} {status}" for status, count in sorted(counts.items()))
    budget = run.get("budget")
    spent = run.get("agents_started", 0)
    agents = f"{spent} of {budget}" if budget is not None else f"{spent}, no budget set"
    lines.append("")
    lines.append(f"Run status: {run.get('status')}. Units: {summary}. Agents started: {agents}.")
    return "\n".join(lines)


def main(argv):
    if len(argv) != 3 or argv[1] not in ("check", "table"):
        print(__doc__.strip(), file=sys.stderr)
        return 2
    workspace = Path(argv[2]).expanduser()
    if not workspace.is_dir():
        print(f"{workspace} is not a directory", file=sys.stderr)
        return 2
    if argv[1] == "table":
        print(table(workspace))
        return 0
    errors, warnings = check(workspace)
    for message in warnings:
        print(f"warning: {message}")
    for message in errors:
        print(f"error: {message}")
    if errors:
        print(f"{len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"ledger and files agree ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))

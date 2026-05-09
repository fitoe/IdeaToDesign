#!/usr/bin/env python3
"""Minimal Level 3 design handoff checker for IdeaToDesign projects.

Run from the design package root:
  python scripts/check-design-handoff.py

The checker is intentionally conservative and token-efficient: it checks file
presence and state gate consistency, not subjective visual quality.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path.cwd()
REQUIRED = [
    "Design-Spec.md",
    "DESIGN.md",
    "tokens.json",
    "visual-source-contract.json",
    "implementation-parity-checklist.md",
    "state.json",
]


def load_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return None
    except json.JSONDecodeError as exc:
        return {"__error__": f"invalid json: {exc}"}


def main() -> int:
    blockers: list[str] = []
    warnings: list[str] = []

    for rel in REQUIRED:
        if not (ROOT / rel).exists():
            blockers.append(f"missing required file: {rel}")

    state = load_json(ROOT / "state.json")
    if isinstance(state, dict) and "__error__" in state:
        blockers.append(f"state.json {state['__error__']}")
    elif state is not None:
        gate = state.get("implementation_gate", {})
        if gate.get("status") != "open":
            blockers.append("implementation_gate.status is not open")
        if state.get("design_tokens", {}).get("status") != "ready":
            blockers.append("design_tokens.status is not ready")
        if state.get("page_style_briefs", {}).get("status") != "ready":
            blockers.append("page_style_briefs.status is not ready")

    contract = load_json(ROOT / "visual-source-contract.json")
    if isinstance(contract, dict) and "__error__" in contract:
        blockers.append(f"visual-source-contract.json {contract['__error__']}")
    elif contract is not None:
        approved = [m for m in contract.get("mockups", []) if m.get("status") == "approved"]
        if not approved:
            blockers.append("visual-source-contract.json has no approved mockups")

    brief_dir = ROOT / "page-style-briefs"
    if not brief_dir.exists():
        blockers.append("missing page-style-briefs/ directory")
    elif not list(brief_dir.glob("*.md")):
        blockers.append("page-style-briefs/ has no page briefs")

    if not (ROOT / "mockup-code-map.json").exists():
        warnings.append("optional mockup-code-map.json is missing")
    if not (ROOT / "design-debt.json").exists():
        warnings.append("optional design-debt.json is missing")

    result = {
        "passed": not blockers,
        "blockers": blockers,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not blockers else 1


if __name__ == "__main__":
    sys.exit(main())

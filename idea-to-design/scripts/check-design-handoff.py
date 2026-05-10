#!/usr/bin/env python3
"""Minimal Level 3 design handoff checker for IdeaToDesign projects.

Run from the design package root:
  python scripts/check-design-handoff.py

The checker is intentionally conservative and token-efficient: it checks file
presence, compact blueprint shape, and state gate consistency, not subjective
visual quality.
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
    "visual-proposals.json",
    "implementation-blueprint.json",
    "page-matrix.json",
    "component-blueprint.json",
    "debt-ledger.json",
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


def require_json_object(rel: str, blockers: list[str]):
    data = load_json(ROOT / rel)
    if data is None:
        blockers.append(f"missing required file: {rel}")
        return None
    if isinstance(data, dict) and "__error__" in data:
        blockers.append(f"{rel} {data['__error__']}")
        return None
    if not isinstance(data, dict):
        blockers.append(f"{rel} must be a JSON object")
        return None
    return data


def require_keys(rel: str, data: dict | None, keys: list[str], blockers: list[str]) -> None:
    if data is None:
        return
    missing = [key for key in keys if key not in data]
    if missing:
        blockers.append(f"{rel} missing keys: {', '.join(missing)}")


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
        visual_freeze = state.get("visual_freeze", {})
        if visual_freeze.get("status") != "approved":
            blockers.append("visual_freeze.status is not approved")
        if visual_freeze.get("post_visual_extraction_status") != "complete":
            blockers.append("visual_freeze.post_visual_extraction_status is not complete")
        if not visual_freeze.get("source_paths"):
            blockers.append("visual_freeze.source_paths is empty")
        if not visual_freeze.get("source_version"):
            blockers.append("visual_freeze.source_version is missing")
        post_extract = state.get("post_visual_extraction", {})
        if post_extract and post_extract.get("status") != "complete":
            blockers.append("post_visual_extraction.status is not complete")
        gate = state.get("implementation_gate", {})
        if gate.get("status") != "open":
            blockers.append("implementation_gate.status is not open")
        if gate.get("requires_visual_freeze") is not True:
            warnings.append("implementation_gate.requires_visual_freeze should be true")
        if gate.get("requires_post_visual_extraction") is not True:
            warnings.append("implementation_gate.requires_post_visual_extraction should be true")
        if gate.get("blueprint_generated_after_visual_freeze") is not True:
            blockers.append("implementation_gate.blueprint_generated_after_visual_freeze is not true")
        if state.get("design_tokens", {}).get("status") != "ready":
            blockers.append("design_tokens.status is not ready")
        if state.get("page_style_briefs", {}).get("status") != "ready":
            blockers.append("page_style_briefs.status is not ready")
        blueprint_state = state.get("implementation_blueprint")
        if blueprint_state is not None and blueprint_state.get("status") != "ready":
            blockers.append("implementation_blueprint.status is not ready")
        dtc = state.get("design_to_code_inputs")
        if dtc is not None and dtc.get("status") != "ready":
            blockers.append("design_to_code_inputs.status is not ready")

    contract = load_json(ROOT / "visual-source-contract.json")
    if isinstance(contract, dict) and "__error__" in contract:
        blockers.append(f"visual-source-contract.json {contract['__error__']}")
    elif contract is not None:
        approved = [m for m in contract.get("mockups", []) if m.get("status") == "approved"]
        if not approved:
            blockers.append("visual-source-contract.json has no approved mockups")

    blueprint = require_json_object("implementation-blueprint.json", blockers)
    require_keys(
        "implementation-blueprint.json",
        blueprint,
        ["version", "mode", "visual_freeze_ref", "source_priority", "read_order", "pass_sequence", "current_pass", "routes", "verification_policy", "read_by_pass"],
        blockers,
    )
    if blueprint is not None:
        if blueprint.get("mode") not in {"blueprint-driven", "blueprint_driven"}:
            warnings.append("implementation-blueprint.json mode is not blueprint-driven")
        visual_ref = blueprint.get("visual_freeze_ref", {})
        if isinstance(visual_ref, dict):
            if visual_ref.get("status") != "approved":
                blockers.append("implementation-blueprint.json visual_freeze_ref.status is not approved")
            if visual_ref.get("post_visual_extraction_status") != "complete":
                blockers.append("implementation-blueprint.json visual_freeze_ref.post_visual_extraction_status is not complete")
        else:
            blockers.append("implementation-blueprint.json visual_freeze_ref must be an object")
        if not isinstance(blueprint.get("routes"), list) or not blueprint.get("routes"):
            blockers.append("implementation-blueprint.json routes must be a non-empty list")
        read_order = blueprint.get("read_order", [])
        for rel in ["page-matrix.json", "component-blueprint.json", "debt-ledger.json"]:
            if rel not in read_order:
                warnings.append(f"implementation-blueprint.json read_order should include {rel}")

    page_matrix = require_json_object("page-matrix.json", blockers)
    require_keys("page-matrix.json", page_matrix, ["version", "pages"], blockers)
    if page_matrix is not None and (not isinstance(page_matrix.get("pages"), list) or not page_matrix.get("pages")):
        blockers.append("page-matrix.json pages must be a non-empty list")

    component_blueprint = require_json_object("component-blueprint.json", blockers)
    require_keys("component-blueprint.json", component_blueprint, ["version", "tiers"], blockers)

    debt_ledger = require_json_object("debt-ledger.json", blockers)
    require_keys("debt-ledger.json", debt_ledger, ["version", "items"], blockers)
    if debt_ledger is not None and not isinstance(debt_ledger.get("items"), list):
        blockers.append("debt-ledger.json items must be a list")

    visual_proposals = require_json_object("visual-proposals.json", blockers)
    if visual_proposals is not None and "proposals" in visual_proposals and not isinstance(visual_proposals.get("proposals"), list):
        blockers.append("visual-proposals.json proposals must be a list")

    visual_contract_dir = ROOT / "visual-contracts"
    if not visual_contract_dir.exists():
        blockers.append("missing visual-contracts/ directory")
    elif not list(visual_contract_dir.glob("*.json")):
        blockers.append("visual-contracts/ has no page contracts")

    brief_dir = ROOT / "page-style-briefs"
    if not brief_dir.exists():
        blockers.append("missing page-style-briefs/ directory")
    elif not list(brief_dir.glob("*.md")):
        blockers.append("page-style-briefs/ has no page briefs")

    if not (ROOT / "mockup-code-map.json").exists():
        warnings.append("optional mockup-code-map.json is missing")

    dtc_dir = ROOT / "design-to-code-inputs"
    prebrief_dir = ROOT / "pre-implementation-briefs"
    if (ROOT / "state.json").exists() and isinstance(state, dict):
        dtc = state.get("design_to_code_inputs")
        if dtc is not None:
            manifest = ROOT / dtc.get("manifest", "design-to-code-inputs/manifest.json")
            if not manifest.exists():
                blockers.append(f"missing design-to-code manifest: {manifest.relative_to(ROOT)}")
            if not dtc_dir.exists():
                blockers.append("missing design-to-code-inputs/ directory")
            if not prebrief_dir.exists() or not list(prebrief_dir.glob("*.md")):
                blockers.append("missing pre-implementation-briefs/*.md for design-to-code")

    result = {
        "passed": not blockers,
        "blockers": blockers,
        "warnings": warnings,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not blockers else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Validate IdeaToDesign's bounded P2D provider execution context.

Dependency-free by design: run this before producing canonical design artifacts.
In real orchestrated runs, keep the running card check enabled and pass a
card-status JSON exported by PlanToDelivery/Hermes Kanban.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

TASK_SCHEMA = "kanban-capability-task/v1"
DIGEST_SCHEMA = "active-slice-digest/v1"
RESULT_SCHEMA = "kanban-capability-result/v1"
PROVIDER = "idea-to-design"
CAPABILITIES = {"product_visual_design", "visual_source_creation"}
VALID_RESULTS = {"completed", "partial", "blocked", "failed"}
DESIGN_ARTIFACT_TYPES = {
    "design_spec",
    "page_matrix",
    "component_blueprint",
    "visual_source",
    "visual_source_contract",
    "visual_ir",
    "level_3_handoff_pack",
    "asset_notes",
    "design_debt_ledger",
    "review_notes",
}
REQUIRED_ENVELOPE_FIELDS = {
    "schema",
    "task_id",
    "capability",
    "project_root",
    "active_slice",
    "input_artifact_refs",
    "output_root",
    "expected_outputs",
    "verification_expectations",
    "allowed_side_effects",
    "review_policy",
    "blocking_policy",
    "design_contract",
    "kanban_constraints",
}
REQUIRED_RESULT_FIELDS = {
    "schema",
    "task_id",
    "capability",
    "provider",
    "result",
    "summary",
    "changed_files",
    "produced_artifacts",
    "evidence",
    "blockers",
    "debts",
    "review_required",
    "design_acceptance",
    "suggested_kanban_updates",
    "next_recommended_task",
}


class ContractError(Exception):
    pass


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise ContractError(f"missing JSON file: {path}")
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ContractError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ContractError(f"JSON root must be an object: {path}")
    return value


def require_nonempty_string(obj: dict[str, Any], field: str, where: str) -> str:
    value = obj.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ContractError(f"{where}.{field} must be a non-empty string")
    return value


def require_list(obj: dict[str, Any], field: str, where: str, *, nonempty: bool = False) -> list[Any]:
    value = obj.get(field)
    if not isinstance(value, list):
        raise ContractError(f"{where}.{field} must be a list")
    if nonempty and not value:
        raise ContractError(f"{where}.{field} must be non-empty")
    return value


def expected_outputs_include_design_artifact(expected_outputs: list[Any], capability: str) -> bool:
    names = [str(item).lower() for item in expected_outputs]
    tokens = ["design", "matrix", "spec", "review"]
    if capability == "visual_source_creation":
        tokens.extend(["visual", "source", "handoff", "ir", "blueprint"])
    return any(token in name for name in names for token in tokens)


def validate_design_contract(envelope: dict[str, Any]) -> None:
    design_contract = envelope.get("design_contract")
    if not isinstance(design_contract, dict) or not design_contract:
        raise ContractError("task.design_contract must be a non-empty object")

    capability = envelope["capability"]
    target_pages = require_list(design_contract, "target_pages", "task.design_contract", nonempty=True)
    if not all(isinstance(item, str) and item.strip() for item in target_pages):
        raise ContractError("task.design_contract.target_pages must contain non-empty strings")
    acceptance = require_list(design_contract, "acceptance_criteria", "task.design_contract", nonempty=True)
    if not all(isinstance(item, str) and item.strip() for item in acceptance):
        raise ContractError("task.design_contract.acceptance_criteria must contain non-empty strings")

    if capability == "product_visual_design":
        require_nonempty_string(design_contract, "project_context", "task.design_contract")
        requirements = require_list(design_contract, "requirements", "task.design_contract", nonempty=True)
        if not all(isinstance(item, str) and item.strip() for item in requirements):
            raise ContractError("task.design_contract.requirements must contain non-empty strings")
    elif capability == "visual_source_creation":
        approved = require_nonempty_string(design_contract, "approved_design_direction", "task.design_contract")
        implementation_constraints = design_contract.get("implementation_constraints")
        if not implementation_constraints:
            raise ContractError("task.design_contract.implementation_constraints must be present for visual_source_creation")
        refs = [str(item) for item in envelope.get("input_artifact_refs", [])]
        if refs and not any(approved == ref or approved in ref or ref in approved for ref in refs):
            raise ContractError("approved design direction must be listed in task.input_artifact_refs")


def validate_task_envelope(envelope: dict[str, Any], expected_capability: str | None) -> None:
    missing = sorted(REQUIRED_ENVELOPE_FIELDS - set(envelope))
    if missing:
        raise ContractError(f"task envelope missing required fields: {', '.join(missing)}")
    if envelope["schema"] != TASK_SCHEMA:
        raise ContractError(f"unsupported task schema: {envelope['schema']!r}")
    require_nonempty_string(envelope, "task_id", "task")
    capability = require_nonempty_string(envelope, "capability", "task")
    if capability not in CAPABILITIES:
        raise ContractError(f"unsupported IdeaToDesign capability: {capability!r}")
    if expected_capability is not None and capability != expected_capability:
        raise ContractError(f"expected capability {expected_capability!r}, got {capability!r}")
    require_nonempty_string(envelope, "project_root", "task")
    output_root = Path(require_nonempty_string(envelope, "output_root", "task"))
    if not isinstance(envelope.get("active_slice"), dict) or not envelope["active_slice"]:
        raise ContractError("task.active_slice must be a non-empty object")
    require_list(envelope, "input_artifact_refs", "task")
    expected_outputs = require_list(envelope, "expected_outputs", "task", nonempty=True)
    require_list(envelope, "verification_expectations", "task", nonempty=True)
    require_list(envelope, "allowed_side_effects", "task", nonempty=True)
    if "result-manifest.json" not in expected_outputs:
        raise ContractError("task.expected_outputs must include result-manifest.json")
    if not expected_outputs_include_design_artifact(expected_outputs, capability):
        raise ContractError("task.expected_outputs must include design, matrix, visual-source, handoff, or review artifacts")
    if not isinstance(envelope.get("review_policy"), dict):
        raise ContractError("task.review_policy must be an object")
    if not isinstance(envelope.get("blocking_policy"), dict):
        raise ContractError("task.blocking_policy must be an object")
    constraints = envelope.get("kanban_constraints")
    if not isinstance(constraints, dict) or not constraints:
        raise ContractError("task.kanban_constraints must be a non-empty object")
    if constraints.get("required") is not True:
        raise ContractError("task.kanban_constraints.required must be true in P2D mode")
    if output_root.name == "":
        raise ContractError("task.output_root is invalid")
    validate_design_contract(envelope)


def validate_digest(digest: dict[str, Any], envelope: dict[str, Any]) -> None:
    if digest.get("schema") != DIGEST_SCHEMA:
        raise ContractError(f"unsupported active-slice digest schema: {digest.get('schema')!r}")
    if digest.get("task_id") != envelope["task_id"] or digest.get("capability") != envelope["capability"]:
        raise ContractError("digest does not match task envelope")
    output_root = Path(envelope["output_root"])
    handoff = digest.get("handoff")
    if not isinstance(handoff, dict):
        raise ContractError("digest.handoff must be an object")
    expected_result_path = output_root / "result-manifest.json"
    result_path = Path(handoff.get("result_manifest_path", ""))
    if result_path != expected_result_path:
        raise ContractError("digest.handoff.result_manifest_path must equal output_root/result-manifest.json")


def validate_card_status(card_status: dict[str, Any], task_id: str) -> None:
    status = card_status.get("status")
    if status is None and isinstance(card_status.get("task"), dict):
        status = card_status["task"].get("status")
    card_id = card_status.get("task_id") or card_status.get("id")
    if card_id is not None and card_id != task_id:
        raise ContractError(f"card status task_id mismatch: expected {task_id!r}, got {card_id!r}")
    if status != "running":
        raise ContractError(f"provider task {task_id} must be running before execution; current status is {status!r}")


def evidence_has_design_item(evidence: list[Any]) -> bool:
    for item in evidence:
        if isinstance(item, dict) and str(item.get("type", "")).lower() in DESIGN_ARTIFACT_TYPES:
            return True
        if isinstance(item, str) and expected_outputs_include_design_artifact([item], "visual_source_creation"):
            return True
    return False


def validate_result_manifest(result: dict[str, Any], envelope: dict[str, Any]) -> None:
    missing = sorted(REQUIRED_RESULT_FIELDS - set(result))
    if missing:
        raise ContractError(f"result manifest missing required fields: {', '.join(missing)}")
    if result["schema"] != RESULT_SCHEMA:
        raise ContractError(f"unsupported result schema: {result['schema']!r}")
    if result["task_id"] != envelope["task_id"]:
        raise ContractError("result task_id does not match task envelope")
    if result["capability"] != envelope["capability"]:
        raise ContractError("result capability does not match task envelope")
    if result["provider"] not in {PROVIDER, "IdeaToDesign"}:
        raise ContractError(f"result.provider must be {PROVIDER!r} or 'IdeaToDesign'")
    if result["result"] not in VALID_RESULTS:
        raise ContractError(f"invalid result: {result['result']!r}")
    require_nonempty_string(result, "summary", "result")
    for field in ["changed_files", "produced_artifacts", "evidence", "blockers", "debts", "suggested_kanban_updates"]:
        require_list(result, field, "result")
    if not isinstance(result["review_required"], bool):
        raise ContractError("result.review_required must be a boolean")
    design_acceptance = result.get("design_acceptance")
    if not isinstance(design_acceptance, dict):
        raise ContractError("result.design_acceptance must be an object")
    if result["result"] in {"completed", "partial"}:
        if not result["produced_artifacts"]:
            raise ContractError(f"{result['result']} result must include produced_artifacts")
        if not result["evidence"] or not evidence_has_design_item(result["evidence"]):
            raise ContractError(f"{result['result']} result must include design evidence")
    if result["result"] == "blocked" and not result["blockers"]:
        raise ContractError("blocked result must include blockers")
    if result["review_required"] and result["result"] in {"completed", "partial"} and not result["suggested_kanban_updates"]:
        raise ContractError("review_required design results must include suggested_kanban_updates")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate IdeaToDesign P2D provider context.")
    parser.add_argument("--task", required=True, type=Path, help="Path to output_root/task-envelope.json")
    parser.add_argument("--digest", required=True, type=Path, help="Path to output_root/active-slice-digest.json")
    parser.add_argument("--result", type=Path, help="Optional path to output_root/result-manifest.json after provider work")
    parser.add_argument("--expected-capability", choices=sorted(CAPABILITIES), help="Expected IdeaToDesign capability")
    parser.add_argument("--card-status", type=Path, help="JSON card snapshot with status=running or task.status=running")
    parser.add_argument("--skip-running-check", action="store_true", help="Allow local/offline contract tests without a Hermes Kanban card snapshot")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        envelope = load_json(args.task)
        digest = load_json(args.digest)
        validate_task_envelope(envelope, args.expected_capability)
        validate_digest(digest, envelope)
        if not args.skip_running_check:
            if args.card_status is None:
                raise ContractError("--card-status is required unless --skip-running-check is used")
            validate_card_status(load_json(args.card_status), envelope["task_id"])
        if args.result is not None:
            validate_result_manifest(load_json(args.result), envelope)
    except ContractError as exc:
        print("IdeaToDesign provider context check: BLOCKED")
        print(f"- {exc}")
        return 1
    print("IdeaToDesign provider context check: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())

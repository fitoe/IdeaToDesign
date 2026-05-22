#!/usr/bin/env python3
"""Contract tests for IdeaToDesign P2D provider admission and manifests."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "idea-to-design" / "scripts" / "check-provider-context.py"
MANIFEST = ROOT / "contracts" / "provider-manifest.json"


class IdeaToDesignProviderContractTests(unittest.TestCase):
    def test_provider_manifest_declares_design_admission_contract(self) -> None:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        self.assertEqual(manifest["schema_version"], "provider-manifest/v1")
        self.assertEqual(manifest["provider_id"], "idea-to-design")
        self.assertEqual(set(manifest["capabilities"]), {"product_visual_design", "visual_source_creation"})
        admission = manifest["admission_contract"]
        self.assertEqual(admission["task_schema"], "kanban-capability-task/v1")
        self.assertEqual(admission["active_slice_digest_schema"], "active-slice-digest/v1")
        self.assertEqual(admission["result_manifest_path"], "output_root/result-manifest.json")
        self.assertIn("running_card_required", admission["required_checks"])
        self.assertIn("design_brief_present", admission["required_checks"])
        self.assertIn("approved_direction_required_for_visual_source_creation", admission["required_checks"])
        self.assertIn("result_manifest_schema_when_present", admission["required_checks"])

    def test_context_checker_accepts_valid_product_visual_design_task_and_result(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "out"
            output_root.mkdir()
            task = {
                "schema": "kanban-capability-task/v1",
                "task_id": "i2d-001",
                "capability": "product_visual_design",
                "project_root": str(root / "project"),
                "active_slice": {"id": "home-design", "summary": "homepage visual direction"},
                "input_artifact_refs": [],
                "output_root": str(output_root),
                "expected_outputs": ["Design-Spec.md", "page-matrix.json", "result-manifest.json"],
                "verification_expectations": ["design direction ready for approval"],
                "allowed_side_effects": ["write output_root design artifacts"],
                "review_policy": {"design_gate_required": True},
                "blocking_policy": {"missing_project_context": "blocked"},
                "design_contract": {
                    "project_context": "International B2B landing page",
                    "target_pages": ["home"],
                    "requirements": ["formal", "low text density", "clear CTA"],
                    "acceptance_criteria": ["direction is decisionable by user"],
                },
                "kanban_constraints": {"required": True, "design_card_id": "i2d-001"},
            }
            digest = {
                "schema": "active-slice-digest/v1",
                "task_id": "i2d-001",
                "capability": "product_visual_design",
                "active_slice": {"id": "home-design"},
                "handoff": {"result_manifest_path": str(output_root / "result-manifest.json")},
            }
            result = {
                "schema": "kanban-capability-result/v1",
                "task_id": "i2d-001",
                "capability": "product_visual_design",
                "provider": "idea-to-design",
                "result": "completed",
                "summary": "Design direction is ready for review.",
                "changed_files": [],
                "produced_artifacts": ["Design-Spec.md", "page-matrix.json"],
                "evidence": [
                    {"type": "design_spec", "path": "Design-Spec.md"},
                    {"type": "page_matrix", "path": "page-matrix.json"},
                ],
                "blockers": [],
                "debts": [],
                "review_required": True,
                "design_acceptance": {
                    "design_ready": True,
                    "accepted_by_user_or_orchestrator": False,
                    "remaining_design_debt": [],
                    "downstream_unblocked": False,
                },
                "suggested_kanban_updates": [
                    {"type": "design_review", "title": "Review homepage direction", "reason": "design gate required"}
                ],
                "next_recommended_task": {"capability": "visual_source_creation", "reason": "after design approval"},
            }
            task_path = output_root / "task-envelope.json"
            digest_path = output_root / "active-slice-digest.json"
            result_path = output_root / "result-manifest.json"
            task_path.write_text(json.dumps(task), encoding="utf-8")
            digest_path.write_text(json.dumps(digest), encoding="utf-8")
            result_path.write_text(json.dumps(result), encoding="utf-8")

            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "--task", str(task_path), "--digest", str(digest_path), "--result", str(result_path), "--skip-running-check"],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stdout + proc.stderr)
            self.assertIn("IdeaToDesign provider context check: PASS", proc.stdout)

    def test_context_checker_rejects_missing_approved_direction_for_visual_source_creation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output_root = root / "out"
            output_root.mkdir()
            task_path = output_root / "task-envelope.json"
            digest_path = output_root / "active-slice-digest.json"
            task_path.write_text(json.dumps({
                "schema": "kanban-capability-task/v1",
                "task_id": "i2d-002",
                "capability": "visual_source_creation",
                "project_root": str(root / "project"),
                "active_slice": {"id": "home-source"},
                "input_artifact_refs": [],
                "output_root": str(output_root),
                "expected_outputs": ["visual-source-contract.json", "result-manifest.json"],
                "verification_expectations": ["source ready for downstream implementation"],
                "allowed_side_effects": ["write output_root visual source artifacts"],
                "review_policy": {},
                "blocking_policy": {},
                "design_contract": {
                    "target_pages": ["home"],
                    "implementation_constraints": {"viewport": "mobile"},
                    "acceptance_criteria": ["visual source is complete"],
                },
                "kanban_constraints": {"required": True},
            }), encoding="utf-8")
            digest_path.write_text(json.dumps({
                "schema": "active-slice-digest/v1",
                "task_id": "i2d-002",
                "capability": "visual_source_creation",
                "handoff": {"result_manifest_path": str(output_root / "result-manifest.json")},
            }), encoding="utf-8")

            proc = subprocess.run(
                [sys.executable, str(SCRIPT), "--task", str(task_path), "--digest", str(digest_path), "--skip-running-check"],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertNotEqual(proc.returncode, 0)
            self.assertIn("approved_design_direction", proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()

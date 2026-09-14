import unittest

from models import RestorationRequest
from planner import build_plan


class ReVivaPlannerTests(unittest.TestCase):
    def test_builds_deterministic_identity_preserving_plan(self):
        plan = build_plan(
            RestorationRequest(
                image_id="portrait-old-001",
                operations=("upscale", "face_restore", "denoise", "deblur"),
            )
        )
        self.assertTrue(plan.allowed)
        self.assertEqual(plan.steps, ("denoise", "deblur", "face_restore", "upscale"))
        self.assertEqual(plan.identity_risk, "medium")
        self.assertTrue(any("identity preservation" in item for item in plan.assumptions))

    def test_blocks_identity_change(self):
        plan = build_plan(
            RestorationRequest(
                image_id="portrait-old-001",
                operations=("face_replace",),
            )
        )
        self.assertFalse(plan.allowed)
        self.assertEqual(plan.identity_risk, "high")

    def test_blocks_disabled_identity_preservation(self):
        plan = build_plan(
            RestorationRequest(
                image_id="portrait-old-001",
                operations=("denoise",),
                preserve_identity=False,
            )
        )
        self.assertFalse(plan.allowed)
        self.assertEqual(plan.identity_risk, "high")

    def test_rejects_face_restore_without_face(self):
        plan = build_plan(
            RestorationRequest(
                image_id="landscape-001",
                operations=("face_restore",),
            )
        )
        self.assertFalse(plan.allowed)

    def test_unknown_image_is_not_planned(self):
        plan = build_plan(
            RestorationRequest(
                image_id="missing",
                operations=("denoise",),
            )
        )
        self.assertFalse(plan.allowed)
        self.assertEqual(plan.identity_risk, "unknown")


if __name__ == "__main__":
    unittest.main()

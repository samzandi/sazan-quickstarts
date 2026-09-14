from data import IMAGES
from models import RestorationPlan, RestorationRequest
from policy import validate_request

STEP_ORDER = ("denoise", "deblur", "face_restore", "upscale")


def build_plan(request: RestorationRequest) -> RestorationPlan:
    image = IMAGES.get(request.image_id)
    if image is None:
        return RestorationPlan(
            image_id=request.image_id,
            allowed=False,
            reason="Unknown image_id; no restoration plan generated.",
            identity_risk="unknown",
        )

    allowed, reason, risk = validate_request(request)
    if not allowed:
        return RestorationPlan(
            image_id=request.image_id,
            allowed=False,
            reason=reason,
            identity_risk=risk,
        )

    requested = set(request.operations)
    if "face_restore" in requested and not image.has_face:
        return RestorationPlan(
            image_id=request.image_id,
            allowed=False,
            reason="Face restoration requested but mock metadata reports no face.",
            identity_risk="unknown",
        )

    steps = tuple(step for step in STEP_ORDER if step in requested)
    assumptions = (
        f"mock metadata only: {image.width}x{image.height}",
        f"blur_score={image.blur_score}",
        f"noise_score={image.noise_score}",
        "identity preservation is mandatory",
        "no image pixels are processed by this quickstart",
    )
    return RestorationPlan(
        image_id=request.image_id,
        allowed=True,
        steps=steps,
        assumptions=assumptions,
        identity_risk=risk,
        reason=reason,
    )

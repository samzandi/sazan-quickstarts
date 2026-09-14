from models import RestorationRequest
from planner import build_plan


def main() -> None:
    request = RestorationRequest(
        image_id="portrait-old-001",
        operations=("denoise", "deblur", "face_restore", "upscale"),
    )
    plan = build_plan(request)
    print(plan)


if __name__ == "__main__":
    main()

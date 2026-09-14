from models import ImageMetadata

IMAGES = {
    "portrait-old-001": ImageMetadata(
        image_id="portrait-old-001",
        width=640,
        height=480,
        has_face=True,
        blur_score=0.72,
        noise_score=0.64,
    ),
    "landscape-001": ImageMetadata(
        image_id="landscape-001",
        width=1024,
        height=768,
        has_face=False,
        blur_score=0.35,
        noise_score=0.22,
    ),
}

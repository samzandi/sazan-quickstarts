from dataclasses import dataclass, field
from typing import Tuple


@dataclass(frozen=True)
class ImageMetadata:
    image_id: str
    width: int
    height: int
    has_face: bool
    blur_score: float
    noise_score: float


@dataclass(frozen=True)
class RestorationRequest:
    image_id: str
    operations: Tuple[str, ...]
    preserve_identity: bool = True


@dataclass(frozen=True)
class RestorationPlan:
    image_id: str
    allowed: bool
    steps: Tuple[str, ...] = field(default_factory=tuple)
    assumptions: Tuple[str, ...] = field(default_factory=tuple)
    identity_risk: str = "unknown"
    reason: str = ""

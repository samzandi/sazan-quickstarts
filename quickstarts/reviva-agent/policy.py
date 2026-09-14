from models import RestorationRequest

ALLOWED_OPERATIONS = {"denoise", "deblur", "face_restore", "upscale"}
BLOCKED_OPERATIONS = {
    "face_replace",
    "identity_change",
    "synthetic_face",
    "add_facial_features",
}


def validate_request(request: RestorationRequest) -> tuple[bool, str, str]:
    if not request.preserve_identity:
        return False, "Identity preservation must remain enabled.", "high"

    requested = set(request.operations)
    if requested & BLOCKED_OPERATIONS:
        return False, "Requested operation could alter identity.", "high"

    unknown = requested - ALLOWED_OPERATIONS
    if unknown:
        return False, f"Unsupported restoration operation: {sorted(unknown)[0]}", "unknown"

    if not requested:
        return False, "At least one restoration operation is required.", "unknown"

    risk = "medium" if "face_restore" in requested else "low"
    return True, "Request is within the bounded restoration policy.", risk

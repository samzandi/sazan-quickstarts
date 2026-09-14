from __future__ import annotations

from actions import ComputerAction


class ActionPolicy:
    """Fail-closed policy for a small computer-use action surface."""

    ALLOWED = {"observe", "move_pointer", "click", "scroll"}

    def validate(self, action: ComputerAction) -> None:
        if action.type not in self.ALLOWED:
            raise PermissionError(f"Action {action.type!r} is blocked by policy.")

        if action.type in {"move_pointer", "click"}:
            if action.x is None or action.y is None:
                raise ValueError("Pointer actions require x and y coordinates.")
            if action.x < 0 or action.y < 0:
                raise ValueError("Coordinates must be non-negative.")

        if action.type == "scroll" and action.delta_y is None:
            raise ValueError("Scroll requires delta_y.")

        if action.text:
            raise PermissionError("Text entry is blocked in this starter.")

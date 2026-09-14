from __future__ import annotations

from pathlib import Path

from models import CodingAction, CodingActionType


class CodingPolicy:
    """Fail-closed policy for a deliberately narrow coding agent."""

    allowed_actions = frozenset(
        {
            CodingActionType.LIST_FILES,
            CodingActionType.READ_FILE,
            CodingActionType.PREVIEW_WRITE,
            CodingActionType.WRITE_FILE,
        }
    )

    def __init__(self, workspace_root: Path) -> None:
        self.workspace_root = workspace_root.resolve()

    def resolve_path(self, relative_path: str) -> Path:
        candidate = (self.workspace_root / relative_path).resolve()
        if candidate != self.workspace_root and self.workspace_root not in candidate.parents:
            raise ValueError("Path escapes the configured workspace root.")
        return candidate

    def validate(self, action: CodingAction) -> Path:
        if action.type not in self.allowed_actions:
            raise ValueError(f"Unsupported action: {action.type}")

        target = self.resolve_path(action.path)

        if action.type in {CodingActionType.PREVIEW_WRITE, CodingActionType.WRITE_FILE}:
            if action.content is None:
                raise ValueError("Write actions require content.")
            if target == self.workspace_root:
                raise ValueError("Writing directly to the workspace root is not allowed.")

        return target

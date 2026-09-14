from __future__ import annotations

from models import CodingAction, CodingActionType
from workspace import ActionResult, SafeWorkspace


class CodingAgent:
    """Minimal orchestration layer with an explicit preview-before-write workflow."""

    def __init__(self, workspace: SafeWorkspace) -> None:
        self.workspace = workspace

    def inspect(self, path: str = ".") -> ActionResult:
        return self.workspace.execute(CodingAction(CodingActionType.LIST_FILES, path))

    def read(self, path: str) -> ActionResult:
        return self.workspace.execute(CodingAction(CodingActionType.READ_FILE, path))

    def preview(self, path: str, content: str) -> ActionResult:
        return self.workspace.execute(
            CodingAction(CodingActionType.PREVIEW_WRITE, path, content)
        )

    def apply(self, path: str, content: str, *, approved: bool = False) -> ActionResult:
        if not approved:
            raise PermissionError("File writes require explicit approval after preview.")
        return self.workspace.execute(CodingAction(CodingActionType.WRITE_FILE, path, content))

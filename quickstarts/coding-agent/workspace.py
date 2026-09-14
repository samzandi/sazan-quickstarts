from __future__ import annotations

from dataclasses import dataclass
from difflib import unified_diff
from pathlib import Path

from models import CodingAction, CodingActionType
from policy import CodingPolicy


@dataclass(frozen=True)
class ActionResult:
    action: CodingActionType
    path: str
    output: str


class SafeWorkspace:
    """Read and edit files only inside one configured workspace root."""

    def __init__(self, root: Path) -> None:
        self.root = root.resolve()
        self.policy = CodingPolicy(self.root)

    def execute(self, action: CodingAction) -> ActionResult:
        target = self.policy.validate(action)

        if action.type == CodingActionType.LIST_FILES:
            if not target.exists() or not target.is_dir():
                raise ValueError("List target must be an existing directory.")
            names = sorted(str(path.relative_to(self.root)) for path in target.iterdir())
            return ActionResult(action.type, action.path, "\n".join(names))

        if action.type == CodingActionType.READ_FILE:
            if not target.exists() or not target.is_file():
                raise ValueError("Read target must be an existing file.")
            return ActionResult(action.type, action.path, target.read_text(encoding="utf-8"))

        if action.type == CodingActionType.PREVIEW_WRITE:
            old = target.read_text(encoding="utf-8") if target.exists() else ""
            new = action.content or ""
            diff = "".join(
                unified_diff(
                    old.splitlines(keepends=True),
                    new.splitlines(keepends=True),
                    fromfile=f"a/{action.path}",
                    tofile=f"b/{action.path}",
                )
            )
            return ActionResult(action.type, action.path, diff)

        if action.type == CodingActionType.WRITE_FILE:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(action.content or "", encoding="utf-8")
            return ActionResult(action.type, action.path, "written")

        raise AssertionError("Policy allowed an unhandled action.")

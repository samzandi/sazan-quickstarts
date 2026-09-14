from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

ActionType = Literal["observe", "move_pointer", "click", "type_text", "scroll"]


@dataclass(frozen=True)
class ComputerAction:
    type: ActionType
    x: int | None = None
    y: int | None = None
    text: str | None = None
    delta_y: int | None = None

    @staticmethod
    def observe() -> "ComputerAction":
        return ComputerAction(type="observe")

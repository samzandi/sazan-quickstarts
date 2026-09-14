from __future__ import annotations

from dataclasses import dataclass

from actions import ComputerAction
from policy import ActionPolicy


@dataclass
class SimulatedState:
    width: int = 1280
    height: int = 720
    pointer_x: int = 0
    pointer_y: int = 0
    scroll_y: int = 0
    clicks: int = 0


class SimulatedComputer:
    """Credential-free local simulator for policy and orchestration testing."""

    def __init__(self, policy: ActionPolicy | None = None) -> None:
        self.policy = policy or ActionPolicy()
        self.state = SimulatedState()

    def execute(self, action: ComputerAction) -> dict[str, int | str]:
        self.policy.validate(action)

        if action.type == "observe":
            return self.snapshot()
        if action.type == "move_pointer":
            assert action.x is not None and action.y is not None
            self._validate_bounds(action.x, action.y)
            self.state.pointer_x = action.x
            self.state.pointer_y = action.y
        elif action.type == "click":
            assert action.x is not None and action.y is not None
            self._validate_bounds(action.x, action.y)
            self.state.pointer_x = action.x
            self.state.pointer_y = action.y
            self.state.clicks += 1
        elif action.type == "scroll":
            assert action.delta_y is not None
            self.state.scroll_y += action.delta_y

        return self.snapshot()

    def snapshot(self) -> dict[str, int | str]:
        return {
            "mode": "simulator",
            "width": self.state.width,
            "height": self.state.height,
            "pointer_x": self.state.pointer_x,
            "pointer_y": self.state.pointer_y,
            "scroll_y": self.state.scroll_y,
            "clicks": self.state.clicks,
        }

    def _validate_bounds(self, x: int, y: int) -> None:
        if x >= self.state.width or y >= self.state.height:
            raise ValueError("Coordinates are outside the simulated screen.")

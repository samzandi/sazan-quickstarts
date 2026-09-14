from __future__ import annotations

from actions import ComputerAction
from simulator import SimulatedComputer


def main() -> None:
    computer = SimulatedComputer()
    print("Sazan Computer Agent Starter")
    print(computer.execute(ComputerAction.observe()))
    print(computer.execute(ComputerAction(type="move_pointer", x=120, y=90)))
    print(computer.execute(ComputerAction(type="click", x=120, y=90)))
    print(computer.execute(ComputerAction(type="scroll", delta_y=180)))


if __name__ == "__main__":
    main()

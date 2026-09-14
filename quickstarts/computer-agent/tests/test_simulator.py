import unittest

from actions import ComputerAction
from simulator import SimulatedComputer


class SimulatorTests(unittest.TestCase):
    def test_click_updates_state(self):
        computer = SimulatedComputer()
        state = computer.execute(ComputerAction(type="click", x=100, y=200))
        self.assertEqual(state["pointer_x"], 100)
        self.assertEqual(state["pointer_y"], 200)
        self.assertEqual(state["clicks"], 1)

    def test_rejects_out_of_bounds_click(self):
        computer = SimulatedComputer()
        with self.assertRaises(ValueError):
            computer.execute(ComputerAction(type="click", x=5000, y=10))

    def test_scroll_updates_state(self):
        computer = SimulatedComputer()
        state = computer.execute(ComputerAction(type="scroll", delta_y=240))
        self.assertEqual(state["scroll_y"], 240)


if __name__ == "__main__":
    unittest.main()

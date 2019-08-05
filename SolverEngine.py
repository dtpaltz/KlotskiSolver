from GridState import *


class SolverEngine:
    def __init__(self, starting_grid):
        state = GridState(None, "START", starting_grid)
        self.state_queue = [state]
        self.state_history = set()

    def find_solution_steps(self):
        if len(self.state_queue) == 0:
            return None
        current_state = self.state_queue.pop(0)
        self.state_history.add(current_state.get_state_str())
        # > generate next states from the current_state
        # > filter out any previously seen states from the next states
        # > if any of the next states is the goal state:
        #       > clear all other next states, solution path found
        #       > work backwards to clear all other paths, should end up with the
        #           starting state that now leads only to the goal state
        #       > return the start state
        # > else:
        #       > add next states to state_queue
        #       > find_solution_steps()

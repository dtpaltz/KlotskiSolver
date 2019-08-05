from itertools import chain


class GridState(object):
    def __init__(self, previous_state, event, grid):
        self.previous_state = previous_state
        self.event = event
        self.grid = grid
        self.step = 0
        self.next_states = []

        if self.previous_state:
            self.step = self.previous_state.step + 1

    def get_state_str(self):
        grid_copy = [row[:] for row in self.grid]
        return str(list(chain.from_iterable(grid_copy)))

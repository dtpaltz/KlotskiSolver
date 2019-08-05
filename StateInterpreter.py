from StateLibrary import *
from Pieces import *


class StateInterpreter:
    def __init__(self):
        self.piece_configuration = {}
        self.special_piece = None

    def interpret_grid(self, grid):
        symbols = {}
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                sym = grid[r][c]
                if sym:
                    location = (r, c)
                    if sym.upper() not in symbols:
                        symbols[sym.upper()] = [location]
                    else:
                        symbols[sym.upper()].append(location)

        for sym, locations in symbols.items():
            n = len(locations)
            if n == 1:
                self.piece_configuration[sym] = Type1Piece(sym, locations[0])
            if n == 2 and locations[0][1] == locations[1][1]:
                self.piece_configuration[sym] = Type2Piece(sym, locations[0])
            if n == 2 and locations[0][0] == locations[1][0]:
                self.piece_configuration[sym] = Type3Piece(sym, locations[0])
            if n == 4:
                special = Type4Piece(sym, locations[0])
                self.piece_configuration[sym] = special
                self.special_piece = special

        # for c, p in self.piece_configuration.items():
        #     print(str(p))

    def is_goal_state(self):
        return self.special_piece.pivot_point == (3, 1)


# si = StateInterpreter()
# si.interpret_grid(start_state)
# print(si.is_goal_state())

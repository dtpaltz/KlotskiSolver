
class GridPiece:
    def __init__(self, symbol, pivot_point):
        self.symbol = symbol
        self.pivot_point = pivot_point
        self.width = 0
        self.height = 0
        self.type = 0

    @staticmethod
    def is_goal_piece():
        return False

    def __str__(self):
        return "Piece {} is a Type: {}  |  Width: {}   Height: {}  |  Location: {}".format(self.symbol,
                                                                                           self.type,
                                                                                           self.width,
                                                                                           self.height,
                                                                                           self.pivot_point)


class Type4Piece(GridPiece):
    def __init__(self, symbol, pivot_point):
        GridPiece.__init__(self, symbol, pivot_point)
        self.width = 2
        self.height = 2
        self.type = 4

    @staticmethod
    def is_goal_piece():
        return True


class Type3Piece(GridPiece):
    def __init__(self, symbol, pivot_point):
        GridPiece.__init__(self, symbol, pivot_point)
        self.width = 2
        self.height = 1
        self.type = 3


class Type2Piece(GridPiece):
    def __init__(self, symbol, pivot_point):
        GridPiece.__init__(self, symbol, pivot_point)
        self.width = 1
        self.height = 2
        self.type = 2


class Type1Piece(GridPiece):
    def __init__(self, symbol, pivot_point):
        GridPiece.__init__(self, symbol, pivot_point)
        self.width = 1
        self.height = 1
        self.type = 1

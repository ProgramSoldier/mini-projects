class Piece():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def move(self):
        raise AssertionError('The method is not defined')


class Pawn(Piece):
    def move(self):
        print('The method is defined')


class Rook(Piece):
    pass


class Knight(Piece):
    pass


class Bishop(Piece):
    pass


class Queen(Piece):
    pass


class King(Piece):
    pass

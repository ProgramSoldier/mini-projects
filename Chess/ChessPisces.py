
import pygame

class Piece():
    active = False
    def __init__(self, img, color):
        self.img = img
        self.color = color

    def move(self):
        raise AssertionError('The method is not defined')

    def draw_move(self):
        raise AssertionError('The method is not defined')

    def draw(self, screen, x, y):
        screen.blit(self.img, (x*64, y*64))


class Empty(Piece):

    def __init__(self):
        pass

    def move(self):
        pass
    def draw(self, screen, x, y):
        pass
class Pawn(Piece):

    def move(self):
        print('The method is defined')

    def draw_move(self):
        pass


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

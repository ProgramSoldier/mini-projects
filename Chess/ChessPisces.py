class Piece():
    def __init__(self, img, color, x, y):
        self.img = img
        self.color = color# If True when piece is white else black
        self.x = x
        self.y = y

    def move(self):
        raise AssertionError('The method is not defined')

    def draw_move(self):
        raise AssertionError('The method is not defined')

    def draw(self, screen, x, y):
        screen.blit(self.img, (x*64, y*64))
    def name(self):
        pass


class Empty(Piece):# класс пустоты

    def __init__(self):
        pass
    def move(self):
        pass
    def draw(self, screen, x, y):
        pass
    def name(self):
        return 'Empty'
class Pawn(Piece):# класс пешки
    first_move = True
    def move(self, board, x, y):
        result = False
        if self.color:# ход для белой пешки
            if type(board[y][x]) == Empty:# ход вперёд
                if self.first_move and x == self.x and y in (self.y-1, self.y-2):# первый ход пешки
                    if y + 2 == self.y and x == self.x:
                        board[y + 2][x], board[y][x] = board[y][x], board[y + 2][x]
                        self.y -= 2
                    self.first_move = False
                    result = True
                if y+1 == self.y and x == self.x:
                    board[y+1][x], board[y][x] = board[y][x], board[y+1][x]
                    self.y -= 1
                    result = True
            elif (x == self.x + 1 or x == self.x - 1) and y == self.y - 1 and board[y][x].color != self.color:# ход для съедения
                board[self.y][self.x] = Empty()
                board[y][x] = self
                self.x, self.y = x, y
                result = True
                if self.first_move:
                    self.first_move = False
        # ход для чёрной пешки
        else:
            # ход вперёд
            if type(board[y][x]) == Empty:
                if self.first_move and x == self.x and y in (self.y+1, self.y+2):# первый ход пешки
                    if y - 2 == self.y and x == self.x:
                        board[y - 2][x], board[y][x] = board[y][x], board[y - 2][x]
                        self.y += 2
                    self.first_move = False
                    result = True
                if x == self.x and y-1 == self.y:#ход пешки
                    board[y-1][x], board[y][x] = board[y][x], board[y-1][x]
                    self.y += 1
                    result = True
            # ход для съедения
            elif (x == self.x + 1 or x == self.x - 1) and y == self.y + 1 and board[y][x].color != self.color:
                board[self.y][self.x] = Empty()
                board[y][x] = self
                self.x, self.y = x, y
                result = True
                if self.first_move:
                    self.first_move = False
        return result


    def draw_move(self,board, x, y):# отрисовка возмжных ходов
        if self.color:
            if ((x == self.x and y == self.y) or
                (y+1 == self.y and x == self.x and type(board[y][x]) == Empty) or
                (self.first_move and x == self.x and y+2 == self.y and type(board[y][x]) == Empty and type(board[y+1][x]) == Empty) or
                (y+1 == self.y and x in (self.x+1, self.x-1) and type(board[y][x]) != Empty and board[y][x].color != self.color)):
                    return True

        else:
            if ((x == self.x and y == self.y) or
                (y - 1 == self.y and x == self.x and type(board[y][x]) == Empty) or
                (self.first_move and (x == self.x and y - 2 == self.y) and type(board[y][x]) == Empty and type(board[y-1][x]) == Empty) or
                (y - 1 == self.y and x in (self.x + 1, self.x - 1) and type(board[y][x]) != Empty and board[y][x].color != self.color)):
                    return True
        pass
    def name(self):
        return 'Pawn'


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

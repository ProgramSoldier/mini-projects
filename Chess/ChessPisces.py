class Piece():
    def __init__(self, img, color, x, y):
        self.img = img
        self.color = color  # If True when piece is white else black
        self.x = x
        self.y = y
        self.active_move = []

    def find_active_move(self, board):
        raise AttributeError('Функция не определена')

    def move(self, board, x, y):
        if (y, x) in self.active_move:
            board[y][x] = self
            board[self.y][self.x] = empty
            self.x = x
            self.y = y
            self.active_move = []
            return True

    def draw_move(self, board, x, y):
        self.active_move.clear()
        self.find_active_move(board)
        if (y, x) in self.active_move or (self.x == x and self.y == y):
            return True

    def draw(self, screen, x, y):
        screen.blit(self.img, (x * 64, y * 64))

    def name(self):
        pass


class Empty(Piece):  # класс пустоты

    def __init__(self):
        self.color = None

    def draw(self, screen, x, y):
        pass

    def name(self):
        return 'Empty'


empty = Empty()


class Pawn(Piece):  # класс пешки
    first_move = True

    def find_active_move(self, board):
        if self.color:
            if self.y - 1 >= 0 and board[self.y - 1][self.x] == empty:
                self.active_move.append((self.y-1, self.x))
            if self.y - 2 >= 0 and self.first_move and board[self.y - 2][self.x] == empty:
                self.active_move.append((self.y - 2, self.x))
            if self.y - 1 >= 0 and self.x + 1 < 8 and board[self.y - 1][self.x + 1] != empty and board[self.y - 1][self.x + 1].color != self.color:
                self.active_move.append((self.y - 1, self.x + 1))
            if self.y - 1 >= 0 and self.x - 1 >= 0 and board[self.y - 1][self.x - 1] != empty and board[self.y - 1][self.x - 1].color != self.color:
                self.active_move.append((self.y - 1, self.x - 1))
        else:
            if self.y + 1 < 8 and board[self.y + 1][self.x] == empty:
                self.active_move.append((self.y+1, self.x))
            if self.first_move and self.y + 2 < 8 and board[self.y + 2][self.x] == empty:
                self.active_move.append((self.y + 2, self.x))
            if self.y + 1 < 8 and self.x + 1 < 8 and board[self.y + 1][self.x + 1] != empty and board[self.y + 1][self.x + 1].color != self.color:
                self.active_move.append((self.y + 1, self.x + 1))
            if self.y + 1 < 8 and self.x - 1 >= 0 and board[self.y + 1][self.x - 1] != empty and board[self.y - 1][self.x - 1].color != self.color:
                self.active_move.append((self.y + 1, self.x - 1))

    def move(self, board, x, y):
        if (y, x) in self.active_move:
            if self.first_move:
                self.first_move = False
            board[y][x] = self
            board[self.y][self.x] = empty
            self.x = x
            self.y = y
            self.active_move = []
            return True


    def name(self):
        return 'Pawn'


class Rook(Piece):

    def find_active_move(self, board):
        isTrue = [True, True, True, True]  # Up, Down, Left, Right
        for i in range(1, 8):

            # Поиск клеток сверху
            if isTrue[0] and self.y - i >= 0:
                if board[self.y - i][self.x].color != self.color:
                    self.active_move.append((self.y - i, self.x))
                if board[self.y - i][self.x] != empty:
                    isTrue[0] = False

            # Поиск клеток снизу
            if isTrue[1] and self.y + i < 8:
                if board[self.y + i][self.x].color != self.color:
                    self.active_move.append((self.y + i, self.x))
                if board[self.y + i][self.x] != empty:
                    isTrue[1] = False

            # Поиск клеток слева
            if isTrue[2] and self.x - i >= 0:
                if board[self.y][self.x - i].color != self.color:
                    self.active_move.append((self.y, self.x - i))
                if board[self.y][self.x - i] != empty:
                    isTrue[2] = False

            # Поиск клеток справа
            if isTrue[3] and self.x + i < 8:
                if board[self.y][self.x + i].color != self.color:
                    self.active_move.append((self.y, self.x + i))
                if board[self.y][self.x + i] != empty:
                    isTrue[3] = False

    def name(self):
        return 'Rook'


class Knight(Piece):


    def find_active_move(self, board):
        for y, x in {
            (self.y - 2, self.x + 1), (self.y - 2, self.x - 1), (self.y - 1, self.x + 2), (self.y + 1, self.x + 2),
            (self.y - 1, self.x - 2), (self.y + 1, self.x - 2), (self.y + 2, self.x + 1), (self.y + 2, self.x - 1)}:
            if 0 <= y < 8 and 0 <= x < 8:
                if board[y][x].color != self.color:
                    self.active_move.append((y, x))

    def name(self):
        pass


class Bishop(Piece):

    def find_active_move(self, board):
        isTrue = [True, True, True, True]  # Up-Left, Up-Right, Down-Left, Down-Right
        for i in range(1, 8):

            # Поиск клеток сверху-слева
            if isTrue[0] and self.y - i >= 0 and self.x - i >= 0:
                if board[self.y - i][self.x - i].color != self.color:
                    self.active_move.append((self.y - i, self.x - i))
                if board[self.y - i][self.x - i] != empty:
                    isTrue[0] = False

            # Поиск клеток сверху-справа
            if isTrue[1] and self.y - i >= 0 and self.x + i < 8:
                if board[self.y - i][self.x + i].color != self.color:
                    self.active_move.append((self.y - i, self.x + i))
                if board[self.y - i][self.x + i] != empty:
                    isTrue[1] = False

            # Поиск клеток снизу-слева
            if isTrue[2] and self.x - i >= 0 and self.y + i < 8:
                if board[self.y + i][self.x - i].color != self.color:
                    self.active_move.append((self.y + i, self.x - i))
                if board[self.y + i][self.x - i] != empty:
                    isTrue[2] = False

            # Поиск клеток снизу-справа
            if isTrue[3] and self.x + i < 8 and self.y + i < 8:
                if board[self.y + i][self.x + i].color != self.color:
                    self.active_move.append((self.y + i, self.x + i))
                if board[self.y + i][self.x + i] != empty:
                    isTrue[3] = False

    def name(self):
        return 'Bishop'


class Queen(Piece):
    def find_active_move(self, board):
        isTrue = [True, True, True, True, True, True, True, True]  # Up, Down, Left, Right, Up-Left, Up-Right, Down-Left, Down-Right
        for i in range(1, 8):

            # Поиск клеток сверху
            if isTrue[0] and self.y - i >= 0:
                if board[self.y - i][self.x].color != self.color:
                    self.active_move.append((self.y - i, self.x))
                if board[self.y - i][self.x] != empty:
                    isTrue[0] = False

            # Поиск клеток снизу
            if isTrue[1] and self.y + i < 8:
                if board[self.y + i][self.x].color != self.color:
                    self.active_move.append((self.y + i, self.x))
                if board[self.y + i][self.x] != empty:
                    isTrue[1] = False

            # Поиск клеток слева
            if isTrue[2] and self.x - i >= 0:
                if board[self.y][self.x - i].color != self.color:
                    self.active_move.append((self.y, self.x - i))
                if board[self.y][self.x - i] != empty:
                    isTrue[2] = False

            # Поиск клеток справа
            if isTrue[3] and self.x + i < 8:
                if board[self.y][self.x + i].color != self.color:
                    self.active_move.append((self.y, self.x + i))
                if board[self.y][self.x + i] != empty:
                    isTrue[3] = False

            # Поиск клеток сверху-слева
            if isTrue[4] and self.y - i >= 0 and self.x - i >= 0:
                if board[self.y - i][self.x - i].color != self.color:
                    self.active_move.append((self.y - i, self.x - i))
                if board[self.y - i][self.x - i] != empty:
                    isTrue[4] = False

            # Поиск клеток сверху-справа
            if isTrue[5] and self.y - i >= 0 and self.x + i < 8:
                if board[self.y - i][self.x + i].color != self.color:
                    self.active_move.append((self.y - i, self.x + i))
                if board[self.y - i][self.x + i] != empty:
                    isTrue[5] = False

            # Поиск клеток снизу-слева
            if isTrue[6] and self.x - i >= 0 and self.y + i < 8:
                if board[self.y + i][self.x - i].color != self.color:
                    self.active_move.append((self.y + i, self.x - i))
                if board[self.y + i][self.x - i] != empty:
                    isTrue[6] = False

            # Поиск клеток снизу-справа
            if isTrue[7] and self.x + i < 8 and self.y + i < 8:
                if board[self.y + i][self.x + i].color != self.color:
                    self.active_move.append((self.y + i, self.x + i))
                if board[self.y + i][self.x + i] != empty:
                    isTrue[7] = False

    def name(self):
        return 'Queen'


class King(Piece):
    count = 0
    def __init__(self, img, color, x, y):
        super().__init__(img, color, x, y)
        King.count += 1

    def __del__(self):
        King.count -= 1

    def find_active_move(self, board):
        for y, x in {
            (self.y - 1, self.x - 1), (self.y - 1, self.x), (self.y - 1, self.x + 1),
            (self.y , self.x - 1),(self.y , self.x + 1),
            (self.y + 1, self.x - 1), (self.y + 1, self.x), (self.y + 1, self.x + 1)}:
            if 0 <= y < 8 and 0 <= x < 8:
                if board[y][x].color != self.color:
                    self.active_move.append((y, x))

    def name(self):
        return 'King'

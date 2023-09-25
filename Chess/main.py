import pygame
from ChessPisces import *
from load_img import *

pygame.init()

screen = pygame.display.set_mode((512, 512))
run = True

#доска с фигурами

board = [[Rook(img_b_rook_serf, False,  0, 0), Knight(img_b_knight_serf, False, 1, 0), Bishop(img_b_bishop_serf, False, 2, 0), Queen(img_b_queen_serf, False, 3, 0), King(img_b_king_serf, False, 4, 0), Bishop(img_b_bishop_serf, False, 5, 0), Knight(img_b_knight_serf, False, 6, 0), Rook(img_b_rook_serf, False,  7, 0)],
         [Pawn(img_b_pawn_serf, False, 0, 1), Pawn(img_b_pawn_serf, False, 1, 1), Pawn(img_b_pawn_serf, False, 2, 1), Pawn(img_b_pawn_serf, False, 3, 1), Pawn(img_b_pawn_serf, False, 4, 1), Pawn(img_b_pawn_serf, False, 5, 1), Pawn(img_b_pawn_serf, False, 6, 1), Pawn(img_b_pawn_serf, False, 7, 1)],
         [empty, empty, empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty, empty, empty],
         [Pawn(img_w_pawn_serf, True, 0, 6),  Pawn(img_w_pawn_serf, True, 1, 6),Pawn(img_w_pawn_serf, True, 2, 6), Pawn(img_w_pawn_serf, True, 3, 6), Pawn(img_w_pawn_serf, True, 4, 6), Pawn(img_w_pawn_serf, True, 5, 6),Pawn(img_w_pawn_serf, True, 6, 6), Pawn(img_w_pawn_serf, True, 7, 6)],
         [Rook(img_w_rook_serf, True,  0, 7), Knight(img_w_kinght_serf, True, 1, 7), Bishop(img_w_bishop_serf, True, 2, 7), Queen(img_w_queen_serf, True, 3, 7), King(img_w_king_serf, True, 4, 7), Bishop(img_w_bishop_serf, True, 5,7), Knight(img_w_kinght_serf, True, 6, 7), Rook(img_w_rook_serf, True,  7, 7)]]
active = None
player_w = True
while run:

    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:# Выключение игры
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:# обработка ЛКМ
            x, y = pygame.mouse.get_pos()
            if type(board[y//64][x//64]) != Empty and board[y//64][x//64].color == player_w:# Выбор активной фигуры, с возможностью выбрать другую фигуру, если уже одна выбрана
                active = board[y//64][x//64]
            elif active:# Выполнить ход фигуры, если это возможно. Метод move возвращет True, если ход сделан, иначе False
                if active.move(board, x// 64, y//64):
                    if King.count == 1: # условие окончания игры (надо съесть вражеского короля)
                        run = False
                        print(f'{("Black","White")[player_w]} WIN!!!')
                    player_w = not player_w #Смена игрока
                    active = None



        '''
        # Этот блок позволяет нажатием мыши узнать положение фигур на доске в реальном времени
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            print('+++++++++++++++++++++++++++++++++++')
            for y, line in enumerate(board):
                print(*map(lambda x: x.name(), line))
            print('+++++++++++++++++++++++++++++++++++')
        '''

    # отрисовка доски
    for y, line in enumerate(board):
        for x, obj in enumerate(line):
            color = 215*-(((y+x)%2)-1)+40 #вычисление цвета для каждой клетки
            if active and active.draw_move(board, x, y):# отрсовка возможных ходов фигуры, если она активная
                pygame.draw.rect(screen, (255, 255, 0), (x * 64, y * 64, 64, 64))
                pygame.draw.rect(screen, (color, color, color), (x * 64 + 5, y * 64 + 5, 54, 54))
            else:#если клетка неактивна
                pygame.draw.rect(screen, (color, color, color), (x * 64, y * 64, 64, 64))

            obj.draw(screen, x, y) #отрисовка объектка, если это не Empty
    # обновление экрана
    pygame.display.update()
pygame.quit()
import pygame
#from random import randint
from ChessPisces import *
from load_img import *

pygame.init()

screen = pygame.display.set_mode((512, 512))
run = True

board = [[Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
         [Pawn(img_b_pawn_serf, 'b'), Pawn(img_b_pawn_serf, 'b'), Pawn(img_b_pawn_serf, 'b'), Pawn(img_b_pawn_serf, 'b'), Pawn(img_b_pawn_serf, 'b'), Pawn(img_b_pawn_serf, 'b'), Pawn(img_b_pawn_serf, 'b'), Pawn(img_b_pawn_serf, 'b')],
         [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
         [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
         [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
         [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()],
         [Pawn(img_w_pawn_serf, 'w'), Pawn(img_w_pawn_serf, 'w'),Pawn(img_w_pawn_serf, 'w'), Pawn(img_w_pawn_serf, 'w'), Pawn(img_w_pawn_serf, 'w'), Pawn(img_w_pawn_serf, 'w'),Pawn(img_w_pawn_serf, 'w'), Pawn(img_w_pawn_serf, 'w')],
         [Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty(), Empty()]]

active = None
while run:

    # цикл обработки событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = pygame.mouse.get_pos()
                if type(board[y//64][x//64]) != Empty:
                    active = board[y//64][x//64]

    # --------
    # изменение объектов
    # --------
    for y, line in enumerate(board):
        for x, obj in enumerate(line):
            color = 215*-(((y+x)%2)-1)+40
            if obj is active:
                pygame.draw.rect(screen, (255, 255, 0), (x * 64, y * 64, 64, 64))
                pygame.draw.rect(screen, (color, color, color), (x * 64 + 5, y * 64 + 5, 54, 54))
            else:
                pygame.draw.rect(screen, (color, color, color), (x * 64, y * 64, 64, 64))
            obj.draw(screen, x, y)

    # обновление экрана
    pygame.display.update()
for y, line in enumerate(board):
    print(*line)
pygame.quit()
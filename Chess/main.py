import pygame
from random import randint

class Empty():
    pass





pygame.init()

screen = pygame.display.set_mode((640, 640))
run = True

board = []
while run:

    # задержка

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
    for i in (0,1,2,3,4,5,6,7):
        for j in (0, 1, 2, 3, 4, 5, 6, 7):
            pygame.draw.rect(screen, (randint(1, 100),randint(1, 100),randint(1, 100)), (j*80, i*80, 80, 80 ))
    # --------
    # изменение объектов
    # --------
    for i in (0,1,2,3,4,5,6,7):
        for j in (0, 1, 2, 3, 4, 5, 6, 7):
            pygame.draw.rect(screen, (randint(1, 100),randint(1, 100),randint(1, 100)), (j*80, i*80, 80, 80))
    # обновление экрана
    pygame.display.update()

pygame.quit()
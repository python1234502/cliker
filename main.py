import pygame
import sys

#Инициализация необходимых объектов
scr = pygame.display.set_mode((800,600))

#Игровой цикл
while True:

    scr.fill((255, 255, 255))
    pygame.display.update()

    for i in pygame.event.get():
        if i.type  == pygame.QUIT:
            pygame.quit()
            sys.exit()
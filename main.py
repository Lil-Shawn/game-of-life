import random
import pygame
import copy

l = [[random.choice([0, 1]) for i in range(48)] for i in range(48)]
k = [[0 for i in range(48)] for i in range(48)]

pygame.init()
s = pygame.display.set_mode((480, 480), 0, 32)
o = True


def z(x, y):
    m = 0
    for i in (x - 1, x, x + 1):
        for j in (y - 1, y, y + 1):
            if i == x and y == j:
                continue
            if i < 0 or i > 47 or j < 0 or j > 47:
                continue
            if l[i][j] == 1:
                m += 1
    return m


while o:
    s.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            o = False

    for x in range(48):
        for y in range(48):
            a = z(x, y)
            if a == 2:
                k[x][y] = l[x][y]
            elif a == 3:
                k[x][y] = 1
            else:
                k[x][y] = 0
    for x in range(48):
        for y in range(48):
            if k[x][y] == 1:
                s.fill((0, 0, 255), (y * 10, x * 10, 10, 10))
                pygame.draw.rect(s, (0, 0, 0), (y * 10, x * 10, 10, 10), 1)
                l = copy.deepcopy(k)
    pygame.display.update()
    pygame.time.wait(100)

import pygame
import os
import random
pygame.init()

Maze = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,1,1,0,1,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,1,1,1,0,1,1,1,0,1,1,1,0,0,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1],
    [1,1,1,1,1,1,0,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,1,1,0,0,0,0,1],
    [1,1,0,0,0,0,0,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,0,1,1,0,1,1,1,1],
    [1,0,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1],
    [1,0,1,1,1,1,1,1,0,1,1,1,1,1,1,1,0,1,1,1,0,0,0,0,1,0,1,1,0,1,1,1,1],
    [1,0,0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,0,1,1,0,1,1,1,1,0,1,1,0,0,0,0,1,1,1,1,0,0,1,1,1],
    [1,1,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,0,1,0,1,1,1,1],
    [1,1,1,0,1,1,1,0,0,1,1,1,0,0,0,0,1,1,1,0,1,1,1,1,1,1,0,0,0,1,1,1,1],
    [1,1,1,0,0,0,1,0,1,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,0,1,1,1,1],
    [1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,0,1],
    [1,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1],
    [1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1],

]

X_X = 1320
Y_Y = 800
keyx = 23
keyy = 2
Keytrue = False
Run = True
cell_size = 40
Size_X = int(X_X/cell_size)
Size_Y = int(Y_Y/cell_size)
exitX = 28
exitY = 19
Main_chrctrX = 1
Main_chrctrY = 1

screen = pygame.display.set_mode((X_X, Y_Y))
Wall_img = pygame.image.load(os.path.join("Project", "assets", "Wall.jpg")).convert_alpha()
Wall_img = pygame.transform.scale(Wall_img, (cell_size, cell_size))

Main_chrctr = pygame.image.load(os.path.join("Project", "assets", "Main_character.png")).convert_alpha()
Main_chrctr = pygame.transform.scale(Main_chrctr, (cell_size, cell_size))

Map_img = pygame.image.load(os.path.join("Project", "assets", "map.webp")).convert_alpha()
Map_img = pygame.transform.scale(Map_img, (cell_size, cell_size))

exit = pygame.image.load(os.path.join("Project", "assets", "Exit.jpg")).convert_alpha()
exit = pygame.transform.scale(exit, (cell_size, cell_size))

maptaken = False

while Run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a and Maze[Main_chrctrY][Main_chrctrX - 1] == 0:
                Main_chrctrX -= 1
            if event.key == pygame.K_d and Maze[Main_chrctrY][Main_chrctrX + 1] == 0:
                Main_chrctrX += 1
            if event.key == pygame.K_w and Maze[Main_chrctrY - 1][Main_chrctrX] == 0:
                Main_chrctrY -= 1
            if event.key == pygame.K_s and Maze[Main_chrctrY + 1][Main_chrctrX] == 0:
                Main_chrctrY += 1

    if Main_chrctrX == keyx and Main_chrctrY == keyy:
        Keytrue = True
        maptaken = True
    if Main_chrctrX == exitX and Main_chrctrY == exitY:
        break

    for x in range(len(Maze)):
        for y in range(len(Maze[0])):
            if Maze[x][y] == 1:
                screen.blit(Wall_img,(cell_size*y,cell_size*x))

    screen.blit(Main_chrctr,(cell_size*Main_chrctrX,cell_size*Main_chrctrY))     
    screen.blit(exit,(cell_size*exitX,cell_size*exitY))    
    
    if not Keytrue:
        screen.blit(Map_img,(cell_size*keyx,cell_size*keyy))     

    if not maptaken:    
        for y in range(len(Maze)):
            for x in range(len(Maze[0])):
                if abs(x - Main_chrctrX) > 2 or abs(y - Main_chrctrY) > 2:
                    pygame.draw.rect(screen,(0,0,0),(cell_size*x,cell_size*y,cell_size,cell_size))
    pygame.display.flip()
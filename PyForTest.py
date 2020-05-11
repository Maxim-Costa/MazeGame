import pygame
import os
from pygame.locals import *
from random import randint

os.environ['SDL_VIDEO_CENTERED'] = '1'

cell = 20

pygame.init()

maze = [[11 if i != 0 and j != 0 else 16 for j in range(64)]for i in range(53)]

fenetre = pygame.display.set_mode((1280, 1080))


def text_objects(text, color):
    smallfont = pygame.font.SysFont("comicsansms", 15)
    textSurface = smallfont.render(text, True, color)
    return textSurface, textSurface.get_rect()


def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, fenetre):
    textSurf, textRect = text_objects(msg, color)
    textRect.center = ((buttonx + (buttonwidth / 2)),
                       buttony + (buttonheight / 2))
    fenetre.blit(textSurf, textRect)


def ColorMap(p):
    sr = 0
    sg = 0
    sb = 0
    if (p < 64):
        sr = 0
        sg = p*4
        sb = 255
    elif (p < 128):
        sr = 0
        sg = 255
        sb = (255-(p-64)*4)
    elif (p < 192):
        sr = (p-128)*4
        sg = 255
        sb = 0
    elif (p < 256):
        sr = 255
        sg = (256-(p-191)*4)
        sb = 0
    return (sr, sg, sb)


def afficherPygame(maze, fenetre, pygame):
    global colorstyle
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Red = (255, 0, 0)
    Blue = (0, 0, 255)
    # On parcourt la liste du niveau
    num_ligne = 0
    modif, modifce = 1, 2
    cell = 20

    for ligne in maze:
        # On parcourt les listes de lignes
        num_case = 0
        for sprite in ligne:
            # On calcule la position réelle en pixels
            x = num_case * cell
            y = num_ligne * cell

            pygame.draw.rect(fenetre, White, (x + modif,
                                              y + modif, cell - modifce, cell - modifce))

            if sprite == 16:
                pygame.draw.rect(fenetre, White, (x + modif,
                                                  y + modif, cell - modifce, cell - modifce))
                text_to_button(str(max(num_case, num_ligne)),
                               (0, 0, 0), x, y, cell, cell, fenetre)

            elif sprite == 13:
                pygame.draw.rect(
                    fenetre, Blue, (x + modif, y + modif, cell - modifce, cell - modifce))
            elif sprite == 12:
                pygame.draw.rect(
                    fenetre, Red, (x + modif, y + modif, cell - modifce, cell - modifce))
            elif sprite == 10:
                pygame.draw.rect(fenetre, Black, (x + modif,
                                                  y + modif, cell - modifce, cell - modifce))
            elif sprite == 11:
                pygame.draw.rect(fenetre, White, (x + modif,
                                                  y + modif, cell - modifce, cell - modifce))

            num_case += 1
        num_ligne += 1
    pygame.display.update()


continuer = True
while continuer:
    pygame.time.Clock().tick(30)
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
            print(maze)
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos[0], pos[1])
            if maze[pos[1]//cell][pos[0]//cell] == 11:
                maze[pos[1]//cell][pos[0]//cell] = 13
            elif maze[pos[1]//cell][pos[0]//cell] == 13:
                maze[pos[1]//cell][pos[0]//cell] = 12
            elif maze[pos[1]//cell][pos[0]//cell] == 12:
                maze[pos[1]//cell][pos[0]//cell] = 10
            elif maze[pos[1]//cell][pos[0]//cell] == 10:
                maze[pos[1]//cell][pos[0]//cell] = 11

        afficherPygame(maze, fenetre, pygame)
        pygame.display.flip()
        pygame.display.update()

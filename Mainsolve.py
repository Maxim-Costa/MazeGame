import pygame
import os
from pygame.locals import *
from MazeGenerateurOver import generateur
from Global import globale
from random import randint

pygame.init()

pygame.OPENGL
pygame.DOUBLEBUF
pygame.HWSURFACE
os.environ['SDL_VIDEO_CENTERED'] = '1'
h, w, cell = 100, 100, 5
globale = globale(cell)


def GetMinCell(maze, lasted1, NumberPoint):
    l = {}
    m = [(lasted1[0] + 1, lasted1[1]), (lasted1[0] - 1, lasted1[1]),
         (lasted1[0], lasted1[1] + 1), (lasted1[0], lasted1[1] - 1)]
    for i in m:
        if maze[i[0]][i[1]] >= 30:
            l[NumberPoint[i]] = i
        elif maze[i[0]][i[1]] == 12:
            maze[i[0]][i[1]] = 25
            return ('Finished', i)

    return l[min(l.keys())]


def GetAfter(L):
    NewL = []
    finished = 0
    for i in L:
        NewCor = [(i[0] + 1, i[1]), (i[0] - 1, i[1]),
                  (i[0], i[1] + 1), (i[0], i[1] - 1)]
        for y, x in NewCor:
            if maze[y][x] == 11:
                NewL.append((y, x))
            if maze[y][x] == 13:
                finished = ("Finished", (y, x))
    if finished == 0:
        return NewL
    else:
        return finished


def GameStart(h, w, cell, fenetre, maze):
    L = [(55, 50)]
    NumberPoint = {(50, 50): 0}
    #maze[50][50] = 12

    continuer = True
    yTmp, xTmp = len(maze) - 2, len(maze[len(maze) - 2]) - 2
    while continuer:
        xTmp -= 1
        if maze[yTmp][xTmp] == 11:
            continuer = False
            maze[yTmp][xTmp] = 13

    SearchEnd = True
    SearchStart = False
    continuer = True
    tour = 0

    L = GetAfter(L)
    globale.afficherPygame(False, maze, fenetre)
    while continuer:
        pygame.time.Clock().tick(60)

        for event in pygame.event.get():
            if event.type == QUIT:
                continuer = False

        if SearchEnd:
            tour += 1
            for i in L:
                maze[i[0]][i[1]] = 30 + tour
                NumberPoint[i] = tour
            L = GetAfter(L)
            if L != []:
                if L[0] == 'Finished':
                    lasted = L[1]
                    SearchEnd = False
                    SearchStart = True
                    tour = 0
            else:
                SearchEnd = False
                tour = 0

            globale.afficherPygame(False, maze, fenetre)

        elif SearchStart:
            tour += 1
            Cor = GetMinCell(maze, lasted, NumberPoint)
            if Cor[0] == "Finished":
                globale.afficherPygame(False, maze, fenetre)
                print('Finish')
                SearchStart = False
            else:
                lasted = Cor
                maze[Cor[0]][Cor[1]] = 25
            globale.afficherPygame(False, maze, fenetre)
        else:
            globale.afficherPygame(False, maze, fenetre)


generateur = generateur(h, w, cell, starteur=0)
maze = generateur.start(h, w)
fenetre = pygame.display.set_mode((cell*w+2*cell, cell*h+2*cell))
GameStart(h, w, cell, fenetre, maze)

from random import *
import pygame
import sys
import os
from pygame.locals import *
from Global import globale
from time import time


class generateur:
    def __init__(self, h, w, cell, maze=None, m=True, starteur=None):
        if maze != None:
            self.maze = maze
        else:
            self.maze = []
        self.h = h
        self.w = w
        self.cell = cell
        self.Xstart = 1
        self.Ystart = 1
        self.cell = cell
        self.charW = 10
        self.charC = 11
        self.continuerPy = True
        self.m = m
        self.starteur = starteur
        """
        10 == Wall
        11 == chemin
        12 == starteur point
        and other number < 10:
            possible chemin with poid
        """

        pygame.init()
        pygame.OPENGL
        pygame.DOUBLEBUF
        pygame.HWSURFACE
        os.environ['SDL_VIDEO_CENTERED'] = '1'

        if m:
            self.fenetre = pygame.display.set_mode(
                (self.cell*self.w+2*self.cell, self.cell*self.h+2*self.cell))
            self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
            self.Master = pygame.transform.scale(pygame.image.load(
                'img/Mage.png').convert_alpha(), (200, 200))
            self.SmallBubble = pygame.transform.scale(
                pygame.image.load('img/Bubble.png').convert_alpha(), (500, 150))
        else:
            self.fenetre = pygame.display.set_mode(
                (self.cell*self.w, self.cell*self.h))
        self.fenetre.fill((0, 0, 0))
        self.globale = globale(self.cell)

    def start(self, h, w, maze=None):
        self.h, self.w = h, w
        print('Debut de le génération')
        self.fenetre.fill((0, 0, 0))
        if maze != None:
            if self.m:
                self.fenetre.blit(pygame.transform.rotate(
                    self.Master, 0), (0, 890))
                self.fenetre.blit(pygame.transform.rotate(
                    self.SmallBubble, 0), (120, 830))
                self.fenetre.blit(self.myfont.render(
                    "Niveau en cours de construction ...", True, (0, 0, 0)), (130, 840))
            self.maze = maze
        else:
            self.firstGen()
            self.Cadre()
        self.secondGen()
        self.threeGen()
        self.finishGen()
        return self.maze

    def Cadre(self):
        self.maze = [[26]+self.maze[i]+[26] for i in range(len(self.maze))]
        self.maze = [[26]*len(self.maze[0])]+self.maze+[[26]*len(self.maze[0])]

    def testCell(self, cell):
        return (cell != 12 and cell != 11 and cell != 10 and cell != 26)

    def testWall(self, cell):
        return ((cell == 12 or cell == 11) and cell != 10)

    def firstGen(self):
        tpTmp = time()
        self.maze = [[randint(0, 9) for _ in range(self.w)]
                     for _ in range(self.h)]  # self arbre
        if self.starteur == 0:
            self.Ystart, self.Xstart = 0, 0
        else:
            self.Ystart, self.Xstart = randint(
                0, self.h-1), randint(0, self.w-1)
        self.maze[self.Ystart][self.Xstart] = 12  # self a starteur point
        print('firstGen finish : ', time() - tpTmp)

    def testCell2(self, maze, L, i, j):
        L2 = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]
        for i, j in L2:
            if self.maze[i][j] != 11 and self.maze[i][j] != 10 and self.maze[i][j] != 26:
                if not (i, j) in L:
                    L.append((i, j))
                else:
                    self.maze[i][j] = 10
                    L.remove((i, j))

    def secondGen(self):
        tpTmp = time()
        itertion = 0
        continuer = True

        L = []
        self.Ystart, self.Xstart = self.Ystart + 1, self.Xstart + 1
        self.maze[self.Ystart][self.Xstart] = 11
        self.testCell2(self.maze, L, self.Ystart, self.Xstart)
        self.globale.afficherPygame(
            True, self.maze, self.fenetre)

        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            TmpPoint = []
            TmpCordo = []
            for Cor in L:
                itertion += 1
                TmpPoint.append(self.maze[Cor[0]][Cor[1]])
                TmpCordo.append(Cor)
            MiniCor = TmpCordo[TmpPoint.index(min(TmpPoint))]
            self.maze[MiniCor[0]][MiniCor[1]] = 11
            L.remove((MiniCor[0], MiniCor[1]))
            self.testCell2(self.maze, L, MiniCor[0], MiniCor[1])

            if itertion % 500 == 0:
                self.globale.afficherPygame(
                    True, self.maze, self.fenetre)

            if L == []:
                continuer = False
                self.globale.afficherPygame(
                    True, self.maze, self.fenetre)
                print('secondGen finish : ', itertion,
                      " time : ", time() - tpTmp)
                itertion = None
                # os.system('pause')

    def threeGen(self):
        tpTmp = time()
        continuer = True
        while continuer:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            for i in range(len(self.maze)):
                for j in range(len(self.maze[i])):
                    if self.maze[i][j] <= 9:
                        self.maze[i][j] = 10
                    elif self.maze[i][j] == 26:
                        self.maze[i][j] = 10
            continuer = False
        self.globale.afficherPygame(
            True, self.maze, self.fenetre)
        print('threeGen finish : ', time() - tpTmp)

    def finishGen(self):
        tpTmp = time()
        for i in range(len(self.maze)):
            for j in range(len(self.maze)):
                if self.maze[i][j] == 12:
                    self.maze[i][j] = 11
        # prin(self.maze)
        print('finish : ', time() - tpTmp)

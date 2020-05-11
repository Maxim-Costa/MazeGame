from random import *
import sys
import os
from Global import globale
from time import *


class generateur:
    def __init__(self, h, w, cell, maze=None, starteur=None):
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
        self.starteur = starteur
        self.continuerPy = True
        """
        10 == Wall
        11 == chemin
        12 == starteur point
        and other number < 10:
            possible chemin with poid
        """
        self.globale = globale(self.cell)

    def start(self, h, w, maze=None):
        self.h, self.w = h, w
        print('Debut de le génération')
        if maze != None:
            self.maze = maze
        else:
            self.firstGen()
            self.Cadre()

        self.secondGen()
        self.threeGen()
        self.finishGen()
        return self.maze

    def Cadre(self):
        self.maze = [[10]+self.maze[i]+[10] for i in range(len(self.maze))]
        self.maze = [[10]*len(self.maze[0])]+self.maze+[[10]*len(self.maze[0])]

    def testCell(self, cell):
        return (cell != 12 and cell != 11 and cell != 10)

    def testWall(self, cell):
        return ((cell == 12 or cell == 11) and cell != 10)

    def firstGen(self):
        tmTpm = time()
        self.maze = [[randint(0, 9) for _ in range(self.w)]
                     for _ in range(self.h)]  # self arbre
        if self.starteur != None:
            self.Ystart, self.Xstart = randint(
                0, self.h-1), randint(0, self.w-1)
        else:
            self.Ystart, self.Xstart = 0, 0
        self.maze[self.Ystart][self.Xstart] = 12  # self a starteur point
        print('firstGen finish : ', time()-tmTpm)

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
        tmTmp = time()
        continuer = True
        L = []
        itertion = 0
        startX, startY = 1, 1
        self.maze[startY][startX] = 11
        self.testCell2(self.maze, L, startY, startX)
        while continuer:
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
            if L == []:
                continuer = False
                print('secondGen finish : ', itertion,
                      " time : ", time() - tmTmp)
                itertion = None

    def threeGen(self):
        tmTpm = time()
        for i in range(1, len(self.maze)-1):
            for j in range(1, len(self.maze[i])-1):
                if self.maze[i][j] <= 9:

                    L = [[i+1, j], [i-1, j], [i, j+1], [i, j-1]]

                    self.globale.counts("create", 1)

                    for k in L:
                        if self.maze[k[0]][k[1]] == 11:
                            self.globale.counts("++")

                    if 0 < self.globale.counts("r") >= 2:
                        self.maze[i][j] = 11
                    else:
                        self.maze[i][j] = 10
        print('threeGen finish : ', time()-tmTpm)

    def finishGen(self):
        tmTpm = time()
        for i in range(len(self.maze)):
            for j in range(len(self.maze)):
                if self.maze[i][j] == 12:
                    self.maze[i][j] = 11
        # prin(self.maze)
        print('finish : ', time()-tmTpm)

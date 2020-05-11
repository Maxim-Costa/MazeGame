import pygame
from pygame.locals import *
from random import shuffle, choice, randint


def MobMoveChoix(self, i):
    L = []
    if verifMob(self, self.Mobcor[i][1], self.Mobcor[i][0] + 1):
        L.append('droite')
    if verifMob(self, self.Mobcor[i][1], self.Mobcor[i][0] - 1):
        L.append('gauche')
    if verifMob(self, self.Mobcor[i][1] - 1, self.Mobcor[i][0]):
        L.append('haut')
    if verifMob(self, self.Mobcor[i][1] + 1, self.Mobcor[i][0]):
        L.append('bas')
    return L


def verifMob(self, y, x):
    return (self.maze[y][x] != 10 and self.maze[y][x] != 16 and not([x, y] in self.Mobcor))


def MobMoveIA(self, MCCor, MobCor, maze, re):
    print(MCCor)
    L = [tuple(MobCor[0])]
    NumberPoint = {tuple(MobCor[0]): 0}
    tour = 0
    Continuer = True
    while Continuer:
        for i in L:
            tour += 1
            maze[i[0]][i[1]] = 30 + tour
            NumberPoint[i] = tour

        # print(L)
        if (MCCor[1], MCCor[0]) in L:
            print("find")

        L = GetAfter(L, MCCor, maze)
        if L[0] == 'Finished':
            lasted = L[1]
            tour = 0
            Continuer = False
    return "findMC"


def GetAfter(L, MCCor, maze):
    NewL = []
    finished = 0
    for i in L:
        NewCor = [(i[0] + 1, i[1]), (i[0] - 1, i[1]),
                  (i[0], i[1] + 1), (i[0], i[1] - 1)]
        for y, x in NewCor:
            try:
                if maze[y][x] == 11:
                    NewL.append((y, x))
            except:
                pass
            if (x, y) == MCCor:
                finished = ("Finished", (y, x))
    if finished == 0:
        return NewL
    else:
        return finished


def MobMove(self):
    for i in range(self.MobNumber):
        L = []
        if self.MobMoveEscape != 100:
            L = MobMoveChoix(self, i)

        if self.MobOldMove[i] == 'droite' and verifMob(self, self.Mobcor[i][1], self.Mobcor[i][0] + 1):
            self.MobOldMove[i] = 'droite'
            L += ['droite']*self.MobMoveEscape

        elif self.MobOldMove[i] == 'gauche' and verifMob(self, self.Mobcor[i][1], self.Mobcor[i][0] - 1):
            self.MobOldMove[i] = 'gauche'
            L += ['gauche']*self.MobMoveEscape

        elif self.MobOldMove[i] == 'haut' and verifMob(self, self.Mobcor[i][1] - 1, self.Mobcor[i][0]):
            self.MobOldMove[i] = 'haut'
            L += ['haut']*self.MobMoveEscape

        elif self.MobOldMove[i] == 'bas' and verifMob(self, self.Mobcor[i][1] + 1, self.Mobcor[i][0]):
            self.MobOldMove[i] = 'bas'
            L += ['bas']*self.MobMoveEscape
        if (L == None or L == []) and self.MobMoveEscape == 100:
            L = MobMoveChoix(self, i)
        if L != None and L != []:
            shuffle(L)
            action = choice(L)
        else:
            action = None

        if action == 'droite':
            try:
                if verifMob(self, self.Mobcor[i][1], self.Mobcor[i][0] + 1):
                    self.Mobcor[i][0] += 1
                    self.MobSens[i] = 90
                    self.MobOldMove[i] = 'droite'
            except:
                print('error')
        elif action == 'gauche':
            try:
                if verifMob(self, self.Mobcor[i][1], self.Mobcor[i][0] - 1):
                    self.Mobcor[i][0] -= 1
                    self.MobSens[i] = -90
                    self.MobOldMove[i] = 'gauche'
            except:
                print('error')
        elif action == 'haut':
            try:
                if verifMob(self, self.Mobcor[i][1] - 1, self.Mobcor[i][0]):
                    self.Mobcor[i][1] -= 1
                    self.MobSens[i] = -180
                    self.MobOldMove[i] = 'haut'
            except:
                print('error')
        elif action == 'bas':
            try:
                if verifMob(self, self.Mobcor[i][1] + 1, self.Mobcor[i][0]):
                    self.Mobcor[i][1] += 1
                    self.MobSens[i] = 0
                    self.MobOldMove[i] = 'bas'
            except:
                print('error')


def MobFun(self, nbMob=None, Cor=None):
    self.Mobcor, self.MobSens, self.MobOldMove = [], [], []
    if nbMob == None:
        self.MobNumber = int(max(self.w, self.h)/2)
    else:
        self.MobNumber = nbMob
    self.MobOldMove = [0]*self.MobNumber
    self.MobSens = [0]*self.MobNumber
    if self.w*self.h >= 30*30:
        startMob = 15
    else:
        startMob = min(self.h, self.w)//2

    for _ in range(self.MobNumber):
        x, y = 0, 0
        Continuer = True
        while Continuer:
            if Cor != None:
                x = Cor[0]
                y = Cor[1]
                Continuer = False
            else:
                y = randint(5, len(self.maze)-1)
                x = randint(5, len(self.maze)-1)
                if (self.maze[y][x] == 11 and (y > startMob or x > startMob)):
                    Continuer = False
        self.Mobcor.append([x, y])


def MobAdventure(self):
    self.i += 1
    if self.i % 6 == 0:
        MobMove(self)
        self.i = 0

    for i in range(self.MobNumber):
        self.fenetre.blit(pygame.transform.rotate(self.MobIM, self.MobSens[i]), (
            self.cell*self.Mobcor[i][0]+1, self.cell*self.Mobcor[i][1]+1))
    gameOver = self.GameTest()
    pygame.display.flip()
    return gameOver

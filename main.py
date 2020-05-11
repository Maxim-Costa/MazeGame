import pygame
import os
import Niveau
import Menu
import MobControler
import time
import math
from MazeGenerateur import generateur
from pygame.locals import *
from Global import globale
from os import system
from random import *
from PauseMenu import *
from network import Network

pygame.init()
pygame.key.set_repeat(1, 60)
try:
    pygame.ftfont.init()
except:
    pygame.font.init()

pygame.OPENGL
pygame.DOUBLEBUF
pygame.HWSURFACE

os.environ['SDL_VIDEO_CENTERED'] = '1'


class MainGame:
    def __init__(self):

        self.maze = []
        self.h = 40
        self.w = 40
        self.cell = 20
        self.charW = 10
        self.charC = 11
        self.Xstart = randint(0, self.w-1)
        self.Ystart = randint(0, self.h-1)
        self.counter = []
        self.MobMoveEscape = 29
        self.i = 0
        self.GetKey = 0
        self.NiveauActu = None
        self.live = True
        """
        10 == Wall
        11 == chemin
        12 == starteur point
        and other number < 10:
            possible chemin with poid
        """

        self.continuerPy = True

        self.Portal = []

        self.fenetre = pygame.display.set_mode(
            (self.cell*self.w+2*self.cell, self.cell*self.h+2*self.cell))

        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.smallfont = pygame.font.SysFont("comicsansms", 25)
        self.medfont = pygame.font.SysFont("comicsansms", 50)
        self.largefont = pygame.font.SysFont("comicsansms", 85)
        self.textsurface = self.medfont.render('Game Over', True, (255, 0, 0))

        self.MCXcor, self.MCYcor, self.MCSens = None, None, 90
        self.MCMove = []
        self.MCIM = pygame.transform.scale(pygame.image.load(
            'img/MC.png').convert_alpha(), (self.cell-2, self.cell-2))

        self.MobNumber = 0
        self.Mobcor, self.MobSens, self.MobOldMove = [], [], []
        self.MobIM = pygame.transform.scale(pygame.image.load(
            'img/Mob.png').convert_alpha(), (self.cell-2, self.cell-2))

        self.globale = globale(self.cell)
        self.generateur = generateur(self.h, self.w, self.cell)

        self.Master = pygame.transform.scale(pygame.image.load(
            'img/Mage.png').convert_alpha(), (200, 200))
        self.SmallBubble = pygame.transform.scale(
            pygame.image.load('img/Bubble.png').convert_alpha(), (400, 150))
        self.BigBubble = pygame.transform.scale(
            pygame.image.load('img/Bubble.png').convert_alpha(), (650, 150))
        self.Bigkey = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('img/Key.png').convert_alpha(), (100, 100)), -20)
        self.BackKeys = pygame.transform.rotate(pygame.transform.scale(
            pygame.image.load('img/BackKeys.png').convert_alpha(), (100, 100)), -20)
        self.Bubble = self.SmallBubble

        self.MultiSens = pygame.transform.scale(
            pygame.image.load('img/sens.png').convert_alpha(), (60, 240))

        self.pause, self.AnimationKey, self.AnimationCadena = False, False, False

        self.CadenaAni = []
        for i in range(1, 7):
            self.CadenaAni.append(pygame.transform.scale(pygame.image.load(
                'img/cadena/Cadena'+str(i)+'.png').convert_alpha(), (200, 200)))

        self.MCMaze = 0
        self.Menu = Menu
        self.MobC = MobControler

    def verifMC(self, NewPosi):
        return NewPosi != 10 and (NewPosi != 15 or (NewPosi == 15 and self.GetKey >= 2))

    def deplacerMC(self, action):

        if action == 'droite':
            try:
                if self.verifMC(self.maze[self.MCYcor][self.MCXcor + 1]):
                    self.MCXcor += 1
                    self.MCSens = 90
            except:
                print('error')

        elif action == 'gauche':
            try:
                if self.verifMC(self.maze[self.MCYcor][self.MCXcor - 1]):
                    self.MCXcor -= 1
                    self.MCSens = -90
            except:
                print('error')

        elif action == 'haut':
            try:
                if self.verifMC(self.maze[self.MCYcor - 1][self.MCXcor]):
                    self.MCYcor -= 1
                    self.MCSens = -180
            except:
                print('error')

        elif action == 'bas':
            try:
                if self.verifMC(self.maze[self.MCYcor + 1][self.MCXcor]):
                    self.MCYcor += 1
                    self.MCSens = 0
            except:
                print('error')

        if self.maze[self.MCYcor][self.MCXcor] == 14:
            self.maze[self.MCYcor][self.MCXcor] = 11
            self.GetKey += 1
            print('Key : ', self.GetKey)
            self.AnimationKey = True
            self.globale.counts("create", 1)

        if self.maze[self.MCYcor][self.MCXcor] == 15 and self.GetKey >= 2:
            print("Key : ", self.GetKey, "- 2")
            self.GetKey -= 2
            self.maze[self.MCYcor][self.MCXcor] = 11
            self.AnimationCadena = True
            self.SaveChange = True
            self.globale.counts("create", 1)

        if self.maze[self.MCYcor][self.MCXcor] == 16:
            self.MCYcor, self.MCXcor = self.Portal[(self.Portal.index(
                (self.MCYcor, self.MCXcor)) + 1) % len(self.Portal)]

    def fenetrePygame(self):
        self.fenetre.blit(pygame.transform.rotate(
            self.MCIM, self.MCSens), (self.cell*self.MCXcor+1, self.cell*self.MCYcor+1))

        self.globale.counts('++')
        if self.globale.counts('r') % 12 == 0:
            self.MobC.MobMove(self)
            self.globale.counts('create', 1)
        for i in range(self.MobNumber):
            self.fenetre.blit(pygame.transform.rotate(self.MobIM, self.MobSens[i]), (
                self.cell*self.Mobcor[i][0]+1, self.cell*self.Mobcor[i][1]+1))
        gameOver = self.GameTest()
        pygame.display.flip()
        return gameOver

    def GameTest(self):
        if [self.MCXcor, self.MCYcor] in self.Mobcor:
            return True
        return False

    def GameStart(self):
        self.MobC.MobFun(self)
        continuer = True
        self.globale.counts('create', 1)
        while continuer:
            if self.maze[1][self.globale.counts('r')] == 11:
                continuer = False
                self.MCXcor, self.MCYcor = self.globale.counts('r'), 1
            else:
                self.globale.counts('++')
        self.MCXcor, self.MCYcor
        continuer = True
        self.globale.afficherPygame(False, self.maze, self.fenetre)
        self.globale.counts('create', 1)
        while continuer:

            pygame.time.Clock().tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = False

                key_pressed = pygame.key.get_pressed()
                if key_pressed[K_RIGHT]:
                    self.deplacerMC('droite')
                elif key_pressed[K_LEFT]:
                    self.deplacerMC('gauche')
                elif key_pressed[K_UP]:
                    self.deplacerMC('haut')
                elif key_pressed[K_DOWN]:
                    self.deplacerMC('bas')

            self.globale.afficherPygame(False, self.maze, self.fenetre, True)
            gameOver = self.fenetrePygame()
            if gameOver:
                continuer = False
        if gameOver:
            self.GameOver()

    def GameOver(self):
        continuer = True
        self.fenetre = pygame.display.set_mode((500, 500))
        self.globale.counts('create', 1)
        while continuer:

            pygame.time.Clock().tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    continuer = False
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if 180+150 > pos[0] > 180 and 260+50 > pos[1] > 260:
                        print('Menu')
                        continuer = False
                        self.fenetre.fill((0, 0, 0))
                    elif 180+150 > pos[0] > 180 and 320+50 > pos[1] > 320:
                        print('left game')
                        continuer = False
                        quit()

            cur = pygame.mouse.get_pos()
            self.fenetre.blit(self.textsurface, (125, 150))
            pygame.draw.rect(self.fenetre, (0, 150, 150),
                             (182, 262, 150, 50), 3)
            if 180+150 > cur[0] > 180 and 260+50 > cur[1] > 260:
                pygame.draw.rect(self.fenetre, (0, 255, 255),
                                 (180, 260, 150, 50))
            else:
                pygame.draw.rect(self.fenetre, (0, 200, 200),
                                 (180, 260, 150, 50))

            pygame.draw.rect(self.fenetre, (150, 0, 0), (182, 322, 150, 50), 3)
            if 180+150 > cur[0] > 180 and 320+50 > cur[1] > 320:
                pygame.draw.rect(self.fenetre, (255, 0, 0),
                                 (180, 320, 150, 50))
            else:
                pygame.draw.rect(self.fenetre, (200, 0, 0),
                                 (180, 320, 150, 50))
            self.Menu.text_to_button(
                self, "Menu", (0, 0, 0), 180, 260, 150, 50)
            self.Menu.text_to_button(
                self, "LEFT GAME", (0, 0, 0), 180, 320, 150, 50)
            pygame.display.update()

    def StartMenu(self):
        GameNotFinish = True
        Play = 'Menu'
        while GameNotFinish:
            Play = 'Menu'
            continuer = True
            MenuChoix = "menu"

            self.fenetre = pygame.display.set_mode((500, 500))

            self.globale.counts("create", 1)
            self.globale.counts("++")

            Menufont = [[choice([0, 10, 13, 12])
                         for _ in range(50)]for _ in range(50)]
            self.globale.afficherPygame(True, Menufont, self.fenetre)

            while continuer:

                pygame.time.Clock().tick(60)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer = False
                        GameNotFinish = False
                        quit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        pos = pygame.mouse.get_pos()
                        if MenuChoix == 'menu':
                            if 180+150 > pos[0] > 180 and 200+50 > pos[1] > 200:
                                print('jouer')
                                self.fenetre.fill((0, 0, 0))
                                if Play != "Adventure" and Play != "Multi":
                                    Play = 'Play'
                                continuer = False

                            elif 180+150 > pos[0] > 180 and 260+50 > pos[1] > 260:
                                print('settings')
                                MenuChoix = 'setting'
                                self.fenetre.fill((0, 0, 0))
                                Menufont = [
                                    [choice([0, 10, 13, 12]) for _ in range(50)]for _ in range(50)]
                                self.globale.afficherPygame(
                                    True, Menufont, self.fenetre)
                            elif 180+150 > pos[0] > 180 and 320+50 > pos[1] > 320:
                                print('left game')
                                continuer = False
                                GameNotFinish = False
                                quit()
                            else:
                                print(pos)

                        elif MenuChoix == 'setting':
                            if 40 > pos[0] > 0 and 40 > pos[1] > 0:
                                print('retour menu')
                                MenuChoix = 'menu'
                                self.fenetre.fill((0, 0, 0))
                                Menufont = [
                                    [choice([0, 10, 13, 12]) for _ in range(50)]for _ in range(50)]
                                self.globale.afficherPygame(
                                    True, Menufont, self.fenetre)
                            elif 80+150 > pos[0] > 80 and 260+50 > pos[1] > 260:
                                self.h, self.w = 10, 10
                                Play = 'Play'
                            elif 260+150 > pos[0] > 260 and 260+50 > pos[1] > 260:
                                self.h, self.w = 20, 20
                                Play = 'Play'
                            elif 80+150 > pos[0] > 80 and 340+50 > pos[1] > 340:
                                self.h, self.w = 40, 40
                                Play = 'Play'
                            elif 260+150 > pos[0] > 260 and 340+50 > pos[1] > 340:
                                self.h, self.w = 50, 50
                                Play = 'Play'
                            elif 80+150 > pos[0] > 80 and 420+50 > pos[1] > 420:
                                # Adventure Huistory
                                self.h, self.w = 40, 50
                                Play = 'Adventure'
                            elif 260+150 > pos[0] > 260 and 420+50 > pos[1] > 420:
                                self.h, self.w = 40, 15
                                Play = 'Multi'

                self.globale.counts("++")
                if self.globale.counts("r") % 3 == 0:
                    Menufont = [[choice([0, 10, 13, 12])
                                 for _ in range(50)]for _ in range(50)]
                    self.globale.afficherPygame(
                        True, Menufont, self.fenetre, True)
                    self.globale.counts("create", 1)
                    self.globale.counts("++")

                pygame.draw.rect(self.fenetre, (255, 255, 255),
                                 (160, 50, 180, 50))
                pygame.draw.rect(self.fenetre, (0, 0, 0),
                                 (160, 50, 180, 50), 2)
                self.fenetre.blit(self.myfont.render(
                    'LABY-MAZE ', False, (0, 0, 0)), (163, 50))

                if MenuChoix == "menu":
                    pygame.draw.rect(
                        self.fenetre, (255, 255, 255), (180, 170, 100, 30))
                    pygame.draw.rect(self.fenetre, (0, 0, 0),
                                     (180, 170, 100, 30), 2)
                    self.fenetre.blit(self.myfont.render(
                        MenuChoix + ' :', False, (0, 0, 0)), (185, 160))
                    self.Menu.menuButton(self)
                    self.Menu.menuText(self)
                elif MenuChoix == "setting":
                    pygame.draw.rect(
                        self.fenetre, (255, 255, 255), (80, 220, 140, 40))
                    pygame.draw.rect(self.fenetre, (0, 0, 0),
                                     (80, 220, 140, 40), 2)
                    pygame.draw.circle(self.fenetre, (0, 255, 0), (20, 20), 20)
                    pygame.draw.circle(
                        self.fenetre, (0, 0, 0), (19, 20), 21, 1)
                    self.fenetre.blit(self.myfont.render(
                        '<-', True, (0, 0, 0)), (7, -5))
                    self.fenetre.blit(self.myfont.render(
                        MenuChoix + ' :', False, (0, 0, 0)), (85, 212))
                    self.Menu.SettingButton(self)
                    self.Menu.SettingText(self)

                pygame.display.update()

            if Play == 'Play':
                self.fenetre = pygame.display.set_mode(
                    (self.cell*self.w+2*self.cell, self.cell*self.h+2*self.cell))
                self.maze = self.generateur.start(self.h, self.w)
                self.GameStart()
                Play = 'Menu'
            elif Play == 'Adventure':
                self.Adventure()
                Play = 'Adventure'
            elif Play == 'Multi':
                self.MultiMode()
                Play = 'Multi'

    def FuncAnimationKey(self):
        self.fenetre.fill((0, 0, 0), (0, 800, 1000, 250))
        if self.globale.counts("r") == 0:
            self.globale.counts('++')
            self.yTemp, self.xTemp = self.MCYcor*self.cell, self.MCXcor*self.cell

        if not self.xTemp >= 800:
            self.xTemp += 50
        if not self.yTemp >= 850:
            self.yTemp += 50
        if self.yTemp >= 850 and self.xTemp >= 800:
            self.AnimationKey = False
            self.fenetre.fill((0, 0, 0), (0, 800, 1000, 250))
            self.SaveChange = True
            self.globale.counts("delete")
        self.fenetre.blit(pygame.transform.rotate(
            self.Bigkey, -20), (self.xTemp, self.yTemp))

    def FuncAnimationCadena(self):
        self.fenetre.blit(self.CadenaAni[self.globale.counts('r')], (350, 250))
        pygame.time.wait(60)
        self.globale.counts('++')
        if self.globale.counts('r') + 1 >= len(self.CadenaAni):
            self.AnimationCadena = False
            self.SaveChange = True
            self.globale.counts("delete")

    def Adventure(self):
        continuer = True
        self.h, self.w = 40, 50
        self.stade, GameLevel = 0, 1
        self.fenetre = pygame.display.set_mode(
            (self.cell*self.w, self.cell*self.h+250))
        self.SaveStade, self.SaveChange, self.AnimationCadena = -1, False, False

        while continuer:
            pygame.time.Clock().tick(60)
            self.globale.afficherPygame(False, self.maze, self.fenetre, True)

            if self.live:
                Niveau.InitLevel(self, GameLevel)

            if not (self.pause or self.AnimationKey or self.AnimationCadena):
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer = False
                        quit()
                    if (GameLevel == 1 or GameLevel == 2 or GameLevel == 3 or GameLevel == 4 or GameLevel == 5) and self.stade == 1:
                        key_pressed = pygame.key.get_pressed()
                        if key_pressed[K_RIGHT]:
                            self.deplacerMC('droite')
                        elif key_pressed[K_LEFT]:
                            self.deplacerMC('gauche')
                        elif key_pressed[K_UP]:
                            self.deplacerMC('haut')
                        elif key_pressed[K_DOWN]:
                            self.deplacerMC('bas')
                        elif key_pressed[K_ESCAPE]:
                            self.pause = True
                            print("Pause")

                    if event.type == pygame.MOUSEBUTTONUP:
                        #pos = pygame.mouse.get_pos()
                        self.NiveauActu.StartNiveau(self)
                        if self.stade == 2:
                            self.fenetre.fill((0, 0, 0), (0, 800, 1000, 250))
                            GameLevel += 1
                            self.stade = 0
                            self.live = True

                self.NiveauActu.StadePrint(self, pygame)

                if self.stade != self.SaveStade or self.SaveChange:
                    self.fenetre.fill((0, 0, 0), (0, 800, 1000, 250))
                    self.fenetre.blit(self.Master, (0, 890))
                    self.fenetre.blit(self.Bubble, (120, 830))
                    self.fenetre.blit(self.BackKeys, (800, 850))
                    self.fenetre.blit(self.BackKeys, (850, 850))
                    if self.GetKey >= 1:
                        self.fenetre.blit(self.Bigkey, (800, 850))
                    if self.GetKey >= 2:
                        self.fenetre.blit(self.Bigkey, (850, 850))
                    self.SaveChange = False
                    self.SaveStade = self.stade

            elif self.AnimationKey:
                self.FuncAnimationKey()

            elif self.AnimationCadena:
                self.FuncAnimationCadena()

            elif self.pause:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer = False
                        quit()
                    if event.type == pygame.MOUSEBUTTONUP:
                        cur = pygame.mouse.get_pos()
                        if (450+200 > cur[0] > 450 and 260+75 > cur[1] > 260):
                            print("RESUME")
                            self.pause = False
                            self.SaveChange = True
                        if (450+200 > cur[0] > 450 and 360+75 > cur[1] > 360):
                            print("settings")
                        if (450+200 > cur[0] > 450 and 460+75 > cur[1] > 460):
                            continuer = False
                            print("Menu")
                        if (450+200 > cur[0] > 450 and 560+75 > cur[1] > 560):
                            continuer = False
                            quit()
                PauseButton(self)
                PauseText(self)
            pygame.display.update()

    def reapet(self, addTime):
        pygame.key.set_repeat(1, addTime)

    def MultiMode(self):
        continuer = True
        self.h, self.w = 40, 10
        self.fenetre = pygame.display.set_mode((800, 800))

        n = Network()
        CLientGetFirst = n.getP()

        if CLientGetFirst != "error":
            self.Allmaze = CLientGetFirst
            p = n.get()
            print(p)
            self.MCXcor, self.MCYcor, self.MCSens, self.MCMaze, self.score, self.id = p[
                0], p[1], p[2], p[3], p[4], p[5]
            print("id joueur : ", self.id)

            self.maze = self.Allmaze[self.MCMaze]
            self.oldRever = True
            continuer = True

            corfele = [330, 410]
            startChrono = True
            while continuer:

                pygame.time.Clock().tick(60)
                p2 = n.send([self.MCXcor, self.MCYcor,
                             self.MCSens, self.MCMaze, self.score])

                if p2 == None:
                    j2M = 0
                else:
                    j2M = p2[3]
                    p2[0] += 21
                    if startChrono:
                        TpsZero = pygame.time.get_ticks()
                        startChrono = False
                    seconds = (pygame.time.get_ticks() - TpsZero) / 1000

                self.globale.afficherPygameMulti(
                    self.Allmaze, self.MCMaze, j2M, self.fenetre, False)

                for event in pygame.event.get():
                    if event.type == QUIT:
                        continuer = False
                        quit()
                    if p2 != None:
                        key_pressed = pygame.key.get_pressed()
                        self.MCXcor -= 2

                        if key_pressed[K_RIGHT]:
                            self.deplacerMC('droite')
                        elif key_pressed[K_LEFT]:
                            self.deplacerMC('gauche')
                        elif key_pressed[K_UP]:
                            self.deplacerMC('haut')
                        elif key_pressed[K_DOWN]:
                            self.deplacerMC('bas')

                        if self.maze[self.MCYcor][self.MCXcor] == 12:

                            self.score += 1
                            self.MCMaze = (self.MCMaze+1) % len(self.Allmaze)
                            self.maze = self.Allmaze[self.MCMaze]
                            self.MCXcor = 7

                        self.MCXcor += 2

                if p2 != None:
                    jouer = [self.MCMaze, j2M]
                    jouerScore = [self.score, p2[4]]
                    for i, j in enumerate(jouer):
                        if j % 2 == 1:
                            tempSens = -180
                        else:
                            tempSens = 0
                        self.fenetre.blit(self.myfont.render(
                            str(jouerScore[i]), False, (0, 0, 0)), (corfele[i], 350))
                        self.fenetre.blit(pygame.transform.rotate(
                            self.MultiSens, tempSens), (corfele[i], 400))
                    self.fenetre.blit(self.myfont.render(
                        "Chrono :", False, (0, 0, 0)), (340, 260))
                    self.fenetre.blit(self.myfont.render(
                        str(math.floor(seconds)), False, (0, 0, 0)), (390, 300))

                    self.fenetre.blit(pygame.transform.rotate(
                        self.MCIM, p2[2]), (self.cell*p2[0]+1, self.cell*p2[1]+1))
                else:
                    pygame.draw.rect(
                        self.fenetre, (200, 200, 200), (300, 350, 200, 100))
                    pygame.draw.rect(self.fenetre, (0, 0, 0),
                                     (300, 350, 200, 100), 2)
                    self.fenetre.blit(self.myfont.render(
                        'wait ...', False, (0, 0, 0)), (350, 375))
                self.fenetre.blit(pygame.transform.rotate(
                    self.MCIM, self.MCSens), (self.cell*self.MCXcor+1, self.cell*self.MCYcor+1))

                pygame.display.update()
        else:
            print("le serveur n'est pas ouvert ou il y a eu une erreur de comunication")


MainGame = MainGame()
MainGame.StartMenu()

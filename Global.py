import pygame
from pygame.locals import *


class globale:
    def __init__(self, cell):
        self.cell = cell
        self.charC = 11
        self.counter = []
        self.colorstyle = []
        self.tour = 0

    def ColorMap(self, p):
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

    def text_objects(self, text, color):
        smallfont = pygame.font.SysFont("comicsansms", 15)
        textSurface = smallfont.render(text, True, color)
        return textSurface, textSurface.get_rect()

    def text_to_button(self, msg, color, buttonx, buttony, buttonwidth, buttonheight, fenetre):
        textSurf, textRect = self.text_objects(msg, color)
        textRect.center = ((buttonx + (buttonwidth / 2)),
                           buttony + (buttonheight / 2))
        fenetre.blit(textSurf, textRect)

    def afficherPygame(self, menu=False, maze=None, fenetre=None, update=False, fun=False):
        if self.colorstyle == []:
            '''
            n = len(maze)*4
            for i in range(n):
                r = round(255.0*i/(n-1))
                self.colorstyle.append(self.ColorMap(r))
                '''
            l = [(255, i, 0) for i in range(0, 256, 5)]
            self.colorstyle += l
            l = [(i, 255, 0) for i in range(255, -1, -5)]
            self.colorstyle += l
            l = [(0, 255, i) for i in range(0, 256, 5)]
            self.colorstyle += l
            l = [(0, i, 255) for i in range(255, -1, -5)]
            self.colorstyle += l
            l = [(i, 0, 255) for i in range(0, 256, 5)]
            self.colorstyle += l
            l = [(255, 0, i) for i in range(255, -1, -5)]
            self.colorstyle += l
        if fun:
            self.tour += 10
        White = (255, 255, 255)
        Black = (0, 0, 0)
        Red = (255, 0, 0)
        Blue = (0, 0, 255)
        Marron = (139, 69, 19)
        Green = (0, 255, 0)
        Grey = (128, 128, 128)
        key = pygame.transform.scale(pygame.image.load(
            './img/Key.png').convert_alpha(), (20, 20))
        # On parcourt la liste du niveau
        num_ligne = 0

        if menu:
            modif = 1
            modifce = 2
        else:
            modif = 0
            modifce = 0

        for ligne in maze:
            # On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                # On calcule la position réelle en pixels
                x = num_case * self.cell
                y = num_ligne * self.cell

                if sprite == 10:
                    pygame.draw.rect(
                        fenetre, White, (x + modif, y + modif, self.cell - modifce, self.cell - modifce))
                elif sprite <= 9:  # m = Mur
                    pygame.draw.rect(
                        fenetre, Grey, (x + modif, y + modif, self.cell - modifce, self.cell - modifce))
                elif sprite == self.charC:  # d = Départ
                    pygame.draw.rect(
                        fenetre, Black, (x + modif, y + modif, self.cell - modifce, self.cell - modifce))
                elif sprite >= 30:
                    pygame.draw.rect(
                        fenetre, self.colorstyle[(((sprite - 30)+self.tour) % len(self.colorstyle))], (x, y, self.cell, self.cell))

                elif sprite == 26:
                    pygame.draw.rect(
                        fenetre, White, (x + modif, y + modif, self.cell - modifce, self.cell - modifce))
                    pygame.draw.rect(
                        fenetre, Marron, (x, y, self.cell, self.cell))
                elif sprite == 25:
                    pygame.draw.rect(
                        fenetre, Black, (x + modif, y + modif, self.cell - modifce, self.cell - modifce))
                    pygame.draw.rect(
                        fenetre, Blue, (x, y, self.cell, self.cell))
                elif sprite == 16:
                    pygame.draw.rect(
                        fenetre, Green, (x + modif, y + modif, self.cell - modifce, self.cell - modifce))
                elif sprite == 15:
                    pygame.draw.rect(
                        fenetre, Marron, (x + modif, y + modif, self.cell - modifce, self.cell - modifce))
                elif sprite == 14:
                    pygame.draw.rect(
                        fenetre, Black, (x + modif, y + modif, self.cell - modifce, self.cell - modifce))
                    fenetre.blit(pygame.transform.rotate(
                        key, 0), (x + modif, y + modif, self.cell - modifce, self.cell - modifce))
                elif sprite == 13:
                    pygame.draw.rect(
                        fenetre, Blue, (x + modif, y + modif, self.cell - modifce, self.cell - modifce))
                elif sprite == 12:
                    pygame.draw.rect(
                        fenetre, Red, (x + modif, y + modif, self.cell - modifce, self.cell - modifce))

                num_case += 1
            num_ligne += 1
        if not update:
            pygame.display.update()

    def afficherPygameMulti(self, mazes, j1, j2, fenetre=None, update=False):
        White = (255, 255, 255)
        Black = (0, 0, 0)
        Red = (255, 0, 0)
        Blue = (0, 0, 255)
        Marron = (139, 69, 19)
        Green = (0, 255, 0)
        key = pygame.transform.scale(pygame.image.load(
            'img/Key.png').convert_alpha(), (20, 20))
        # On parcourt la liste du niveau
        num_ligne = 0

        maze = []
        for i in range(len(mazes[j1])):
            maze.append([10]*2+mazes[j1][i]+[10]*6+mazes[j2][i]+[10]*2)

        for ligne in maze:
            # On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                # On calcule la position réelle en pixels
                x = num_case * self.cell
                y = num_ligne * self.cell
                if sprite == 16:
                    pygame.draw.rect(
                        fenetre, Green, (x, y, self.cell, self.cell))
                elif sprite == 15:
                    pygame.draw.rect(
                        fenetre, Marron, (x, y, self.cell, self.cell))
                elif sprite == 14:
                    pygame.draw.rect(
                        fenetre, Black, (x, y, self.cell, self.cell))
                    fenetre.blit(pygame.transform.rotate(key, 0),
                                 (x, y, self.cell, self.cell))
                elif sprite == 13:
                    pygame.draw.rect(
                        fenetre, Blue, (x, y, self.cell, self.cell))
                elif sprite == 12:
                    pygame.draw.rect(
                        fenetre, Red, (x, y, self.cell, self.cell))
                elif sprite != self.charC:  # m = Mur
                    pygame.draw.rect(
                        fenetre, White, (x, y, self.cell, self.cell))
                elif sprite == self.charC:  # d = Départ
                    pygame.draw.rect(
                        fenetre, Black, (x, y, self.cell, self.cell))

                num_case += 1
            num_ligne += 1
        if update:
            pygame.display.update()

    def counts(self, action, number=0):
        if action == "create":
            self.counter = []
            self.counter = [0]*number

        elif action == "add":
            self.counter += [0]*number

        elif action == "++":
            self.counter[number] += 1

        elif action == "r":
            return self.counter[number]

        elif action == "delete":
            self.counter = []

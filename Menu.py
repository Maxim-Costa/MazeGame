import pygame
from pygame.locals import *

def text_objects(self, text, color, size = "small"):
    if size == "small":
        textSurface = self.smallfont.render(text, True, color)
    elif size == "medium":
        textSurface = self.medfont.render(text, True, color)
    elif size == "large":
        textSurface = self.largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()

def text_to_button(self, msg, color, buttonx, buttony, buttonwidth, buttonheight, size = "small"):
    textSurf, textRect = text_objects(self, msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    self.fenetre.blit(textSurf, textRect)

def menuButton(self):
    cur = pygame.mouse.get_pos()

    pygame.draw.rect(self.fenetre,(0,150,150),(182,202,150,50), 3)
    if 180+150 > cur[0] > 180 and 200+50 > cur[1] > 200:
        pygame.draw.rect(self.fenetre,(0,255,255),(180,200,150,50))
    else:
        pygame.draw.rect(self.fenetre,(0,200,200),(180,200,150,50))

    pygame.draw.rect(self.fenetre,(150,150,0),(182,262,150,50), 3)
    if 180+150 > cur[0] > 180 and 260+50 > cur[1] > 260:
        pygame.draw.rect(self.fenetre,(255,255,0),(180,260,150,50))
    else:
        pygame.draw.rect(self.fenetre,(200,200,0),(180,260,150,50))

    pygame.draw.rect(self.fenetre,(150,0,0),(182,322,150,50), 3)
    if 180+150 > cur[0] > 180 and 320+50 > cur[1] > 320:
        pygame.draw.rect(self.fenetre,(255,0,0),(180,320,150,50))
    else:
        pygame.draw.rect(self.fenetre,(200,0,0),(180,320,150,50))

def menuText(self):
    text_to_button(self, "PLAY", (0,0,0), 180,200,150,50)
    text_to_button(self, "SETTING", (0,0,0), 180,260,150,50)
    text_to_button(self, "LEFT GAME", (0,0,0), 180,320,150,50)

def SettingButton(self):
    cur = pygame.mouse.get_pos()

    pygame.draw.rect(self.fenetre,(75,75,75),(82,262,150,50), 3)
    if (80+150 > cur[0] > 80 and 260+50 > cur[1] > 260) or (self.h == 10 and self.w == 10):
        pygame.draw.rect(self.fenetre,(220,220,220),(80,260,150,50))
    else:
        pygame.draw.rect(self.fenetre,(150,150,150),(80,260,150,50))

    pygame.draw.rect(self.fenetre,(75,75,75),(262,262,150,50), 3)
    if (260+150 > cur[0] > 260 and 260+50 > cur[1] > 260) or (self.h == 20 and self.w == 20):
        pygame.draw.rect(self.fenetre,(220,220,220),(260,260,150,50))
    else:
        pygame.draw.rect(self.fenetre,(150,150,150),(260,260,150,50))

    pygame.draw.rect(self.fenetre,(75,75,75),(82,342,150,50), 3)
    if (80+150 > cur[0] > 80 and 340+50 > cur[1] > 340) or (self.h == 40 and self.w == 40):
        pygame.draw.rect(self.fenetre,(220,220,220),(80,340,150,50))
    else:
        pygame.draw.rect(self.fenetre,(150,150,150),(80,340,150,50))

    pygame.draw.rect(self.fenetre,(75,75,75),(262,342,150,50), 3)
    if (260+150 > cur[0] > 260 and 340+50 > cur[1] > 340) or (self.h == 50 and self.w == 50):
        pygame.draw.rect(self.fenetre,(220,220,220),(260,340,150,50))
    else:
        pygame.draw.rect(self.fenetre,(150,150,150),(260,340,150,50))

    pygame.draw.rect(self.fenetre,(75,75,75),(82,422,150,50), 3)
    if (80+150 > cur[0] > 80 and 420+50 > cur[1] > 420) or (self.h == 40 and self.w == 50):
        pygame.draw.rect(self.fenetre,(220,220,220),(80,420,150,50))
    else:
        pygame.draw.rect(self.fenetre,(150,150,150),(80,420,150,50))

    pygame.draw.rect(self.fenetre,(75,75,75),(262,422,150,50), 3)
    if (260+150 > cur[0] > 260 and 420+50 > cur[1] > 420) or (self.h == 40 and self.w == 15):
        pygame.draw.rect(self.fenetre,(220,220,220),(260,420,150,50))
    else:
        pygame.draw.rect(self.fenetre,(150,150,150),(260,420,150,50))

def SettingText(self):
    text_to_button(self, "10*10", (0,0,0), 80,260,150,50)
    text_to_button(self, "20*20", (0,0,0), 260,260,150,50)
    text_to_button(self, "40*40", (0,0,0), 80,340,150,50)
    text_to_button(self, "50*50", (0,0,0), 260,340,150,50)
    text_to_button(self, "History", (0,0,0), 80,420,150,50)
    text_to_button(self, "Multi", (0,0,0), 260,420,150,50)
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

def PauseText(self):
    text_to_button(self, "RESUME", (0,0,0), 400,260,200,75)
    text_to_button(self, "MENU", (0,0,0), 400,460,200,75)
    text_to_button(self, "SETTINGS", (0,0,0), 400,360,200,75)
    text_to_button(self, "LEFT GAME", (0,0,0), 400,560,200,75)

def PauseButton(self):
    cur = pygame.mouse.get_pos()

    pygame.draw.rect(self.fenetre,(75,75,75),(402,262,200,75), 3)
    if (400+200 > cur[0] > 400 and 260+75 > cur[1] > 260):
        pygame.draw.rect(self.fenetre,(220,220,220),(400,260,200,75))
    else:
        pygame.draw.rect(self.fenetre,(150,150,150),(400,260,200,75))

    pygame.draw.rect(self.fenetre,(75,75,75),(402,362,200,75), 3)
    if (400+200 > cur[0] > 400 and 360+75 > cur[1] > 360):
        pygame.draw.rect(self.fenetre,(220,220,220),(400,360,200,75))
    else:
        pygame.draw.rect(self.fenetre,(150,150,150),(400,360,200,75))

    pygame.draw.rect(self.fenetre,(75,75,75),(402,462,200,75), 3)
    if (400+200 > cur[0] > 400 and 460+75 > cur[1] > 460):
        pygame.draw.rect(self.fenetre,(220,220,220),(400,460,200,75))
    else:
        pygame.draw.rect(self.fenetre,(150,150,150),(400,460,200,75))

    pygame.draw.rect(self.fenetre,(75,75,75),(402,562,200,75), 3)
    if (400+200 > cur[0] > 400 and 560+75 > cur[1] > 560):
        pygame.draw.rect(self.fenetre,(220,220,220),(400,560,200,75))
    else:
        pygame.draw.rect(self.fenetre,(150,150,150),(400,560,200,75))
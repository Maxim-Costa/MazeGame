
TextNiveau4 = [["Avant dernier tuto, Alors écoute","Lors des Niveau tu verra des porte"],["elles sont de couleur marron, pour les ouvrir"," il te faudra deux clés. aller vasi essaie"],["Bravo je pensai vraiment pas que tu réussirais","MTN passon au choses sérieuses"],["Tes vraiment nul","aller recommance"]]


def LevelConstruct():
    temps_niveau4 = [[11 if (15<i<24 and (j == 13 or j == 28)) or (13<i<24 and (j == 15 or j == 17 or j == 24 or j == 26)) or (15<i<26 and (j == 19 or j == 22)) or (i == 13 and (14<j<18 or 23<j<27)) or (i == 15 and (12<j<20 or 21<j<29)) or (i == 23 and (12<j<16 or 16<j<25 or 25<j<29)) or (i == 25 and (18<j<23)) or (i == 20 and (4<j<13 or j==16 or 19<j<22 or j==25 or 28<j<41)) or (i == 19 and (j==14 or j==18 or j==23 or j==27)) else 10  for j in range(50)]for i in range(40)] # self arbre
    temps_niveau4[20][5] = 13
    temps_niveau4[20][40] = 12
    temps_niveau4[20][29] = 15
    temps_niveau4[13][15] = 14
    temps_niveau4[13][26] = 14
    niveau4 = temps_niveau4
    return niveau4

def StartNiveau(self):
    if self.stade == 0 or self.stade == 3:
        self.stade = 0
        self.MobNumber = 4
        self.Mobcor,self.MobSens = [[15,13],[26,13],[19,25],[22,25]],[0,0,180,180]
        self.MobMoveEscape = 100
        self.MobOldMove = ['bas','bas','haut','haut']
        self.MCXcor,self.MCYcor = 5,20
    if self.stade == 0 :
        self.stade = 1

def StadePrint(self, pygame):
    if self.stade == 1:
        self.fenetre.blit(pygame.transform.rotate(self.MCIM, self.MCSens), (self.cell*self.MCXcor+1, self.cell*self.MCYcor+1))
        GameOver = self.MobC.MobAdventure(self)
        if self.maze[self.MCYcor][self.MCXcor] == 12:
            self.stade = 2
        elif GameOver:
            self.stade = 3
    
    self.fenetre.blit(self.myfont.render(TextNiveau4[self.stade][0], True, (0, 0, 0)),(130,840))
    self.fenetre.blit(self.myfont.render(TextNiveau4[self.stade][1], True, (0, 0, 0)),(130,870))

    if self.stade != 3:
        self.Bubble = self.BigBubble
        self.fenetre.blit(self.myfont.render("->", True, (0, 0, 0)),(740,905))
    else:
        self.Bubble = self.SmallBubble
        self.fenetre.blit(self.myfont.render("->", True, (0, 0, 0)),(490,905))

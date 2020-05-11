TextNiveau1 = [["Binvenue dans se","Dungeon"],["Deplacez vous de la ","case bleu a la rouge"],["Bravo tu a réussi","le niveau 1"]]


def LevelConstruct():
    temps_niveau1 = [[11 if i == 20 and 9 < j < 41 else 10  for j in range(50)]for i in range(40)] # self arbre
    temps_niveau1[20][10] = 13
    temps_niveau1[20][40] = 12
    niveau1 = temps_niveau1
    return niveau1

def StartNiveau(self):
    if self.stade == 0:
        self.stade = 1
        self.MCXcor,self.MCYcor = 10,20

def StadePrint(self, pygame):
    self.fenetre.blit(self.myfont.render(TextNiveau1[self.stade][0], True, (0, 0, 0)),(130,840))
    self.fenetre.blit(self.myfont.render(TextNiveau1[self.stade][1], True, (0, 0, 0)),(130,870))
    if self.stade == 1:
        self.fenetre.blit(pygame.transform.rotate(self.MCIM, self.MCSens), (self.cell*self.MCXcor+1, self.cell*self.MCYcor+1))
        if self.maze[self.MCYcor][self.MCXcor] == 12:
            self.stade = 2
    self.fenetre.blit(self.myfont.render("->", True, (0, 0, 0)),(490,905))




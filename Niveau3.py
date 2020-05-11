

TextNiveau3 = [["Binvenue au niveau 3","Cette fois encore plus dure"],["Toujours la même mais avec"," un monstre cette fois"],["la vie est dure mais tu as"," réussi :) :) aller NV suivant"],["Tes vraiment nul","aller recommance"]]

def LevelConstruct():
    temps_niveau3 = [[11 if (i == 20 and 9 < j < 41) or ( 15 < i < 25 and j == 25) else 10  for j in range(50)]for i in range(40)] # self arbre
    temps_niveau3[20][10] = 13
    temps_niveau3[20][40] = 12
    niveau3 = temps_niveau3
    return niveau3

def StadePrint(self, pygame):
    self.fenetre.blit(self.myfont.render(TextNiveau3[self.stade][0], True, (0, 0, 0)),(130,840))
    self.fenetre.blit(self.myfont.render(TextNiveau3[self.stade][1], True, (0, 0, 0)),(130,870))
    if self.stade == 1:
        self.fenetre.blit(pygame.transform.rotate(self.MCIM, self.MCSens), (self.cell*self.MCXcor+1, self.cell*self.MCYcor+1))
        GameOver = self.MobC.MobAdventure(self)
        if self.maze[self.MCYcor][self.MCXcor] == 12:
            self.stade = 2
        elif GameOver:
            self.stade = 3
    self.fenetre.blit(self.myfont.render("->", True, (0, 0, 0)),(490,905))

def StartNiveau(self):
    if self.stade == 0 or self.stade == 3:
        self.stade = 0
        self.MobNumber = 1
        self.Mobcor,self.MobSens = [[25,16]],[0]
        self.MobMoveEscape = 100
        self.MobOldMove = ['bas']
        self.MCXcor,self.MCYcor = 10,20
    if self.stade == 0 :
        self.stade = 1
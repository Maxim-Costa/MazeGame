
TextNiveau2 = [["Binvenue au niveau 2","Cette fois plus dure"],["Même chose qu'au niveau 1"," (on sait jamais)"],["Bravo tu sais écouter","Passon au niveau 3"]]

def LevelConstruct():
    temps_niveau2 = [[11 if (i == 17 and 9 < j < 14) or ( 21 > i > 16 and j == 13) or (i == 20 and 13 < j < 37) or (23 > i > 20  and j == 36) or (i == 23 and 35 < j < 40) else 10  for j in range(50)]for i in range(40)] # self arbre
    temps_niveau2[17][10] = 13
    temps_niveau2[23][39] = 12
    niveau2 = temps_niveau2
    return niveau2

def StadePrint(self, pygame):
    self.fenetre.blit(self.myfont.render(TextNiveau2[self.stade][0], True, (0, 0, 0)),(130,840))
    self.fenetre.blit(self.myfont.render(TextNiveau2[self.stade][1], True, (0, 0, 0)),(130,870))
    if self.stade == 1:
        self.fenetre.blit(pygame.transform.rotate(self.MCIM, self.MCSens), (self.cell*self.MCXcor+1, self.cell*self.MCYcor+1))
        if self.maze[self.MCYcor][self.MCXcor] == 12:
            self.stade = 2
    self.fenetre.blit(self.myfont.render("->", True, (0, 0, 0)),(490,905))

def StartNiveau(self):
    if self.stade == 0 :
        self.stade = 1
        self.MCXcor,self.MCYcor = 10,17
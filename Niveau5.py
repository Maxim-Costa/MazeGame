from random import randint
from MazeGenerateur import generateur

TextNiveau5 = [["Dernier tuto, apres","ont vas avoir  du lourd"],["vasy j'ai rien a dire",""],["Bas c'est pas trop tôt","aller ta quete commence"],["Tes vraiment nul","aller recommance"]]
generateur = generateur(40, 50, 20)

def LevelConstruct(self):
    temps_niveau5 = [[11 if ((18<=i<=22 and 40<=j<=44) or (24<=i<=28 and 6<=j<=10)) else 10 if (i<=5 or j<=5 or 37<=i or 45<=j or i == 23) else randint(0,9)  for j in range(50)]for i in range(40)] # self arbre
    niveau5 = generateur.start(40,50, temps_niveau5)

    x,y = 6,6
    while niveau5[y][x] != 11:
        x += 1
    niveau5[y][x] = 13
    self.MCTcor = x,y

    x,y = 44,36
    while niveau5[y][x] != 11:
        x -= 1
    niveau5[y][x] = 12

    niveau5[22][44],niveau5[24][6] = 16,16
    return niveau5

def StartNiveau(self):
    if self.stade == 0 or self.stade == 3:
        self.stade = 0
        self.MobNumber = 8
        self.MobMoveEscape = 15
        self.MobC.MobFun(self, self.MobNumber)
        self.MCXcor,self.MCYcor = self.MCTcor
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
    
    self.fenetre.blit(self.myfont.render(TextNiveau5[self.stade][0], True, (0, 0, 0)),(130,840))
    self.fenetre.blit(self.myfont.render(TextNiveau5[self.stade][1], True, (0, 0, 0)),(130,870))

    if self.stade != 3:
        self.Bubble = self.BigBubble
        self.fenetre.blit(self.myfont.render("->", True, (0, 0, 0)),(740,905))
    else:
        self.Bubble = self.SmallBubble
        self.fenetre.blit(self.myfont.render("->", True, (0, 0, 0)),(490,905))
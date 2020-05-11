import Niveau5,Niveau4,Niveau3,Niveau2,Niveau1

def InitLevel(self, GameLevel):
    if GameLevel == 1 and self.live:
        self.NiveauActu = Niveau1
        self.maze = self.NiveauActu.LevelConstruct()
        self.live = False

    elif GameLevel == 2 and self.live:
        self.NiveauActu = Niveau2
        self.maze = self.NiveauActu.LevelConstruct()
        self.live = False

    elif GameLevel == 3 and self.live:
        self.NiveauActu = Niveau3
        self.maze = self.NiveauActu.LevelConstruct()
        self.live = False

    elif GameLevel == 4 and self.live: 
        self.NiveauActu = Niveau4
        self.maze = self.NiveauActu.LevelConstruct()
        self.live = False

    elif GameLevel == 5 and self.live:
        self.NiveauActu = Niveau5
        self.maze = self.NiveauActu.LevelConstruct(self)
        self.live = False
        self.Portal  = [(22,44),(24,6)]
        
    self.SaveChange = True

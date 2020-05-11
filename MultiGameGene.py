import pygame
from pygame.locals import *
from MazeGenerateurOver import generateur
from random import randint

def MultiGenerateur():

    AllStartMaze = []
    for k in range(12):
        AllStartMaze.append([[10 if ((i==0 or i==40 or j <= 13 or j >= 27 )) else 12 if (i == 38 and j == 20) else randint(0,9)  for j in range(40)]for i in range(40)])


    Generateur = generateur(40, 40, 20, None)

    for i in range(len(AllStartMaze)):
        print(i+1,"/",12)
        AllStartMaze[i] = Generateur.start(40,40, AllStartMaze[i])



    AllMaze = AllStartMaze.copy()

    for k in range(len(AllMaze)):
        for i in range(len(AllMaze[k])):
            for j in range(len(AllMaze[k][i])):
                if AllMaze[k][i][j] < 10:
                    AllMaze[k][i][j] = 10

    mazes = []
    for k in range(len(AllMaze)):
        mazes.append([])
        for i in AllMaze[k]:
            mazes[k].append(i[13:28])

    x = 10

    for i in range(len(mazes)):
        while mazes[i][1][x] != 11:
            x -= 1
        mazes[i][1][x] = 12

    for i in range(len(mazes)):
        if i%2 == 1:
            mazes[i].reverse()

    pygame.quit()
    
    return mazes
from random import randint

def prin(tab):
    for i in tab:
        for j in i:
            if j == 11 :
                print("+", end=' ')
            elif j == 10 :
                print("#", end=' ')
            elif j == 12 :
                print("D", end=' ')
            elif j != 10:
                print(j, end=' ')
        print()

def Cadre(T):
    T = [[10]+T[i]+[10] for i in range(len(T))]
    T = [[10]*len(T[0])]+T+[[10]*len(T[0])]
    return T

def finish(maze):
    for i in range(1,len(maze)-1):
        for j in range(1,len(maze[i])-1):
            if maze[i][j] <= 9:
                countW = 0
                countC = 0
                if maze[i+1][j] == 11:
                    countC += 1
                elif maze[i+1][j] == 10:
                    countW += 1
                if maze[i-1][j] == 11:
                    countC += 1
                elif maze[i-1][j] == 10:
                    countW += 1
                if maze[i][j+1] == 11:
                    countC += 1
                elif maze[i][j+1] == 10:
                    countW += 1
                if maze[i][j-1] == 11:
                    countC += 1
                elif maze[i][j-1] == 10:
                    countW += 1

                if 0 < countC >= 2:
                    maze[i][j] = 11
                else:
                    maze[i][j] = 10


def testWall(m):
    return (m != 12 and m != 11 and m != 10)

def testWall1(m):
    return ((m == 12 or m == 11) and m != 10)

maze = [[randint(0,9) for _ in range(10)]for _ in range(10)]
maze[randint(0,9)][randint(0,9)] = 12
maze = Cadre(maze)          

prin(maze)
continuer = True

while continuer:
    L = []
    L1 = []
    for i in range(1,11):
        for j in range(1,11):
            if testWall(maze[i][j]):
                count = 0
                if testWall1(maze[i+1][j]):
                    count += 1
                if testWall1(maze[i-1][j]):
                    count += 1
                if testWall1(maze[i][j+1]):
                    count += 1
                if testWall1(maze[i][j-1]):
                    count += 1

                if count == 0:
                    pass
                elif count == 1:
                    L.append(maze[i][j])
                    L1.append((i,j))
                elif count > 1:
                    maze[i][j] = 10
    if L == [] or L1 == []:
        print ('finish')
        continuer = False
        finish(maze)
    else:
        maze[L1[L.index(min(L))][0]][L1[L.index(min(L))][1]] = 11
    prin(maze)

                


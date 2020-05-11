import socket
from _thread import *
import pickle
import MultiGameGene


server = 'localhost'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


s.listen(2)
print("Waiting for a connection, Server Started")

def threaded_client(conn, addr, player, mazes):
    conn.send(pickle.dumps(mazes))
    m = players[player]
    conn.send(pickle.dumps([m[0],m[1],m[2],m[3],m[4],player]))
    global Client

    replay = ""

    while True:
        try:
            data = pickle.loads(conn.recv(8192))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if len(Client) > 1:
                    if player == 1:
                        replay = players[0]
                    else:
                        replay = players[1]
                else:
                    replay = None
            conn.sendall(pickle.dumps(replay))
        except:
            break
    Client.remove(addr)
    print("Lost connection")
    conn.close()

Client = []
players = [[9,38,-180,0,0],[9,38,-180,0,0]]
currentPlayer = 0
mazes = MultiGameGene.MultiGenerateur()
while True:
    conn, addr = s.accept()
    Client.append(addr)
    print("Connected to :",addr, 'client id : ',len(Client))
    currentPlayer = len(Client) - 1
    
    start_new_thread(threaded_client, (conn, addr, currentPlayer, mazes))
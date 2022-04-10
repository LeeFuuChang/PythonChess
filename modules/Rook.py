from .Constants import *
import pygame


class Rook: # 城堡
    Value = Values["Rook"]
    def __init__(self, Side, r, c):
        self.Side = Side
        self.image = pygame.image.load( os.path.join(ProjectRoot, "assets", "images", f"{self.__class__.__name__}{Side}.png") )
        self.r, self.c = r, c

        self.directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]


    def checkAvailable(self, r, c):
        return 0<=r<8 and 0<=c<8


    def getMove(self, board):
        available = []

        for dIdx in range(len(self.directions)):
            now = (self.r, self.c)
            vector = self.directions[dIdx]
            while(True):
                now = (now[0]+vector[0], now[1]+vector[1])
                print("checking", now)
                if self.checkAvailable(now[0], now[1]): 
                    if not board[now[0]][now[1]]:
                        available.append((now[0]-self.r, now[1]-self.c))
                    else:
                        if board[now[0]][now[1]].Side != self.Side:
                            available.append((now[0]-self.r, now[1]-self.c))
                        break
                else: break

        return available


    def MoveTo(self, r, c):
        self.r = r
        self.c = c
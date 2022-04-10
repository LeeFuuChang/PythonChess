from .Constants import *
import pygame

class Pawn: # 士兵
    Value = Values["Pawn"]
    def __init__(self, Side, r, c):
        self.Side = Side
        self.image = pygame.image.load( os.path.join(ProjectRoot, "assets", "images", f"{self.__class__.__name__}{Side}.png") )
        self.r, self.c = r, c

        self.moved = False
        self.directions = [
            (1, 0), (1, -1), (1, 1), (2, 0), (-1, 0), (-1, -1), (-1, 1), (-2, 0)
        ][(self.Side-1)*4 : self.Side*4]


    def checkAvailable(self, r, c):
        return 0<=r<8 and 0<=c<8


    def getMove(self, board):
        available = []

        if self.checkAvailable(
            self.r+self.directions[0][0], 
            self.c+self.directions[0][1]
        ) and (
            not board[self.r+self.directions[0][0]][self.c+self.directions[0][1]]
        ): 
            available.append(self.directions[0])
            if self.checkAvailable(
                self.r+self.directions[3][0], 
                self.c+self.directions[3][1]
            ) and (
                not self.moved
            ) and (
                not board[self.r+self.directions[3][0]][self.c+self.directions[3][1]]
            ): available.append(self.directions[3])

        if self.checkAvailable(
            self.r+self.directions[1][0], 
            self.c+self.directions[1][1]
        ) and (
            board[self.r+self.directions[1][0]][self.c+self.directions[1][1]]
        ) and (
            board[self.r+self.directions[1][0]][self.c+self.directions[1][1]].Side != self.Side
        ): available.append(self.directions[1])

        if self.checkAvailable(
            self.r+self.directions[2][0], 
            self.c+self.directions[2][1]
        ) and (
            board[self.r+self.directions[2][0]][self.c+self.directions[2][1]]
        ) and (
            board[self.r+self.directions[2][0]][self.c+self.directions[2][1]].Side != self.Side
        ): available.append(self.directions[2])

        print("Pawn from", self.r, self.c, available)
        return available


    def MoveTo(self, r, c):
        self.r = r
        self.c = c
        self.moved = True
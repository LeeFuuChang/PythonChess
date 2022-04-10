from .Constants import *
import pygame

class Knight: # 騎士
    Value = Values["Knight"]
    def __init__(self, Side, r, c):
        self.Side = Side
        self.image = pygame.image.load( os.path.join(ProjectRoot, "assets", "images", f"{self.__class__.__name__}{Side}.png") )
        self.r, self.c = r, c

        self.directions = [
            (-2, -1),
            (-2,  1),
            ( 2, -1),
            ( 2,  1),
            (-1, -2),
            ( 1, -2),
            (-1,  2),
            ( 1,  2),
        ]


    def checkAvailable(self, r, c):
        return 0<=r<8 and 0<=c<8


    def getMove(self, board):
        available = []
        for d in self.directions:
            if self.checkAvailable(
                self.r+d[0], self.c+d[1]
            ) and (
                (
                    not board[self.r+d[0]][self.c+d[1]]
                ) or (
                    board[self.r+d[0]][self.c+d[1]].Side != self.Side
                )
            ): available.append(d)
        return available


    def MoveTo(self, r, c):
        self.r = r
        self.c = c
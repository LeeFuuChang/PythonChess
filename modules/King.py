from .Constants import *
import pygame

class King:
    Value = Values["King"]
    def __init__(self, Side, r, c):
        self.Side = Side
        self.image = pygame.image.load( os.path.join(ProjectRoot, "assets", "images", f"{self.__class__.__name__}{Side}.png") )
        self.r, self.c = r, c

        self.directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


    def checkAvailable(self, r, c):
        return 0<=r<8 and 0<=c<8


    def getMove(self, board):
        available = []
        for d in self.directions:
            if not self.checkAvailable(self.r+d[0], self.c+d[1]): continue
            target = board[self.r+d[0]][self.c+d[1]]
            if not target or target.Side != self.Side:
                available.append(d)
        return available


    def MoveTo(self, r, c):
        self.r = r
        self.c = c
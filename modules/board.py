from .King import *
from .Queen import *
from .Bishop import *
from .Knight import *
from .Rook import *
from .Pawn import *
from .Empty import *


class Board:
    Pieces = {
        0:Empty,  #空
        1:Pawn,         #士兵
        2:Rook,         #城堡
        3:Knight,       #騎士
        4:Bishop,       #主教
        5:Queen,        #皇后
        6:King          #國王
    }
    Sides = {
        "Empty":0,
        "Black":1,
        "White":2
    }

    DefaultBoard = [
        [ (2, 1) , (3, 1) , (4, 1) , (5, 1) , (6, 1) , (4, 1) , (3, 1) , (2, 1) ],
        [ (1, 1) , (1, 1) , (1, 1) , (1, 1) , (1, 1) , (1, 1) , (1, 1) , (1, 1) ],
        [ (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) ],
        [ (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) ],
        [ (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) ],
        [ (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) , (0, 0) ],
        [ (1, 2) , (1, 2) , (1, 2) , (1, 2) , (1, 2) , (1, 2) , (1, 2) , (1, 2) ],
        [ (2, 2) , (3, 2) , (4, 2) , (5, 2) , (6, 2) , (4, 2) , (3, 2) , (2, 2) ],
    ]


    def __init__(self):
        self.resetBoard()


    def resetBoard(self):
        self.Side = 2
        self.board = []
        for i in range(8):
            self.board.append([])
            for j in range(8):
                block = self.DefaultBoard[i][j]
                piece = self.Pieces[ block[0] ]
                self.board[-1].append(
                    piece(block[1], i, j)
                )


    def get(self, r, c):
        return self.board[r][c]


    def movePiece(self, r1, c1, r2, c2):
        if not self.board[r1][c1]: return
        self.board[r1][c1], self.board[r2][c2] = None, self.board[r1][c1]
        self.board[r2][c2].MoveTo(r2, c2)


    def switchSide(self):
        if self.Side == self.Sides["White"]:
            self.Side = self.Sides["Black"]
            return
        if self.Side == self.Sides["Black"]:
            self.Side = self.Sides["White"]
            return
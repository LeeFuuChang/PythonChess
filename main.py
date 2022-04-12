from modules import *
import pygame
pygame.init()



class Game:
    FPS = pygame.time.Clock().tick

    State = {
        "Choosing":True,
        "Moving":False
    }

    TempStorage = {
        "DotHighLight":[],
        "SquareHighLight":[],
        "Moving":None,
        "MovingAvailable":[]
    }


    def _resetTempStorage(self):
        self.TempStorage["DotHighLight"] = []
        self.TempStorage["SquareHighLight"] = []
        self.TempStorage["Moving"] = None
        self.TempStorage["MovingAvailable"] = []
        self.State["Choosing"] = True
        self.State["Moving"] = False


    def _validScreenSize(self, screenSize):
        blockSize = round(screenSize/16)
        return blockSize*16


    def _handleQuit(self):
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                return True
        return False


    def __init__(self, screenSize):
        self.screenSize = self._validScreenSize(screenSize)
        self.window = pygame.display.set_mode((self.screenSize, self.screenSize))

        self.blockSize = self.screenSize//8

        self.board = Board()


    def drawHighLight(self, drawType, pos):
        drawFuncRef = {
            "dot":(HighLighter.typeDot, DotHighLightColor),
            "square":(HighLighter.typeSquare, SquareHighLightColor)
        }
        drawFunc = drawFuncRef[drawType]

        for r, c in pos:
            drawFunc[0](self.window, self.blockSize, r, c, drawFunc[1])


    def drawBoard(self):
        color = {0:(235, 235, 210), 1:(120, 150, 90)}
        for i in range(8):
            for j in range(8):
                pygame.draw.rect(
                    self.window,
                    color[(i*8 + j + (i%2))%2],
                    pygame.Rect(
                        j*self.blockSize,
                        i*self.blockSize,
                        self.blockSize,
                        self.blockSize
                    )
                )


    def drawPieces(self):
        for i in range(8):
            for j in range(8):
                piece = self.board.board[i][j]
                if not piece: continue
                self.window.blit(piece.image, (j*self.blockSize, i*self.blockSize))


    def getClickGrid(self):
        if not pygame.mouse.get_pressed()[0]: return False
        px, py = pygame.mouse.get_pos()
        return (py//self.blockSize, px//self.blockSize)


    def getChoosePiece(self, side):
        clickPos = self.getClickGrid()
        if not clickPos: return
        clicked = self.board.get(clickPos[0], clickPos[1])
        if not clicked or clicked.Side != side:
            self._resetTempStorage()
            return 
        thisAvailable = [
            (clicked.r+d[0], clicked.c+d[1]) for d in clicked.getMove(self.board.board)
        ]
        self.TempStorage["SquareHighLight"] = [(clicked.r, clicked.c)]
        self.TempStorage["DotHighLight"] = thisAvailable
        self.TempStorage["Moving"] = clicked
        self.TempStorage["MovingAvailable"] = thisAvailable
        self.State["Choosing"] = False
        self.State["Moving"] = True


    def getPieceMove(self):
        clickPos = self.getClickGrid()
        if not clickPos or not self.TempStorage["Moving"] or clickPos == (self.TempStorage["Moving"].r, self.TempStorage["Moving"].c): return 0
        if clickPos not in self.TempStorage["MovingAvailable"]: return -1
        self.board.movePiece(self.TempStorage["Moving"].r, self.TempStorage["Moving"].c, clickPos[0], clickPos[1])
        return 1


    def mainloop(self):
        while(True):
            if self._handleQuit(): break

            self.drawBoard()
            self.drawPieces()
            self.drawHighLight("square", self.TempStorage["SquareHighLight"])
            self.drawHighLight("dot", self.TempStorage["DotHighLight"])

            if self.State["Moving"]:
                moved = self.getPieceMove()
                if moved == 1: 
                    self.board.switchSide()
                    print(self.board.Side)
                    self._resetTempStorage()
                elif moved == -1:
                    self._resetTempStorage()
            elif self.State["Choosing"]:
                self.getChoosePiece(self.board.Side)


            self.FPS(60)
            pygame.display.update()

G = Game(760)
G.mainloop()

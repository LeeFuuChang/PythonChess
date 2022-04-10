import os

ProjectRoot = os.path.join(
    os.path.dirname(
        os.path.dirname(
            __file__
        )
    )
)

DotHighLightColor = (150, 22, 22)
DotHighLightRadius = 16
SquareHighLightColor = (22, 22, 150)


Values = {
    "King":12,
    "Queen":9,
    "Rook":5,
    "Bishop":3,
    "Knight":3,
    "Pawn":1,
    "Empty":0
}
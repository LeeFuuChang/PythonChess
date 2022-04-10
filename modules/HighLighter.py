from .Constants import *
import pygame

def typeDot(window, blockSize, r, c, color):
    pygame.draw.circle(
        window,
        color,
        (c*blockSize + blockSize//2, r*blockSize + blockSize//2),
        DotHighLightRadius, 
        0
    )

def typeSquare(window, blockSize, r, c, color):
    x, y, s1, s2 = c*blockSize, r*blockSize, blockSize/4, blockSize/12
    infos = [
        (x, y, s1, s2),
        (x, y, s2, s1),
        (x+blockSize-s1, y, s1, s2),
        (x+blockSize-s2, y, s2, s1),
        (x+blockSize-s1, y+blockSize-s2, s1, s2),
        (x+blockSize-s2, y+blockSize-s1, s2, s1),
        (x, y+blockSize-s2, s1, s2),
        (x, y+blockSize-s1, s2, s1),
    ]
    for ifo in infos:
        pygame.draw.rect(
            window,
            color,
            pygame.Rect(
                *ifo
            )
        )
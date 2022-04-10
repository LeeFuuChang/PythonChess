from .Constants import *

class Empty:
    Value = Values["Empty"]
    def __init__(self, Side, r, c):
        self.Side = Side
        self.r, self.c = r, c


    def __bool__(self):
        return False
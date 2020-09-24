from main import pygame
class Bomb:

        #bRad is blastRadius
    def __init__(self, bRadX, bRadY, bState, bTimer, bReload):
        self.bRadX = bRadX
        self.bRadY = bRadY
        self.bState = bState
        self.bTimer = bTimer
        self.bReload = bReload
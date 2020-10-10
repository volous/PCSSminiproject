import pygame as pg
import numpy as np


class Level:

    def __init__(self, sizeX, sizeY, posX, posY, objects):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX
        self.posY = posY
        self.objects = objects

    def level(self, screen):
        white = (255, 255, 255)
        pg.draw.rect(screen, white, (217, 117, 466, 466))

    def postitional_grid(self):
        for i in range(0, 13):
            for j in range(0, 13):


    def level2(self):
        pass

    def level3(self):
        pass

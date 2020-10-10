import pygame as pg
import numpy as np


class Level:

    def __init__(self, sizeX, sizeY, posX, posY, objects):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX
        self.posY = posY
        self.objects = objects

    # level
    def level(self, screen):
        # assigning a color
        white = (255, 255, 255)
        pg.draw.rect(screen, white, (217, 117, 480, 480))

    # position grid
    def postitional_grid(self, screen):
        # assigning a color
        black = (0, 0, 0)
        # for loop that, creates a grid from start of level edge to the end
        for i in range(0, 480):
            for j in range(0, 480):
                # assigning a pygame function that draws a rectangle
                rect = pg.Rect(217 + i * 32, 117 + j * 32, 32, 32)
                # using methods from pygame to draw a rectangle on the src screen,
                pg.draw.rect(screen, black, rect, 1)

    def level2(self):
        pass

    def level3(self):
        pass

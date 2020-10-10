import pygame as pg
import numpy as np


class Level:

    def __init__(self, sizeX, sizeY, posX, posY, objects, screen):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX
        self.posY = posY
        self.objects = objects
        self.screen = screen

    # level
    def level(self):
        # assigning a color
        white = (255, 255, 255)
        pg.draw.rect(self.screen, white, (217, 117, 480, 480))


    # position grid
    def postitional_grid(self):
        # assigning a color
        black = (0, 0, 0)
        block_size = 32
        # for loop that, creates a grid from start of level edge to the end
        for i in range(0, 480):
            for j in range(0, 480):
                # assigning a pygame function that draws a rectangle
                rect = pg.Rect(217 + i * block_size, 117 + j * block_size, block_size, block_size)
                # using methods from pygame to draw a rectangle on the src screen,
                pg.draw.rect(self.screen, black, rect, 1)
        for i in range(0, 480):
            for j in range(0, 480):
                rect = pg.Rect((217+block_size) + i * block_size, (117+block_size) + j * block_size, block_size, block_size)
                pg.draw.rect(self.screen, (125, 125, 125), rect, 1)
    def level2(self):
        pass

    def level3(self):
        pass
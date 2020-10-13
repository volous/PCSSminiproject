import pygame as pg
import numpy as np


class Level:

    def __init__(self, sizeX, sizeY, posX, posY, objects, screen, other_object):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.posX = posX
        self.posY = posY
        self.objects = objects
        self.screen = screen
        self.block_size = 32
        self.other_object = other_object
        self.hit = False

    # level
    def level(self):
        # assigning a color
        white = (255, 255, 255)
        pg.draw.rect(self.screen, white, (217, 117, 480, 480))

    # position grid
    def positional_grid(self):
        # assigning a color for the rectangles
        black = (0, 0, 0)
        blue = (0, 0, 255)
        # setting the size of the rectangles
        block_size = self.block_size
        # setting the map_size
        map_size = 15
        # adding a 2D array to store the rectangles
        positional_array = np.ndarray([map_size, map_size], dtype=pg.Rect)
        positional_array_bomb = np.ndarray([map_size, map_size], dtype=pg.Rect)
        # for loop that, creates a grid from start of level edge to the end
        for i in range(0, map_size):
            for j in range(0, map_size):
                # assigning a pygame function that draws a rectangle
                rect = pg.Rect(217 + i * block_size, 117 + j * block_size, block_size, block_size)
                positional_array[i, j] = [rect.x, rect.y]
                positional_array_bomb[i, j] = [(rect.x + 16), (rect.y + 16)]
                # pg.draw.line(self.screen, blue, (positional_array[i, j]), (positional_array[i, j]))
                # using methods from pygame to draw a rectangle on the src screen,
                pg.draw.rect(self.screen, black, rect, 1)

    def impassible_blocks(self):
        hit = self.hit
        player = self.other_object
        grey = (125, 125, 125)
        distance = 64
        block_size = self.block_size
        for i in range(0, 6):
            for j in range(0, 6):
                rect = pg.Rect(281 + i * distance, 181 + j * distance, block_size, block_size)
                pg.draw.rect(self.screen, grey, rect, 0)

        for i in range(0, 15):
            for j in range(0, 15):
                wall_rect_vert = pg.Rect(217 + i * block_size, 117 + j * 448, block_size, block_size)
                pg.draw.rect(self.screen, grey, wall_rect_vert, 0)
                wall_rect_hori = pg.Rect(217 + i * 448, 117 + j * block_size, block_size, block_size)
                pg.draw.rect(self.screen, grey, wall_rect_hori)
                if pg.sprite.collide_rect(wall_rect_hori, player):
                    hit = True
                    print("hit")
                else:
                    hit = False
                    print("not hit")









    def level3(self):
        pass

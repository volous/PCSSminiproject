import pygame as pg
from Bomber import Bomb

# initialize the pygame
pg.init()
# setting screen height, width and accessible size
size = width, height = 900, 700
# create screen
screen = pg.display.set_mode((width, height))
bomb_player_one = Bomb(10, 10, True, 200, True)
bomb_player_two = Bomb(10, 10, True, 200, True)
running = True
# game loop-ish
while running:
    # checks if there are events in the pygame window
    for event in pg.event.get():
        # if the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False
        # if a key is pressed down event is triggered
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                bomb_player_one.timer()
            if event.key == pg.K_UP:
                bomb_player_two.timer()
            pg.display.update()

import _thread
import pygame as pg
from Bomber import Bomb

# initialize the pygame
pg.init()
# setting screen height, width and accessible size
size = width, height = 900, 700

pg.display.set_caption("Bomberman Spin-off Game")
icon = pg.image.load("Res/bomb_icon.png")
pg.display.set_icon(icon)

bRadX, bRadY = 10, 10
# create screen
screen = pg.display.set_mode((width, height))
# instantiating Bomb class
bomb_player_one = Bomb(bRadX, bRadY, True, 5, True)
running = True
# game loop-ish
while running:
    # timer is available from start, but when an event type of keydown on space, timer_start from bomb class is set
    # to true and begins countdown
    bomb_player_one.timer()
    # checks if there are events in the pygame window
    for event in pg.event.get():
        # if the window closes, it gets closed properly
        if event.type == pg.QUIT:
            running = False
        # if a key is pressed down event is triggered
        if event.type == pg.KEYDOWN:
            # if key pressed is space the timer_start is set to true
            if event.key == pg.K_SPACE:
                bomb_player_one.timer_start = True
                bomb_player_one.bomb()

    pg.display.update()

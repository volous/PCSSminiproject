import time
import sys
class Bomb:

    # bRad is blastRadius
    def __init__(self, bRadX, bRadY, bState, bTimer, bMin, bReload):

        self.bRadX = bRadX
        self.bRadY = bRadY
        self.bState = bState
        self.bTimer = bTimer
        self.bMin = bMin
        self.bReload = bReload
    #     timer stuff

        self.start_timer = time.time()

    def bomb(self):
        pass

    def timer(self):
        while True:
            self.bTimer = int(time.time() - self.start_timer) - self.bMin

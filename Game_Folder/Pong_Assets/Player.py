import pygame as pg

class Player:

    def __init__(self):

        # size variables in case I need them
        self.sizeX = 30 
        self.sizeY = 100

        self.surface = pg.Surface((self.sizeX, self.sizeY))
        self.surface.fill('Blue')

        # Look at implementing a rectangle

        self.PosY = 100
        self.bottomY = self.PosY + self.sizeY
        self.Rect = self.surface.get_rect()

        #frictional coefficeint
        self.frictco = 0.09
    
    def update(self, focus, screenY):
        if focus and self.bottomY < screenY:
            self.PosY += 7
            self.up = 1
        if not focus and self.PosY >= 0:
            self.PosY -= 7
            self.up = -1
        self.bottomY = self.PosY + self.sizeY
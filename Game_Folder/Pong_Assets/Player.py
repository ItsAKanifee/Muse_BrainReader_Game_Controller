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
    
    def update(self, focus, screenY, down):
        if focus and self.bottomY < screenY and down:
            self.PosY += 3
            self.up = 1 # up vector to tell the ball whether the paddle is moving up or down
        elif focus and self.PosY >= 0 and not down: # move the ball down if the player is focusing on it going down
            self.PosY -= 3
            self.up = -1
        else:
            self.up = 0
        self.bottomY = self.PosY + self.sizeY
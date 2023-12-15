import pygame as pg
import math as mt

class Enemy:
    
    def __init__(self):

        # size variables in case I need them
        self.sizeX = 30 
        self.sizeY = 100

        self.surface = pg.Surface((self.sizeX, self.sizeY))
        self.surface.fill('Green')

        # Look at implementing a rectangle

        self.PosY = 100
        self.bottomY = self.PosY + self.sizeY

        #frictional coefficeint
        self.frictco = 0.09

    def update(self, BallV, screenY, BallPy, BallPx, Ball_Ang):
        self.up = 0
        destination = self.calculate(BallV, BallPy, BallPx, Ball_Ang)
        if self.PosY <= destination and self.bottomY <= screenY:
            self.PosY += 5
            self.up = 1
        if self.PosY >= destination and self.PosY >= 0:
            self.PosY -= 5
            self.up = -1
        self.bottomY = self.PosY + self.sizeY
    
    def calculate(self, BallV, BallPy, BallPx, Ball_Ang):
        Posx = 900 - BallPx

        Ball_Vx = mt.cos(mt.radians(Ball_Ang)) * BallV
        Ball_Vy = mt.sin(mt.radians(Ball_Ang)) * BallV

        time = Posx / Ball_Vx

        destination = (Ball_Vy * time) + BallPy

        return destination - 50



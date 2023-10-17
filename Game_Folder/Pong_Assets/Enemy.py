import pygame as pg

class Enemy:
    
    def __init__(self):

        # size variables in case I need them
        self.sizeX = 50 
        self.sizeY = 300

        self.surface = pg.Surface((self.sizeX, self.sizeY))
        self.surface.fill('Green')

        # Look at implementing a rectangle

        self.PosY = 100
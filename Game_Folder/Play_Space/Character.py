import pygame as pg

class Character:

    def __init__(self, posX, posY):
        self.surface = pg.Surface((50, 50))
        self.surface.fill('Red')

        self.posX = posX
        self.posY = posY
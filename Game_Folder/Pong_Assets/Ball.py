import pygame as pg

class Ball:

    def __init__(self):
        self.surface = pg.Surface((50,50))
        self.surface.fill('Red')

        self.Posx = 225
        self.Posy = 225
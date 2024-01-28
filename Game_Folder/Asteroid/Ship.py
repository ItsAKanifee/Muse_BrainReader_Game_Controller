import pygame as pg

class Ship:

    def __init__(self):

        # Base image of the ship, may replace with a PNG if I feel like it
        self.Surface = pg.Surface((10, 10))
        self.Surface.fill('Red')

        
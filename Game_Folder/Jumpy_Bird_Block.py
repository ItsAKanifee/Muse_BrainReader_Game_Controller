import pygame as pg

class Block:
    def __init__(self, size_y, screen_size_x, blocknum):
        self.block_surface = pg.Surface((70, size_y))
        self.block_surface.fill('Green')
        self.Posx = screen_size_x + blocknum*300
        self.Posy = 400 - size_y
        self.opening = self.Posy - 100
        self.Top_surface = pg.Surface((70, self.opening))
        self.Top_surface.fill('Green')


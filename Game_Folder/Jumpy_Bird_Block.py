import pygame as pg

class Block:
    def __init__(self, size_y):
        block_surface = pg.Surface((50, size_y))
        block_surface.fill('Green')


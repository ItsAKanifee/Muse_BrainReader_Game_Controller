import pygame as pg
import random

class Block:
    
    def __init__(self, xLength) -> None: # initialize the block with a determined length based on the previous tile
        self.surface = pg.Surface((xLength, 50))

        colors = ['Red', 'Green', 'Blue', 'White', 'Black', 'Brown', 'Yellow', 'Orange']
        i = random.randrange(0, len(colors))
        self.surface.fill(colors[i])

        self.direction = 1 # put a boolean int for the direction of the object

    
    def fall(self, cutoffEnd):
        pass



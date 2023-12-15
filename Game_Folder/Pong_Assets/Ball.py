import pygame as pg
import math as mt
import random

class Ball:

    def __init__(self):
        self.surface = pg.Surface((50,50))
        self.surface.fill('Red')

        self.Posx = 300
        self.Posy = 300
        
        self.velocity = 7
        self.angle = 30

        #get the full block
        self.bottomY = self.Posy + 50 

        self.mass = .0027

    def update(self, screen_x):
        self.xvelocity = mt.cos(mt.radians(self.angle)) * self.velocity
        self.Posx += self.xvelocity
        self.yvelocity = mt.sin(mt.radians(self.angle)) * self.velocity
        self.Posy += self.yvelocity

        self.bottomY = self.Posy + 50

        if self.Posx <= -50 or self.Posx>= screen_x:
            self.Posx = screen_x/2
            self.Posy = 300
            self.angle = random.randrange(20,45)
            self.velocity = -self.velocity
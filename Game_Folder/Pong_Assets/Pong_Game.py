import pygame as pg
import math as mt
from .Player import Player
from .Ball import Ball
from .Enemy import Enemy

class Game:

    def __init__(self, screen_size_x, screen_size_y): # initialize the game

        self.screen_x = screen_size_x
        self.screen_y = screen_size_y

        self.screen = pg.display.set_mode((screen_size_x, screen_size_y))
        self.screen_surface =  pg.Surface((screen_size_x, screen_size_y))
        self.screen_surface.fill('Cyan')

        pg.display.set_caption("Ping") # named for copyright purposes

        # add in the player, enemy, and ball objects

        self.ball = Ball()
        self.player = Player()
        self.enemy = Enemy()

        pg.display.flip()

    def logic():
        pass
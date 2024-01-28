import pygame as pg
from Character import Character

class Field:

    def __init__(self, screen_size_x, screen_size_y):

        #initialize the screen size of the game
        self.screenX = screen_size_x
        self.screenY = screen_size_y

        # Make a screen of the game
        self.screen = pg.display.set_mode((screen_size_x, screen_size_y))
        self.screen_surface =  pg.Surface((screen_size_x, screen_size_y))
        self.screen_surface.fill('Cyan')

        pg.display.set_caption("Play Space")

        self.Player = Character(50, 50) # character of player

        pg.display.flip()

    def logic():
        pass




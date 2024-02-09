import pygame as pg

class Game:

    def __init__(self, screen_size_x, screen_size_y):

        #initialize the screen size of the game
        self.screenX = screen_size_x
        self.screenY = screen_size_y

        # Make a screen of the game
        self.screen = pg.display.set_mode((screen_size_x, screen_size_y))
        self.screen_surface =  pg.Surface((screen_size_x, screen_size_y))
        self.screen_surface.fill('Cyan')

        pg.display.set_caption("Stacker")

        self.base = pg.Surface((50, 50))
        self.base.fill('Black')
    

    def logic(self):
        pass

        
import pygame as pg

class Player:

    def __init__(self, size_x, size_y):
        self.Player_surface = pg.Surface((size_x, size_y))
        self.Player_surface.fill('Red')

        # setting up positional variables for the object
        self.Size_x, self.Size_y = size_x, size_y
        self.Posx, self.Posy = 50, 50

        # counting variables 
        self.frame = 0
        self.falltime = 0
        self.Jump_Velocity = 0
        self.bounceFrame = 0

    def update_position(self, posx, posy):
        pass

        
    
    def update_size(self, size_x, size_y):
        self.Size_x, self.Size_y = size_x, size_y
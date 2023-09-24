import pygame as pg

class Player:

    def __init__(self, size_x, size_y):
        self.Player_surface = pg.Surface((size_x, size_y))
        self.Player_surface.fill('Red')
        self.Size_x, self.Size_y = size_x, size_y
        self.Posx, self.Posy = 50, 50

    def update_position(self, posx, posy):
        self.Posx = posx
        self.Posy = posy
        
    
    def update_size(self, size_x, size_y):
        self.Size_x, self.Size_y = size_x, size_y
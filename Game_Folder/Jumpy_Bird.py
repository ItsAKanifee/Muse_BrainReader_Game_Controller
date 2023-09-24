import pygame as pg
from .Jumpy_Bird_Player import Player


class Game:

    def __init__(self, screen_size_x, screen_size_y): # initialize the game

        object_length = 50
        object_height = 100

        self.frame = 0 # initialize counting variables
        self.falltime = 0
        self.Jump_Velocity = 0
        self.Ground_surface_y = 0

        background_color = (234,212,252)
        self.clock = pg.time.Clock()

        self.screen = pg.display.set_mode((screen_size_x, screen_size_y))
        self.screen_surface =  pg.Surface((screen_size_x, screen_size_y))
        self.screen_surface.fill('Cyan')

        pg.display.set_caption("Jumpy Bird")

        self.screen.fill(background_color)

        self.ground_surface = pg.Surface((screen_size_x, object_height))
        self.ground_surface.fill('Brown')

        self.Player = Player(object_length, object_length) # create the player character
        self.Player_original_x, self.Player_original_y = object_length, object_length #store the valus of the player

        pg.display.flip()
    
    def logic(self, blink, focus): # need a method for jumping, gravity, and the pipe movement
        if self.frame > 0:
            self.frame -= 1 # count the frames to finish the cooldown in physics
        self.falltime += 1 # count the frames to declare a falltime in physics

        self.physics(blink)
        #self.shrink(focus)

        self.Ground_surface_y = self.screen.get_size()[1] - 100 # Make the ground around 100 above the height of the screen
        self.screen.blit(self.screen_surface, (0,0))
        self.screen.blit(self.ground_surface, (0, self.Ground_surface_y))
        self.screen.blit(self.Player.Player_surface, (self.Player.Posx, self.Player.Posy))
        pg.display.update()
    


    def physics(self, blink): # Here is the function that defines falls, bounces, and jumps
        Gravity = 9.8

        if blink and self.frame == 0: # add in a cooldown so that someone cannot spam the jump
            self.falltime = 0
            self.Jump_Velocity = -5
            self.frame = 30
        
        fall_velocity = self.Jump_Velocity + Gravity * self.frame # falling animation

        if self.Player.Posy >= self.Ground_surface_y: # bounce if it hits the ground
            self.Jump_Velocity = -fall_velocity

        if 0 <= self.Player.Posy <= self.Ground_surface_y:
            self.Player.Posy = self.Player.Posy + 1
            
            self.Player.update_position(self.Player.Posx, self.Player.Posy)
            print(self.Player.Posy)
            

           

    def shrink(self, focus): # make the block shrink when the player is focused on it

        if focus and self.Player.Size_x >= 10 and self.Player.Size_y >= 10: # if the player is focusing, allow avatar to shrink as long as size limit has not been reached
            self.Player.update_size(self.Player.Size_x - 1, self.Player.Size_y - 1)
        elif focus: # if size limit has been reached, do nothing
            pass 
        elif self.Player.Size_x < self.Player_original_x and self.Player.Size_y < self.Player_original_y: # if player is not focusing, make avatar grow back to original size
            self.Player.update_size(self.Player.Size_x + 1, self.Player.Size_y + 1)

    def generateBlock(): # figure out a way to generate random blocks
        pass

        

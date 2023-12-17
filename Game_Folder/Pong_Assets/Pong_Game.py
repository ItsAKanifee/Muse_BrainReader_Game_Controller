import pygame as pg
import math as mt
from .Player import Player
from .Ball import Ball
from .Enemy import Enemy

class Game:

    def __init__(self, screen_size_x, screen_size_y): # initialize the game

        self.screen_x = screen_size_x
        self.screen_y = screen_size_y

        self.frame = 0

        self.screen = pg.display.set_mode((screen_size_x, screen_size_y))
        self.screen_surface =  pg.Surface((screen_size_x, screen_size_y))
        self.screen_surface.fill('Cyan')

        pg.display.set_caption("Ping") # named for copyright purposes

        # add in the player, enemy, and ball objects
        self.ball = Ball()
        self.player = Player()
        self.enemy = Enemy()

        pg.display.flip()

    def logic(self, blink, focus):
        # move the objects
        self.ball.update(self.screen_x)
        self.player.update(focus, self.screen_y)
        self.enemy.update(self.ball.velocity, self.screen_y, self.ball.Posy, self.ball.Posx, self.ball.angle)

        self.physics()
        
        self.screen.blit(self.screen_surface, (0,0))
        self.screen.blit(self.player.surface, (50, self.player.PosY))
        self.screen.blit(self.enemy.surface, (900, self.enemy.PosY))
        self.screen.blit(self.ball.surface, (self.ball.Posx, self.ball.Posy))
        pg.display.update()

    def physics(self):
        #frame cooldown 
        if self.frame > 0:
            outside = False
            self.frame -= 1
        else:
            outside = True
        # if the ball hits, bounce
        if self.ball.Posy <= 0 or self.ball.Posy >= self.screen_y:
            self.ball.angle = -self.ball.angle

        if 30 <= self.ball.Posx <= 80  and (self.player.PosY <= self.ball.Posy <= self.player.bottomY or self.player.PosY <= self.ball.bottomY <= self.player.bottomY) and outside:
            self.collision(True)
            self.ball.velocity = -self.ball.velocity
            self.frame = 10
        
        if 950 >= self.ball.Posx + 50 >= 900 and (self.enemy.PosY <= self.ball.Posy <= self.enemy.bottomY or self.enemy.PosY <= self.ball.bottomY <= self.enemy.bottomY) and outside:
            self.collision(False)
            self.ball.velocity = -self.ball.velocity
            self.frame = 10
    
    def collision(self, player):
        #Calculate the force the ball acts on the paddle
        momentum = self.ball.mass * self.ball.xvelocity
        netForce = momentum * 2 / 0.01 # multply momentum by two to get change in momentum

        if player:
            FrictForce = self.player.frictco * netForce
            upwards = self.player.up
        else:
            FrictForce = self.enemy.frictco * netForce
            upwards = self.enemy.up

        MomentY = FrictForce * 0.01 #change in momentum y

        
        MomentY = upwards * MomentY # Make change negative if going down
        
        Vely = MomentY / self.ball.mass # change in y velocity

        FinVelx = self.ball.xvelocity - (netForce/ self.ball.mass * .01)
        FinVely = self.ball.yvelocity + Vely

        self.ball.angle = int(mt.degrees(mt.atan(FinVely / FinVelx)))
        
        
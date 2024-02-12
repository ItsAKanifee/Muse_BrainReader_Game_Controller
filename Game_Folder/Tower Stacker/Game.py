import pygame as pg
import random

class Game:

    def __init__(self, screen_size_x, screen_size_y):

        #initialize the screen size of the game
        self.screenX = screen_size_x
        self.screenY = screen_size_y

        # maybe make a deque or something to store the blocks in
        self.stack = []

        # Make a screen of the game
        self.screen = pg.display.set_mode((screen_size_x, screen_size_y))
        self.screen_surface =  pg.Surface((screen_size_x, screen_size_y))
        self.screen_surface.fill('Cyan')

        pg.display.set_caption("Stacker")
        pg.display.flip()

        base = Block(100, [0,0,0], 0) # set color to black, and velocity to 0
        base.posx = screen_size_x/ 3
        base.posy = 500

        self.stack.append(base) # put in the first block of the stack

        # conditions for the 'landing zone' of the block
        self.base_xStart = screen_size_x/ 3
        self.base_xEnd = self.base_xStart + 100

        self.stack.append(base)

        self.rgb = [250, 0, 0]
        self.velocity = 5

        self.block = Block(100, self.rgb, self.velocity)

        self.stillIn = True # make a boolean that will tell if the player has lost the game
    

    def logic(self, blink):
       self.block.update(self.screenX)
    
    # Have next method be called whenever the user blinks, where it will drop the current block onto the base,
    # Cutoff any thing extending the base, move base down, and call in a new block assuiming still has length
    def drop(self): 

        self.block.drop(self.base_xStart, self.base_xEnd)
        floor = self.block # set the landing zone for the next block

        self.base_xStart = floor.posx
        self.base_xEnd = floor.posx + floor.length

        self.rgb = [self.rgb[0] - 10, self.rgb[1] + 15, self.rgb[2] + 25]

        self.stack.append(floor)
        self.velocity += 0.3
        self.block = Block(floor.length, self.rgb, self.velocity)




class Block:
    
    def __init__(self, xLength, rgb, velocity) -> None: # initialize the block with a determined length based on the previous tile
        self.surface = pg.Surface((xLength, 10))
        self.length = xLength

        self.surface.fill(rgb[0], rgb[1], rgb[2]) # change the rgb values outside of the block, and init them inside block

        self.direction = 1 # put a boolean int for the direction of the object

        self.velocity = velocity

        self.posx = 0
        self.posy = 490
    
    def update(self, screenX):
        checked = False # make a variable to keep studders from happening
        self.posx += self.velocity * self.direction
        if (self.posx + self.length >= screenX or self.posx <= 0) and not checked:
            self.direction *= -1
        if checked and (self.posx + self.length < screenX or self.posx > 0): # update checked only when the block comes back into bounds
            checked = False
        
    def drop(self, xStart, xEnd) -> bool:
        self.velocity = 0

        if self.posx + self.length < xStart or self.posx > xEnd: # determines if none of the block is on the landing zone
            return False # tells game logic that the move was a loss
        
        if self.posx > xStart: # if the left of the block is within the zone
            self.length = xEnd - self.posx # will not change if block is within bounds
            self.surface = pg.Surface((self.length, 10))
            return True
        else:
            cutoff = xStart - self.posx # find the difference between the landing point and where the block actually is
            self.posx = xStart # move the pos of the block to the start of the landing
            self.length -= cutoff # remove anything else from the length
            self.surface = pg.Surface((self.length, 10))
            return True
import pygame as pg
import random

class Game:

    def __init__(self, screen_size_x, screen_size_y):

        #initialize the screen size of the game
        self.screenX = screen_size_x
        self.screenY = screen_size_y

        # maybe make a deque or something to store the blocks in

        # Make a screen of the game
        self.screen = pg.display.set_mode((screen_size_x, screen_size_y))
        self.screen_surface =  pg.Surface((screen_size_x, screen_size_y))
        self.screen_surface.fill('Cyan')

        pg.display.set_caption("Stacker")
        pg.display.flip()

        self.game_font = pg.font.SysFont('Comic Sans MS', 30)
        self.highScore = 0
        self.highScore_surface = self.game_font.render("High Score: " + str(self.highScore), False, (0, 0, 0))

        self.create()

    def create(self):

        self.score = 0
        self.score_surface = self.game_font.render("Score: " + str(self.score), False, (0, 0, 0))

        base = Block(200, [0,0,0], 0) # set color to black, and velocity to 0
        base.posx = self.screenX/ 3
        base.posy = 500

        # conditions for the 'landing zone' of the block
        self.base_xStart = self.screenX/ 3
        self.base_xEnd = self.base_xStart + 200

        self.stack = [base]

        self.rgb = [250, 0, 0]
        self.velocity = 2

        self.block = Block(200, self.rgb, self.velocity)

        self.stillIn = True # make a boolean that will tell if the player has lost the game

        self.wait = 0

        self.lose = False
    

    def logic(self, blink, focus):

        if blink and self.wait == 0:
           self.drop()
           self.wait = 60

        self.screen.blit(self.screen_surface, (0,0))

        if self.lose:
            youLose = self.game_font.render("You Lose", True, (0, 0, 0))
            self.screen.blit(youLose, (self.screenX / 2, self.screenY / 2))

            if self.wait == 0:
                self.create()
                    
        
        else:
            self.drawStack()
            self.screen.blit(self.block.surface, (self.block.posx, self.block.posy))
            self.screen.blit(self.score_surface, (850, 10))
            self.screen.blit(self.highScore_surface, (800, 50))

        pg.display.update()  

        self.block.update(self.screenX) # realized this should be afterwards so that the image does not update before the press is realized


        if self.wait > 0:
            self.wait -= 1
    
    # Have next method be called whenever the user blinks, where it will drop the current block onto the base,
    # Cutoff any thing extending the base, move base down, and call in a new block assuiming still has length
    def drop(self): 

        success = self.block.drop(self.base_xStart, self.base_xEnd)

        if not success:
            print("You lose")
            self.lose = True
            return
        else:
            self.score += 1
            self.score_surface = self.game_font.render("Score: " + str(self.score), True, (0, 0, 0))

            if self.score > self.highScore:
                self.highScore = self.score
                self.highScore_surface = self.game_font.render("High Score: " + str(self.highScore), True, (0, 0, 0))

        floor = self.block # set the landing zone for the next block

        self.base_xStart = floor.posx
        self.base_xEnd = floor.posx + floor.length

        self.rgb = [self.rgb[0] - 10, self.rgb[1] + 15, self.rgb[2] + 25]

        self.stack.append(floor)
        self.velocity += 0.2

        self.shift()

        self.block = Block(floor.length, self.rgb, self.velocity) # make a new block to move around
    
    def shift(self): # shift all blocks down when block is dropped
        length = len(self.stack)
        i = 0
        while i < length: 
            self.stack[i].posy += 10

            # remove blocks from the list if they stretch out of bounds so as to not be capped in RAM
            if self.stack[i].posy >= self.screenY: 
                self.stack.pop(i)
                length -= 1
            
            i += 1

    def drawStack(self):
        for i in range(len(self.stack)):
            block = self.stack[i]
            self.screen.blit(block.surface, (block.posx, block.posy))




class Block:
    
    def __init__(self, xLength, rgb, velocity) -> None: # initialize the block with a determined length based on the previous tile
        self.surface = pg.Surface((xLength, 10))
        self.length = xLength

        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        self.surface.fill('Red') # change the rgb values outside of the block, and init them inside block

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
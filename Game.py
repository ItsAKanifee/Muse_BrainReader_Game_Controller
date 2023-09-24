import pygame as pg
import Experiment as ex
import asyncio as asyn

BUFFER_LENGTH = 5

EPOCH_LENGTH = 1

OVERLAP_LENGTH = 0.8

SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH

INDEX_CHANNEL = [0]

inlet, eeg_buffer, filter_state, band_buffer, fs = ex.define(BUFFER_LENGTH, EPOCH_LENGTH, SHIFT_LENGTH) # set up the data stream with the Muse device


#create surface to test the game
# all of this can probably be placed into a class method as well
pg.init()
background_color = (234,212,252)
clock = pg.time.Clock()

screen = pg.display.set_mode((500,500))

screen_surface = pg.Surface((500,500))
screen_surface.fill('White')

d1 = 50

test_surface = pg.Surface((d1,d1))
test_surface.fill('Red')

pg.display.set_caption("Mindgame")

screen.fill(background_color)

pg.display.flip()

# position of the block
posx = 100
posy = 100

# counting the frames to determine when to call
frame = 0

# global values for the brain reader to alter
blink = False
focus = False

async def controller_Function(inlet, eeg_buffer, filter_state, band_buffer, fs): # calls the brain scanner method
    while True:
        global blink, focus
        values, timestamp, beta = (ex.samples(SHIFT_LENGTH, fs, INDEX_CHANNEL, EPOCH_LENGTH, eeg_buffer, band_buffer, filter_state, inlet)) # get values that prove necessary
        if values[0] > .72:
            blink = True
        else:
            blink = False
        if beta > 10:
            focus = True
        else:
            focus = False
        await asyn.sleep(0.1) #need a cooldown time so that pygmame can be closed without causing errors
    
def game_logic(blink, focus): # plug in the user boolean of the game
    pass # convert this into a seperate class, this will be the basis for the games

async def main():
    global inlet, eeg_buffer, filter_state, band_buffer, fs
    controller_task = asyn.create_task(controller_Function(inlet, eeg_buffer, filter_state, band_buffer, fs)) # calls the controller_Function to run asynchronously

    running = True

    while running:
        global posx, posy, blink, focus, d1, test_surface # call global variables so that data can be shared between methods
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break
            if event.type == pg.KEYUP:
                posy += 5

        # Sample conditions to try out functions for the actual game
        if blink: 
            posx += 1 # move block to the right whenever the user blinks
        if focus: # grow or shrink the block depending on if the user is focusing, can also be used as a way to debug the focus reader on the scanner fucnction
            d1 += 10
            test_surface = pg.Surface((d1,d1))
            test_surface.fill('Red')
        elif d1 > 10:
            d1 -= 10
            test_surface = pg.Surface((d1,d1))
            test_surface.fill('Red')

        screen.blit(screen_surface,(0,0))
        screen.blit(test_surface,(posx,posy))
        pg.display.update()
        await asyn.sleep(.01)

    controller_task.cancel() 


try:
    asyn.run(main())
except asyn.CancelledError:
    pass  # Ignore CancelledError when the controller task is canceled

# Quit Pygame
pg.quit()
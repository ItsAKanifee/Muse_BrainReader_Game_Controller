import pygame as pg
import Experiment as ex

BUFFER_LENGTH = 5

EPOCH_LENGTH = 1

OVERLAP_LENGTH = 0.8

SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH

INDEX_CHANNEL = [0]

inlet, eeg_buffer, filter_state, band_buffer, fs = ex.define(BUFFER_LENGTH, EPOCH_LENGTH, SHIFT_LENGTH)

background_color = (234,212,252)
clock = pg.time.Clock()

screen = pg.display.set_mode((500,500))

screen_surface = pg.Surface((500,500))
screen_surface.fill('Cyan')

ground_surface = pg.Surface((500, 50))
ground_surface.fill('Green')

block_surface = pg.Surface((50, 50))
block_surface.fill('Brown')

test_surface = pg.Surface((50, 50))
test_surface.fill('Red')

pg.display.set_caption("Jumper")

screen.fill(background_color)

pg.display.flip()

running = True

Tposx = 100
Tposy = 100

Bposx = 490

falltime = 0
gravity = 9.8
jump = 0

while running:

    values, timestamp, smooth = (ex.samples(SHIFT_LENGTH, fs, INDEX_CHANNEL, EPOCH_LENGTH, eeg_buffer, band_buffer, filter_state, inlet))

    
    # actions for when keys are pressed
    for event in pg.event.get(): 
        if event.type == pg.QUIT:
            running = False
            break
        if event.type == pg.K_SPACE:
            Tposx += 5
        if event.type == pg.KEYUP:
            falltime = 0
            jump = -5


    if values[0] > 1:
        falltime = 0
        jump = -5
    # changes in position and velocity while the game is running 
    Bposx -= 2
    falltime += 1/60
    Tposy += jump + 0.5 * (gravity * falltime **2)

    

    # bounce
    if Tposy > 400:
        jump = -5
        falltime = 0

    if Bposx < -40:
        Bposx = 500

    #Layering hte screen from background to forground
    screen.blit(screen_surface,(0, 0))
    screen.blit(ground_surface, (0, 450))
    screen.blit(block_surface, (Bposx, 400))
    screen.blit(test_surface,(Tposx, Tposy))

    #Updating the screen so that all changes can be seen
    pg.display.update()
    clock.tick(256)
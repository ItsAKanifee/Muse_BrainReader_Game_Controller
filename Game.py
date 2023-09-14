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
screen_surface.fill('White')

d1 = 50

test_surface = pg.Surface((d1,d1))
test_surface.fill('Red')

pg.display.set_caption("Mindgame")

screen.fill(background_color)

pg.display.flip()

running = True

posx = 100
posy = 100

while running:
    values, timestamp, smooth = (ex.samples(SHIFT_LENGTH, fs, INDEX_CHANNEL, EPOCH_LENGTH, eeg_buffer, band_buffer, filter_state, inlet))

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
            break
        if event.type == pg.KEYUP:
            posx += 5

    if values[0] > 1:
        posx += 10
    if smooth[1] / smooth[3] > 1:
        d1 += 10
        test_surface = pg.Surface((d1,d1))
        test_surface.fill('Red')

    screen.blit(screen_surface,(0,0))
    screen.blit(test_surface,(posx,posy))

    pg.display.update()
    clock.tick(60)
import pygame as pg
import asyncio as asyn
import random

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

condition_one = False
condition_two = False

Tposx = 100
Tposy = 100

Bposx = 490

falltime = 0
gravity = 9.8
jump_Velocity = 0

async def Controller_Method(): # simulate the output of the Muse Device
    while True: 
        global condition_one, condition_two
        if random.randrange(0,9) <= 5: # give the numbers a 50% chance to produce either true or false
            condition_one = True
            print('something')
        else:
            condition_one = False # change the global variables to be either true or false
            print('something else')
        if random.randrange(0,9)  <= 5: 
            condition_two = True
        else:
            condition_two = False
        await asyn.sleep(1) # simulates delay in reader, and is necessary to allow for the pygame method not to break
         
def game_Method():
    pass # call the method for the game class here

async def main():

    global Tposx, Tposy, Bposx, falltime, gravity, jump_Velocity

    frame = 0

    controller_Function = asyn.create_task(Controller_Method())

    running = True
    while running:
    
    
        # actions for when keys are pressed
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                running = False
                break
            if event.type == pg.K_SPACE:
                Tposx += 5
            if event.type == pg.KEYUP:
                falltime = 0
                jump_Velocity = -5


        if condition_one and frame == 0: # make a coold down method
            falltime = 0
            jump_Velocity = -5
            frame = 30

        # changes in position and velocity while the game is running 
        Bposx -= 2
        falltime += 1/100
        if Tposy >= 0:
            yVelocity = (gravity * falltime)
            Tposy += jump_Velocity + yVelocity



        # bounce
        if Tposy > 400:
            jump_Velocity = -(jump_Velocity + yVelocity)
            falltime = 0

        if Tposy <= 0:
            jump_Velocity = 0
            yVelocity = (gravity * falltime)
            Tposy += yVelocity
            

        if Bposx < -40:
            Bposx = 500

        if frame > 0:
            frame -= 1 # count frames for a delay input

        #Layering the screen from background to forground
        screen.blit(screen_surface,(0, 0))
        screen.blit(ground_surface, (0, 450))
        screen.blit(block_surface, (Bposx, 400))
        screen.blit(test_surface,(Tposx, Tposy))

        #Updating the screen so that all changes can be seen
        pg.display.update()
        await asyn.sleep(0.01)

    controller_Function.cancel()

try:
    asyn.run(main())
except asyn.CancelledError: pass

pg.quit()
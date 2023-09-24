from Game_Folder import Jumpy_Bird as JB
import pygame as pg
import asyncio as asyn
import random



condition_one, condition_two = False, False

async def Controller_Method(): # simulate the output of the Muse Device
    while True: 
        global condition_one, condition_two
        if random.randrange(0,9) <= 5: # give the numbers a 50% chance to produce either true or false
            #condition_one = True
            print('something')
        else:
            condition_one = False # change the global variables to be either true or false
            print('something else')
        if random.randrange(0,9)  <= 5: 
            condition_two = True
        else:
            condition_two = False
        await asyn.sleep(1) # simulates delay in reader, and is necessary to allow for the pygame method not to break
         

async def main():

    global  condition_one, condition_two

    pg.init()

    Game = JB.Game(500, 500)

    controller_Function = asyn.create_task(Controller_Method())

    running = True
    while running:
    
    
        # actions for when keys are pressed
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                running = False
                break
                  
        Game.logic(blink= condition_one, focus= condition_two)
        await asyn.sleep(0.01)

    controller_Function.cancel()

try:
    asyn.run(main())
except asyn.CancelledError: pass
pg.quit()

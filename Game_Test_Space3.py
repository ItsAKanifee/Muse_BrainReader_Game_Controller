from Game_Folder import Jumpy_Bird as JB
import pygame as pg
import asyncio as asyn
import random


blink, focus = False, False

wait = 0

async def Controller_Method(): # Output of the Muse Device
    while True: 
        global blink, focus, wait

        if wait > 0:
            wait -= 1
        
        delta_metric = random.randrange(-1,4)
        beta_metric = random.randrange(-1,4)

        if delta_metric > 2 and wait == 0:# I need a cooldown for blinks because it stays active for too long
            blink = True
            wait = 5
        else:
            blink = False

        if 0.18 < beta_metric and delta_metric < 0.8:
            focus = False
        elif .7 < beta_metric:
            focus = False
        else:
            focus = False

        await asyn.sleep(0.15) # necessary to not allow the pygame method to break
         

async def main():

    global  blink, focus

    pg.init()

    Game = JB.Game(500, 500)

    controller_Function = asyn.create_task(Controller_Method())

    running = True
    while running:
        test = False
    
        # actions for when keys are pressed
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                running = False
                break
            if event.type == pg.KEYUP:
                test = True
                  
        Game.logic(test, focus)
        await asyn.sleep(0.01)

    controller_Function.cancel()

try:
    asyn.run(main())
except asyn.CancelledError: pass
pg.quit()

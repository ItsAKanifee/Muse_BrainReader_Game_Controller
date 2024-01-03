from Game_Folder import Jumpy_Bird as JB
import pygame as pg
import asyncio as asyn
import random
from Muse_Reader_Assets import Reader
from Game_Folder.Pong_Assets import Pong_Game as PG

Muse_Device = Reader.Muse()

blink, focus = False, False

wait = 0


async def Controller_Method(): # Output of the Muse Device
    deltBef = 0 # store delta metric from previous instance
    increasing = False
    beta_decreasing = 0
    betBef = 0
    checked = 0
    lowestB = 0
    while True: 
        global blink, focus, wait

        if wait > 0:
            wait -= 1
        
        print('help')
        
        alpha_metric, beta_metric, theta_metric, delta_metric = Muse_Device.process()

        
        if delta_metric - deltBef >= 0.37: # I just realized, if there is a huge jump in this value when you blink, just measure that as true or false
            increasing = True
           
        else:
            increasing = False

        

        if  wait == 0 and increasing and delta_metric > 1:# I need a cooldown for blinks because it stays active for too long
            blink = True
            wait = 2
            print('jump')
        else:
            blink = False

    
        deltBef = delta_metric

        if delta_metric < 1:
            checked = 0

        print(beta_metric)

        if beta_metric < lowestB:
            lowestB = beta_metric
        
        # test whether the player is focusing or not on the object
        if betBef > beta_metric:
            if beta_metric < 10: # count up to 10 times, then stop counter
                beta_decreasing += 1
            
        else:
            if beta_metric > -10: # repeat with the other one but in the opposite direction
                beta_decreasing -= 1
        
        betBef = beta_metric
        
        if delta_metric > 1: # reset function
            lowestB = 0
        

        # count how many times the player is focusing to not focusing 
        if beta_metric > (lowestB + 0.1):
            focus = True
        else:
            focus = False


        await asyn.sleep(0.2) # necessary to not allow the pygame method to break
         

async def main():

    global blink, focus

    pg.init()

    #Game = JB.Game(500, 500) # Flappy Bird
    Game = PG.Game(1020, 700) # Pong

    controller_Function = asyn.create_task(Controller_Method())

    running = True
    while running:
        focus = False
    
        # actions for when keys are pressed
        for event in pg.event.get(): 
            if event.type == pg.QUIT:
                running = False
                break

        

        Game.logic(blink, focus)
        await asyn.sleep(0.01)

    controller_Function.cancel()

try:
    asyn.run(main())
except asyn.CancelledError: pass
pg.quit()

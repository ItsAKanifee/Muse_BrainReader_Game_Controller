import pygame
import asyncio
import random

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pygame with Controller Function")
clock = pygame.time.Clock()

d1 = 50

screen_surface = pygame.Surface((800,600))
screen_surface.fill('White')

test_surface = pygame.Surface((d1,d1))
test_surface.fill('Red')
pygame.display.flip()

posx = 100
posy = 100



# Define your controller function (which takes 0.1 seconds to run)
async def controller_function():
    while True:
        # Your controller logic here
        global posy
        a = random.randrange(0,9)
        if(a > 5):
            posy += 5
            print('hello')
        else:
            posy -= 5
            print('goodbye')
        await asyncio.sleep(0.1)  # Simulate a 0.1-second delay

# Define your game logic function
def game_logic():
    global posx, posy, screen
    if(posy > 100):
        print('what')
    else:
        print('why')  
    screen.blit(screen_surface,(0,0))  
    screen.blit(test_surface,(posx,posy))
    pygame.display.update()


# Create an asyncio event loop
async def main():
    # Create tasks for the controller function and game logic
    controller_task = asyncio.create_task(controller_function()) #This part right here is what is needed to make it work

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Your game logic is called here at 60 FPS
        game_logic()

        # Allow the controller function to run asynchronously
        await asyncio.sleep(0.01)  # This determines the frame rate (60 FPS)

    # Stop the controller function when the user quits
    controller_task.cancel()

# Run the main event loop
pygame.key.set_repeat(1, 1)  # Enable key repeat for better user input handling
pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

try:
    asyncio.run(main())
except asyncio.CancelledError:
    pass  # Ignore CancelledError when the controller task is canceled

# Quit Pygame
pygame.quit()

import pandas as pd
import pygame as pg
from Muse_Reader_Assets import Reader

Device = Reader.Muse()
timestamp = 0
i = 0

screen = pg.display.set_mode((1020, 700))
screen_surface =  pg.Surface((1020, 700))
screen_surface.fill('Cyan')

pg.display.set_caption("Scanner Test")
pg.display.flip()

test_surface = pg.Surface((50,50))
test_surface.fill('Red')

running = True
wait = 0 
on = 60

df1 = pd.DataFrame([["Timestamp: ", "Beta: ", "Delta: "], [0,0,0]])

x = 400
y = 400

while running:
        
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        running = False
                        break
        
        screen.blit(screen_surface, ((0,0)))
 
        
        if not on == 0:
          screen.blit(test_surface, (x, y))
          on -= 1
        elif wait == 0:
            wait = 30
            print('stop', timestamp)
        else:
            wait -= 1
            if wait == 0:
                on = 60
                print('start', timestamp)
                  
        alpha, beta, theta, delta = Device.process()
        
        df1.loc[i+1] = [timestamp, beta, delta]

        timestamp += 1/3
        i += 1
        pg.display.update()
    

print('closing')
df1.to_excel('output.xlsx', index=False)
print(df1)
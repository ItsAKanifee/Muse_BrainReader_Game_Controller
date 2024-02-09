
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import pandas as pd
import math
import pylsl
import numpy as np
from Muse_Reader_Assets import Reader

values = []
time = []
y1 = []
y2 = []
y3 = []
y4 = []

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4)
ax1.plot(time, y1)
ax2.plot(time, y2)
ax3.plot(time, y3)
ax4.plot(time, y4)



plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

Device = Reader.Muse()

timestamp = 0

df1 = pd.DataFrame([["timestamp: ", "Beta: ", "Delta: "], [0,0,0]])

def update(i):
    global timestamp
    
    alpha, beta, theta, delta = Device.process()
    time.append(timestamp)

    df1.loc[i+1] = [timestamp, beta, delta]
    
    y1.append(alpha)
    y2.append(beta)
    print("timestamp: ", timestamp,  "Delta: ", delta)
    y3.append(theta)
    y4.append(delta)
    plt.cla()
    ax1.plot(time, y1)
    ax2.plot(time, y2)
    ax3.plot(time, y3)
    ax4.plot(time, y4)


    timestamp += .1
    


animation = ani.FuncAnimation(fig, update, interval = 100, cache_frame_data=False)
plt.show()
plt.close()

print("Done")
print(df1)



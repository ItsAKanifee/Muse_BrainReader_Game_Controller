
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import pandas as pd
import math
import pylsl
import numpy as np
import Experiment as ex

BUFFER_LENGTH = 5

EPOCH_LENGTH = 1

OVERLAP_LENGTH = 0.8

SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH

INDEX_CHANNEL = [0]


values = []
time = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5)
ax1.plot(time, y1)
ax2.plot(time, y2)
ax3.plot(time, y3)
ax4.plot(time, y4)
ax5.plot(time, y5)

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

streams = pylsl.resolve_stream('name', 'PetalStream_gyroscope')
inlet = pylsl.StreamInlet(streams[0])


def update(i):
    
    sample, timestamp = inlet.pull_sample()
    time.append(timestamp)
    values.append(sample)
    
    y1.append(sample[0])
    y2.append(sample[1])
    y3.append(sample[2])
    y4.append(sample[3])
    y5.append(sample[4])
    plt.cla()
    ax1.plot(time, y1)
    ax2.plot(time, y2)
    ax3.plot(time, y3)
    ax4.plot(time, y4)
    ax5.plot(time, y5)
    


animation = ani.FuncAnimation(fig, update, interval = 100)
plt.show()
plt.close()
print("Done")




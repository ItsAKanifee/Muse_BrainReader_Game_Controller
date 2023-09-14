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

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

inlet, eeg_buffer, filter_state, band_buffer, fs = ex.define(BUFFER_LENGTH, EPOCH_LENGTH, SHIFT_LENGTH)

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

def output(i):
    values, timestamp, _ = (ex.samples(SHIFT_LENGTH, fs, 0, EPOCH_LENGTH, eeg_buffer, band_buffer, filter_state, inlet))
    y1.append(values[0])
    y2.append(values[1])
    y3.append(values[2])
    y4.append(values[3])
    time.append(timestamp[0])

    plt.cla()
    ax1.plot(time, y1)
    ax2.plot(time, y2)
    ax3.plot(time, y3)
    ax4.plot(time, y4)

animation = ani.FuncAnimation(fig, output, interval = 100)
plt.show()
plt.close()
print("Done")

#values, timestamp = (ex.samples(SHIFT_LENGTH, fs, 0, EPOCH_LENGTH, eeg_buffer, band_buffer, filter_state, inlet))

#timestamp1 = 0

#while timestamp1 < 10000:
    #if timestamp1 % 100 == 0:
        #print(values[1] / values[2])
    #timestamp1 += 1


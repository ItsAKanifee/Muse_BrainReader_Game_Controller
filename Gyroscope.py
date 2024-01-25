## test 2
import pylsl
import muselsl
import matplotlib.pyplot as plt
import matplotlib.animation as ani
import pandas as pd

values = []
time = []
y1 = []
y2 = []
y3 = []

fig, (ax1, ax2, ax3) = plt.subplots(3)
ax1.plot(time, y1)
ax2.plot(time, y2)
ax3.plot(time, y3)

streams = pylsl.resolve_stream('name', 'PetalStream_gyroscope')
inlet = pylsl.StreamInlet(streams[0])

timestamp = 0

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def update(i):
    global timestamp, inlet
    
    time.append(timestamp)
    
    y1.append(inlet.pull_sample())
    #y2.append(streams[1])
    #y3.append(streams[2])

    plt.cla()

    ax1.plot(time, y1)
    #ax2.plot(time, y2)
    #ax3.plot(time, y3)


    timestamp += .1

animation = ani.FuncAnimation(fig, update, interval = 100, cache_frame_data=False)
plt.show()
plt.close()
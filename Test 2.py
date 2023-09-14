## test 2
import pylsl
import muselsl
num = 0
condition = num < 100

streams = pylsl.resolve_stream('name', 'PetalStream_gyroscope')
inlet = pylsl.StreamInlet(streams[0])
timestamp1 = 0

while condition:
    sample, timestamp = inlet.pull_sample()
    if ((timestamp - timestamp1) > 0.2):
        ##if sample[0] < 0:
            ##print('left')
        ##elif sample[0] > 0:
            ##print('right')
        if sample[1] < 0:
            print('down')
        elif sample[1] > 0:
            print('up')
        timestamp1 = timestamp
    num += 1
    if num > 500:
        break
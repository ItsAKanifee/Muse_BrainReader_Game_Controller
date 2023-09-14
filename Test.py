import Experiment as ex
import numpy as np

BUFFER_LENGTH = 5

EPOCH_LENGTH = 1

OVERLAP_LENGTH = 0.8

SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH

INDEX_CHANNEL = [0]

inlet, eeg_buffer, filter_state, band_buffer, fs = ex.define(BUFFER_LENGTH, EPOCH_LENGTH, SHIFT_LENGTH)

try:
    while True:
        values, timestamp, smooth = (ex.samples(SHIFT_LENGTH, fs, INDEX_CHANNEL, EPOCH_LENGTH, eeg_buffer, band_buffer, filter_state, inlet))
        #print(values)
        print("Delta: ", values[0], "Alpha: ", values[2], " Beta: ", values[3], " Theta: ", values[1] )

       
        
except KeyboardInterrupt:
        print('Closing!')
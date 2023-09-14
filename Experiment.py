import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
import utils  # Our own utility functions


def define(BUFFER_LENGTH, EPOCH_LENGTH, SHIFT_LENGTH):
    print('Looking for an EEG stream...')
    streams = resolve_byprop('type', 'EEG', timeout=2)
    if len(streams) == 0:
        raise RuntimeError('Can\'t find EEG stream.')

    # Set active EEG stream to inlet and apply time correction
    print("Start acquiring data")
    inlet = StreamInlet(streams[0], max_chunklen=12)
    eeg_time_correction = inlet.time_correction()

   
    info = inlet.info()
    description = info.desc()

    fs = int(info.nominal_srate())

    eeg_buffer = np.zeros((int(fs * BUFFER_LENGTH), 1))
    filter_state = None  

    n_win_test = int(np.floor((BUFFER_LENGTH - EPOCH_LENGTH) /
                              SHIFT_LENGTH + 1))

    band_buffer = np.zeros((n_win_test, 4))

    return inlet, eeg_buffer, filter_state, band_buffer, fs


#copying the example code from the analyzer and covnerting it into a method that can be used by other programs
def samples(SHIFT_LENGTH, fs, INDEX_CHANNEL, EPOCH_LENGTH, eeg_buffer, band_buffer, filter_state, inlet = StreamInlet): 
    

    eeg_data, timestamp = inlet.pull_chunk(
    timeout=0.01, max_samples=int(SHIFT_LENGTH * fs))




    ch_data = np.array(eeg_data)[:, INDEX_CHANNEL]

        
    eeg_buffer, filter_state = utils.update_buffer(
        eeg_buffer, ch_data, notch=True,
        filter_state=filter_state)

            
    data_epoch = utils.get_last_data(eeg_buffer,
                            EPOCH_LENGTH * fs)

            
    band_powers = utils.compute_band_powers(data_epoch, fs)
    band_buffer, _ = utils.update_buffer(band_buffer,
                    np.asarray([band_powers]))
    smooth_band_powers = np.mean(band_buffer, axis = 0)
           
    return band_powers, timestamp, smooth_band_powers
    
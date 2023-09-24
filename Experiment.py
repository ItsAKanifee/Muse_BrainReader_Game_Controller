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


    # Obtain EEG data from the LSL stream
    eeg_data, timestamp = inlet.pull_chunk(
        timeout=1, max_samples=int(SHIFT_LENGTH * fs))

    # Only keep the channel we're interested in
    ch_data = np.array(eeg_data)[:, INDEX_CHANNEL]

    # Update EEG buffer with the new data
    eeg_buffer, filter_state = utils.update_buffer(
        eeg_buffer, ch_data, notch=True,
        filter_state=filter_state)

    """ 3.2 COMPUTE BAND POWERS """
    # Get newest samples from the buffer
    data_epoch = utils.get_last_data(eeg_buffer,
                                        EPOCH_LENGTH * fs)

    # Compute band powers
    band_powers = utils.compute_band_powers(data_epoch, fs)
    band_buffer, _ = utils.update_buffer(band_buffer,
                                            np.asarray([band_powers]))
    # Compute the average band powers for all epochs in buffer
    # This helps to smooth out noise
    smooth_band_powers = np.mean(band_buffer, axis=0)
    #print("Delta: ", band_powers[0])
    #if band_powers[0] > 1:
        #print("blink")

    #print('Delta: ', band_powers[0], ' Theta: ', band_powers[1],
            #' Alpha: ', band_powers[2], ' Beta: ', band_powers[3])

    """ 3.3 COMPUTE NEUROFEEDBACK METRICS """
    # These metrics could also be used to drive brain-computer interfaces

    # Alpha Protocol:
    # Simple redout of alpha power, divided by delta waves in order to rule out noise
    alpha_metric = smooth_band_powers[2] / \
        smooth_band_powers[0]
    #print('Alpha Relaxation: ', alpha_metric)

    # Beta Protocol:
    # Beta waves have been used as a measure of mental activity and concentration
    # This beta over theta ratio is commonly used as neurofeedback for ADHD
    beta_metric = smooth_band_powers[3] / \
            smooth_band_powers[1]
    print('Beta Concentration: ', beta_metric)

    # Alpha/Theta Protocol:
    # This is another popular neurofeedback metric for stress reduction
    # Higher theta over alpha is supposedly associated with reduced anxiety
    theta_metric = smooth_band_powers[1] / \
        smooth_band_powers[2]
    #print('Theta Relaxation: ', theta_metric)
    return band_powers, timestamp, beta_metric
    
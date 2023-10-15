import numpy as np  # Module that simplifies computations on matrices
import matplotlib.pyplot as plt  # Module used for plotting
from pylsl import StreamInlet, resolve_byprop  # Module to receive EEG data
import utils  # Our own utility functions

class Muse:

    # Length of the EEG data buffer (in seconds)
    # This buffer will hold last n seconds of data and be used for calculations
    BUFFER_LENGTH = 5

    # Length of the epochs used to compute the FFT (in seconds)
    EPOCH_LENGTH = 1

    # Amount of overlap between two consecutive epochs (in seconds)
    OVERLAP_LENGTH = 0.8

    # Amount to 'shift' the start of each next consecutive epoch
    SHIFT_LENGTH = EPOCH_LENGTH - OVERLAP_LENGTH

    # Index of the channel(s) (electrodes) to be used
    # 0 = left ear, 1 = left forehead, 2 = right forehead, 3 = right ear
    INDEX_CHANNEL = [1]

    

    def __init__(self):

        print('Looking for an EEG stream...')
        streams = resolve_byprop('type', 'EEG', timeout=2)
        if len(streams) == 0:
            raise RuntimeError('Can\'t find EEG stream.')

        # Set active EEG stream to inlet and apply time correction
        print("Start acquiring data")
        self.inlet = StreamInlet(streams[0], max_chunklen=12)
        self.eeg_time_correction = self.inlet.time_correction()

    
        info = self.inlet.info()
        self.description = info.desc()

        self.fs = int(info.nominal_srate())

        self.eeg_buffer = np.zeros((int(self.fs * self.BUFFER_LENGTH), 1))
        self.filter_state = None  

        n_win_test = int(np.floor((self.BUFFER_LENGTH - self.EPOCH_LENGTH) /
                                self.SHIFT_LENGTH + 1))

        self.band_buffer = np.zeros((n_win_test, 4))

    
    def process(self):

        class Band: # Define the bands 
            Delta = 0
            Theta = 1
            Alpha = 2
            Beta = 3

        self.eeg_data, self.timestamp = self.inlet.pull_chunk(
                timeout=1, max_samples=int(self.SHIFT_LENGTH * self.fs))

        # Only keep the channel we're interested in
        self.ch_data = np.array(self.eeg_data)[:, self.INDEX_CHANNEL]

        # Update EEG buffer with the new data
        self.eeg_buffer, self.filter_state = utils.update_buffer(
            self.eeg_buffer, self.ch_data, notch=True,
            filter_state=self.filter_state)

        """ 3.2 COMPUTE BAND POWERS """
        # Get newest samples from the buffer
        data_epoch = utils.get_last_data(self.eeg_buffer,
                                            self.EPOCH_LENGTH * self.fs)

        # Compute band powers
        band_powers = utils.compute_band_powers(data_epoch, self.fs)
        self.band_buffer, _ = utils.update_buffer(self.band_buffer,
                                                np.asarray([band_powers]))
        # Compute the average band powers for all epochs in buffer
        # This helps to smooth out noise
        smooth_band_powers = np.mean(self.band_buffer, axis=0)
        delta_metric = band_powers[Band.Delta] # Blink signal

        #print('Delta: ', band_powers[Band.Delta], ' Theta: ', band_powers[Band.Theta],
                #' Alpha: ', band_powers[Band.Alpha], ' Beta: ', band_powers[Band.Beta])

        """ 3.3 COMPUTE NEUROFEEDBACK METRICS """
        # These metrics could also be used to drive brain-computer interfaces

        # Alpha Protocol:
        # Simple redout of alpha power, divided by delta waves in order to rule out noise
        alpha_metric = smooth_band_powers[Band.Alpha] / \
            smooth_band_powers[Band.Delta]
        #print('Alpha Relaxation: ', alpha_metric)

        # Beta Protocol:
        # Beta waves have been used as a measure of mental activity and concentration
        # This beta over theta ratio is commonly used as neurofeedback for ADHD
        beta_metric = smooth_band_powers[Band.Beta]# / \
                #smooth_band_powers[Band.Theta]
        #print('Beta Concentration: ', beta_metric)

        # Alpha/Theta Protocol:
        # This is another popular neurofeedback metric for stress reduction
        # Higher theta over alpha is supposedly associated with reduced anxiety
        theta_metric = smooth_band_powers[Band.Theta] / \
            smooth_band_powers[Band.Alpha]
        #print('Theta Relaxation: ', theta_metric)
        return alpha_metric, beta_metric, theta_metric, delta_metric
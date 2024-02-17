from Reader import Muse
import time
import os

def calibrate(muse: Muse):
    os.system('cls')
    timestamp = 0
    i = 0
    delta_before = 0 # use to gain see max shift in delta, signalling what should be registered as a blink
    max_change = 0
    delta_max = 0

    highChange = []
    delta_peaks = []


    # probably make print statements instead of a pygame screen, just so then I can have words on the screen and not worry about quiting issues

    _, base_beta, _, base_delta = muse.process() # get the base values for the measurements, so then I can reset

    print("\n Starting Calbiration: \n Start Blinking")
    start = time.time()
    end = time.time()

    record = True # set a variable to tell when the device should record data
    t = 0 # set a variable for time surpassed 

    while(end - start <= 10): # time for 30 seconds
        _, _, _, delta = muse.process()

        change = delta - delta_before # compare the differences in the delta

        delta_before = delta # set the current delta as a previous delta

        if(delta > delta_max):
            delta_max = delta
         

        if change > max_change: # if the change in delta is higher than previously recorded
            max_change = change
        

        t += 1

        if(t == 10): # record change after half a second 
            highChange.append(max_change)
            delta_peaks.append(delta_max)

            max_change = 0
            delta_max = 0

            t = 0

        end = time.time()

    avg_delt_shift = average(highChange)
    avg_delt_peak = average(delta_peaks)

    betaPeak = []
    betaLow = []

    for i in range(4):
        start = time.time()
        end = time.time()
        print("Focus on the square, do not blink")
        printBlock()

        betaMin = 0
        betaMax = -0.5 # setting this low bc the beta signal is somewhat low

        while(end - start <= 10): # Time for 10 seconds
            _, beta, _, _ = muse.process()

            if beta > betaMax: # The higher the beta signal, add it as the peak
                betaMax = beta
            
            end = time.time()
        

        betaPeak.append(betaMax) # after operation is done, add final value to the list

        os.system('cls')
        print("Rest")

        start = time.time()
        end = time.time()

        while(end - start <= 10): # time for 10 seconds
            _, beta, _, _ = muse.process()

            if beta < betaMin:
                betaMin = beta
            
            end = time.time()
        

        betaLow.append(betaMin) # after operation is done, add final value to the list

        os.system('cls')
    
    avg_beta_peak = average(betaPeak)
    avg_beta_min = average(betaLow)

    print(avg_beta_min, avg_beta_peak)

    beta_threshold = (avg_beta_peak + avg_beta_min) / 2


    return avg_delt_shift, avg_delt_peak, beta_threshold

        
        

    




def printBlock():
    print("⌈‾‾‾‾⌉")
    print("⌊____⌋")

def inRange(baseNum, toCompare, error):
    if baseNum + error == toCompare or baseNum - error == toCompare:
        return True
    else:
        return False
    
def average(data: list):
    total = 0.0
    length = len(data)

    if length == 0:
        return 0

    for i in range(length):
        total += data[i]

    avg = total / length 

    return avg


Device = Muse()

dShift, dPeak, betaSig = calibrate(Device)

dBef = 0

print(dShift, dPeak, betaSig)

while True:
    _, beta, _, delta = Device.process()

    if(delta - dBef >= dShift - 0.1):
        print('blink')
    
    dBef = delta

    if(delta > dPeak):
        print('blink2')

    






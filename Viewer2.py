import matplotlib.pyplot as plt
import matplotlib.animation as ani
#import pandas as pd
import math
import pylsl
import numpy as np
from Muse_Reader_Assets import Reader

Device = Reader.Muse()


# Idea Test: Record the lowest value of the beta signal, should be when the player is not focusing. Raising the beta signal to an arbitrary value above
# should act as a threshold for the foucs value
lowest = 0
while True:
    alpha, beta, theta, delta = Device.process()
    if beta < lowest:
        lowest = beta
    
    if beta > (lowest + 0.1):
        pass
    print(delta)
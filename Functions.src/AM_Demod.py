#-------------------------------------------------------------
# Created: 11/2/2023 by Nikolas Poholik
#
# Revision History:
#           11/2/23         Original Function created in Matlab
#           12/15/23        Ported from Matlab project to Python
#
# Purpose: The purpose of this function is take a AM modulated signal and
# use a desired bandwidth range to demodulate the signal and obtain the
# original audio 
#
# Variables:
#   t = (input) time vector of the input RF signal
#   RF = (input) sample vector of input modulated RF signal
#   fc = (input) carrier frequency of signal
#   BW = (input) bandwidth of the audio signal in RF signal
#   rolloff = (input) fp-fs 
#   z = (output) original audio signal present in RF
#
# function z = AMdemod(t,RF,fc,BW,rolloff) <- Original Form in Matlab
#-------------------------------------------------------------
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def AMdemod(t,RF,fc,BW,rolloff):
    z = [];

    #PRECUATIONS:
    #Check if the length of t and x are equal
    if len(t) != len(RF):
        print('ERROR: Mismatched Time and Sample Lengths')
        return
    #Check if the length of t and x are greater than one 
    if len(t) <= 1:
        print('ERROR: Length of t and x vectors must be greater than 1')
        return
    #Check if all values of fc, BW, and rolloff are positive
    if fc < 0 or BW < 0 or rolloff < 0:
        print('ERROR: Carrier Frequency, Bandwidth, and Rolloff must all be positive values')
        return
    
    #Start Main Function:
    ##########################################################################################

    #Define the desired frequencies to filter around
    BPF_f_cutoff = [fc-BW/2, fc+BW/2]

    #Use a bandpass filter to filter out other signals that me be present in RF
    y = filter(t,RF,BPF_f_cutoff,rolloff)
    
    #Eliminate the carrier frequency associated with the signal 
    y = y*2*np.cos(2*np.pi*fc*t)

    #Find the mean of the demodulated signal (opposite of shifting amplitude)
    m = np.mean(y)
    
    #Subtract the average from y
    z = y - m

    #End of function: return the original audio sample obtained from the RF
    return z

#############################################################################################
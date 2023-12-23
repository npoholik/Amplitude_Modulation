#--------------------------------------------------
# Created 11/2/23 by Nikolas Poholik
#
# Revision History:
#           11/2/23         Original Function created in Matlab
#           12/15/23        Ported from Matlab project to Python
#
# Purpose: The purpose of this function is to modulate an audio signal to a
# designated carrier frequency and associated bandwidth (~4.7 kHz)
#
# Variables:
#   t = (input) time vector of input audio signal
#   x = (input) sample vector of input audio signal
#   fc = (input) carrier frequency of modulated signal
#   BW = (input) bandwidth of low pass filter
#   rolloff = (input) fp-fs 
#   y = (output) Modulated signal output
#   xLPF = (output) Low passed audio signal 
#
#   function [y, xLPF] = AMmod(t,x,fc,BW,rolloff) <- Original Form in Matlab
#--------------------------------------------------
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from Functions.Filter import filter

#Function definition:
def AMmod(t, x, fc, BW, rolloff):
    y = [];
    xLPF = [];

    #PRECUATIONS:
    #Check if the length of t and x are equal
    if len(t) != len(x):
        print('ERROR: Mismatched Time and Sample Lengths')
        return
    #Check if the length of t and x are greater than one 
    if len(t) <= 1:
        print('ERROR: Length of t and x vectors must be greater than 1')
        return
    #Check if all values of fc, BW, and rolloff are positive
    if fc < 0 or BW[0] < 0 or rolloff < 0:
        print('ERROR: Carrier Frequency, Bandwidth, and Rolloff must all be positive values')
        return
    
    #Start Main Function:
    ##########################################################################################
    #Use a low pass filter on the input signal:
    xLPF = filter(t,x,BW,rolloff) 

    #Find the absolute minimum point and shift the signal up to remove negative values 
    A = np.abs(min(xLPF))
    y = xLPF + A;

    #Multiply by cos to achieve a carry frequency of fc that contains all the signal information
    y = y * np.cos(2*np.pi*fc*t)

    #End of function: return the new RF (modulated) signal and the original filtered signal
    return y, xLPF

#############################################################################################
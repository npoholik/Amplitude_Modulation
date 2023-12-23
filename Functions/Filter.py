#--------------------------------------------------
# Created 10/5/23 by Nikolas Poholik
#
# Revision History:
#           10/5/23         Original Function created in Matlab
#           12/15/23        Ported from Matlab project to Python
#           12/15/23        Depreceated outputs tau,th (impulse time vector), and h (impulse response)
# 
# Purpose: The goal of this program is to take a signal and a given cutoff
# frequency and create an impulse response to return a filtered signal.
# This function can take either one value for fc as a low pass filter or
# two values for fc as a band pass filter. 
#
# Variables:
#   t = (input) Time vector of input signal
#   x = (input) Sample vector of input signal
#   fc = (input) Cutoff frequency 
#   rolloff = (input) fp - fs 
#   y = (output) Filtered (low pass or band pass) signal
#
#   function y = myfilter(t,x,fc,rolloff) <- Original form in Matlab
#--------------------------------------------------
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#Function definition:
def filter(t,x,fc,rolloff):
    y = [];

    #PRECAUTIONS:
    #Check if the length of t and x are equal
    if len(t) != len(x):
        print('ERROR: Mismatched Time and Sample Lengths')
        return
    #Check if the length of t and x are greater than one 
    if len(t) <= 1:
        print('ERROR: Length of t and x vectors must be greater than 1')
        return

    #Start Main Function:
    ##########################################################################################
    p = [0.5799, 0.0109] #Hardcoded P value found via outside calibration of window function

    #Calculate the tau value based on p and rolloff
    Rtau = np.polyval(p,rolloff)
    tau = 1/Rtau

    #Define the time step based off of the input time vector
    T = t[1] - t[0] 

    #Find the impulse response time vector
    th = np.arange(tau*-0.6,tau*0.6, T)

    #Construct window function to create a basis for the filter
    window = np.bartlett(len(th))

    #Two possible branches for this filter: Low Pass or BandPass

    #Low pass branch:
    if len(fc) == 1:
        h = 2*fc*np.sinc(2*fc.dot(th)).dot(window)
        #Convolve the signal with the impulse response for y:
        y = np.convolve(t,x,th,h)

    #Band Pass Branch
    if len(fc) == 2:
        #Find cutoff frequency by finding the average of the bandwidth
        B = fc[1] - fc[0]
        f0 = (fc[1]+fc[0])/2
        fc = B/2
        #Construct the impulse response
        hLPF = 2*fc*np.sinc(2*fc*th)*window #This represents the low pass impulse response
        h = 2*np.cos(2*np.pi*f0*th)*hLPF

        #Convolve the signal with the impulse response for y:
        y = np.convolve(t,x,th,h)

    #End of function: return the filtered signal
    return y

#############################################################################################
    






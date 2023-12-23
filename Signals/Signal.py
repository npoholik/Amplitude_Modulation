#This is a class that will hold all associate values of a current signal
import sounddevice as sd
import numpy as np
import scipy as sp
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)  
from Functions import AM_Mod
import os

class Signal:
    __t_vect = []
    __sample_vect = []
    __carrier_freq = 0
    __rolloff = 0
    __fileType = -1
    __samplerate = 0
    __fileName = ''

    def __init__(self,t,x, samplerate, fc, rolloff, fileType, fileName):
        self.__t_vect = t
        self.__sample_vect = x
        self.__carrier_freq = fc
        self.__rolloff = rolloff
        self.__fileType = fileType
        self.__samplerate = samplerate
        self.__fileName = fileName
    
    def playAudio(self):
        if (self.__fileType == 0 and len(self.__sample_vect) >= 1 and len(self.__t_vect) >= 1):
            sd.play(self.__sample_vect, self.__samplerate)
            msg = 'Successfully Played ' + self.__fileName
            return msg
        else:
            msg = 'Error: An Issue has Occured During Playback'
            return msg
        
    def plotTimeSignal(self, canvas):
        if ((self.__fileType == 0 or self.__fileType == 1) and len(self.__sample_vect) >= 1 and len(self.__t_vect) >= 1):
            fig = plt.Figure(figsize = (10,10), dpi=100)
            plot = fig.add_subplot(111)
            plot.set_autoscaley_on(True)
            plot.set_ylabel('Amplitude')
            plot.set_xlabel('Time')
            plot.plot(self.__t_vect, self.__sample_vect)
            output = FigureCanvasTkAgg(fig, master=canvas)
            output.get_tk_widget().pack()
            msg = 'Successfully Plotted the Time Domain of ' + self.__fileName
            return msg
        else:
            msg = 'Error: Improper Number of Samples or File Type; Could not Plot the Fourier Transform'
            return msg

    def plotFTSignal(self, canvas):
        if ((self.__fileType == 0 or self.__fileType == 1) and len(self.__sample_vect) >= 1 and len(self.__t_vect) >= 1):
            sample_f = fft(self.__sample_vect)
            
            #Find the frequency domain
            freq = np.fft.fftfreq(len(self.__sample_vect), self.__t_vect[1] - self.__t_vect[0])

            fig = plt.Figure(figsize = (10,10), dpi = 100)
            plot = fig.add_subplot(111)
            plot.set_autoscaley_on(True)
            plot.set_ylabel('Power')
            plot.set_xlabel('Frequency')
            plot.plot(freq, np.abs(sample_f))
            output = FigureCanvasTkAgg(fig, master=canvas)
            output.get_tk_widget().pack()
            msg = 'Successfully Plotted the Fourier Transform of ' + self.__fileName
            return msg
        else:
            msg = 'Error: Improper Number of Samples or File Type; Could not Plot the Fourier Transform'
            return msg

    def modulateSignal(self, fc, rolloff):
        if (fc < 5000 or rolloff < 10):
            msg = 'Error: Invalid Carrier Frequency or Rolloff Value Provided'
            return msg
        else:
            fBW = np.array([4700])
            z = AM_Mod.AMmod(self.__t_vect, self.__sample_vect, fc, fBW, rolloff)

            cwd = os.getcwd()
            projectPath = os.path.abspath(os.path.join(cwd, os.pardir))
            filePath = projectPath + '\\Amplitude_Modulation\\UserGenerated\\RF_Files'
            np.savez(filePath + '\\' + self.__fileName + ' (MODULATED)', self.__t_vect, z)

            msg = 'Successfully modulated signal as \'' + self.__fileName + ' (MODULATED).npz'
            return msg


    def getTimeVector(self):
        return self.__t_vect
    
    def getSampleVector(self):
        return self.__sample_vect
    
    def getCarrierFreq(self):
        return self.__carrier_freq
    
    def getRolloff(self):
        return self.__rolloff
    
    def getFileType(self):
        return self.__fileType
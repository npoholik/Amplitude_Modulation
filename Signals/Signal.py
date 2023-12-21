#This is a class that will hold all associate values of a current signal
import sounddevice as sd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

class Signal:
    __t_vect = []
    __sample_vect = []
    __carrier_freq = 0
    __rolloff = 0
    __fileType = -1
    __samplerate = 0
    __fileName = ''
    #fig, ax = plt.subplots()

    def __init__(self,t,x, samplerate, fc, rolloff, fileType, fileName):
        self.__t_vect = t
        self.__sample_vect = x
        self.__carrier_freq = fc
        self.__rolloff = rolloff
        self.__fileType = fileType
        self.__samplerate = samplerate
        self.__fileName = fileName
    
    def playAudio(self):
        if (self.__fileType == 0):
            sd.play(self.__sample_vect, self.__samplerate)

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
    
'''
    def plotTimeSignal(self):
        self.fig.set_visible(not self.fig.get_visible())
        plt.draw()
        self.ax.set_title(self.__fileName + ' Time Domain Plot')
        self.ax.plot(self.__t_vect,self.__sample_vect, color = 'black')
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Amplitude")
        plt.show()
'''
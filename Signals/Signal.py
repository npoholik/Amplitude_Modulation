#This is a class that will hold all associate values of a current signal
import sounddevice as sd

class Signal:
    __t_vect = []
    __sample_vect = []
    __carrier_freq = 0
    __rolloff = 0
    __fileType = -1
    __samplerate = 0

    def __init__(self,t,x, samplerate, fc, rolloff, fileType):
        self.__t_vect = t
        self.__sample_vect = x
        self.__carrier_freq = fc
        self.__rolloff = rolloff
        self.__fileType = fileType
        self.__samplerate = samplerate

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
    
    def playAudio(self, filePath):
        if (self.__fileType == 0):
            sd.play(self.__sample_vect, self.__samplerate)
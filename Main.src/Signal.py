#This is a class that will hold all associate values of a current signal

class Signal:
    __t_vect = []
    __sample_vect = []
    __carrier_freq = 0

    def __init__(self,t,x,fc):
        self.__t_vect = t
        self.__sample_vect = x
        self.__carrier_freq = fc

    def getTimeVector(self):
        return self.__t_vect
    
    def getSampleVector(self):
        return self.__sample_vect
    
    def getCarrierFreq(self):
        return self.__carrier_freq
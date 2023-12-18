import numpy as np
import scipy as sp
import os

def loadFile(filePath):

    time = [];
    data = [];

    #Obtain the current file path for the project
    #cwd = os.getcwd()
    #projectPath = os.path.abspath(os.path.join(cwd, os.pardir))
    #filePath = projectPath + '\\Amplitude_Modulation\\Audio_Files\\' + filename 

    #Check if valid filename
    try:
        sampling, data = sp.io.wavfile.read(filePath) #Read  the data and sampling rate in from a .wav file 

        #Calculate the time vector for the audio signal
        duration = len(data)/sampling
        time = np.arange(0,duration, 1/sampling)

        return time, data
    
    except OSError:
        print('Could not open/read file of path: ', filePath)
        return time, data



import numpy as np
import scipy as sp
import os

def loadFile(filePath):

    time = [];
    data = [];
    fileType = -1 # -1 for unknown, 0 for .wav, 1 for .npz

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

        fileType = 0
        return time, data, fileType
    
    except OSError:
        try: 
            content = np.load(filePath)
            content['time'] = time
            content['data'] = data
            fileType = 1
            return time, data, fileType

        except OSError:
            return time, data, fileType



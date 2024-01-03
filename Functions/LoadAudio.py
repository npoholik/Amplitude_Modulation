import numpy as np
import scipy as sp
from scipy.io import wavfile
import os

def loadFile(filePath):

    time = [];
    data = [];
    sampling = 0
    fileType = -1 # -1 for unknown, 0 for .wav, 1 for .npz
    msg = ''

    #Obtain the current file path for the project
    #cwd = os.getcwd()
    #projectPath = os.path.abspath(os.path.join(cwd, os.pardir))
    #filePath = projectPath + '\\Amplitude_Modulation\\Audio_Files\\' + filename 

    #Check if valid filename
    try:
        sampling, data = wavfile.read(filePath) #Read  the data and sampling rate in from a .wav file 
        
        # Eliminate stereo data (strip 2D array back to 1D)
        data = data[:,0] #Will only save left channel (may not be ideal solution in some cases)

        #Calculate the time vector for the audio signal
        duration = len(data)/sampling
        time = np.arange(0,duration, 1/sampling)

        fileName = os.path.basename(filePath).split('.')
        msg = 'Successfully Opened File: ' + fileName[len(fileName)-2] + ' (Source: .wav Audio)'
        fileType = 0
        return time, data, sampling, fileType, msg
    
    except wavfile.WavFileWarning:
        msg = 'Error: '
    except OSError:
        try: 
            content = np.load(filePath)
            content['time'] = time
            content['data'] = data

            fileType = 1

            fileName = os.path.basename(filePath).split('.')
            msg = 'Successfully Opened File: ' + fileName[len(fileName)-2] + ' (Source: .npz RF)'
            
            return time, data, sampling, fileType, msg

        except OSError:
            msg = 'Error: Missing File Path or Unsupported File Type (Source: UNKNOWN)'
            return time, data, sampling, fileType, msg



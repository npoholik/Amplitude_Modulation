import numpy as np
import scipy as sp
from scipy.io import wavfile
import os

def loadFile(filePath):

    time = [];
    data = [];
    sampling = 0
    msg = ''

    #Obtain the current file path for the project
    #cwd = os.getcwd()
    #projectPath = os.path.abspath(os.path.join(cwd, os.pardir))
    #filePath = projectPath + '\\Amplitude_Modulation\\Audio_Files\\' + filename 

    # Determine file type before attempting to open:
    pathList = os.path.basename(filePath).split('.')
    fileType = pathList[len(pathList)-1]

    #Check if valid filename
    if (fileType == 'wav'):
        fileType = -1
        try:
            sampling, data = wavfile.read(filePath) #Read  the data and sampling rate in from a .wav file 
            fileType = 0

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
            msg = 'Error: ...'
        except ValueError:
            msg = 'Error: ...'
        except OSError:
            msg = 'Error: ...'
    if (fileType == 'npz'):
        fileType = -1
        try: 
            content = np.load(filePath)
            fileType = 1

            #for key in content.keys(): #just for determining what names the np.save designates for time and data arrays
            #    print(key)

            time = content['arr_0']
            data = content['arr_1']

            fileType = 1

            fileName = os.path.basename(filePath).split('.')
            msg = 'Successfully Opened File: ' + fileName[len(fileName)-2] + ' (Source: .npz RF)'
            
            return time, data, sampling, fileType, msg

        except OSError:
            msg = 'Error: Missing File Path or Unsupported File Type (Source: UNKNOWN)'
            return time, data, sampling, fileType, msg
        
    if (fileType != 'wav' and fileType != 'npz'):
        fileType = -1
        msg = 'Error: Unknown File Type or Incomplete File Path'
        return time, data, sampling, fileType, msg



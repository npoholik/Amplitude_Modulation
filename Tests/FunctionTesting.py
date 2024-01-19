import unittest
import sys
import os
import sounddevice as sd
import matplotlib.pyplot as plt

#Define the correct file path for the unittest to import the Functions module and all associated files
sys.path.append("./")
from Functions import *
from Signals import Signal

#Define the test class
class testFunctions(unittest.TestCase):
    signal = None
    filePath = ''

    #Set up instance variables through a Setup Class
    @classmethod
    def setUpClass(self):
        cwd = os.getcwd()
        projectPath = os.path.abspath(os.path.join(cwd, os.pardir))
        self.filePath = projectPath + '\\Amplitude_Modulation\\Tests\\TestAudio.wav' 

        time, data, sampling, fileType, msg = LoadAudio.loadFile(self.filePath)
        self.signal = Signal.Signal(time, data, sampling, 10000, 10, fileType, 'TestAudio.wav')


    def testLoading(self):
        time, data, samplerate, fileType, msg = LoadAudio.loadFile(self.filePath)

        #Currently testing to ensure that not only did the function successfully execute, 
        #but all variables have reasonably expected values
        if ('Success' in msg 
        and len(time) > 1 
        and len(data) > 1 
        and len(time) == len(data) 
        and samplerate > 10000 
        and fileType == 0):
            result = True
        else:
            result = False
        self.assertTrue(result, '\nError in function file LoadAudio... Could not Successfully Open the TestAudio: \n Results:' 
                        + '\n   Length of Time Vector: ' + str(len(time)) + ' (expected > 1)'
                        + '\n   Length of Samples Vector: ' + str(len(data)) + ' (expected > 1)'
                        + '\n   Sample Rate: ' + str(samplerate) + ' (expected > 10000)'
                        + '\n   File Type: ' + str(fileType) + ' (expected 0)')


    def testFilter(self):
        y = Filter.filter(self.signal.getTimeVector(), self.signal.getSampleVector(), 4700, self.signal.getRolloff())

        self.assertTrue(len(y) > 1, '\nError: Filter failed to return a non-empty vector.' + '\n Results: ' 
                        + '\n   Length of Filtered Signal: ' + str(len(y))) 
        
    
    


if __name__ == '__main__':
    unittest.main()

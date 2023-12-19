import tkinter as tk
import numpy as np
import os
import scipy as sp
import matplotlib.pyplot as plt
from Functions import LoadAudio
from UserInterface.GUI import GUI
from Signals.Signal import Signal

root = tk.Tk()
ui = GUI(root)

root.mainloop()



def userPressedOpenFile(filePath):
    time, samples = LoadAudio.loadFile(filePath)
    if (len(time) == 0):
        ui.setSelectedFile('ERROR: Missing File Path or Unsupported File Type (Source: UNKNOWN)')
    else:
        fileName = os.Path(filePath).stem
        ui.setSelectedFile('Successfully Opened File: ' + fileName + '(Source: .wav Audio)')



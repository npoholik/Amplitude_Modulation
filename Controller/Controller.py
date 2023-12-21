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

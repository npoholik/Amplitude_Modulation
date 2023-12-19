import tkinter as tk
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from Functions import LoadAudio
from UserInterface.GUI import GUI

root = tk.Tk()
ui = GUI(root)

root.mainloop()

'''
# Initialize GUI using tkinter API
master = tk.Tk()
master.geometry('1280x720')
master.configure(bg='#87CEEB')
master.resizable(False,False)
master.title('Amplitude Modulation')

window = tk.Canvas(master, width=1280,height=700)
window.configure(bg='#87CEEB')
window.grid(row=0, column = 5)

title = tk.Label(window,text='Welcome to the Amplitude Modulation Program', font=('Times New Roman bold', 22))
title.configure(bg='#87CEEB')
title.grid(row = 0, column = 0)


buttonFrame = tk.Frame()
buttonFrame.grid(row=1, column=0, columnspan = 4)

modButton = tk.Button(buttonFrame,text='Modulate Selected Audio File',width=25,command=modulateFile).grid(row=0, column = 0)

demodButton = tk.Button(buttonFrame,text='Demodulate Selected RF File',width=25, command=demodulateFile).grid(row=0, column=1)

playButton = tk.Button(buttonFrame,text='Play Selected File', width = 25, command=playFile).grid(row=0, column=2)


quitButton = tk.Button(master,text='Quit', width=25,command=master.destroy)
quitButton.grid()

master.mainloop()


time, data = LoadAudio.loadFile('Sicko Mode.wav')

if (len(time) != 0):
    plt.style.use('_mpl-gallery')
    plt.plot(time,data)
    plt.show()
    
'''
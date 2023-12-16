import tkinter as tk
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

from Functions import LoadAudio


time, data = LoadAudio.loadFile('Sicko Mode.wav')

plt.style.use('_mpl-gallery')
plt.plot(time,data)
plt.show()




'''
# Initialize GUI using tkinter API
master = tk.Tk()
master.geometry('1280x720')
master.configure(bg='#87CEEB')
master.resizable(False,False)
master.title('Amplitude Modulation')

window = tk.Canvas(master, width=1280,height=700)
window.configure(bg='#87CEEB')
window.pack()

title = tk.Label(window,text='Welcome to the Amplitude Modulation Program', font=('Times New Roman bold', 22))
title.configure(bg='#87CEEB')
title.pack()





modButton = tk.Button(master,text='Quit', width=25,command=master.destroy)
modButton.pack()

master.mainloop()
'''
import tkinter as tk


# Initialize GUI using tkinter API
master = tk.Tk()
master.geometry('720x500')
master.configure(bg='#87CEEB')
master.resizable(False,False)
master.title('Amplitude Modulation')

window = tk.Canvas(master, width=720,height=480)
window.configure(bg='#87CEEB')
window.pack()

title = tk.Label(window,text='Welcome to the Amplitude Modulation Program', font=('Times New Roman bold', 22))
title.configure(bg='#87CEEB')
title.pack()






modButton = tk.Button(master,text='Quit', width=25,command=master.destroy)
modButton.pack()

master.mainloop()
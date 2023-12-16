import tkinter as tk


# Initialize GUI using tkinter API
master = tk.Tk()

window = tk.Canvas(master, width=720,height=480)
window.pack()
master.title('Amplitude Modulation')

master.mainloop()
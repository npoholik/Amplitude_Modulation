import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk
import time
import os

class GUI:
    def __init__(self, root):
        #setting title
        root.title("Amplitude Modulation")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(background='#28282B')

        #MAIN TITLE LABEL
        titleLabel=tk.Label(root)
        ft = tkFont.Font(family='Times New Roman bold',size=16)
        titleLabel["font"] = ft
        titleLabel["fg"] = "#FFFFFF"
        titleLabel["justify"] = "center"
        titleLabel["background"]= '#28282B'
        titleLabel["text"] = "Welcome to the Amplitude Modulation Program"
        titleLabel.place(x=70,y=10,width=464,height=73)

        #USER ENTRY FILE PATH
        fileEntry=tk.Entry(root)
        fileEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times New Roman italics',size=10)
        fileEntry["font"] = ft
        fileEntry["fg"] = "#333333"
        fileEntry["justify"] = "center"
        fileEntry["text"] = "File Path"
        fileEntry.place(x=80,y=190,width=263,height=30)

        #BUTTON TO OPEN FILE EXPLORER
        fileExplore =tk.Button(root)
        fileExplore["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        fileExplore["font"] = ft
        fileExplore["fg"] = "#000000"
        fileExplore["justify"] = "center"
        fileExplore["text"] = "Open File"
        fileExplore.place(x=350,y=190,width=82,height=30)
        fileExplore["command"] = self.GButton_115_command

        #BUTTON TO LOAD SELECTED FILE
        loadFile=tk.Button(root)
        loadFile["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        loadFile["font"] = ft
        loadFile["fg"] = "#000000"
        loadFile["justify"] = "center"
        loadFile["text"] = "Load File"
        loadFile.place(x=440,y=190,width=77,height=30)
        loadFile["command"] = self.GButton_563_command

        #FILE INFO TEXT
        fileInfo=tk.Label(root)
        ft = tkFont.Font(family='Times',size=8)
        fileInfo["font"] = ft
        fileInfo["fg"] = "#FFFFFF"
        fileInfo["justify"] = "center"
        fileInfo["text"] = "**Supported File Types: .wav (for audio) and .csv for generate RF signals**"
        fileInfo["background"]= '#28282B'
        fileInfo.place(x=80,y=160,width=353,height=30)

        #BUTTON TO MOD/DEMOD
        demodMod=tk.Button(root)
        demodMod["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        demodMod["font"] = ft
        demodMod["fg"] = "#000000"
        demodMod["justify"] = "center"
        demodMod["text"] = "Mod/Demod Audio Sinal"
        demodMod.place(x=140,y=320,width=134,height=30)
        demodMod["command"] = self.GButton_476_command

        # SIGNAL OPTIONS LABEL
        signalOpt=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        signalOpt["font"] = ft
        signalOpt["fg"] = "#FFFFFF"
        signalOpt["justify"] = "center"
        signalOpt["text"] = "Signal Options:"
        signalOpt["background"]= '#28282B'
        signalOpt.place(x=60,y=290,width=144,height=30)


        #ANIMATED GIF
        frameCount = 10;
        frames = [ImageTk.PhotoImage(file='UserInterface/Sin.gif',format = 'gif -index %i' %(i)) for i in range(frameCount)]

        def update(ind):
            frame = frames[ind]
            ind += 1
            if ind >= frameCount:
                ind = 0
            animatedLabel.configure(image=frame)
            root.after(10, update, ind)

        animatedLabel=tk.Label(root)
        animatedLabel.place(x=120,y=60,width=363,height=103)
        root.after(0, update, 0)


        # LABEL TO SHOWCASE SELECTED FILE AND ITS TYPE
        selectedFile=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        selectedFile["font"] = ft
        selectedFile["fg"] = "#FFFFFF"
        selectedFile["justify"] = "left"
        selectedFile["text"] = "Current Signal Selected: ____________________ (*AUDIO*)/(*RF*)"
        selectedFile["background"]= '#28282B'
        selectedFile.place(x=80,y=240,width=413,height=38)


        GButton_173=tk.Button(root)
        GButton_173["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_173["font"] = ft
        GButton_173["fg"] = "#000000"
        GButton_173["justify"] = "center"
        GButton_173["text"] = "Plot Signal"
        GButton_173.place(x=300,y=320,width=134,height=30)
        GButton_173["command"] = self.GButton_173_command

        GButton_469=tk.Button(root)
        GButton_469["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        GButton_469["font"] = ft
        GButton_469["fg"] = "#000000"
        GButton_469["justify"] = "center"
        GButton_469["text"] = "Play Music"
        GButton_469.place(x=220,y=360,width=133,height=30)
        GButton_469["command"] = self.GButton_469_command

        #SHOWCASE CURRENT VERSION NUMBER
        currentVers=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        currentVers["font"] = ft
        currentVers["fg"] = "#FFFFFF"
        currentVers["justify"] = "center"
        currentVers["text"] = "Version: Beta 12.18.1"
        currentVers["background"]= '#28282B'
        currentVers.place(x=20,y=460,width=80,height=25)

    def GButton_115_command(self):
        print("command")


    def GButton_563_command(self):
        print("command")


    def GButton_476_command(self):
        print("command")


    def GButton_173_command(self):
        print("command")


    def GButton_469_command(self):
        print("command")

'''
if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
'''
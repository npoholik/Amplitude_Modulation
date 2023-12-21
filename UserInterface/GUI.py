import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk
from tkinter import filedialog
from ctypes import windll
from Functions import LoadAudio
from Signals.Signal import Signal
import os

class GUI:
    version = 'Beta 12.21.23.2'
    signal = Signal(0,0,0,0,0,-1, '')
    filePath = ''

    def __init__(self, root):
        #Avoid blurry font:
        windll.shcore.SetProcessDpiAwareness(1)
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
        self.titleLabel=tk.Label(root)
        ft = tkFont.Font(family='Times New Roman bold',size=16)
        self.titleLabel["font"] = ft
        self.titleLabel["fg"] = "#FFFFFF"
        self.titleLabel["justify"] = "center"
        self.titleLabel["background"]= '#28282B'
        self.titleLabel["text"] = "Welcome to the Amplitude Modulation Program"
        self.titleLabel.place(x=70,y=10,width=464,height=73)

        #USER ENTRY FILE PATH
        default = tk.StringVar()
        default.set('File Path')
        self.fileEntry=tk.Entry(root, textvariable=default)
        self.fileEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times New Roman italics',size=10)
        self.fileEntry["font"] = ft
        self.fileEntry["fg"] = "#333333"
        self.fileEntry["justify"] = "center"
        self.fileEntry.place(x=80,y=190,width=263,height=30)

        #BUTTON TO OPEN FILE EXPLORER
        self.fileExplore =tk.Button(root)
        self.fileExplore["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.fileExplore["font"] = ft
        self.fileExplore["fg"] = "#000000"
        self.fileExplore["border"] = 0
        self.fileExplore["highlightthickness"] = 0
        self.fileExplore["justify"] = "center"
        self.fileExplore["text"] = "Select File"
        self.fileExplore.place(x=350,y=190,width=82,height=30)
        self.fileExplore["command"] = self.openFileExplore

        #BUTTON TO LOAD SELECTED FILE
        self.loadFile=tk.Button(root)
        self.loadFile["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.loadFile["font"] = ft
        self.loadFile["fg"] = "#000000"
        self.loadFile["border"] = 0
        self.loadFile["highlightthickness"] = 0
        self.loadFile["justify"] = "center"
        self.loadFile["text"] = "Open File"
        self.loadFile.place(x=440,y=190,width=77,height=30)
        self.loadFile["command"] = self.openFile

        #FILE INFO TEXT
        self.fileInfo=tk.Label(root)
        ft = tkFont.Font(family='Times',size=9)
        self.fileInfo["font"] = ft
        self.fileInfo["fg"] = "#FFFFFF"
        self.fileInfo["justify"] = "center"
        self.fileInfo["text"] = "**Supported File Types: .wav (for audio) and .npz (for generated RF signals)**"
        self.fileInfo["background"]= '#28282B'
        self.fileInfo.place(x=80,y=160,width=390,height=30)

        #BUTTON TO MOD/DEMOD
        self.demodMod=tk.Button(root)
        self.demodMod["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.demodMod["font"] = ft
        self.demodMod["fg"] = "#000000"
        self.demodMod["border"] = 0
        self.demodMod["highlightthickness"] = 0
        self.demodMod["justify"] = "center"
        self.demodMod["text"] = "Mod/Demod Audio Signal"
        self.demodMod["state"] = "disabled"
        self.demodMod.place(x=400,y=360,width=134,height=30)
        #self.demodMod["command"] = self.GButton_476_command

        # SIGNAL OPTIONS LABEL
        self.signalOpt=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.signalOpt["font"] = ft
        self.signalOpt["fg"] = "#FFFFFF"
        self.signalOpt["justify"] = "center"
        self.signalOpt["text"] = "Signal Options:"
        self.signalOpt["background"]= '#28282B'
        self.signalOpt.place(x=10,y=280,width=144,height=30)


        #ANIMATED GIF
        frames = []
        frame_ind = 0
        last_frame = 0

        while True:
            try:
                # Read a frame from GIF file
                part = 'gif -index {}'.format(frame_ind)
                frame = tk.PhotoImage(file='UserInterface/Sin.gif', format=part)
            except:
                last_frame = frame_ind - 1    # Save index for last frame
                break               # Will break when GIF index is reached
            frames.append(frame)
            frame_ind += 1        # Next frame index

        def update(frame_num):
            frame = frames[frame_num]
            frame_num += 1
            if frame_num > last_frame:
                frame_num = 0
            animatedLabel.configure(image=frame)
            root.after(35, update, frame_num)

        animatedLabel=tk.Label(root)
        animatedLabel["borderwidth"] = 0
        animatedLabel["highlightthickness"] = 0
        animatedLabel["background"]= '#28282B'
        animatedLabel.place(x=120,y=60,width=363,height=103)
        update(0) #Start animation


        # LABEL TO SHOWCASE SELECTED FILE AND ITS TYPE
        self.selectedFile=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.selectedFile["font"] = ft
        self.selectedFile["fg"] = "#FFFFFF"
        self.selectedFile["justify"] = "left"
        self.selectedFile["text"] = "Current Signal Selected: ____________________ (*AUDIO*)/(*RF*)"
        self.selectedFile["background"]= '#28282B'
        self.selectedFile.place(x=80,y=240,width=413,height=38)


        #PLOT SIGNAL BUTTON
        self.plotSignal=tk.Button(root)
        self.plotSignal["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.plotSignal["font"] = ft
        self.plotSignal["fg"] = "#000000"
        self.plotSignal["border"] = 0
        self.plotSignal["highlightthickness"] = 0
        self.plotSignal["justify"] = "center"
        self.plotSignal["text"] = "Plot Time Signal"
        self.plotSignal["state"] = "disabled"
        self.plotSignal.place(x=60,y=310,width=134,height=30)
        self.plotSignal["command"] = self.plotTime


        # PLOT FOURIER TRANSF. 
        self.ftPlot = tk.Button(root)
        self.ftPlot["bg"] = "#e9e9ed"
        ft = tkFont.Font(family = 'Times', size = 10)
        self.ftPlot["font"]= ft
        self.ftPlot["fg"] = "#000000"
        self.ftPlot["border"] = 0
        self.ftPlot["highlightthickness"] = 0
        self.ftPlot["justify"] = "center"
        self.ftPlot["state"] = "disabled"
        self.ftPlot["text"] = "Plot Fourier Transf."
        self.ftPlot.place(x=400,y=310,width=134,height=30)
        #ftPlot["command"] = self.plotFT

        #PLAY AUDIO FILE
        self.playAudio=tk.Button(root)
        self.playAudio["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        self.playAudio["font"] = ft
        self.playAudio["fg"] = "#000000"
        self.playAudio["justify"] = "center"
        self.playAudio["border"] = 0
        self.playAudio["highlightthickness"] = 0
        self.playAudio["text"] = "Play Audio"
        self.playAudio["state"] = "disabled"
        self.playAudio.place(x=230,y=310,width=133,height=30)
        self.playAudio["command"] = self.play

        #SHOWCASE CURRENT VERSION NUMBER
        currentVers=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        currentVers["font"] = ft
        currentVers["fg"] = "#FFFFFF"
        currentVers["justify"] = "center"
        currentVers["text"] = 'Version: ' + self.version
        currentVers["background"]= '#28282B'
        currentVers.place(x=20,y=460,width=80,height=25)


        #QUIT BUTTON
        quitButton = tk.Button(root)
        ft = tkFont.Font(family='Times New Roman bold', size = 10)
        quitButton["font"] = ft
        quitButton["fg"] = "#000000"
        quitButton["bg"] = "#f03232"
        quitButton["border"] = 0
        quitButton["highlightthickness"] = 0
        quitButton["justify"] = "center"
        quitButton["text"] = "Quit"
        quitButton.place(x=100,y=460, width=134, height=30)
        quitButton["command"] = root.destroy

        #DEV CONSOLE BUTTON
        devConsole = tk.Button(root)
        devConsole["bg"] = "#000000"
        ft = tkFont.Font(family = 'Times New Roman bold',size = 10)
        devConsole["font"] = ft
        devConsole["fg"] = "#FFFFFF"
        devConsole["border"] = 0
        devConsole["highlightthickness"] = 0
        devConsole["justify"] = "center"
        devConsole["text"] = "Open Console"
        devConsole["state"] = "disabled"
        devConsole.place(x=255, y = 460, width = 134, height = 30)
        #devConsole["command"] = self.openConsole

        #CARRIER FREQUENCY INPUT
        defaultText = tk.StringVar()
        defaultText.set('Enter Carrier Freq.')
        self.carFreq = tk.Entry(root,textvariable=defaultText)
        self.carFreq["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        self.carFreq["font"] = ft
        self.carFreq["fg"] = "#333333"
        self.carFreq["state"] = "disabled"
        self.carFreq["justify"] = "center"
        self.carFreq.place(x=60, y=360, width=132, height = 30)

        #ROLLOFF INPUT
        defaultText = tk.StringVar()
        defaultText.set('Enter Rolloff')
        self.rolloff = tk.Entry(root,textvariable=defaultText)
        self.rolloff["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.rolloff["font"] = ft
        self.rolloff["fg"] = "#333333"
        self.rolloff["state"] = "disabled"
        self.rolloff["justify"] = "center"
        self.rolloff.place(x=230,y=360,width=133,height=30)

        #Error message output to the user:
        self.errorOut = tk.Label(root)
        ft = tkFont.Font(family='Times New Roman bold', size = 10)
        self.errorOut["font"] = ft
        self.errorOut["fg"] = "#FFFFFF"
        self.errorOut["justify"] = "left"
        self.errorOut["bg"] =  '#28282B'
        self.errorOut["text"] = ''
        self.errorOut.place(x=60, y=410, width=368, height=36)

    
    def openFileExplore(self):
        cwd = os.getcwd()
        projectPath = os.path.abspath(os.path.join(cwd, os.pardir))
        initialDir = projectPath + '\\Amplitude_Modulation\\UserGenerated\\' 
        filePath = filedialog.askopenfilename(initialdir=initialDir, title = "Select a File",filetypes = (("Audio files","*.wav*"),("RF files","*.npz*")))
        self.fileEntry.delete(0, "end")
        self.fileEntry.insert(0,filePath)


    def openFile(self):
        self.filePath = self.fileEntry.get()
        time, data, sampling, fileType, msg = LoadAudio.loadFile(self.filePath)

        file = os.path.basename(self.filePath).split('.')
        fileName = file[len(file)-2] + '.' + file[len(file)-1]

        if (fileType == -1):
            self.setSelectedFile(msg)
            self.plotSignal["state"] = "disabled"
            self.playAudio["state"] = "disabled"
            self.ftPlot["state"] = "disabled"
            self.carFreq["state"] = "disabled"
            self.rolloff["state"] = "disabled"
            self.demodMod["text"] = "Mod/Demod Signal"
            self.demodMod["state"] = "disabled"
        elif (fileType == 0):
            self.setSelectedFile(msg)
            self.plotSignal["state"] = "normal"
            self.playAudio["state"] = "normal"
            self.ftPlot["state"] = "normal"
            self.carFreq["state"] = "normal"
            self.rolloff["state"] = "normal"
            self.demodMod["text"] = "Modulate Audio Signal"
            self.demodMod["state"] = "normal"
            self.signal = Signal(time,data, sampling,0,0,0,fileName)
        elif (fileType == 1): 
            self.setSelectedFile(msg)
            self.plotSignal["state"] = "normal"
            self.playAudio["state"] = "disabled"
            self.ftPlot["state"] = "normal"
            self.carFreq["state"] = "normal"
            self.rolloff["state"] = "normal"
            self.demodMod["text"] = "Demodulate Audio Signal"
            self.demodMod["state"] = "normal"
            self.signal = Signal(time,data,sampling,0,0,1,fileName)

    def plotTime(self):
        self.signal.plotTimeSignal

    def play(self):
        self.signal.playAudio()

    def setSelectedFile(self,message):
        self.selectedFile.config(text = message)

'''
    def openConsole(self):
        cmdWind = tk.Tk()
        cmd = os.popen("Dev Console").read()
        tk.Label(cmdWind, text = cmd).grid(row=0,column=0)
        cmdWind.mainloop()
        return
'''
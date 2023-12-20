import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
from ctypes import windll
from Functions import LoadAudio
import os
from os import path

class GUI:
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
        titleLabel=tk.Label(root)
        ft = tkFont.Font(family='Times New Roman bold',size=16)
        titleLabel["font"] = ft
        titleLabel["fg"] = "#FFFFFF"
        titleLabel["justify"] = "center"
        titleLabel["background"]= '#28282B'
        titleLabel["text"] = "Welcome to the Amplitude Modulation Program"
        titleLabel.place(x=70,y=10,width=464,height=73)

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
        fileExplore =tk.Button(root)
        fileExplore["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        fileExplore["font"] = ft
        fileExplore["fg"] = "#000000"
        fileExplore["border"] = 0
        fileExplore["highlightthickness"] = 0
        fileExplore["justify"] = "center"
        fileExplore["text"] = "Select File"
        fileExplore.place(x=350,y=190,width=82,height=30)
        fileExplore["command"] = self.fileExplore

        #BUTTON TO LOAD SELECTED FILE
        loadFile=tk.Button(root)
        loadFile["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        loadFile["font"] = ft
        loadFile["fg"] = "#000000"
        loadFile["border"] = 0
        loadFile["highlightthickness"] = 0
        loadFile["justify"] = "center"
        loadFile["text"] = "Open File"
        loadFile.place(x=440,y=190,width=77,height=30)
        loadFile["command"] = self.openFile

        #FILE INFO TEXT
        fileInfo=tk.Label(root)
        ft = tkFont.Font(family='Times',size=9)
        fileInfo["font"] = ft
        fileInfo["fg"] = "#FFFFFF"
        fileInfo["justify"] = "center"
        fileInfo["text"] = "**Supported File Types: .wav (for audio) and .npz (for generated RF signals)**"
        fileInfo["background"]= '#28282B'
        fileInfo.place(x=80,y=160,width=390,height=30)

        #BUTTON TO MOD/DEMOD
        demodMod=tk.Button(root)
        demodMod["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        demodMod["font"] = ft
        demodMod["fg"] = "#000000"
        demodMod["border"] = 0
        demodMod["highlightthickness"] = 0
        demodMod["justify"] = "center"
        demodMod["text"] = "Mod/Demod Audio Signal"
        demodMod["state"] = "disabled"
        demodMod.place(x=400,y=360,width=134,height=30)
        demodMod["command"] = self.GButton_476_command

        # SIGNAL OPTIONS LABEL
        signalOpt=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        signalOpt["font"] = ft
        signalOpt["fg"] = "#FFFFFF"
        signalOpt["justify"] = "center"
        signalOpt["text"] = "Signal Options:"
        signalOpt["background"]= '#28282B'
        signalOpt.place(x=10,y=280,width=144,height=30)


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
        plotSignal=tk.Button(root)
        plotSignal["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        plotSignal["font"] = ft
        plotSignal["fg"] = "#000000"
        plotSignal["border"] = 0
        plotSignal["highlightthickness"] = 0
        plotSignal["justify"] = "center"
        plotSignal["text"] = "Plot Time Signal"
        plotSignal["state"] = "disabled"
        plotSignal.place(x=60,y=310,width=134,height=30)
        plotSignal["command"] = self.GButton_173_command


        # PLOT FOURIER TRANSF. 
        ftPlot = tk.Button(root)
        ftPlot["bg"] = "#e9e9ed"
        ft = tkFont.Font(family = 'Times', size = 10)
        ftPlot["font"]= ft
        ftPlot["fg"] = "#000000"
        ftPlot["border"] = 0
        ftPlot["highlightthickness"] = 0
        ftPlot["justify"] = "center"
        ftPlot["state"] = "disabled"
        ftPlot["text"] = "Plot Fourier Transf."
        ftPlot.place(x=400,y=310,width=134,height=30)
        #ftPlot["command"] = self.plotFT

        #PLAY AUDIO FILE
        playAudio=tk.Button(root)
        playAudio["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=10)
        playAudio["font"] = ft
        playAudio["fg"] = "#000000"
        playAudio["justify"] = "center"
        playAudio["border"] = 0
        playAudio["highlightthickness"] = 0
        playAudio["text"] = "Play Audio"
        playAudio["state"] = "disabled"
        playAudio.place(x=230,y=310,width=133,height=30)
        playAudio["command"] = self.GButton_469_command

        #SHOWCASE CURRENT VERSION NUMBER
        currentVers=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        currentVers["font"] = ft
        currentVers["fg"] = "#FFFFFF"
        currentVers["justify"] = "center"
        currentVers["text"] = "Version: Beta 12.19.23.1"
        currentVers["background"]= '#28282B'
        currentVers.place(x=20,y=460,width=80,height=25)


        #QUIT BUTTON
        quitButton = tk.Button(root)
        quitButton["bg"] = "#e9e9ed"
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

        #CARRIER FREQUENCY INPUT
        defaultText = tk.StringVar()
        defaultText.set('Enter Carrier Freq.')
        carFreq = tk.Entry(root,textvariable=defaultText)
        carFreq["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times', size=10)
        carFreq["font"] = ft
        carFreq["fg"] = "#333333"
        carFreq["state"] = "disabled"
        carFreq["justify"] = "center"
        carFreq.place(x=60, y=360, width=132, height = 30)

        #ROLLOFF INPUT
        defaultText = tk.StringVar()
        defaultText.set('Enter Rolloff')
        rolloff = tk.Entry(root,textvariable=defaultText)
        rolloff["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        rolloff["font"] = ft
        rolloff["fg"] = "#333333"
        rolloff["state"] = "disabled"
        rolloff["justify"] = "center"
        rolloff.place(x=230,y=360,width=133,height=30)

        #Error message output to the user:
        errorOut = tk.Label(root)
        ft = tkFont.Font(family='Times New Roman bold', size = 10)
        errorOut["font"] = ft
        errorOut["fg"] = "#FFFFFF"
        errorOut["justify"] = "left"
        errorOut["bg"] =  '#28282B'
        errorOut["text"] = ''
        errorOut.place(x=60, y=410, width=368, height=36)

    
    def fileExplore(self):
        cwd = os.getcwd()
        projectPath = os.path.abspath(os.path.join(cwd, os.pardir))
        initialDir = projectPath + '\\Amplitude_Modulation\\UserGenerated\\' 
        filePath = filedialog.askopenfilename(initialdir=initialDir, title = "Select a File",filetypes = (("Audio files","*.wav*"),("RF files","*.npz*")))
        self.fileEntry.delete(0, "end")
        self.fileEntry.insert(0,filePath)


    def openFile(self):
        filePath = self.fileEntry.get()
        try:
            time, samples, fileType = LoadAudio.loadFile(filePath)

            if (fileType == -1):
                self.setSelectedFile('ERROR: Missing File Path or Unsupported File Type (Source: UNKNOWN)')
            elif (fileType == 0):
                fileName = os.Path(filePath).stem
                self.setSelectedFile('Successfully Opened File: ' + fileName + '(Source: .wav Audio)')
            elif (fileType == 1): 
                fileName = os.Path(filePath).stem
                self.setSelectedFile('Successfully Opened File: ' + fileName + '(Source: .npz RF)')
        except:
            fileName = os.path.basename(filePath).split('.')
            self.setSelectedFile('***CRITICAL ERROR:*** Unsupported File Type: .' + fileName[len(fileName)-1])
            return



    def GButton_476_command(self):
        print("command")


    def GButton_173_command(self):
        print("command")


    def GButton_469_command(self):
        print("command")

    def setSelectedFile(self,message):
        self.selectedFile.config(text = message)



import tkinter as tk
from UserInterface.GUI import GUI

def main():
    root = tk.Tk() #Create a master root for tkinter

    #Initialize the GUI class:
    GUI(root)

    root.mainloop()

#Define main as the entry point to the program:
if __name__ == '__main__':
    main()



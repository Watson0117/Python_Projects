

from tkinter import *
import tkinter as tk
from tkinter import messagebox


import phonebook_gui
import phonebook_func



class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(width=500, height=300) #this sets the min size for the window
        self.master.maxsize(width=500, height=300) #this sets the max size of the window making it un resizable

        phonebook_func.center_window(self, 500,300) # the function center window dose what is says it dose
        
        self.master.title('The Tkinter phonebook!')
        self.master.config(bg='#F0F0F0')# black i think
            #below is a tkinter method that askes
            #for conformation when clicking the top right red x
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        
        phonebook_gui.load_gui(self)
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1,accelerator="Ctrl+Q",command=lambda: drill50_phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo")
        menubar.add_cascade(label="Help", menu=helpmenu)
       
        self.master.config(menu=menubar, borderwidth='1')

        
if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

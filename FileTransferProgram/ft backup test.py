import shutil
import os
import datetime as dt
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        
        self.master.title('Daily Updates Program')
        self.master.config(bg='darkblue')

        self.btnAFD = Button(self.master,text='Choose a file path.', width=15, height=2, command=self.AFD)
        self.btnAFD.grid(row=1,column=0,padx=(10,10), pady=(10,10))
        
        self.btnAFD2 = Button(self.master,text='Choose a file path.', width=15, height=2, command=self.AFD2)
        self.btnAFD2.grid(row=2,column=0,padx=(10,10), pady=(10,10))

        self.lblDisplay = Label(self.master,text='First select the path to the files.', font= ('Helvetica', 16), fg='black', bg='lightblue')
        self.lblDisplay.grid(row=1,column=1,padx=(10,10), pady=(10,10))

        self.lblDisplay2 = Label(self.master,text='next select the path to copy the files to.', font= ('Helvetica', 16), fg='black', bg='lightblue')
        self.lblDisplay2.grid(row=2,column=1,padx=(10,10), pady=(10,10))

        self.btnFUP = Button(self.master,text='Update files', width=15, height=2, command=self.FileUpdate)
        self.btnFUP.grid(row=3,column=0,padx=(10,10), pady=(10,10))

        
           

    def AFD(self):
        TFP = fd.askdirectory()
        TFP_var = StringVar()
        TFP_var.set(TFP)
        self.lblDisplay.config(text= "The FP: {} ".format(TFP))
        

    def AFD2(self):
        TFP2 = fd.askdirectory()
        TFP2_var = StringVar()
        TFP2_var.set(TFP2)
        self.lblDisplay2.config(text= "The FP: {} ".format(TFP2))

   
        
       
    def FileUpdate(self):
    # set the source file location
        src = TFP_var.get()

        #set the destination path to FolderB
        dest = TFP2_var.get()
        files = os.listdir()

        for i in files:
            
            now = dt.datetime.now() # this shold set the current time
            ago = now-dt.timedelta(hours=24) # this should specify the last 24 hours
        
            st = os.stat(src)    
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
            # we are saying mobve the files represented by i to the destination folder
                shutil.copy(src+i, dest)






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()




"""

     def get_file_path():
    # Open and return file path
    file_path= filedialog.askopenfilename(title = "Select A File", filetypes = (("mov files", "*.png"), ("mp4", "*.mp4"), ("wmv", "*.wmv"), ("avi", "*.avi")))
    file_path_var.set(file_path) #setting the variable to the value from file path
    #Now the file_path can be acessed from inside the function and outside
    file_path_var.get() # will return the value stored in file_path_var
    l1 = Label(window, text = "File path: " + file_path).pack()

"""

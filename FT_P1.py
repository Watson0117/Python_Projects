import shutil
import os
import datetime as dt
import tkinter
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import * 


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        
        self.master.title('Learning Tkinter!')
        self.master.config(bg='darkblue')

       
        self.btnAFD = Button(self.master,text='Choose a file path.', width=15, height=2, command=self.FileUpdate)
        self.btnAFD.grid(row=1,column=0,padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='Your file path will show here.', font= ('Helvetica', 16), fg='black', bg='lightblue')
        self.lblDisplay.grid(row=1,column=1,padx=(20,20), pady=(30,0))

        
       
    def AFD(self):
        TFP = fd.askdirectory()
        self.lblDisplay.config(text= "The FP: {} ".format(TFP))



    def FileUpdate(self):
    # set the source file location
        src = fd.askdirectory()

        #set the destination path to FolderB
        dest = fd.askdirectory()
        files = os.listdir(src)

        for i in files:
            
            now = dt.datetime.now() # this shold set the current time
            ago = now-dt.timedelta(hours=24) # this should specify the last 24 hours
            
            st = os.stat(src+i)    
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
            # we are saying mobve the files represented by i to the destination folder
                shutil.copy(src+i, dest)






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()















import shutil
import os
import datetime as dt






import tkinter as tk
from tkinter import filedialog as fd





import tkinter
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
        self.lblDisplay.config(text= "The FP: {} ".format(TFP))
        

    def AFD2(self):
        TFP2 = fd.askdirectory()
        self.lblDisplay2.config(text= "The FP: {} ".format(TFP2))
       




    def FileUpdate(self):
    # set the source file location
        src = self.lblDisplay

        #set the destination path to FolderB
        dest = self.lblDisplay2
        files = os.listdir()

        for i in files:
            
            now = dt.datetime.now() # this shold set the current time
            ago = now-dt.timedelta(hours=24) # this should specify the last 24 hours
            
            st = os.stat(src + i)    
            mtime = dt.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
            # we are saying mobve the files represented by i to the destination folder
                shutil.copy(src+i, dest)






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()





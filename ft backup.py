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

        self.TFP_var = StringVar()
        self.TFP2_var = StringVar()


       
        self.btnAFD = Button(self.master,text='Choose a file path.', width=15, height=2, command=self.AFD)
        self.btnAFD.grid(row=1,column=0,padx=(10,10), pady=(10,10))
        
        self.btnAFD2 = Button(self.master,text='Choose a file path.', width=15, height=2, command=self.AFD2)
        self.btnAFD2.grid(row=2,column=0,padx=(10,10), pady=(10,10))

        
        self.txtTFP_var = Entry(self.master,text=self.TFP_var, font= ('Helvetica', 16), fg='black', bg='lightblue')
        self.txtTFP_var.grid(row=1,column=1,padx=(30,0), pady=(30,0))

        self.txtTFP2_var = Entry(self.master,text=self.TFP2_var, font= ('Helvetica', 16), fg='black', bg='lightblue')
        self.txtTFP2_var.grid(row=2,column=1,padx=(30,0), pady=(30,0))
        
        self.btnFUP = Button(self.master,text='Update files', width=15, height=2, command=self.FileUpdate)
        self.btnFUP.grid(row=3,column=0,padx=(10,10), pady=(10,10))

        
        


    def AFD(self):
        TFP = fd.askdirectory()
        self.TFP_var.set("{}".format(TFP))
        
        

    def AFD2(self):
        TFP2 = fd.askdirectory()
        self.TFP2_var.set("{}".format(TFP2))
        
       




    def FileUpdate(self):
    # set the source file location
        src = self.TFP_var.get()

        #set the destination path to FolderB
        dest = self.TFP2_var.get()
        files = os.listdir()

        for i in files:
            
            now = dt.datetime.now() # this shold set the current time
            ago = now-dt.timedelta(hours=24) # this should specify the last 24 hours
        
            st = os.path.getmtime(src) 
            
            if st > ago:
            # we are saying mobve the files represented by i to the destination folder
                shutil.copy(src+i, dest)






if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()





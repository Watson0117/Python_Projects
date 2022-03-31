
******broken***********





import tkinter as tk
from tkinter import *
from tkinter import filedialog as fd 


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
       
        self.master.title('Check file path')
       

        
        self.btncallback = Button(self.master,text='Browse...', width=12, height=1, command=self.callback)
        self.btncallback.grid(row=0,column=0,padx=(20,0), pady=(20,0))

        self.txtFP = Entry(self.master,text='')
        self.txtFP.grid(row=0,column=1, columnspan=12, padx=(20,20), pady=(20,0))     
        
        self.btnCancel = Button(self.master,text='Cancel', width=12, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=10,padx=(20,20), pady=(20,10), sticky=NE)






    def callback():
        name= fd.askdirectory() 
        print(name)
        
  



    def submit(self):
        TFP = self.varFP.get()
        self.lblDisplay.config(text= "the FP: {} ".format(TFP))

    def cancel(self):
        self.master.destroy()
        
        
        
        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()


import tkinter as tk
from tkinter import filedialog as fd





import tkinter
from tkinter import * 


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        
        self.master.title('Learning Tkinter!')
        self.master.config(bg='darkblue')

       
        self.btnAFD = Button(self.master,text='Choose a file path.', width=15, height=2, command=self.AFD)
        self.btnAFD.grid(row=1,column=0,padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text='Your file path will show here.', font= ('Helvetica', 16), fg='black', bg='lightblue')
        self.lblDisplay.grid(row=1,column=1,padx=(20,20), pady=(30,0))

        
        self.btnCancel = Button(self.master,text='Cancel', width=15, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=0,padx=(30,0), pady=(10,10))

    def AFD(self):
        TFP = fd.askdirectory()
        self.lblDisplay.config(text= "The FP: {} ".format(TFP))

    def cancel(self):
        self.master.destroy()
        
        


    def callback():
        TFP = fd.askopenfilename()
        self.lblDisplay.config(text= "the FP: {} ".format(TFP))
    


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

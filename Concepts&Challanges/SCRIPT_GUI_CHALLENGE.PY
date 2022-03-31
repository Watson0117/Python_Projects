import tkinter
from tkinter import * 


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
       
        self.master.title('Check files')
       

        self.varFName = StringVar()
        self.varLName = StringVar()

        

        self.btnSubmit1 = Button(self.master,text='Browse...', width=12, height=1)
        self.btnSubmit1.grid(row=0,column=0,padx=(20,0), pady=(20,0))

        self.btnSubmit2 = Button(self.master,text='Browse...', width=12, height=1)
        self.btnSubmit2.grid(row=1,column=0,padx=(20,0), pady=(20,0))

    

        self.txtFName = Entry(self.master,text=self.varFName)
        self.txtFName.grid(row=0,column=1, columnspan=12, padx=(20,20), pady=(20,0))

        self.txtLName = Entry(self.master,text=self.varLName)
        self.txtLName.grid(row=1,column=1, columnspan=12, padx=(20,20), pady=(20,0))



        
        
        self.btnSubmit = Button(self.master,text='Chech for files...', width=12, height=2, command=self.submit)
        self.btnSubmit.grid(row=2,column=0,padx=(20,0), pady=(20,10), sticky=N+E+S+W)

        self.btnCancel = Button(self.master,text='Cancel', width=12, height=2, command=self.cancel)
        self.btnCancel.grid(row=2,column=10,padx=(20,20), pady=(20,10), sticky=NE)





    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text= "Hello {} {}!".format(fn,ln))

    def cancel(self):
        self.master.destroy()
        
        
        
        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

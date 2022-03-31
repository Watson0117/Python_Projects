import os
import webbrowser
import tkinter
from tkinter import * 


class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width=True, height=True)
        self.master.geometry('{}x{}'.format(700, 400))
        self.master.title('Webpage Generator')
        self.master.config(bg='darkblue')

        self.UI = StringVar()
        

        # This is the WPgen button. it calles the WPgen func below Its possitioned at the top of the app
        # I set my code up so that it mirrors the apps final look. everything is in the same order it is n the GUI
        # im not sure if it is good practice or not but i feel it helps me keep things in order as well as making edits to placement very easy.
        self.btnWPgen = Button(self.master,text='Generate webpage', width=18, height=2, command=self.WPgen)
        self.btnWPgen.grid(row=0,column=0,padx=(20,0), pady=(20,20), sticky=W)

        #I added this label just to make the app look better. befor it was just 2 buttons and a txt field now it looks more put together
        self.lbldesc = Label(self.master,text='Enter new text for web page below.', font= ('Helvetica', 16), fg='black', bg='lightblue')
        self.lbldesc.grid(row=1,column=0,padx=(20,0), pady=(0,20), sticky=W)

        #this is the entry box for the text when text is entered and the submit new text button is clicked it calls
        #the WPgenEDIT func below and uses the text in the field as the user input
        self.txtUI = Entry(self.master,text=self.UI, font= ('Helvetica', 16), fg='black', bg='lightgreen')
        self.txtUI.grid(row=2,column=0,padx=(20,0), pady=(0,20), sticky=W)

        # This is the WPgenEDIT button it calles the WPgenEDIT function. Its function uses the input from the entry feild as input for the pages text 
        self.btnWPgenEDIT = Button(self.master,text='Submit new text', width=18, height=2, command=self.WPgenEDIT)
        self.btnWPgenEDIT.grid(row=3,column=0,padx=(20,0), pady=(0,20), sticky=W)


        # This is the WPgen or Web Page Generator function. It uses open() to open/create the HTML file. the w in the function
        # Sets it to overwrite the current text if any. for this function there is no text to start with so the f.write part sets the text for the page
        # I included the tabs and the line breaks that would make the HTML indentation correct for the first function but i found
        # i dident realy need towhen i made the second
    def WPgen(self):
        f = open("WPgenPage.html", "w")
        f.write("<html>\n   <body>\n        <h1>\n  Stay tuned for our amazing summer sale!\n       </h1>\n </body>\n</html>")
        f.close()
        fn = 'WPgenPage.html'
        webbrowser.open_new_tab(fn)

        # This is the WPgenEDIT Web Page Generator Edit function. it functions almos identicly to the WPgen function but it uses self.UI.get() to
        # retreve the text in the self.UI entry field. whatever text is in the feild whent the submit button is clicked is used as the input.
        # With the WPgenPage.html in the same file you can use the filename as is. if it was in a different file you would have to use the file path.
        # I had issues with this at first as i was desegnatinf a file path to the folder i had the PY file in and it was difficult.
    def WPgenEDIT(self):
        f = open("WPgenPage.html", "w")
        UserInput = self.UI.get()
        f.write("<html>\n<body>\n<h1>\n{}\n</h1>\n</body>\n</html>".format(UserInput))
        f.close()
        fn = 'WPgenPage.html'
        webbrowser.open_new_tab(fn)



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

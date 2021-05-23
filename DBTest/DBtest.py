
import sqlite3
import os
import sys
import time

path = "D:\\Watson Tech Academy repositories\\Python_Projects\\DBtest"
dirs = os.listdir(path) #

def tblmaker():
    conn = sqlite3.connect('DBTestDB.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_TXTfiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_Files STRING \
            )") #
        conn.commit()
    conn.close() #this closes the db to prevent memory leaks

def index_txt():
    conn = sqlite3.connect('DBTestDB.db')
    with conn:
        for file in dirs: # this targets the files in a certin directory
            if file.endswith(".txt"): # this targets the txt files
                name, ext = os.path.splitext(file) # this splits the file name from the extension 
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_TXTfiles(col_Files) VALUES(?)",(name,)) #
                print("{}".format(name)) #this prints the file names to the console.
                conn.commit() #this commits the changes stated above
    conn.close() #this closes the db to prevent memory leaks

def printfile():
   for file in dirs: #
            if file.endswith(".txt"): #this specifies which files we are working with
                with open(file, 'r') as f: # this opens thoes files
                    data = f.read() #this gets the program to read the data in the text files and stores it as "data"
                    print(data) #this print the contents of the txt files so we can read them in the console

if __name__ == "__main__":
    tblmaker()
    index_txt()
    printfile()



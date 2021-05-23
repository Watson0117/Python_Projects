
"""

Your script will need to use Python 3 and the sqlite3 module.

Your database will require 2 fields: an auto-increment
primary integer field and a field with the data type “string.”

Your script will need to read from the supplied list of file
names at the bottom of this page and determine only the files
from the list which end with a “.txt” file extension.

Next, your script should add those file names from the list
ending with “.txt” file extension within your database.

Finally, your script should legibly print the qualifying text
files to the console.

Add comments throughout your Python explaining your code.
Adding comments to your code is a good practice, and is
expected in theindustry.It will help you understand what
your code is doing and will also make iteasier when you
need reference back to previous projects.


"""

import sqlite3
import os
import sys
import time

path = "D:\\Watson Tech Academy repositories\\Python_Projects\\DBtest"
dirs = os.listdir(path)
conn = sqlite3.connect('DBTestDB.db')


def tblmaker():
    conn = sqlite3.connect('DBTestDB.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS tbl_TXTfiles( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_Files STRING \
            )")
        conn.commit()
    conn.close()

conn = sqlite3.connect('DBTestDB.db')
def index_txt():
    conn = sqlite3.connect('DBTestDB.db')
    with conn:
        for file in dirs:
            if file.endswith(".txt"):
                name, ext = os.path.splitext(file)
                f = "{}".format(name)
                cur = conn.cursor()
                cur.execute("INSERT INTO tbl_TXTfiles(col_Files) VALUES(?)",file)
                print("name = {}\n".format(name))
                conn.commit()
                
                conn.close()
                


if __name__ == "__main__":
    tblmaker()
    index_txt()


"""

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname,col_lname,col_email FROM tbl_persons WHERE col_fname = 'Sarah'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First name: {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
        print(msg)        
        
    conn.commit()
conn.close()



def index():# This would print all the files and directories
    for file in dirs:
        abpath = os.path.join(path, file)
        modification_time = os.path.getmtime(file)  # Get the time of last modifation 
        local_time = time.ctime(modification_time)  # convert the time to local time
        print(abpath, local_time)

"""


"""
DONE- Your script will need to use the listdir() method from the OS module to iterate through all files within a specific directory.
DONE- script will need to use the path.join() method from the OS module to concatenate the file name to its file path, forming an absolute path.
DONE ish- your script will need to use the getmtime() method from the OS module to find the latest date that each text file has been created or modified.
DONE- Your script will need to print each file ending with a .”txt” file extension and its corresponding mtime to the console.
"""

import os
import sys
import time
path = "D:\\Watson Tech Academy repositories\\Python_Projects\\SAtest"

dirs = os.listdir(path)
modification_time = os.path.getmtime(path)  # Get the time of last modifation 
local_time = time.ctime(modification_time)  # convert the time to local time

def index():# This would print all the files and directories
    for file in dirs:
        abpath = os.path.join(path, file)
        print(abpath, local_time)

def index_txt():
    for file in dirs:
        if file.endswith(".txt"):
            with open(file, 'r') as f:
                data = f.read()
                print(data, local_time,"\n")
                f.close()

                

if __name__ == "__main__":
    index()
    index_txt()

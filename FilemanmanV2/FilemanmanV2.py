import os
import re
from re import sub
#from tkinter import Tk
from tkinter.filedialog import Directory, askdirectory
print("The first step will be to chooses the folder containing the files you wish to rename.\n")
print("After this selection is made the user may pick up to 3 keywords to remove from the file names your selections are case sensitive. leave unused inputs blank and continue.\n")
dirName = askdirectory() # shows dialog box and return the path

###########---kEYWORD KEYS---######################
keyword1 = input('Choose the first keyword would you like to remove from file names?\n')# First keyword
keyword2 = input('Choose the second keyword would you like to remove from file names?\n')# can be left blank
keyword3 = input('Choose the third keyword would you like to remove from file names?\n')# can be left blank

#############---STANDARD REMOVAL KEYS---##########
keysearch = [keyword1, keyword2, keyword3]
badformating = ["\.", "-", "_", "  "]
keywords = ["720", "720p", "480", "480p","1080p", "1080", "DUAL Audio", "10bit", "DVD", "BluRay", "BRrip", "x256", "HDrip", "EVO"]
emStr = ""# initialize an empty string

##################### Main ############################################################
for fname in os.listdir(dirName):
    if emStr.join(keysearch) in fname:
        print(fname, "has one of the keywords with keysearch\n")

################### Keywords ##########################################################
for filename in os.listdir(dirName):
    fName = (emStr.join(filename)) # changes list to string
    curfilename, suff = os.path.splitext(fName) # splits the path into root and extension pair such that root + extension == path
    upfilename = sub('|'.join(keysearch),'',curfilename) # finds any instances of keysearch and repalaces them with an empty string.
    finfilename = (upfilename + suff)# remakes the full file name
    filepath = os.path.join(dirName, filename) # this get the directory name and file name and sets them as a single string
    newfilepath = os.path.join(dirName, finfilename)#this takes the directory name and finfilename and set them as a single string 
    os.rename(filepath, newfilepath)#renames file with the string created by newfilename above

################  Cleanup --- () and [] removal ----###########################################################
for filename in os.listdir(dirName):
    fName = (emStr.join(filename)) # changes list to string
    newFname = re.sub(r'\[.*?\]',"",fName) # this finds all instances of [] deletes them and the contents.
    filepath = os.path.join(dirName, filename) # should take the path and file name an create a string
    newfilepath = os.path.join(dirName, filename.replace(filename,newFname)) # should creat the string to rename the file, take dir name and file name but replace fiel name with newFname
    os.rename(filepath, newfilepath)# this should take the now modified file name and renamt the target with the new name.

for filename in os.listdir(dirName):
    fName = (emStr.join(filename)) # changes list to string
    newFname = re.sub(r'\(.*?\)',"",fName)# this finds all instances of () deletes them and the contents
    filepath = os.path.join(dirName, filename) # should take the path and file name an create a string
    newfilepath = os.path.join(dirName, filename.replace(filename,newFname)) # should creat the string to rename the file, take dir name and file name but replace fiel name with newFname
    os.rename(filepath, newfilepath)# this should take the now modified file name and renamt the target with the new name.

for filename in os.listdir(dirName):   
        filepath = os.path.join(dirName, filename) # could i use a cut or split at the end to keep the extension sepperate or maby file_extension = pathlib('my_file.txt').suffix
        newfilepath = sub('|'.join(keywords),"",filepath) # finds any instances of keywords and repalaces them with an empty string.
        os.rename(filepath,newfilepath) # this renames the file name modified by newfilepath

#######################   formating    ###########################
for filename in os.listdir(dirName):
    fName = (emStr.join(filename)) # changes list to string
    curfilename, suff = os.path.splitext(fName) # splits the path into root and extension pair such that root + extension == path
    upfilename = sub('|'.join(badformating),' ',curfilename)
    finfilename = (upfilename + suff)# recombines the name and suff into single string
    filepath = os.path.join(dirName, filename) # could i use a cut or split at the end to keep the extension sepperate or maby file_extension = pathlib.Path('my_file.txt').suffix
    newfilepath = os.path.join(dirName, finfilename)#this subs anything in the "keywords" lsit with an empty string
    os.rename(filepath, newfilepath)#renames file with newfilename

for filename in os.listdir(dirName):
    fName = (emStr.join(filename)) # changes list to string
    curfilename, suff = os.path.splitext(fName) # splits the path into root and extension pair such that root + extension == path
    upfilename = curfilename.rstrip(" ") # rstrip removes whitspace at the end of a string
    finfilename = (upfilename + suff) # recombine them
    filepath = os.path.join(dirName, filename) # could i use a cut or split at the end to keep the extension sepperate or maby file_extension = pathlib.Path('my_file.txt').suffix
    newfilepath = os.path.join(dirName, finfilename)#this subs anything in the "keywords" lsit with an empty string
    os.rename(filepath, newfilepath)#renames file with newfilename

for fname in os.listdir(dirName):
   print(fname, "Has been renamed\n")

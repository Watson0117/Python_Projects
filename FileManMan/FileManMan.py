import os
import re
from tkinter import Tk
from tkinter.filedialog import Directory, askdirectory
print("The first step will be to chooses the folder containing the files you wish to rename.\n")
print("After this selection is made the user may pick up to 3 keywords to remove from the file names. leave unneeded inputs blank and continue./n")
dirName = askdirectory() # shows dialog box and return the path
print(dirName)
###########---kEYWORD KEYS---######################
keyword1 = input('Choose the first keyword would you like to remove from file names?\n')# First keyword
keyword2 = input('Choose the second keyword would you like to remove from file names?\n')# can be left blank
keyword3 = input('Choose the third keyword would you like to remove from file names?\n')# can be left blank
#############---STANDARD REMOVAL KEYS---##########

keyDF1 = "."
keyDF2 = "  "
keyDF3 = "x265"
keyDF4 = "10bit"
keyDF5 = "[CBM]"
keyDF6 = "480p"
keyDF7 = "480"
keyDF8 = "720p"
keyDF9 = "720"
keyDF10 = "1080p"
keyDF11 = "1080"
keyDF12 = "DUAL Audio"
keyDF13 = "_"
keyDF14 = "DVD"
keyDF15= "BluRay" 
keyDF16 = "()"
#keyDF17 = "" 
#############---FILE TYPE KEYS---#######
keyjpg = " jpg"
keymov = " mov"
keymkv = " mkv"
keygif = " gif"
keymp4 = " mp4"
keymp3 = " mp3"
keysrt = " srt"
keypdf = " pdf"

##################### Main ############################################################
for fname in os.listdir(dirName):
    if keyword1 or keyword2 or keyword3 in fname:
        print(fname, "has one of the keywords\n")
################### Keywords ##########################################################
for filename in os.listdir(dirName):
    if keyword1 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keyword1,""))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keyword2 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keyword2,""))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keyword3 in filename:    
        filepath = os.path.join(dirName, filename) 
        newfilepath = os.path.join(dirName, filename.replace(keyword3,""))
        os.rename(filepath, newfilepath)
################  Cleanup --- () and [] removal ----###########################################################



for filename in os.listdir(dirName):
    str1 = ""# initialize an empty string
    fName = (str1.join(filename)) # changes list to string
    newFname = re.sub(r'\[.*?\]',"",fName)
    filepath = os.path.join(dirName, filename) # should take the path and file name an create a string
    newfilepath = os.path.join(dirName, filename.replace(filename,newFname)) # should creat the string to rename the file, take dir name and file name but replace fiel name with newFname
    os.rename(filepath, newfilepath)# this should take the now modified file name and renamt the target with the new name.

for filename in os.listdir(dirName):
    str1 = ""# initialize an empty string
    fName = (str1.join(filename)) # changes list to string
    newFname = re.sub(r'\(.*?\)',"",fName)
    filepath = os.path.join(dirName, filename) # should take the path and file name an create a string
    newfilepath = os.path.join(dirName, filename.replace(filename,newFname)) # should creat the string to rename the file, take dir name and file name but replace fiel name with newFname
    os.rename(filepath, newfilepath)# this should take the now modified file name and renamt the target with the new name.



#for filename in os.listdir(dirName):
#    str1 = ""# initialize an empty string
#    fName = (str1.join(filename)) # changes list to string
#    for braks in fName:
#        res = re.findall(r'\[.*?\]', fName) # find all brakets [] and everything contained within.
#        em1 = ""
#        braklist = em1.join(res)
#        newFname = re.sub(braklist,"",fName)   # should sub the bracks and info for and empty string.
#        filepath = os.path.join(dirName, filename) # should take the path and file name an create a string
#        newfilepath = os.path.join(dirName, filename.replace(filename,newFname)) # should creat the string to rename the file, take dir name and file name but replace fiel name with newFname
#        os.rename(filepath, newfilepath)# this should take the now modified file name and renamt the target with the new name.


#################  Cleanup --- STANDARD REMOVALS ----###########################################################
#for filename in os.listdir(dirName):
#    if keyDF1 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF1," "))
#        os.rename(filepath, newfilepath)

#def dblspcRemover(): # must be befor file type fixes to not mess up ther pattern
#    for filename in os.listdir(dirName):
#        if keyDF2 in filename:    
#            filepath = os.path.join(dirName, filename)
#            newfilepath = os.path.join(dirName, filename.replace(keyDF2," "))
#            os.rename(filepath, newfilepath)
#for x in range(6):
#    dblspcRemover()

#for filename in os.listdir(dirName):
#    if keyDF3 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF3,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF4 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF4,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF5 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF5,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF6 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF6,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF7 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF7,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF8 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF8,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF9 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF9,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF10 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF10,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF11 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF11,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF12 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF12,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF13 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF13,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF14 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF14,""))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF15 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF15,""))
#        os.rename(filepath, newfilepath)


############## Fixing file type section # rquiered to get the files to save as ther current type the period remover lso removes the . in .jpg and such this fixes that.
#for filename in os.listdir(dirName):
#    if keyjpg in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyjpg,".jpg"))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keymov in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keymov,".mov"))
#        os.rename(filepath, newfilepath)


#for filename in os.listdir(dirName):
#    if keymkv in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keymkv,".mkv"))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keygif in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keygif,".gif"))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keymp4 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keymp4,".mp4"))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keymp3 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keymp3,".mp3"))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keysrt in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keymp3,".srt"))
#        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):
#    if keyDF16 in filename:    
#        filepath = os.path.join(dirName, filename)
#        newfilepath = os.path.join(dirName, filename.replace(keyDF16,""))
#        os.rename(filepath, newfilepath)

#### conformation   #########
for fname in os.listdir(dirName):
   print(fname, "Has been renamed\n")
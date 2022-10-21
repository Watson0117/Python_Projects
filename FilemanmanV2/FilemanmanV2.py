import os
import re
from re import sub
from tkinter import Tk
from tkinter.filedialog import Directory, askdirectory
print("The first step will be to chooses the folder containing the files you wish to rename.\n")
print("After this selection is made the user may pick up to 3 keywords to remove from the file names. leave unneeded inputs blank and continue.\n")
dirName = askdirectory() # shows dialog box and return the path
print(dirName)
###########---kEYWORD KEYS---######################
keyword1 = input('Choose the first keyword would you like to remove from file names?\n')# First keyword
keyword2 = input('Choose the second keyword would you like to remove from file names?\n')# can be left blank
keyword3 = input('Choose the third keyword would you like to remove from file names?\n')# can be left blank
#############---STANDARD REMOVAL KEYS---##########
badformating = [".", "-", "_", "  "]
keywords = ["720", "720p", "480", "480p","1080p", "1080", "[CBM]", "DUAL Audio", "10bit", "DVD", "BluRay", "BRrip", "x256", "HDrip", "EVO"]

#keyDF1 = "."
#keyDF2 = "-"
#keyDF3 = "_"
#keyDF4 = "  "

#############---FILE TYPE KEYS---#######
keyjpg = " jpg"
keymov = " mov"
keymkv = " mkv"
keygif = " gif"
keymp4 = " mp4"
keymp3 = " mp3"
keysrt = " srt"
keypdf = " pdf"
keysrt = " srt"
keysfv = " sfv"

keyjpg2 = " .jpg"
keymov2 = " .mov"
keymkv2 = " .mkv"
keygif2 = " .gif"
keymp42 = " .mp4"
keymp32 = " .mp3"
keysrt2 = " .srt"
keypdf2 = " .pdf"
keysrt2 = " .srt"
keysfv2 = " .sfv"




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

for filename in os.listdir(dirName):   
        filepath = os.path.join(dirName, filename)
        newfilepath = sub('|'.join(keywords),'',filepath)
        os.rename(filepath, newfilepath)

#for filename in os.listdir(dirName):   
#        filepath = os.path.join(dirName, filename.split(type)
#        newfilepath = sub('|'.join(badformating),'',filepath)
#        os.rename(filepath, newfilepath)


#################  Cleanup --- STANDARD REMOVALS ----###########################################################

for filename in os.listdir(dirName):
    if keyDF1 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keyDF1," "))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keyDF2 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keyDF2," "))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keyDF3 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keyDF3," "))
        os.rename(filepath, newfilepath)

def dblspcRemover(): # must be before file type fixes to not mess up there pattern
    for filename in os.listdir(dirName):
        if keyDF4 in filename:    
            filepath = os.path.join(dirName, filename)
            newfilepath = os.path.join(dirName, filename.replace(keyDF4," "))
            os.rename(filepath, newfilepath)
for x in range(6):
    dblspcRemover()

for filename in os.listdir(dirName):
    for keys in keys:
        if keys in filename:    
            filepath = os.path.join(dirName, filename)
            newfilepath = os.path.join(dirName, filename.replace(keys,""))
            os.rename(filepath, newfilepath)

############# Fixing file type section # rquiered to get the files to save as ther current type the period remover lso removes the . in .jpg and such this fixes that.
for filename in os.listdir(dirName):
    if keyjpg in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keyjpg,".jpg"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keymov in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keymov,".mov"))
        os.rename(filepath, newfilepath)


for filename in os.listdir(dirName):
    if keymkv in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keymkv,".mkv"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keygif in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keygif,".gif"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keymp4 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keymp4,".mp4"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keymp3 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keymp3,".mp3"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keysrt in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keysrt,".srt"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keysfv in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keysfv,".sfv"))
        os.rename(filepath, newfilepath)


###added space elimination
for filename in os.listdir(dirName):
    if keyjpg2 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keyjpg2,".jpg"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keymov2 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keymov2,".mov"))
        os.rename(filepath, newfilepath)


for filename in os.listdir(dirName):
    if keymkv2 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keymkv2,".mkv"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keygif2 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keygif2,".gif"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keymp42 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keymp42,".mp4"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keymp32 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keymp32,".mp3"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keysrt2 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keysrt2,".srt"))
        os.rename(filepath, newfilepath)

for filename in os.listdir(dirName):
    if keysfv2 in filename:    
        filepath = os.path.join(dirName, filename)
        newfilepath = os.path.join(dirName, filename.replace(keysfv2,".sfv"))
        os.rename(filepath, newfilepath)

for x in range(6):
    dblspcRemover()

#### conformation   #########
for fname in os.listdir(dirName):
   print(fname, "Has been renamed\n")



























#import re

#target_str = "Jessa Knows Testing    And Machine     Learning \t \n"

## \s+ to match all whitespaces
## replace them using single space " "
#res_str = re.sub(r"\s+", " ", target_str)

## string after replacement
#print(res_str)
## Output 'Jessa Knows Testing And Machine Learning'



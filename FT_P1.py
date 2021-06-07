import shutil
import os
import datetime as dt


def FileUpdate():
    # set the source file location
    src = 'C:/Users/watso/Desktop/FolderB/'

    #set the destination path to FolderB
    dest = 'C:/Users/watso/Desktop/FolderA/'
    files = os.listdir(src)

    for i in files:
        
        now = dt.datetime.now() # this shold set the current time
        ago = now-dt.timedelta(hours=24) # this should specify the last 24 hours
        
        st = os.stat(src)    
        mtime = dt.datetime.fromtimestamp(st.st_mtime)
        if mtime > ago:
        # we are saying mobve the files represented by i to the destination folder
            shutil.copy(src+i, dest)


"""
if os.path.getctime
os.path.getctime
"""

if __name__ == "__main__":
    FileUpdate()

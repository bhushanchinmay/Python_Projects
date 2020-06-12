"""
This script is used to create multiple copies of a single file with defined file type using 'EXTENSION' and names of the files are chosen from 'adblist'.
Also no of files depends upon no of lines in 'adblist'
"""

import glob
import os
import shutil
from os import path

DIRECTORY_NAME = r'C:\Users\chinbhus\OneDrive - Qualcomm\Desktop\Progs'  # this variable contains directory name which stores file whose copies will be created
FILE_NAME = './QCN/'  # name of the folder where copies will be created
adblist = 'adb.txt'  # this variable contains txt file containing name which will be used for naming

# We can either use the function 'getFileName()' or we can directly use 'QCN_FILE_NAME' and 'EXTENSION'
QCN_FILE = 'a'  # default name for file whose copies will be created
EXTENSION = '.xqcn'  # Extension for file type whose copies will be created
DEVICE_ABD_ID = []  # used for storing list of abd devices


# Function gets the name of the file whose copies will be created with
def getFileName():
    global QCN_FILE
    for findFile in glob.glob('*' + EXTENSION):
        QCN_FILE = findFile.split('.')[:1]
    return QCN_FILE[0]


# Get list of names that will be used for naming
def GET_DEVICE_LIST(filename):
    with open(filename) as adb_list:
        for devices in adb_list:
            devices = devices.strip()
            if devices != "":
                DEVICE_ABD_ID.append(devices)
    return DEVICE_ABD_ID


def main():
    global QCN_FILE, EXTENSION
    os.chdir(DIRECTORY_NAME)  # changing directory where we have pasted our file, whose copies will be created
    QCN_FILE = str(getFileName())
    DEVICE_LIST = GET_DEVICE_LIST(adblist)
    for d in range(len(DEVICE_LIST)):
        if path.exists(QCN_FILE + EXTENSION):
            shutil.copyfile(QCN_FILE + EXTENSION, FILE_NAME + DEVICE_LIST[d] + EXTENSION)  # function copies files and renames the file, both the functions are performed simultaneously


if __name__ == "__main__":
    main()

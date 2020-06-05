"""
This script is used to create multiple copies of a single file with defined file type using 'EXTENSION' and names of the files are chosen from 'adblist'.
Also no of files depends upon no of lines in 'adblist'
"""

import glob
import os
import shutil
from os import path

DIRECTORY_NAME = 'C:\\Users\\chinbhus\\OneDrive - Qualcomm\\Desktop\\Progs\\Hello\\'  # Directory where file whose copies are to be made is pasted
FILE_NAME = '../QCN/'  # Folder where these copies will be created
adblist = 'adb.txt'

os.chdir(
    'C:\\Users\\chinbhus\\OneDrive - Qualcomm\\Desktop\\Progs\\Hello\\')  # changing directory where we have pasted our file whose copies will be created


# We can either use the function 'getFileName()' or we can directly use 'QCN_FILE_NAME' and 'EXTENSION'
# QCN_FILE_NAME = 'a'
EXTENSION = '.xqcn'  # Extension for file type whose copies will be created

DEVICE_ABD_ID = []  # used for storing list of abd devices


# Function will find the file whose copies will be created according to its 'EXTENSION'
def getFileName():
    for findFile in glob.glob('*' + EXTENSION):
        global QCN_FILE_NAME, EXTENSIONS
        QCN_FILE_NAME, EXTENSIONS = findFile.split('.')


# Get list of devices using the 'abdlist' file
def GET_DEVICE_LIST(filename):
    with open(filename) as adb_list:
        for devices in adb_list:
            devices = devices.strip()
            if devices != "":
                DEVICE_ABD_ID.append(devices)
    return DEVICE_ABD_ID


def main():
    if path.exists(QCN_FILE + EXTENSION):
        getFileName()
        GET_DEVICE_LIST(adblist)
        for d in range(len(DEVICE_ABD_ID)):
            shutil.copyfile(QCN_FILE + EXTENSIONS, FILE_NAME + DEVICE_ABD_ID[
                d] + EXTENSIONS)  # function copies files and renames it, both functions are done simultaneously


if __name__ == "__main__":
    main()

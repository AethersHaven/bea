import os

import shutil

 

#layout "last first ID"

def IsValidFolder(nameFolder):

    arr = nameFolder.split()

    return len(arr) == 3 and IsName(arr[0]) and IsName(arr[1]) and arr[2].isnumeric() and len(arr[2]) <= 5

 

#layout "last first ID other"

def IsValidFile(fileName):

    arr = fileName[:len(fileName)-4].split()

    return not fileName.endswith(".py") and "." in fileName and len(arr) > 3 and IsName(arr[0]) and IsName(arr[1]) and arr[2].isnumeric() and len(arr[2]) <= 5

 

def IsName(name):

    for c in name:

        if not c.isalpha() and not c == "-" and not c == "\'":

            return False

    return True

 

def SortFile(file):

    arr = file.split()

    letter = file[0].upper()

    toFolder = os.getcwd()[:os.getcwd().rfind('\\')+1] + letter + '\\' + file[:file.find(arr[2])+len(arr[2])]

    if letter == 'S' or letter == 'M':

        sAdd = "SM to SZ"

        if letter == 'M' and file[:2].upper() < "MI":

            sAdd = "Ma to Mh"

        elif letter == 'M':

            sAdd = "Mi to Mz"

        elif letter == 'S' and file[:2].upper() < "SM":

            sAdd = "SA to SL"

        if not os.path.isdir(os.getcwd()[:os.getcwd().rfind('\\')+1] + letter + '\\' + sAdd + '\\' + file[:file.find(arr[2])+len(arr[2])]):

            os.makedirs(os.getcwd()[:os.getcwd().rfind('\\')+1] + letter + '\\' + sAdd + '\\' + file[:file.find(arr[2])+len(arr[2])])

        shutil.move(os.getcwd() + '\\' + file, os.getcwd()[:os.getcwd().rfind('\\')+1] + letter + '\\' + sAdd + '\\' + file[:file.find(arr[2])+len(arr[2])] + '\\' + file[:file.find(arr[2])-1] + file[file.find(arr[2])+len(arr[2]):])

    else:

        if not os.path.isdir(toFolder):

            os.makedirs(toFolder)

        shutil.move(os.getcwd() + '\\' + file, toFolder + '\\' + file[:file.find(arr[2])-1] + file[file.find(arr[2])+len(arr[2]):])

    print("Sorted " + file)

 

def main():

    for file in os.listdir(os.getcwd()):

        if IsValidFile(file):

            SortFile(file)

 

main()

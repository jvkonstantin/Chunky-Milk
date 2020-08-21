import os
import sys
from time import sleep
import traceback
import pathlib
import json

def nameFromFiles(nameFilePath, fileType):
    print("Please Put The Names You Want On This File And Then Save & Close")
    sleep(3)
    os.startfile("names.txt")
    input("Press [Enter] To Continue")
    x = 0
    count = 0
    for path in pathlib.Path(".").iterdir():
        if path.is_file():
            count += 1
    try:
        if count == 0:
            i2 = input(f"There are no files in this directory. Do you want to continue?: ")
            if i2 == "yes":
                for file in os.listdir(nameFilePath):
                        with open("names.txt", "r") as f:
                                # global nameFromLine
                                lines=f.readlines()
                                lineChooserint = x
                                nameFromLine = lines[lineChooserint]
                                # print(f"nameFromLine: {nameFromLine}")
                        fileName , fileEXT = os.path.splitext(file)
                        newFileName = nameFromLine.split("\n")
                        
                        # print(newFileName[0])
                        # print(file)w
                        if fileEXT.lower() == f"{fileType}":
                            print("-----------------------------------------------------")
                            print("Previous Name: " + fileName)
                            print(fileEXT)
                            os.rename(f"{nameFilePath}/{file}", f"{nameFilePath}/{newFileName[0]}{fileEXT.lower()}")
                            print("-----------------------------------------------------------")
                            # print(file)
                            x = x + 1
                        else:
                            print("ELSE at nameChangerWithTXT")
        else:
            for file in os.listdir(nameFilePath):
                        with open("names.txt", "r") as f:
                                # global nameFromLine
                                lines=f.readlines()
                                lineChooserint = x
                                nameFromLine = lines[lineChooserint]
                                # print(f"nameFromLine: {nameFromLine}")
                        fileName , fileEXT = os.path.splitext(file)
                        newFileName = nameFromLine.split("\n")
                        
                        # print(newFileName[0])
                        # print(file)w
                        if fileEXT.lower() == f"{fileType}":
                            print("-----------------------------------------------------")
                            print("Previous Name: " + fileName)
                            print(fileEXT)
                            os.rename(f"{nameFilePath}/{file}", f"{nameFilePath}/{newFileName[0]}{fileEXT.lower()}")
                            print("-----------------------------------------------------------")
                            # print(file)
                            x = x + 1
                        else:
                            print(f"There are no files with the suggested file type {fileType}")
                            break
            import printAsciiTitles
            printAsciiTitles.decide()
                
    except IndexError:
                print("[Names in name list are smaller than the files in the folder]")
            


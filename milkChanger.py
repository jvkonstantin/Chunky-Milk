import os
import fnmatch
import milkChangerWithTXT

def chooser():
    chooserInput = input("-------------- \n[1]LowerCase / UpperCase Change \n[2]Uniform Name Change \n[3]Change Names From TXT File \n[4] Capitalization![Beta but try it] \n-------------- \n")
    if chooserInput.lower() == "1":
        selection()
    elif chooserInput.lower() == "2":
        sameNameMoreNumbers()
    elif chooserInput.lower() == "3":
        print               ("0-------------------------------------------0")
        nameFromPath = input("[Where are your files?]")
        print("0-------------------------------------------0")
        fileType = input("[What type are your files? (include the '.')]")
        print("0-------------------------------------------0")
        milkChangerWithTXT.nameFromFiles(nameFromPath, fileType)
    elif chooserInput.lower() == "4":
        changeFristNumber()
    else:
        print("0--------------0 \n Sorry didnt got that please try again \n0---------------0")
        chooser()
def sameNameMoreNumbers():
    newFileName = input("[What is going to be the name of your files?]: ")
    fileNumber = input("[File Number?]: ")
    fileType = input("[File Type?]: ")
    filePath = input("[File Path?]:")
    for file in os.listdir(filePath):
        
        fileName , fileEXT = os.path.splitext(file)
        
        if fileEXT.lower() == f"{fileType}":
            # try:
            #     print("-----------------------------------------------------")
            #     print("Previous file: " + file)
            #     print("File Type " +fileEXT)
            #     os.rename(f"{filePath}/{file}", f"{filePath}/{newFileName}_{fileNumber}{fileType}")
            #     print("Next file: " + file.lower())
            #     print("-----------------------------------------------------------")
            #     fileNumber = int(fileNumber) + 1
            # except FileExistsError:
            #     print("Oops!  You already have a file named that.  Trying again...")
            print("-----------------------------------------------------")
            print("Previous Name: " + file)
            print(fileEXT)
            os.rename(f"{filePath}/{file}", f"{filePath}/{newFileName}_{fileNumber}{fileType.lower()}")
            print("New Name: " + fileName.lower())
            print("-----------------------------------------------------------")
            fileNumber = int(fileNumber) + 1

def lower():
    fileType = input("File Type?: ")
    filePath = input("File Path?:")

    for file in os.listdir(filePath):
    
        fileName , fileEXT = os.path.splitext(file)
        
        if fileEXT.lower() == f"{fileType}":
            print("-----------------------------------------------------")
            print("Previous file: " + fileName)
            print(fileEXT)
            os.rename(f"{filePath}/{file}", f"{filePath}/{file.lower()}")
            print("Next file: " + file.lower())
            print("-----------------------------------------------------------")
            import printAsciiTitles
            printAsciiTitles.decide()
    
def upper():
    fileType = input("File Type?: ")
    filePath = input("File Path?:")
    
    for file in os.listdir(filePath):
    
        fileName , fileEXT = os.path.splitext(file)
        
        if fileEXT.lower() == f"{fileType}":
            print("-----------------------------------------------------")
            print("Previous file: " + fileName)
            print(fileEXT)
            os.rename(f"{filePath}/{file}", f"{filePath}/{fileName.upper()}{fileEXT.lower()}")
            print("Next file: " + file.upper())
            print("-----------------------------------------------------------")
    import printAsciiTitles
    printAsciiTitles.decide()
        
    # os.rename(f"{filePath}/{file}", f"{filePath}/{file.lower()}")
    
    # if file.endswith(".txt"):
        # os.rename(filePath + "/" + file, filePath + "/" + file.lower())
        # os.rename(file, file.lower())
        # os.rename(f"./test/{file}", f"./test/{file.lower()}")
        # print("ended")
    # os.rename(f"{filePath}/{file}", f"{filePath}/{file.lower}")
    # print("ended")


def changeFristNumber():
    fileType = input("File Type?: ")
    filePath = input("File Path?:")
    
    for file in os.listdir(filePath):
    
        fileName , fileEXT = os.path.splitext(file)
        
        if fileEXT.lower() == f"{fileType}":
            print("-----------------------------------------------------")
            print("Previous file: " + fileName)
            print(fileEXT)
            os.rename(f"{filePath}/{file}", f"{filePath}/{fileName.capitalize()}{fileEXT.lower()}")
            print("Next file: " + file.upper())
            print("-----------------------------------------------------------")
    import printAsciiTitles
    printAsciiTitles.decide()
def selection():
    i1 = input("------------- \n[1] Change Names To Lower Case \n[2] Change Name To Upper Case \n------------- \n")
    if i1.lower() == "1":
        lower()
    elif i1.lower() == "2":
        upper()
    
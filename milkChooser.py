from time import sleep
import os
import sys
import webbrowser
import json
import writeReadMilk
import printAsciiTitles
def chooser():
   
    songCommand = input("What song would you like to play?: ")
    songName = songCommand.lower()
    jsonForPath = open("config.json")
    data = json.load(jsonForPath)
    pathMusic = data["pathMUSIC"]
    if pathMusic.lower() == "none":
        writeReadMilk.write()
    else:
        print

    # path = 

    if os.path.isfile(f"{pathMusic}\\{songCommand}.mp3") == True:
        print(f"Playing {songCommand}.mp3 in {pathMusic}")
        os.startfile(f"{pathMusic}\\{songCommand}.mp3")
        exitForMilky()
        
            
    elif songCommand.lower() == "exit":
        print
        printAsciiTitles.decide()
    elif songCommand.lower() == "list":
        lister() 
    elif songCommand.endswith(".alone"):
        try:
            print(f"Playing {songName}.mp3 in {pathMusic}")
            songNameStart , songNameEXT = songCommand.split(".")
            os.startfile(f"{songNameStart}.mp3")
            print(f"Command Name: {songNameStart} \nCommand Extention: .{songNameEXT}")
            exitForMilky()
        except FileNotFoundError:
            print("-------------------------")
            print(f"Sorry {songName} Not Found")
            print("-------------------------")
            chooser()
    else:
        print(f"Song Not Found in {pathMusic}... Please try changing tha names to lowercase with the command 2")
        exitForMilky()
    
def lister():
    pathListerMusic = input("File Path?:")
    print("-------------------------")
    try:
        files = os.listdir(f'{pathListerMusic}')
    except (FileNotFoundError, NameError):
        print("Direcotry Not Found | Please use a working directory")
        exitForMilky()
    try:
        for file in files:
            fileName , fileEXT = os.path.splitext(file)
            if fileEXT.lower() == f".mp3":
                print(f">>> {fileName}")
    except UnboundLocalError:
        print
        writeReadMilk.write()
    print("-------------------------")
    chooser()

def exitForMilky():
    i12 = input("Want to continue?: ")
    if i12.lower() == "yes":
        chooser()
    else:
        print("Ok Bye Bye Type Exit Next!!!")
        
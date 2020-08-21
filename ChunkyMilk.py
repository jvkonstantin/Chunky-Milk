from time import sleep
import os
import sys
import webbrowser
import milkChanger
import milkChooser
import printAsciiTitles
import momentaryJson
import writeReadMilk
import json


                 


os.system('mode 140,40')
printAsciiTitles.decide()
songChooserList = ['1', 'song chooser']
nameChangerList = ['2', 'name changer']
pathChangerList = ['3', 'path changer']

while True:
    mainCommand = input("\n\n\n                  >>")
    if mainCommand.lower() in songChooserList:
        milkChooser.lister()
        milkChooser.chooser()
        
    elif mainCommand.lower() in nameChangerList:
        milkChanger.chooser()
    elif mainCommand.lower() in pathChangerList:
        writeReadMilk.write()
        
    elif mainCommand.lower() == "list":
        ascii3 = open("ascii3.txt", "r")
        ascii3art = ascii3.read()
        print(ascii3art)
    elif mainCommand.lower() == "exit":
        break
    elif mainCommand.lower() == "exit -r":
        exit()
    else:
        print(f"Error Unkown Please Get Help At contactemail@email.com")
input("Please Press [Enter] To close The Window")

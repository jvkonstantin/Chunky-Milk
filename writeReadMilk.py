import os
import sys
import json
from time import sleep

def read():  
        global readJSON
        with open("config.json") as readJSON:
                global data
                global pathFileJSON
                global pathMusicJSON
                data = json.load(readJSON)
                pathMusicJSON = data["pathMUSIC"]
                pathFileJSON = data["pathFILES"]
                 

def write():
        
        read()
        if pathMusicJSON.lower() == "none":
                with open("config.json") as json_write:
                        data = json.load(json_write) 
                        pathMusicInput = input("Please put a path folder for your music: ")
                        musicortext = "MUSIC"
                        y = {f"path{musicortext}" : f"{pathMusicInput}"}
                        data.update(y)
                        writeJSON(data)
                if pathFileJSON.lower() == "none":
                        with open("config.json") as json_write:
                                data = json.load(json_write) 
                                pathFileInput = input("Please put a path folder for your files: ")
                                musicortext = "FILES"
                                y = {f"path{musicortext}" : f"{pathFileInput}"}
                                data.update(y)
                                writeJSON(data)
                                import printAsciiTitles
                                printAsciiTitles.decide()
                else:
                        i122 = input("There is already a path would you like to continue?: ")
                        if i122.lower() == "yes":
                                with open("config.json") as json_write:
                                        data = json.load(json_write) 
                                        pathFileInput = input("Please put a path folder for your files: ")
                                        musicortext = "FILES"
                                        y = {f"path{musicortext}" : f"{pathFileInput}"}
                                        data.update(y)
                                        writeJSON(data)
                        else:
                                print("Okay")
                                import printAsciiTitles
                                printAsciiTitles.decide()
                
        else:
                i123 = input("There is already a path would you like to change it?:")
                if i123.lower() == "yes":

                        with open("config.json") as json_write:
                                data = json.load(json_write) 
                                pathMusicInput = input("Please put a path folder for your music: ")
                                musicortext = "MUSIC"
                                y = {f"path{musicortext}" : f"{pathMusicInput}"}
                                data.update(y)
                                writeJSON(data)
                        if pathFileJSON.lower() == "none":
                                with open("config.json") as json_write:
                                        data = json.load(json_write) 
                                        pathFileInput = input("Please put a path folder for your files: ")
                                        musicortext = "FILES"
                                        y = {f"path{musicortext}" : f"{pathFileInput}"}
                                        data.update(y)
                                        writeJSON(data)
                
                        import printAsciiTitles
                        printAsciiTitles.decide()
                else:
                        print("Okay")
                        import printAsciiTitles
                        printAsciiTitles.decide()

def writeJSON(dataForWrite):
              with open("config.json", "w") as f:
                      json.dump(dataForWrite, f, indent=4)





                

import json



with open("config.json") as readJSON:
        global data
        global pathFileJSON
        global pathMusicJSON
        data = json.load(readJSON)
        pathMusicJSON = data["pathMUSIC"]
        
                 
def decide():
    import json
    with open("config.json") as readJSON:
        data = json.load(readJSON)
        pathMusicJSONForStrart = data["pathMUSIC"]
        # pathFileJSONForStart = data["pathFILES"]
    if pathMusicJSONForStrart.lower() == "none":
        with open("ascii2.txt", "r") as asciiTXT:
            asciiart = asciiTXT.read()
            print(asciiart)

    else:
        with open("ascii.txt", "r") as asciiTXT:
            asciiart = asciiTXT.read()
            print(asciiart)                                                                                         
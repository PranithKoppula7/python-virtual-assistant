import requests
import wikipedia
import pywhatkit as kit
from termcolor import colored
import os
import math

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def search_on_google(query):
    kit.search(query)

def play_on_youtube(video):
    kit.playonyt(video)

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_iss_location():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("http://api.open-notify.org/iss-now.json", headers=headers).json()
    iss_position = res["iss_position"]
    latitude = float(iss_position["latitude"])
    longitude = float(iss_position["longitude"])
    mapped_coordinates = convert_coordinates(latitude=latitude, longitude=longitude)
    """
    4 Cases: 
        (+,+): (90, 180)  ==> (0, 73)
        (+,-): (90, -180) ==> (0, 0)
        (-,-): (-90,-180) ==> (23,0)
        (-,+): (-90, 180) ==> (23,73)
    """
    world_map_array = [
        ["""+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+"""],
        ["""|           . _..::__:  ,-"-"._        |7       ,     _,.__             |"""],
        ["""|   _.___ _ _<_>`!(._`.`-.    /         _._     `_ ,_/  '  '-._.---.-.__|"""],
        ["""|>.{     " " `-==,',._\{  \  / {)      / _ ">_,-' `                mt-2_|"""],
        ["""+  \_.:--.       `._ )`^-. "'       , [_/(                       __,/-' +"""],
        ["""| '"'     \         "    _L        oD_,--'                )     /. (|   |"""],
        ["""|          |           ,'          _)_.\\\\._<> 6              _,' /  '   |"""],
        ["""|          `.         /           [_/_'` `"(                <'}  )      |"""],
        ["""+           \\\\    .-. )           /   `-'"..' `:._          _)  '       +"""],
        ["""|    `        \  (  `(           /         `:\  > \  ,-^.  /' '         |"""],
        ["""|              `._,   ""         |           \`'   \|   ?_)  {\         |"""],
        ["""|                 `=.---.        `._._       ,'     "`  |' ,- '.        |"""],
        ["""+                   |    `-._         |     /          `:`<_|h--._      +"""],
        ["""|                   (        >        .     | ,          `=.__.`-'\     |"""],
        ["""|                    `.     /         |     |{|              ,-.,\     .|"""],
        ["""|                     |   ,'           \   / `'            ,"     \     |"""],
        ["""+                     |  /              |_'                |  __  /     +"""],
        ["""|                     | |                                  '-'  `-'   \.|"""],
        ["""|                     |/                                         "    / |"""],
        ["""|                     \.                                             '  |"""],
        ["""+                                                                       +"""],
        ["""|                      ,/            ______._.--._ _..---.---------._   |"""],
        ["""|     ,-----"-..?----_/ )      __,-'"             "                  (  |"""],
        ["""|-.._(                  `-----'                                       `-|"""],
        ["""+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+"""]
    ]
    credit = "Map 1998 Matthew Thomas. Freely usable as long as this line is included."
    os.system("color")
    line_to_edit = world_map_array[mapped_coordinates[0]][0]
    eddited_line = list(line_to_edit)
    eddited_line[mapped_coordinates[1]] = colored("*", "green")
    eddited_line = "".join(eddited_line)
    world_map_array[mapped_coordinates[0]][0] = eddited_line
    for i in world_map_array:
        print(i[0])
    print(credit)

def convert_coordinates(latitude, longitude):
    latitude = 90 - latitude
    longitude = longitude + 180

    converted_latitude = (latitude/180)*23
    converted_longitude = (longitude/360)*72
    return [math.ceil(converted_latitude), math.ceil(converted_longitude)]
import csv
import os
import pprint
import time
import sys
import urllib.request, json
import requests
from os import path
import math
import re
import random


from lib import ui
from lib import database

################################################################################
"""
Check if the game passed is in the steam drm free list
"""
################################################################################

#main function for checking drm status of a game from steam
def drmMenu(steam_db):
    os.system('cls' if os.name == 'nt' else 'clear')
    while 2==2:
        text=ui.drmMenuUI()
        os.system('cls' if os.name == 'nt' else 'clear')

        #game checker code
        if text == "c":
            while 2==2:
                boo=1
                text_1=ui.drmCheckMenu()
                os.system('cls' if os.name == 'nt' else 'clear')
                if text_1 =="b":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    for i in steam_db:
                        if text_1 in i[0]:
                            print(" ")
                            print(ui.pcol.G+"    Game is DRM Free: "+ui.pcol.ENDC+i[0]+" " +i[1])
                            if(len(i)>2):
                                print(ui.pcol.Y+"    "+i[2]+ui.pcol.ENDC)
                            boo=0
                    if(boo==1):
                        print(ui.pcol.R+"The game you typed in: [ "+ text_1 + " ] is not drm free."+ui.pcol.ENDC)
                print(" ")
                print(ui.pcol.B + "Type anything to go back." + ui.pcol.ENDC)
                text_2=input(": ")
                os.system('cls' if os.name == 'nt' else 'clear')

        #back option
        elif text == "b":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print(ui.pcol.R+"Not a valid command, please try again."+ui.pcol.ENDC)
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')



###############################################################################
"""
code for the backend of the gog store query menu
"""
###############################################################################

#gog main menu
def gogMenu(gog_data):
    os.system('cls' if os.name == 'nt' else 'clear')
    while 0==0:
        os.system('cls' if os.name == 'nt' else 'clear')
        text=ui.gogMenuUI()
        if text =="l":
            gogSells(gog_data)
        elif text =="s":
            listy=gogOnSale(gog_data)
        elif text =="g":
            listy=gogGenre(gog_data)
        elif text== "b":
            break
        else:
            print("Not a valid input. Please try again.")
            time.sleep(2)

#function for finding if a game exists on gog store
def gogSells(gog_data):
    os.system('cls' if os.name == 'nt' else 'clear')
    while 2==2:
        text=input(ui.pcol.P + "Type in the name of a game: " + ui.pcol.ENDC)
        boo=0
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in gog_data:
            if text in i["title"]:
                inner=i["price"]
                inner=inner.split(",")
                inner=inner[0].split(":")
                inner=inner[1]
                ui.gogGameSearch(i,inner)
                boo=1
        if(boo==0):
            print(ui.pcol.R + "The game you typed in: ["+ ui.pcol.G + text + ui.pcol.R + "] is not on GOG rip :(" + ui.pcol.ENDC)

        print(" ")
        print(ui.pcol.Blank)
        print(ui.pcol.B + "Type anything to go back." + ui.pcol.ENDC)
        text=input(": ")
        break

#prints list of games currently on sale on gog
def gogOnSale(gog_data):
    listy=[]
    while 2==2:
        for i in gog_data:
            name=i["title"]
            inner=i["price"]
            inner=inner.split(",")
            inner=inner[5].split(":")
            inner=str(inner[1][2:-1])
            inner=float(inner)

            price=i["price"]
            price=price.split(",")
            price=price[0].split(":")
            price=price[1]
            if inner >0.0:
                print(ui.pcol.G + i["title"] + ui.pcol.Y + " | Discount: " + str(inner) + " | Sale Price: " + price +ui.pcol.ENDC )
                print(" ")
                listy.append(str(i['title'] + " | Discount: " + str(inner) + " | Sale Price: " + price))
        print(" ")
        print(ui.pcol.Blank)
        print(ui.pcol.B + "Type anything to go back." + ui.pcol.ENDC)
        text=input(": ")
        break
    return listy

#finds all games on gog of the chosen genre
def gogGenre(gog_data):
    os.system('cls' if os.name == 'nt' else 'clear')
    text=ui.genreUI().lower()
    os.system('cls' if os.name == 'nt' else 'clear')
    listy=[]
    while 2==2:
        counter=0
        for i in gog_data:
            if i['category'].lower() == text:
                print(i['title'])
                listy.append(i['title'])
                counter+=1
        print(" ")
        print(str(counter) + ui.pcol.G + " games that are " + ui.pcol.B + text + ui.pcol.G + " games." + ui.pcol.ENDC)
        print(" ")
        print(ui.pcol.Blank)
        print(ui.pcol.B + "Type anything to go back." + ui.pcol.ENDC)
        text=input(": ")
        break
    return listy

################################################################################
"""
Code for querying the local games data from GOG Galaxy 2.0
"""
################################################################################

#main library menu code
def galaxyMenu(opened_data):
    #os.system('cls' if os.name == 'nt' else 'clear')

    #outer loop handling galaxy 2 main menu
    while 2==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        text=ui.galaxyMenuUI()
        bool=0
        if text=="b":
            break
        elif text=="t":
            print(" ")
            print(ui.pcol.Blank)
            print("Total Time Played:")
            print(timeTotalHelp(opened_data))
            bool=1
            print(ui.pcol.B + "Type anything to continue." + ui.pcol.ENDC)
            text1=input(": ")
        elif text.lower()=="r":
            print(" ")
            print(ui.pcol.Blank)
            print("Heres a game you should play:")
            randomHelp(opened_data)
            bool=1
            print(ui.pcol.B + "Type anything to continue." + ui.pcol.ENDC)
            text1=input(": ")
        else:
            try:
                text=text.split(": ")
                command=text[0]
                game=text[1].lower()
            except:
                print(ui.pcol.Blank)
                print(ui.pcol.R + "Command not valid. Try again" + ui.pcol.ENDC)
                time.sleep(3)
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                for i in opened_data:
                    temp=i[0].lower()
                    if command == "p" or command == "d":
                        bool+=platformHelper(game,i,command)

                    elif game in temp:
                        bool=1
                        if command=="e":
                            print(ui.pcol.G + "You own this game: " + ui.pcol.Y +i[0] + ui.pcol.ENDC)
                            print(" ")

                        elif command=="s":
                            ui.statsUI(i)

            if bool==0:
                print(ui.pcol.R + "You dont own this game." + ui.pcol.ENDC)
            elif bool >=1 and command == "p" or command == "d":
                print(ui.pcol.C + str(bool) + " Games" + ui.pcol.ENDC)

            print(" ")
            print(ui.pcol.B + "Type anything to go back." + ui.pcol.ENDC)
            text=input(": ")

def randomHelp(opened_data):
    name_list=[]
    score_list=[]
    current_name=""
    current_score=0.0
    counter=0
    for i in opened_data:
        if counter>0:
            if i[3] =="":
                rating=0
            else:
                rating=int(i[3])

            if i[9] =="":
                time=0.5
            else:
                time=float(i[9])*0.1
            score=rating/time
            if score > 600:
                current_score=score
                current_name=i[0]
                name_list.append(current_name)
                score_list.append(score)
        counter+=1

    choose=random.randint(0,len(name_list)-1)
    current_name=name_list[choose]
    current_score=score_list[choose]

    for i in opened_data:
        if i[0] == current_name:
            print(ui.pcol.G + "Title: " + ui.pcol.Y + i[0] + ui.pcol.ENDC)
            print(ui.pcol.G + "Summary: " + ui.pcol.Y + i[1] + ui.pcol.ENDC)
            print(ui.pcol.G + "Platform: " + ui.pcol.Y + i[2][2:-2] + ui.pcol.ENDC)
            print(ui.pcol.G + "Score: " + ui.pcol.Y + str(current_score) + ui.pcol.ENDC)


#helper function to sum playtime of all games
def timeTotalHelp(opened_data):
    sum=0
    for i in opened_data:
        try:
            sum+=int(i[9])
        except:
            sum+=0

    hours,mins=divmod(float(sum),60)
    return("Hours:"+str(hours)+" Minutes:"+str(mins))

def platformHelper(info,i, command):
    if command == "p":
        if info in i[2].lower():
            print(ui.pcol.G + "Title: " + ui.pcol.Y + i[0] + ui.pcol.ENDC)
            print(" ")
            return 1
        elif info =="all":
            print(ui.pcol.G + "Title: " + ui.pcol.Y + i[0] + ui.pcol.ENDC)
            print(" ")
            return 1
        else:
            return 0
    else:
        platforms=i[2]
        platforms=platforms[2:-2]
        platforms=platforms.split("', '")
        if len(platforms) == 1:
            return 0
        else:
            print(ui.pcol.G + "Title: " + ui.pcol.Y + i[0] + ui.pcol.ENDC)
            print(ui.pcol.G + "Platforms: " + ui.pcol.Y + str(platforms) + ui.pcol.ENDC)
            print(" ")
            return 1


################################################################################
"""
Code for printing menus
"""
################################################################################

#main printer function
def printMenu(opened_data,steam_db):
    while 2==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        text=ui.printUI()
        if text.lower() == "b":
            break
        elif text.lower() == "f":
            printDRMFree(opened_data,steam_db)
            print(ui.pcol.G + "file" + ui.pcol.B + " 'drmFreeSteamGamesOwned.txt' " + ui.pcol.G + "generated in 'outputs' folder." + ui.pcol.ENDC)
            time.sleep(3)
        elif text.lower() =="d":
            printDuplicates(opened_data,steam_db)
            print(ui.pcol.G + "file" + ui.pcol.B + " 'duplicates.txt' " + ui.pcol.G + "generated in 'outputs' folder." + ui.pcol.ENDC)
            time.sleep(3)
        else:
            printLibrary(opened_data,text.lower())
            print(ui.pcol.G + "file " + ui.pcol.B + "'" + text.lower() + ".txt' " + ui.pcol.G + "generated in 'outputs' folder." + ui.pcol.ENDC)
            time.sleep(3)

#drm free printer function
def printDRMFree(opened_data,steam_db):
    listy=[]
    regex = re.compile('[^a-zA-Z0-9]')

    for j in steam_db:
        for i in opened_data:
            inner=j[0].split(": ",1)
            inner=inner[1]
            regex.sub(' ',inner)
            inner2=i[0]
            regex.sub(' ',inner2)
            inner=inner.replace("-","")
            inner=inner.replace(" - ","")
            inner=inner.replace('  ',' ')
            inner2=inner2.replace("-","")
            inner2=inner2.replace(" - ","")
            inner2=inner2.replace('  ',' ')
            if inner in inner2:
                if "Steam" in i[2]:
                    listy.append(str(i[0]))

    listy=list(dict.fromkeys(listy))
    database.createTextFile('outputs/drmFreeSteamGamesOwned.txt',listy)

#printing all games that are on multiple platforms to a file.
def printDuplicates(opened_data,steam_db):
    listy=[]
    for i in opened_data:
        inner=i[2][2:-2].split("', '")
        if len(inner) > 1:
            inner2="Title: " + i[0] + " | Platforms: "
            for j in inner:
                inner2=inner2+str(j) + " ; "
            listy.append(inner2)
    database.createTextFile('outputs/duplicates.txt',listy)

#function to generate file of all owned games on a specific platform.
def printLibrary(opened_data,text):
    listy=[]
    for i in opened_data:
        if text in i[2][2:-2].lower() or text=="all":
            listy.append(i[0])
    database.createTextFile('outputs/'+text+'.txt',listy)

import csv
import os
import pprint
import time
import sys
import urllib.request, json
import requests
from os import path
from pathlib import Path
import math
import re


import ui

################################################################################
"""
Check if the game passed is in the steam drm free list
"""
################################################################################

#main function for checking drm status of a game from steam
def exists(fetchedSteamDB):
    os.system('cls' if os.name == 'nt' else 'clear')
    while 2==2:
        print(" ")
        print(ui.pcol.Blank)
        print(" ")
        print(ui.pcol.B+'chk' +ui.pcol.ENDC+" - check if your steam game has drm.")
        print(ui.pcol.B+'bk' +ui.pcol.ENDC+" - go back to the main menu.")
        text=input(": ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if text == "chk":
            while 2==2:
                boo=0
                print(" ")
                print(ui.pcol.Blank)
                print(" ")
                print(ui.pcol.P + "Type in the name of the game to check if its drm free." + ui.pcol.ENDC)
                print(ui.pcol.B+'bk' +ui.pcol.ENDC+ " - go back to previous menu.")
                text1=input(": ")
                os.system('cls' if os.name == 'nt' else 'clear')
                if text1 =="bk":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                else:
                    for i in fetchedSteamDB:
                        if text1 in i[0]:
                            print(" ")
                            print(" ")
                            print(ui.pcol.G+"    Game is DRM Free: "+ui.pcol.ENDC+i[0]+" " +i[1])
                            if(len(i)>2):
                                print(ui.pcol.Y+"    "+i[2]+ui.pcol.ENDC)
                            boo=0
                            break
                        else:
                            boo=1
                    if(boo==1):
                        print(ui.pcol.R+"The game you typed in: [ "+ text1 + " ] is not drm free."+ui.pcol.ENDC)

        elif text == "bk":
            os.system('cls' if os.name == 'nt' else 'clear')
            break
        else:
            print(ui.pcol.R+"Not a valid command, please try again."+ui.pcol.ENDC)


###############################################################################
"""
code for the backend of the gog store query menu
"""
###############################################################################



def selectAction(gogdata):
    os.system('cls' if os.name == 'nt' else 'clear')
    ui.picPrint("GOG Store Page")
    while 0==0:
        text=ui.gogQueryMenu()
        if text =="look":
            existsGog(gogdata)

        elif text =="sale":
            gamesOnSale(gogdata)
        elif text== "bk":
            break
        else:
            print("Not a valid input. Please try again.")


def existsGog(gogdata):
    os.system('cls' if os.name == 'nt' else 'clear')
    text=input(ui.pcol.P + "Type in the name of a game: " + ui.pcol.ENDC)
    boo=0
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in gogdata:
        if text in i["title"]:
            inner=i["price"]
            inner=inner.split(",")
            inner=inner[0].split(":")
            inner=inner[1]
            ui.gogGameSearch(i,inner)
            boo=1
    if(boo==0):
        print(ui.pcol.R + "The game you typed in: ["+ ui.pcol.G + text + ui.pcol.R + "] is not on GOG rip :(" + ui.pcol.ENDC)

def gamesOnSale(gogdata):
    for i in gogdata:
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


################################################################################
"""
Code for querying the local games data from GOG Galaxy 2.0
"""
################################################################################

def timeTotalHelp(opened_data):
    sum=0
    for i in opened_data:
        try:
            sum+=int(i[9])
        except:
            sum+=0

    hours,mins=divmod(float(sum),60)
    return("Hours:"+str(hours)+" Minutes:"+str(mins))

def platformHelper(platformyey,i, command):
    if command == "p":
        if platformyey in i[2].lower():
            print(ui.pcol.G + "Title: " + ui.pcol.Y + i[0] + ui.pcol.ENDC)
            print(" ")
            return 1
        elif platformyey =="all":
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


def queryDB(opened_data):
    os.system('cls' if os.name == 'nt' else 'clear')

    #outer loop handling galaxy 2 main menu
    while 2==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        ui.picPrint("Games Library Viewer.")
        text=ui.libraryUI()
        if text=="bk":
            break
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
                bool=0
                os.system('cls' if os.name == 'nt' else 'clear')
                for i in opened_data:
                    titleTemp=i[0].lower()
                    if command=="t":
                        print(timeTotalHelp(opened_data))
                        bool=1
                        break

                    elif command == "p" or command == "d":
                        bool+=platformHelper(game,i,command)

                    elif game in titleTemp:
                        bool=1
                        if command=="e":
                            print(ui.pcol.G + "You own this game: " + ui.pcol.Y +i[0] + ui.pcol.ENDC)
                            print(" ")

                        elif command=="s":
                            ui.galaxyUI(i)


                if bool==0:
                    print(ui.pcol.R + "You dont own this game." + ui.pcol.ENDC)
                elif bool >=1 and command == "p" or command == "d":
                    print(ui.pcol.C + str(bool) + ui.pcol.ENDC)

                print(" ")
                print(ui.pcol.B + "bk" + ui.pcol.ENDC +" - go back and select another option.")
                text=input(": ")


################################################################################
"""
Code for printing menus
"""
################################################################################

#drm free printer function
def printDRMFree(opened_data,fetchedSteamDB):
    listy=[]
    regex = re.compile('[^a-zA-Z0-9]')

    for j in fetchedSteamDB:
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
    with open('outputs/drmFreeSteamGamesOwned.txt', 'w') as filehandle:
        for listitem in listy:
            filehandle.write('%s\n' % listitem)

#printing all games that are on multiple platforms to a file.
def printDuplicates(opened_data,fetchedSteamDB):
    listy=[]
    for i in opened_data:
        inner=i[2][2:-2].split("', '")
        if len(inner) > 1:
            inner2="Title: " + i[0] + " | Platforms: "
            for j in inner:
                inner2=inner2+str(j) + " ; "
            listy.append(inner2)
    with open('outputs/duplicates.txt', 'w') as filehandle:
        for listitem in listy:
            filehandle.write('%s\n' % listitem)

#function to generate file of all owned games on a specific platform.
def printLibrary(opened_data,text):
    listy=[]
    for i in opened_data:
        if text in i[2][2:-2].lower():
            listy.append(i[0])
    with open('outputs/'+text+'.txt', 'w') as filehandle:
        for listitem in listy:
            filehandle.write('%s\n' % listitem)


#main printer function
def printerFun(opened_data,fetchedSteamDB):
    while 2==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        ui.picPrint("Print Menu.")
        text=ui.printUI()
        if text.lower() == "bk":
            break
        elif text.lower() == "drmfree":
            printDRMFree(opened_data,fetchedSteamDB)
            print(ui.pcol.G + "file" + ui.pcol.B + " 'drmFreeSteamGamesOwned.txt' " + ui.pcol.G + "generated in 'outputs' folder." + ui.pcol.ENDC)
            time.sleep(3)
        elif text.lower() =="duplicates":
            printDuplicates(opened_data,fetchedSteamDB)
            print(ui.pcol.G + "file" + ui.pcol.B + " 'duplicates.txt' " + ui.pcol.G + "generated in 'outputs' folder." + ui.pcol.ENDC)
            time.sleep(3)
        else:
            printLibrary(opened_data,text.lower())
            print(ui.pcol.G + "file " + ui.pcol.B + "'" + text.lower() + ".txt' " + ui.pcol.G + "generated in 'outputs' folder." + ui.pcol.ENDC)
            time.sleep(3)

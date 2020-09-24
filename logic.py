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

import galaxy
import ui

###############################################################################
#Check if the game passed is in the steam drm free list
#argv = steamdrm? -DEPRICATED
###############################################################################
def exists(fetchedSteamDB):
    os.system('cls' if os.name == 'nt' else 'clear')
    while 2==2:
        print(" ")
        print("_____________________________________________________________________________")
        print(" ")
        print("Type "+ui.pcol.B+'chk' +ui.pcol.ENDC+" to see if the game on steam has drm.")
        print("Type "+ui.pcol.B+'bk' +ui.pcol.ENDC+" to go back to the main menu.")
        text=input("Response: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if text == "chk":
            while 2==2:
                boo=0
                print(" ")
                print("_____________________________________________________________________________")
                print(" ")
                print("Type in the name of the game to check if its drm free.")
                print("Type "+ui.pcol.B+'bk' +ui.pcol.ENDC+ " to go back.")
                text1=input("Response: ")
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

################################################################################

###############################################################################
#code for the backend of the gog store query menu
#arg = onGog
###############################################################################

def gogOpen():
    with open('dataBases/GOG.csv') as f:
        a = [{k: str(v) for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]
    return a

def selectAction():
    os.system('cls' if os.name == 'nt' else 'clear')
    ui.picPrint("GOG Store Page")
    gogdata=gogOpen()
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

################################################################################
"""
#Code for querying the local games data from GOG Galaxy 2.0
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

def platformHelp(opened_data,game):
    sum=0
    platform=""
    if game=="steam":
        platform="['Steam']"
    elif game=="epic":
        platform="['Epic Games Store']"
    elif game=="playstation":
        platform="['PlayStation Network']"
        
def queryDBHelper(opened_data,text):

    while 2==2:
        try:
            text=text.split(": ")
            command=text[0]
            game=text[1]
        except:
            print("_____________________________________________________________________________")
            print(ui.pcol.R + "Command not valid. Try again" + ui.pcol.ENDC)
            time.sleep(3)
            break

        else:
            bool=0
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in opened_data:
                if command=="t":
                    print(timeTotalHelp(opened_data))
                    bool=1
                    break
                #elif command =="n":
                #    platformHelp(opened_data,game)
                #    bool=1
                #    break

                elif game in i[0]:
                    bool=1
                    if command=="e":
                        print(ui.pcol.G + "You own this game: " + ui.pcol.Y +i[0] + ui.pcol.ENDC)
                        print(" ")

                    elif command=="s":
                        ui.galaxyUI(i)
                    elif command=="p":
                        print(ui.pcol.G + "Title: " + ui.pcol.Y + i[0] +ui.pcol.ENDC)
                        print(ui.pcol.G + "Time Played: " + ui. pcol.Y + i[9] +" minutes." + ui.pcol.ENDC)
                        print(" ")

            if bool==0:
                print("You dont own this game.")

        print(" ")
        print(ui.pcol.B + "bk" + ui.pcol.ENDC +" - go back and select another option.")
        text=input(": ")
        if text=="bk":
            break

def queryDB(opened_data):
    os.system('cls' if os.name == 'nt' else 'clear')

    while 2==2:
        os.system('cls' if os.name == 'nt' else 'clear')
        ui.picPrint("Games Library Viewer.")
        text=ui.libraryUI()
        if text=="bk":
            break
        else:
            queryDBHelper(opened_data,text)

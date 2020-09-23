#welcome to steamTuuls
#snmackay
#This tool is not meant for any malicious or criminal activity.

import os
import csv
import sys
import urllib, json
import time

import steam
import gog
import settings
import help

def createFile(cleanedList,fileName):
    with open(fileName, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(cleanedList)

def openFile(fileName):
    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        array_boii=[]
        for row in csv_reader:
            array_boii.append(row)
    return array_boii

def main():
    settingStore=settings.loadSettings()
    settingStore2=settings.processSettings(settingStore)
    os.system("clear")
    while 0==0:
        os.system("clear")
        print(help.pcol.Y+"WELCOME TO STEAMTUULS!"+help.pcol.ENDC)
        print(" ")
        print(" ")
        print(help.pcol.R+"                       ueeeeeu..")
        print("  "+"                ur d$$$$$$$$$$$$$$Nu")
        print("  "+"              d$$$ \"$$$$$$$$$$$$$$$$$$e.")
        print("  "+"          u$$c   \"\"   ^\"^**$$$$$$$$$$$$$b.")
        print("  "+"        z$$#\"\"\"           `!?$$$$$$$$$$$$$N.")
        print("  "+"      .$P                   ~!R$$$$$$$$$$$$$b")
        print("  "+"     x$F                 **$b. '\"R).$$$$$$$$$$")
        print("  "+"    J^\"                           #$$$$$$$$$$$$.")
        print("  "+"   z$e                      ..      \"**$$$$$$$$$")
        print("  "+"  :$P           .        .$$$$$b.    ..  \"  #$$$$")
        print("  "+"  $$            L          ^*$$$$b   \"      4$$$$L")
        print("  "+" 4$$            ^u    .e$$$$e.\"*$$$N.       @$$$$$")
        print("  "+" $$E            d$$$$$$$$$$$$$$L \"$$$$$  mu $$$$$$F")
        print("  "+" $$&            $$$$$$$$$$$$$$$$N   \"#* * ?$$$$$$$N")
        print("  "+" $$F            '$$$$$$$$$$$$$$$$$bec...z$ $$$$$$$$")
        print("  "+"'$$F             `$$$$$$$$$$$$$$$$$$$$$$$$ '$$$$E\"$")
        print("  "+" $$                  ^\"\"\"\"\"\"`       ^\"*$$$& 9$$$$N")
        print("  "+" k  u$                                  \"$$. \"$$P r")
        print("  "+" 4$$$$L                                   \"$. eeeR")
        print("  "+"  $$$$$k                                   '$e. .@")
        print("  "+"  3$$$$$b                                   '$$$$")
        print("  "+"   $$$$$$                                    3$$\"")
        print("  "+"    $$$$$  dc                                4$F")
        print("  "+"     RF** <$$                                J\"")
        print("  "+"      #bue$$$LJ$$$Nc.                        \"")
        print("  "+"       ^$$$$$$$$$$$$$r")
        print("  "+"         `\"*$$$$$$$$$")
        print(help.pcol.ENDC)
        print("_____________________________________________________________________________")
        print(" ")
        print(help.pcol.P + "Choose a command from the list below." + help.pcol.ENDC)
        print(help.pcol.B + "sdb" + help.pcol.ENDC + " - generate steam drm free games database.")
        print(help.pcol.B + "sdrm" + help.pcol.ENDC + " - check if a steam game has drm.")
        print(help.pcol.B + "gdb" + help.pcol.ENDC + " - generate the GOG games database.")
        print(help.pcol.B + "gog" + help.pcol.ENDC + " - interact with GOG store database.")
        print(help.pcol.B + "galdb" + help.pcol.ENDC + " - generate database from your GOG Galaxy 2 library.")
        print(help.pcol.B + "galax" + help.pcol.ENDC + " - interact with your GOG Galaxy 2 library.")
        print(help.pcol.B + "quit" + help.pcol.ENDC + " - exit SteamTuuls.")
        text=input(": ")
        print("_____________________________________________________________________________")
        print(" ")
        if text=="sdb":
            createFile(steam.drmListOpen(),"dataBases/SteamDRMFree.csv")
            print("database creation successful")
            time.sleep(3)
        elif text=="sdrm":
            fetchedSteamDB=openFile("dataBases/SteamDRMFree.csv")
            steam.exists(fetchedSteamDB)
        elif text =="gdb":
            gog.processGog()
        elif text=="gog":
            fetchedGogDB=openFile("dataBases/GOG.csv")
            gog.selectAction(fetchedGogDB)
        elif text=="galdb":
            settings.generateDB()
        elif text == "galaxy":
            opened_data=openFile("dataBases/gameDB.csv")
            settings.queryDB(opened_data)
        elif text=="quit":
            print(help.pcol.Y +"Hope ya enjoyed!")
            break
        else:
            print("Not a valid input please try again.")
            time.sleep(3)




if "__name__==__main__":
    inputer= os.getcwd()
    main()

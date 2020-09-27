#welcome to steamTuuls
#snmackay
#This tool is not meant for any malicious or criminal activity.
import os
import csv
import sys
import urllib, json
import time

from lib import ui
from lib import database
from lib import logic



def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    #fetch all database files first.

    while 0==0:
        os.system('cls' if os.name == 'nt' else 'clear')
        ui.picPrint("WELCOME TO STEAMTUULS!")
        text=ui.mainMenu()

        #file exists safety checks
        existsdrm= os.path.isfile('dataBases/SteamDRMFree.csv')
        existsgog= os.path.isfile('dataBases/GOG.csv')
        existgalax= os.path.isfile('dataBases/libraryDB.csv')

        #database generation tools
        if text=="1":
            database.processDrm()
            print(ui.pcol.G + "database creation successful" + ui.pcol.ENDC)
            time.sleep(3)
        elif text =="2":
            database.processGog()
            print(ui.pcol.G + "database creation successful" + ui.pcol.ENDC)
            time.sleep(3)
        elif text=="3":
            database.processLib()
            print(ui.pcol.G + "database creation successful" + ui.pcol.ENDC)
            time.sleep(3)

        #querys
        elif text=="s" and existsdrm:
            logic.drmMenu(database.openListCsv("dataBases/SteamDRMFree.csv"))

        elif text=="g" and existsgog:
            logic.gogMenu(database.openDictCsv())

        elif text == "l" and existgalax:
            logic.galaxyMenu(database.openListCsv("dataBases/libraryDB.csv"))

        elif text =="p" and existsdrm and existgalax:
            logic.printMenu(database.openListCsv("dataBases/libraryDB.csv"),database.openListCsv("dataBases/SteamDRMFree.csv"))

        elif text=="q":
            print(ui.pcol.Y +"Hope ya enjoyed!")
            break
        else:
            print(ui.pcol.R + "Not a valid command please try again, or the command you tried is missing a database file." + ui.pcol.ENDC)
            time.sleep(3)


if "__name__==__main__":
    inputer= os.getcwd()
    main()

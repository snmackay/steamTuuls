#welcome to steamTuuls
#snmackay
#This tool is not meant for any malicious or criminal activity.

import os
import csv
import sys
import urllib, json
import time


import ui
import database
import logic



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
        if text=="sdb":
            database.createFile(database.drmListOpen(),"dataBases/SteamDRMFree.csv")
            print(ui.pcol.G + "database creation successful" + ui.pcol.ENDC)
            time.sleep(3)
        elif text =="gdb":
            database.processGog()
        elif text=="galdb":
            database.generateDB()

        #querys
        elif text=="sdrm" and existsdrm:
            fetchedSteamDB=database.openFile("dataBases/SteamDRMFree.csv")
            logic.exists(fetchedSteamDB)
        elif text=="gog" and existsgog:
            gogdata=database.gogOpen()
            logic.selectAction(gogdata)
        elif text == "galax" and existgalax:
            opened_data=database.openFile("dataBases/libraryDB.csv")
            logic.queryDB(opened_data)
        elif text =="print" and existsdrm and existgalax:
            fetchedSteamDB=database.openFile("dataBases/SteamDRMFree.csv")
            opened_data=database.openFile("dataBases/libraryDB.csv")
            logic.printerFun(opened_data,fetchedSteamDB)
        elif text=="quit":
            print(ui.pcol.Y +"Hope ya enjoyed!")
            break
        else:
            print(ui.pcol.R + "Not a valid command please try again, or the command you tried is missing a database file." + ui.pcol.ENDC)
            time.sleep(3)


if "__name__==__main__":
    inputer= os.getcwd()
    main()

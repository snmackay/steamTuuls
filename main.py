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
    os.system('cls' if os.name == 'nt' else 'clear')
    while 0==0:
        os.system('cls' if os.name == 'nt' else 'clear')
        ui.picPrint("WELCOME TO STEAMTUULS!")
        text=ui.mainMenu()
        if text=="sdb":
            createFile(database.drmListOpen(),"dataBases/SteamDRMFree.csv")
            print("database creation successful")
            time.sleep(3)
        elif text=="sdrm":
            fetchedSteamDB=openFile("dataBases/SteamDRMFree.csv")
            logic.exists(fetchedSteamDB)
        elif text =="gdb":
            database.processGog()
        elif text=="gog":
            logic.selectAction()
        elif text=="galdb":
            database.generateDB()
        elif text == "galax":
            opened_data=openFile("dataBases/libraryDB.csv")
            logic.queryDB(opened_data)
        elif text=="quit":
            print(ui.pcol.Y +"Hope ya enjoyed!")
            break
        else:
            print(ui.pcol.R + "Not a valid command please try again." + ui.pcol.ENDC)
            time.sleep(3)




if "__name__==__main__":
    inputer= os.getcwd()
    main()

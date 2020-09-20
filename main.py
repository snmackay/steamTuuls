#welcome to steamTuuls
#snmackay
#This tool is not meant for any malicious or criminal activity.

import os
import csv
import sys
import urllib, json

import steam
import gog
import settings



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

    while 0==0:
        print(" ")
        print("________________________________________________________________")
        print(" ")
        print("Type 'steamDB' to regenerate the steam drm free games list.")
        print("Type 'steamdrm?' to check and see if a game has drm.")
        print("Type 'gogDB' to regenerate the GOG games database.")
        print("Type 'onGog' to check discounts and see if GOG has a game.")
        print("Type 'onDisk' to generate lists of what games you have")
        print("^Note: This requires providing the directories via settings.txt")
        print("Type 'quit' to exit the tool.")
        text=input("Response: ")
        if text=="steamDB":
            drmList=steam.drmListOpen()
            print("parsed text file")
            cleanedList=steam.listCleaner(drmList)
            cleanedList=steam.listOrganize(cleanedList)
            print("data cleaned")
            createFile(cleanedList,"dataBases/SteamDRMFree.csv")
            print("database creation successful")
        elif text=="steamdrm?":
            fetchedSteamDB=openFile("dataBases/SteamDRMFree.csv")
            steam.exists(fetchedSteamDB)
        elif text =="gogDB":
            rawdb=gog.processGog()
            writeOut=gog.createRaw(rawdb)
            contents=gog.readRaw()
            cleanedFile=gog.cleaner(contents)
            createFile(cleanedFile,"dataBases/GOG.csv")
        elif text=="onGog":
            fetchedGogDB=openFile("dataBases/GOG.csv")
            gog.selectAction(fetchedGogDB)
        elif text=="onDisk":
            settings.onDisk(settingStore2)
        elif text=="quit":
            print("Hope ya enjoyed!")
            break
        else:
            print("Not a valid input please try again.")




if "__name__==__main__":
    inputer= os.getcwd()
    main()

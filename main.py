#welcome to steamTuuls
#snmackay
#This tool is not meant for any malicious or criminal activity.

import os
import csv
import sys
import urllib, json

import steam
import gog



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

def main(arg):
    if arg=="steamDB":
        drmList=steam.drmListOpen()
        print("parsed text file")
        cleanedList=steam.listCleaner(drmList)
        cleanedList=steam.listOrganize(cleanedList)
        print("data cleaned")
        createFile(cleanedList,"dataBases/SteamDRMFree.csv")
        print("database creation successful")
    elif arg=="steamdrm?":
        fetchedSteamDB=openFile("dataBases/SteamDRMFree.csv")
        steam.exists(fetchedSteamDB)
    elif arg =="gogDB":
        rawdb=gog.processGog()
        writeOut=gog.createRaw(rawdb)
        contents=gog.readRaw()
        cleanedFile=gog.cleaner(contents)
        createFile(cleanedFile,"dataBases/GOG.csv")
    elif arg =="onGog":
        fetchedGogDB=openFile("dataBases/GOG.csv")
        gog.exists(fetchedGogDB)





if "__name__==__main__":
    inputer= os.getcwd()
    main(sys.argv[1])

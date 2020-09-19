#welcome to steamTuuls
#snmackay
#This tool is not meant for any malicious or criminal activity.

import os
import csv
import steam



def createFile(cleanedList,fileName):
    with open(fileName, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(cleanedList)


def main():
    drmList=steam.drmListOpen()
    cleanedList=steam.listCleaner(drmList)
    cleanedList=steam.listOrganize(cleanedList)
    createFile(cleanedList,"SteamDRMFree.csv")

if "__name__==__main__":
    inputer= os.getcwd()
    main()

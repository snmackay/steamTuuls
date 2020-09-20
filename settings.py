import os
import csv
import sys

def loadSettings():
    lines=[]
    with open("settings.txt",'r') as fp:
        line=fp.readline()
        count=1
        while line:
            line=line.rstrip()
            lines.append(line)
            line=fp.readline()
            count+=1
    return lines

def processSettings(settingsStore):
    steamDirs=[]
    otherDirs=[]
    userEmail=""

    temp=settingsStore[0]
    temp=temp.replace(']','')
    temp=temp.replace('[','')
    temp=temp.replace("'","")
    temp=temp.split(':')
    temp2=temp[1].split(",")
    steamDirs=temp2

    temp=settingsStore[1]
    temp=temp.replace(']','')
    temp=temp.replace('[','')
    temp=temp.replace("'","")
    temp=temp.split(':')
    temp2=temp[1].split(",")
    otherDirs=temp2

    temp=settingsStore[2]
    temp=temp.replace(']','')
    temp=temp.replace('[','')
    temp=temp.replace("'","")
    temp=temp.split(':')
    userEmail=temp[1]

    returner=[]
    returner.append(steamDirs)
    returner.append(otherDirs)
    returner.append(userEmail)
    return returner

################################################################################

################################################################################
#Local Games processing Code
################################################################################

def onDisk(settingStore2):
    while 2==2:
        print("Feature is not complete.")
        break

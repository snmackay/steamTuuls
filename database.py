import csv
import os
import time
import sys
import urllib.request, json
import requests
from os import path
from pathlib import Path
import math

import galaxy
import ui


################################################################################
"""
Create Steam Database csv
"""
################################################################################

def drmListOpen():
    lines=[]
    with open("dataBases/steam_drm_free.txt",'r') as fp:
        line=fp.readline()
        count=1
        while line:
            line.rstrip()
            lines.append(line)
            line=fp.readline()
            count+=1
    print(ui.pcol.G + "Parsed drm free games." + ui.pcol.ENDC)
    cleanedList=listCleaner(lines)
    cleanedList=listOrganize(cleanedList)
    print(ui.pcol.G + "Data has been cleaned" + ui.pcol.ENDC)
    return cleanedList

def listCleaner(drmList):
    cleanedList=[]
    for line in drmList:
        if line[0]=='|' and len(line) >4:
            if line[len(line)-3] != '|':
                cleanedList.append(line)

    cleanedList2=[]
    temp=[]
    while len(cleanedList)!= 0:
        top=cleanedList.pop()
        if(top[1]=='[' and top[2]=='[' and len(temp)!=0):
            cleanedList2.append(temp)
            temp=[]
            temp.append(top)

        elif(top[1]=='[' and top[2]=='['):
            temp=[]
            temp.append(top)

        elif(top[1]=='s' or top[1]=='S'):
            temp.append(top)

    cleanedList3=[]
    for i in cleanedList2:
        temp=[]
        for j in i:
            tempInner=j.rstrip()
            tempInner=tempInner.replace("|","")
            tempInner=tempInner.replace("[","")
            tempInner=tempInner.replace("]","")
            tempInner=tempInner.replace("{","")
            tempInner=tempInner.replace("}","")
            tempInner=tempInner.replace("style=\"text-align: center;\"","")
            tempInner=tempInner.replace("style=\"text-align:center;\"","")
            tempInner=tempInner.replace("linkSteam","")
            tempInner=tempInner.replace("store ","")
            temp.append(tempInner)
        cleanedList3.append(temp)

    return cleanedList3

def listOrganize(cleanedList):
    newList=[]

    for i in cleanedList:
        temp=[]
        numElems=len(i)
        temp.append("NAME: "+i[0])
        i[numElems-1]=i[numElems-1].replace("Link","")
        temp.append("STEAMID: "+i[numElems -1])
        if(numElems==3):
            if("style=" not in i[1]):
                temp.append("NOTES: "+ i[1])
        elif(numElems==4):
            if("style=" not in i[1]):
                temp.append("NOTES: "+ i[1])
            elif("style=" not in i[2]):
                temp.append("NOTES: "+ i[2])
        newList.append(temp)

    return newList


################################################################################
"""
Code for parsing GOG database of Games
"""
################################################################################

def processGog():
    os.system('cls' if os.name == 'nt' else 'clear')
    outer=[]
    counter=1
    while counter<90:
        url= "https://www.gog.com/games/ajax/filtered?mediaType=game&page="+str(counter)+"&sort=popularity"

        time.sleep(2)

        r = requests.get(url)
        a = r.json()
        for each in a['products']:
            del each['gallery']
            del each['video']
            del each['image']
            del each['url']
            del each['supportUrl']
            del each['forumUrl']
            del each['type']
            del each['isWishlistable']
            del each['slug']
            del each['isMovie']
            del each['isGame']
            del each['salesVisibility']
            del each['customAttributes']
            del each['developer']
            del each['rating']
        outer.append(a['products'])
        print(ui.pcol.G + "Pages Handled: " + ui.pcol.ENDC + str(counter))
        counter+=1
    dbGen(outer)

def dbGen(contents):
    list=[]
    for i in contents: #j is a dict. Parse assuming this now.
        for j in i:
            list.append(j)

    keys=list[0].keys()
    with open('dataBases/GOG.csv','w',newline='') as output_file:
        dict_writer=csv.DictWriter(output_file,keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)
    print(ui.pcol.G + "Database has been generated." + ui.pcol.ENDC)
    time.sleep(3)


################################################################################
"""
Local Games processing Code
"""
################################################################################

def generateDB():
    os.system('cls' if os.name == 'nt' else 'clear')
    ui.picPrint("Loading in GOG Galaxy DB")
    print(ui.pcol.Blank)
    try:
        os.system('python3 galaxy.py -a')
        time.sleep(2)
    except:
        print(ui.pcol.R + "file was not generated correctly.")
        print(ui.pcol.Y + "Please copy the file 'galaxy-2.0.db' from:")
        print(ui.pcol.G + "C:\\ProgramData\\GOG.com\\Galaxy\\storage\\galaxy-2.0.db" + ui.pcol.ENDC )
    else:
        print(ui.pcol.G + "database of games in GOG Galaxy 2 launcher completed creation" + ui.pcol.ENDC)
    time.sleep(5)



################################################################################
"""
Code for opening database files generated.
"""
################################################################################
def gogOpen():
    with open('dataBases/GOG.csv') as f:
        a = [{k: str(v) for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]
    return a


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

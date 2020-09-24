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
###############################################################################
#Create Steam Database csv
#passed argv: steamDB -DEPRICATED
###############################################################################

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
    print("Parsed drm free games.")
    cleanedList=listCleaner(lines)
    cleanedList=listOrganize(cleanedList)
    print("Data has been cleaned")
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

###############################################################################

###############################################################################
#Code for parsing GOG database of Games
#arg = gogDB
###############################################################################

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
        print("Pages Handled: "+str(counter))
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
    print("Database has been generated.")
    time.sleep(3)

################################################################################

################################################################################
#Local Games processing Code
################################################################################

def generateDB():
    os.system('cls' if os.name == 'nt' else 'clear')
    ui.picPrint("Loading in GOG Galaxy DB")
    print("_____________________________________________________________________________")
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

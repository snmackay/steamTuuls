import csv
import os
import time
import sys
import urllib.request, json
import requests
from os import path
#from pathlib import Path
import math

from lib import galaxy
from lib import ui


################################################################################
"""
Create Steam Database csv
"""
################################################################################

def processDrm():
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
    cleaned_list=listCleaner(lines)
    print(ui.pcol.G + "Data has been cleaned" + ui.pcol.ENDC)
    createListCsv(cleaned_list,"dataBases/SteamDRMFree.csv")

def listCleaner(drm_list):
    cleaned_list=[]
    for line in drm_list:
        if line[0]=='|' and len(line) >4:
            if line[len(line)-3] != '|':
                cleaned_list.append(line)

    cleaned_list_2=[]
    temp=[]
    while len(cleaned_list)!= 0:
        top=cleaned_list.pop()
        if(top[1]=='[' and top[2]=='[' and len(temp)!=0):
            cleaned_list_2.append(temp)
            temp=[]
            temp.append(top)

        elif(top[1]=='[' and top[2]=='['):
            temp=[]
            temp.append(top)

        elif(top[1]=='s' or top[1]=='S'):
            temp.append(top)

    cleaned_list_3=[]
    for i in cleaned_list_2:
        temp=[]
        for j in i:
            inner=j.rstrip()
            inner=inner.replace("|","")
            inner=inner.replace("[","")
            inner=inner.replace("]","")
            inner=inner.replace("{","")
            inner=inner.replace("}","")
            inner=inner.replace("style=\"text-align: center;\"","")
            inner=inner.replace("style=\"text-align:center;\"","")
            inner=inner.replace("linkSteam","")
            inner=inner.replace("store ","")
            temp.append(inner)
        cleaned_list_3.append(temp)

    new_list=[]

    for i in cleaned_list_3:
        temp=[]
        num_elems=len(i)
        temp.append("NAME: "+i[0])
        i[num_elems-1]=i[num_elems-1].replace("Link","")
        temp.append("STEAMID: "+i[num_elems -1])
        if(num_elems==3):
            if("style=" not in i[1]):
                temp.append("NOTES: "+ i[1])
        elif(num_elems==4):
            if("style=" not in i[1]):
                temp.append("NOTES: "+ i[1])
            elif("style=" not in i[2]):
                temp.append("NOTES: "+ i[2])
        new_list.append(temp)

    return new_list


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

    #clean up and create database
    list=[]
    for i in outer: #j is a dict.
        for j in i:
            list.append(j)
    createDictCsv(list,'dataBases/GOG.csv')
    print(ui.pcol.G + "Database has been generated." + ui.pcol.ENDC)
    time.sleep(3)


################################################################################
"""
Local Games processing Code
"""
################################################################################

def processLib():
    os.system('cls' if os.name == 'nt' else 'clear')
    ui.picPrint("Loading in GOG Galaxy DB")
    print(ui.pcol.Blank)
    try:
        os.system('python3 lib/galaxy.py -a')
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
Code for opening/writing database csv's
"""
################################################################################
def createDictCsv(list,file_name):
    keys=list[0].keys()
    with open(file_name,'w',newline='') as f:
        dict_writer=csv.DictWriter(f,keys)
        dict_writer.writeheader()
        dict_writer.writerows(list)

def openDictCsv():
    with open('dataBases/GOG.csv') as f:
        a = [{k: str(v) for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]
    return a

def createListCsv(cleanedList,fileName):
    with open(fileName, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(cleanedList)

def openListCsv(file_name):
    with open(file_name) as f:
        csv_reader = csv.reader(f, delimiter=',')
        list=[]
        for row in csv_reader:
            list.append(row)
    return list

def createTextFile(file_name,listy):
    with open(file_name, 'w') as f:
        for item in listy:
            f.write('%s\n' % item)

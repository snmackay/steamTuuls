import os
from os import path
import csv
import sys
from pathlib import Path
import time
import math

import galaxy

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

def generateDB():
    try:
        os.system('python3 galaxy.py -a')
        time.sleep(2)
        path.exists("dataBases\gameDB.csv")
    except:
        print("file was not generated correctly.")
        print("Please copy the file 'galaxy-2.0.db' from:")
        print("C:\\ProgramData\\GOG.com\\Galaxy\\storage\\galaxy-2.0.db")
    else:
        print("database of games in GOG Galaxy 2 launcher completed creation")

################################################################################

################################################################################
#Code for querying the local games data from GOG Galaxy 2.0
################################################################################

def queryDB(opened_data):
    while 2==2:
        print(" ")
        print("________________________________________________________________")
        print(" ")
        print("Usage commands:")
        print("e: 'title' -do you own the game")
        print("s: 'title' -view your stats for the game.")
        print("p: 'title' -what platforms is the game on.")
        print("t: 'total' -gives you total time played ever")
        #print("n: 'steam' -gives you number of and list of games you own on steam")
        #print("n: 'epic' -gives you number of and list of games you own on Epic")
        #print("n: 'playstation' -gives you number of and list of games you own on Playstation")
        #print("n: 'gog' -gives you number of and list of games you own on GOG")
        print("back -returns you back.")

        text=input("Response: ")

        if text=="back":
            break
        else:
            try:
                text=text.split(": ")
                command=text[0]
                game=text[1]
            except:
                print("Command not valid. Try again")
            else:
                bool=0

                for i in opened_data:
                    if command=="t":
                        print(timeHelp(opened_data))
                        bool=1
                        break
                    elif command =="n":
                        platformHelp(opened_data,game)
                        bool=1
                        break

                    elif game in i[0]:
                        bool=1
                        if command=="e":
                            print("You own this game!")
                        elif command=="s":
                            print("Summary:")
                            print(i[1])
                            print("")
                            print("Platform:")
                            print(i[2])
                            print("")
                            print("Time Played:")
                            print(i[9])
                        elif command=="p":
                            print("Time Played:")
                            print(i[9])

                if bool==0:
                    print("You dont own this game.")

def timeHelp(opened_data):
    sum=0
    for i in opened_data:
        try:
            sum+=int(i[9])
        except:
            sum+=0

    hours,mins=divmod(float(sum),60)
    return("Hours:"+str(hours)+" Minutes:"+str(mins))

def platformHelp(opened_data,game):
    sum=0
    platform=""
    if game=="steam":
        platform="['Steam']"
    elif game=="epic":
        platform="['Epic Games Store']"
    elif game=="playstation":
        platform="['PlayStation Network']"
    #elif game=="gog":

    #for i in opened_data:

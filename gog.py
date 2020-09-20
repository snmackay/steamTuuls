import os
import csv
import sys
import urllib.request, json
import requests
import time

###############################################################################
#Code for parsing GOG database of GameS
#arg = gogDB
###############################################################################

def processGog():
    outer=[]
    counter=1
    while counter<90:
        url= "https://www.gog.com/games/ajax/filtered?mediaType=game&page="+str(counter)+"&sort=popularity"

        time.sleep(2)

        r = requests.get(url)
        a = r.json()
        for each in a['products']:
            #print(each)
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
        print(counter)
        counter+=1
    return outer

def createRaw(rawdb):
    f= open('dataBases/rawFile.txt','w')
    for i in rawdb:
        f.write(str(i))
    f.close()
    print("Raw file generated")

def readRaw():
    f = open('dataBases/rawfile.txt','r')
    returner=f.read()
    #print(returner)
    return returner

def cleaner(contents):
    print(type(contents))
    list=contents.split("{'publisher': ")
    #print(list[1])
    temp1=[]
    for i in list:
        inner=i.split(", ")
        temp1.append(inner)

    temp2=[]
    temp1.pop(0)
    #print(temp1[0])
    for i in temp1:
        inner=[]
        wow=i[0]
        wow=wow.replace("'","")
        inner.append(wow)
        for j in i:
            k=j.replace("'","")
            if 'supportedOperatingSystems' in k:
                inner.append(k)
            elif 'globalReleaseDate' in k:
                inner.append(k)
            elif 'isTBA' in k:
                inner.append(k)
            elif 'baseAmount' in k:
                inner.append(k)
            elif 'finalAmount' in k:
                inner.append(k)
            elif 'discountDifference' in k:
                inner.append(k)
            elif 'title' in k:
                inner.append(k)
        temp2.append(inner)

    temp3=[]
    for i in temp2:
        inner=[]
        inner.append(i[7])
        inner.append(i[0])
        inner.append(i[5])
        inner.append(i[4])
        inner.append(i[6])
        inner.append(i[1])
        inner.append(i[2])
        inner.append(i[3])
        temp3.append(inner)
    #print(temp3[0])

    temp4=[]
    for i in temp3:
        inner=[]
        counter=0
        for j in i:
            if counter==1:
                inner.append(j)
            else:
                tempy=j.split(": ")
                inner.append(tempy[1])
            counter+=1
        temp4.append(inner)
    #print(temp4[1])
    print("Data has been cleaned")
    return temp4

#0 - Title
#1 - Publisher
#2 - finalAmount
#3 - baseAmount
#4 - discountDifference
#5 - supportedOperatingSystems
#6 - globalReleaseDate
#7 - isTBA

###############################################################################

###############################################################################
#code for checking if a game is on GOG
#arg = onGog
###############################################################################

def selectAction(fetchedGogDB):
    while 0==0:
        print(" ")
        print("________________________________________________________________")
        print(" ")
        print("Type 'on gog' for if Gog has the game.")
        print("Type 'on sale' for a list of games with a reduced price")
        print("Type 'back' to go back to the main menu.")
        text=input("Response: ")
        if text =="on gog":
            exists(fetchedGogDB)

        elif text =="on sale":
            gamesOnSale(fetchedGogDB)
        elif text== "back":
            break
        else:
            print("Not a valid input. Please try again.")


def exists(fetchedGogDB):
    text=input("Type in the name of a game: ")
    boo=0
    for i in fetchedGogDB:
        if text in i[0]:
            print("Game is on GOG")
            print(i)
            boo=1
    if(boo==0):
        print("The game you typed in: [ "+ text + " ] is not on GOG rip :(")

def gamesOnSale(fetchedGogDB):
    for i in fetchedGogDB:
        if float(i[4])!=0.00:
            print(i[0] + " : " + i[4])

###############################################################################

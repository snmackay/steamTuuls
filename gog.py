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
    os.system("clear")
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

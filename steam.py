import csv
import os
import pprint
import help
import time

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
#Check if the game passed is in the steam drm free list
#argv = steamdrm? -DEPRICATED
###############################################################################



def exists(fetchedSteamDB):
    os.system("clear")
    while 2==2:
        print(" ")
        print("_____________________________________________________________________________")
        print(" ")
        print("Type "+help.pcol.B+'chk' +help.pcol.ENDC+" to see if the game on steam has drm.")
        print("Type "+help.pcol.B+'bk' +help.pcol.ENDC+" to go back to the main menu.")
        text=input("Response: ")
        os.system("clear")
        if text == "chk":
            while 2==2:
                boo=0
                print(" ")
                print("_____________________________________________________________________________")
                print(" ")
                print("Type in the name of the game to check if its drm free.")
                print("Type "+help.pcol.B+'bk' +help.pcol.ENDC+ " to go back.")
                text1=input("Response: ")
                os.system("clear")
                if text1 =="bk":
                    os.system("clear")
                    break
                else:
                    for i in fetchedSteamDB:
                        if text1 in i[0]:
                            print(" ")
                            print(" ")
                            print(help.pcol.G+"    Game is DRM Free: "+help.pcol.ENDC+i[0]+" " +i[1])
                            if(len(i)>2):
                                print(help.pcol.Y+"    "+i[2]+help.pcol.ENDC)
                            boo=0
                            break
                        else:
                            boo=1
                    if(boo==1):
                        print(help.pcol.R+"The game you typed in: [ "+ text1 + " ] is not drm free."+help.pcol.ENDC)

        elif text == "bk":
            os.system("clear")
            break
        else:
            print(help.pcol.R+"Not a valid command, please try again."+help.pcol.ENDC)

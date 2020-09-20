import csv
import os

###############################################################################
#Create Steam Database csv
#passed arg: steamDB
###############################################################################
def drmListOpen():
    lines=[]
    with open("dataBases/steam_drm_free.txt",'r') as fp:
        line=fp.readline()
        count=1
        while line:
            line.rstrip()
            lines.append(line)
            #print(line)
            line=fp.readline()
            count+=1
    return lines

def listCleaner(drmList):
    cleanedList=[]
    for line in drmList:
        #print(line)
        if line[0]=='|' and len(line) >4:
            if line[len(line)-3] != '|':
                cleanedList.append(line)
                #print(line)

    cleanedList2=[]
    counter=0
    counter2=0
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
            #tempInner=tempInner.replace("\"style=\"\"text-align: center;\"\"","")
            tempInner=tempInner.replace("linkSteam","")
            tempInner=tempInner.replace("store ","")
            temp.append(tempInner)
        cleanedList3.append(temp)

    #for i in cleanedList3:
        #print(i)
    return cleanedList3

def listOrganize(cleanedList):
    newList=[]

    for i in cleanedList:
        temp=[]
        numElems=len(i)
        temp.append("NAME: "+i[0])
        i[numElems-1]=i[numElems-1].replace("Link","")
        temp.append("STEAMID: "+i[numElems -1])
        #print(temp)
        if(numElems==3):
            if("style=" not in i[1]):
                temp.append("NOTES: "+ i[1])
        elif(numElems==4):
            if("style=" not in i[1]):
                temp.append("NOTES: "+ i[1])
            elif("style=" not in i[2]):
                temp.append("NOTES: "+ i[2])
        newList.append(temp)

    #for i in newList:
        #print(i)
    return newList

###############################################################################



###############################################################################
#Check if the game passed is in the steam drm free list
#arg = steamdrm?
###############################################################################

def exists(fetchedSteamDB):
    while 2==2:
        print(" ")
        print("________________________________________________________________")
        print(" ")
        print("Type 'check' to see if the game on steam has drm")
        print("Type 'back' to go back to the main menu")
        text=input("Response: ")
        if text == "check":
            while 2==2:
                boo=0
                print(" ")
                print("________________________________________________________________")
                print(" ")
                print("Type in the name of the game to check if its drm free.")
                print("Type 'back' to go back")
                text1=input("Response: ")
                if text1 =="back":
                    break
                else:
                    for i in fetchedSteamDB:
                        if text1 in i[0]:
                            print("Game is DRM Free")
                            print(i)
                            boo=0
                            break
                        else:
                            boo=1
                    if(boo==1):
                        print("The game you typed in: [ "+ text + " ] is not drm free")

        elif text == "back":
            break
        else:
            print("Not a valid command, try again.")

import random
import os
import time

class pcol:
    P = '\033[95m'
    B = '\033[94m'
    G = '\033[92m'
    Y = '\033[93m'
    R = '\033[91m'
    C = '\u001b[36m'
    M = '\u001b[35m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UL = '\033[4m'
    BW = '\u001b[47m'
    BB = '\u001b[40m'
    BY = '\u001b[43;1m'
    BG = '\u001b[42;1m'
    Reset = '\u001b[0m'

    Blank = UL + "                                                                           " + Reset


    """
    Background Bright Black: \u001b[40;1m
    Background Bright Red: \u001b[41;1m
    Background Bright Green: \u001b[42;1m
    Background Bright Yellow: \u001b[43;1m
    Background Bright Blue: \u001b[44;1m
    Background Bright Magenta: \u001b[45;1m
    Background Bright Cyan: \u001b[46;1m
    Background Bright White: \u001b[47;1m
    """

    """
    P = purple
    B = blue
    G = green
    Y = yellow
    R = red
    C = cyan
    M = magenta
    """

#random colour selector
#for da memz
def randomColour():
    rando=random.randint(1,7)
    if rando == 1:
        colo=pcol.P
    elif rando ==2:
        colo=pcol.B
    elif rando ==3:
        colo=pcol.G
    elif rando ==4:
        colo=pcol.Y
    elif rando ==5:
        colo=pcol.R
    elif rando ==6:
        colo=pcol.C
    else:
        colo=pcol.M
    return colo

def playAudio(file):
    os.system("mpg123 " + file)
    time.sleep(50)


#picture for menus
def picPrint(passed):
    colo=randomColour()
    print(pcol.Y+passed+pcol.ENDC)
    print(" ")
    print(colo )
    print("                           ueeeeeu..                                  ")
    print("  "+"                ur d$$$$$$$$$$$$$$Nu                            ")
    print("  "+"              d$$$ \"$$$$$$$$$$$$$$$$$$e.                       ")
    print("  "+"          u$$c   \"\"   ^\"^**$$$$$$$$$$$$$b.                   ")
    print("  "+"        z$$#\"\"\"           `!?$$$$$$$$$$$$$N.                 ")
    print("  "+"      .$P                   ~!R$$$$$$$$$$$$$b                   ")
    print("  "+"     x$F                 **$b. '\"R).$$$$$$$$$$                 ")
    print("  "+"    J^\"                           #$$$$$$$$$$$$.               ")
    print("  "+"   z$e                      ..      \"**$$$$$$$$$               ")
    print("  "+"  :$P           .        .$$$$$b.    ..  \"  #$$$$              ")
    print("  "+"  $$            L          ^*$$$$b   \"      4$$$$L             ")
    print("  "+" 4$$            ^u    .e$$$$e.\"*$$$N.       @$$$$$             ")
    print("  "+" $$E            d$$$$$$$$$$$$$$L \"$$$$$  mu $$$$$$F            ")
    print("  "+" $$&            $$$$$$$$$$$$$$$$N   \"#* * ?$$$$$$$N            ")
    print("  "+" $$F            '$$$$$$$$$$$$$$$$$bec...z$ $$$$$$$$             ")
    print("  "+"'$$F             `$$$$$$$$$$$$$$$$$$$$$$$$ '$$$$E\"$            ")
    print("  "+" $$                  ^\"\"\"\"\"\"`       ^\"*$$$& 9$$$$N       ")
    print("  "+" k  u$                                  \"$$. \"$$P r           ")
    print("  "+" 4$$$$L                                   \"$. eeeR             ")
    print("  "+"  $$$$$k                                   '$e. .@              ")
    print("  "+"  3$$$$$b                                   '$$$$               ")
    print("  "+"   $$$$$$                                    3$$\"              ")
    print("  "+"    $$$$$  dc                                4$F                ")
    print("  "+"     RF** <$$                                J\"                ")
    print("  "+"      #bue$$$LJ$$$Nc.                        \"                 ")
    print("  "+"       ^$$$$$$$$$$$$$r                                          ")
    print("  "+"         `\"*$$$$$$$$$                                          ")
    print(pcol.ENDC)

#main menu UI
def mainMenu():
    print(pcol.Blank)
    print(" ")
    print(" ")
    print(pcol.P + "Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "sdb" + pcol.ENDC + " - generate database file for drm free steam games.")
    print(pcol.B + "gdb" + pcol.ENDC + " - generate the GOG games database.")
    print(pcol.B + "galdb" + pcol.ENDC + " - generate database from your GOG Galaxy 2 library.")
    print(" ")
    print(pcol.B + "sdrm" + pcol.ENDC + " - check if a steam game has drm.")
    print(pcol.B + "gog" + pcol.ENDC + " - interact with GOG store database.")
    print(pcol.B + "galax" + pcol.ENDC + " - interact with your GOG Galaxy 2 library.")
    print(pcol.B + "print" + pcol.ENDC + " - use the file print menu.")
    print(pcol.B + "quit" + pcol.ENDC + " - exit SteamTuuls.")
    text=input(": ")
    print(pcol.Blank)
    print(" ")
    return text

#Code for the gog store query menu. Called from gog.py second half
def gogQueryMenu():
    print(" ")
    print(pcol.Blank)
    print(" ")
    print(pcol.P+"Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "look" + pcol.ENDC + " - look up a game on GOG.")
    print(pcol.B + "sale" +pcol.ENDC +" - returns list of games on sale on GOG.")
    print(pcol.B + "bk" + pcol.ENDC + " - return to main menu.")
    text=input(": ")
    return text

#UI for gog store search
def gogGameSearch(i,inner):
    print(pcol.Blank)
    print(pcol.G + "Game is on GOG: " + pcol.Y + i["title"])
    print(pcol.G + "Developer: " + pcol.Y + i["publisher"])
    print(pcol.G + "Price: " + pcol.Y + inner +pcol.ENDC)


#code for GOG Galaxy library queries. Called from library.py
def libraryUI():
    print(" ")
    print(pcol.Blank)
    print(" ")
    print(pcol.P + "Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "e: 'title'" + pcol.ENDC + " - see if you own 'title'.")
    print(pcol.B + "s: 'title'" + pcol.ENDC + " - view your stats for 'title'.")
    print(pcol.B + "t: 'total'" + pcol.ENDC + " - gives you total time played ever.")
    print(pcol.B + "p: 'platform'" + pcol.ENDC + " - prints a list of all games on 'platform'.")
    print(pcol.B + "d: 'dupe'" + pcol.ENDC + " - prints list of games you have multiple times and the platforms.")
    print(" ")
    print(pcol.B + "print" + pcol.ENDC + " - takes you to menu to print out various library query results.")
    print(pcol.B + "bk" + pcol.ENDC + " - returns you back.")
    text=input(": ")
    return text


#UI function called from logic.py line 188
def galaxyUI(i):
    print(pcol.G + "Title: " + pcol.Y + i[0] + pcol.ENDC)
    print(pcol.G + "Summary: " + pcol.Y + i[1] + pcol.ENDC)
    print(pcol.G + "Platform: " + pcol.Y + i[2][2:-2] + pcol.ENDC)
    if(i[9]==""):
        print(pcol.G + "Time Played: " + pcol.Y + "0 minutes." + pcol.ENDC)
    else:
        print(pcol.G + "Time Played: " + pcol.Y + i[9] + " minutes." + pcol.ENDC)
    print("")
    print("")

#UI function for print menu from main menu.
def printUI():
    print(" ")
    print(pcol.Blank)
    print(" ")
    print(pcol.P + "Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "drmFree" + pcol.ENDC + " - generates a text file of all steam games you own that are drm free.")
    print(pcol.B + "'platform'" + pcol.ENDC + " - generates a text file of all games on 'platform' -e.g. 'steam'.")
    print(pcol.B + "duplicates" + pcol.ENDC + " - generates a text file of all games on 'platform' -e.g. 'steam'.")
    print(pcol.B + "bk" + pcol.ENDC + " - return to main menu.")
    text=input(": ")
    return text

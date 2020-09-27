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

    P = purple
    B = blue
    G = green
    Y = yellow
    R = red
    C = cyan
    M = magenta
    UL = underline
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
    print("                   " + pcol.Y+passed+pcol.ENDC)
    print(" ")
    print(colo )
    print("                           ueeeeeu..                                  ")
    print("     "+"                ur d$$$$$$$$$$$$$$Nu                            ")
    print("     "+"              d$$$ \"$$$$$$$$$$$$$$$$$$e.                       ")
    print("     "+"          u$$c   \"\"   ^\"^**$$$$$$$$$$$$$b.                   ")
    print("     "+"        z$$#\"\"\"           `!?$$$$$$$$$$$$$N.                 ")
    print("     "+"      .$P                   ~!R$$$$$$$$$$$$$b                   ")
    print("     "+"     x$F                 **$b. '\"R).$$$$$$$$$$                 ")
    print("     "+"    J^\"                           #$$$$$$$$$$$$.               ")
    print("     "+"   z$e                      ..      \"**$$$$$$$$$               ")
    print("     "+"  :$P           .        .$$$$$b.    ..  \"  #$$$$              ")
    print("     "+"  $$            L          ^*$$$$b   \"      4$$$$L             ")
    print("     "+" 4$$            ^u    .e$$$$e.\"*$$$N.       @$$$$$             ")
    print("     "+" $$E            d$$$$$$$$$$$$$$L \"$$$$$  mu $$$$$$F            ")
    print("     "+" $$&            $$$$$$$$$$$$$$$$N   \"#* * ?$$$$$$$N            ")
    print("     "+" $$F            '$$$$$$$$$$$$$$$$$bec...z$ $$$$$$$$             ")
    print("     "+"'$$F             `$$$$$$$$$$$$$$$$$$$$$$$$ '$$$$E\"$            ")
    print("     "+" $$                  ^\"\"\"\"\"\"`       ^\"*$$$& 9$$$$N       ")
    print("     "+" k  u$                                  \"$$. \"$$P r           ")
    print("     "+" 4$$$$L                                   \"$. eeeR             ")
    print("     "+"  $$$$$k                                   '$e. .@              ")
    print("     "+"  3$$$$$b                                   '$$$$               ")
    print("     "+"   $$$$$$                                    3$$\"              ")
    print("     "+"    $$$$$  dc                                4$F                ")
    print("     "+"     RF** <$$                                J\"                ")
    print("     "+"      #bue$$$LJ$$$Nc.                        \"                 ")
    print("     "+"       ^$$$$$$$$$$$$$r                                          ")
    print("     "+"         `\"*$$$$$$$$$                                          ")
    print(pcol.ENDC)

################################################################################
#main menu UI
#called from main.py line 25
def mainMenu():
    print(pcol.Blank)
    print(" ")
    print(" ")
    print(pcol.P + "Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "1" + pcol.ENDC + " - generate database file for drm free steam games.")
    print(pcol.B + "2" + pcol.ENDC + " - generate the GOG games database.")
    print(pcol.B + "3" + pcol.ENDC + " - generate database from your GOG Galaxy 2 library.")
    print(" ")
    print(pcol.B + "s" + pcol.ENDC + " - check if a steam game has drm.")
    print(pcol.B + "g" + pcol.ENDC + " - interact with GOG store database.")
    print(pcol.B + "l" + pcol.ENDC + " - interact with your GOG Galaxy 2 library.")
    print(pcol.B + "p" + pcol.ENDC + " - use the file print menu.")
    print(pcol.B + "q" + pcol.ENDC + " - exit SteamTuuls.")
    text=input(": ")
    print(pcol.Blank)
    print(" ")
    return text

################################################################################
#steam drm main menu
#called from logic.py line 26
def drmMenuUI():
    picPrint("Steam DRM Menu.")
    print(" ")
    print(pcol.Blank)
    print(" ")
    print(pcol.B + 'c' + pcol.ENDC + " - check if your steam game has drm.")
    print(pcol.B + 'b' + pcol.ENDC + " - go back to the main menu.")
    text=input(": ")
    return text

#check if game title has drm menu
#called from logic.py line 34
def drmCheckMenu():
    picPrint("Game DRM Checker")
    print(" ")
    print(pcol.Blank)
    print(" ")
    print(pcol.P + "Type in the name of the game to check if its drm free." + pcol.ENDC)
    print(pcol.B+'b' +pcol.ENDC+ " - go back to previous menu.")
    text=input(": ")
    return text

################################################################################
#Code for the gog store query menu. Called from gog.py second half
#called from logic.py line 75
def gogMenuUI():
    picPrint("GOG Store Page")
    print(" ")
    print(pcol.Blank)
    print(" ")
    print(pcol.P+"Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "l" + pcol.ENDC + " - look up a game on GOG.")
    print(pcol.B + "s" + pcol.ENDC + " - returns list of games on sale on GOG.")
    print(pcol.B + "g" + pcol.ENDC + " - returns list of games in a chosen genre (feature buggy).")
    print(pcol.B + "b" + pcol.ENDC + " - return to main menu.")
    text=input(": ")
    return text

#UI for gog store search (called from logic.gogSells())
#called from logic.py line 101
def gogGameSearch(i,inner):
    print(pcol.Blank)
    print(pcol.G + "Game is on GOG: " + pcol.Y + i["title"])
    print(pcol.G + "Developer: " + pcol.Y + i["publisher"])
    print(pcol.G + "Price: " + pcol.Y + inner +pcol.ENDC)

#UI for finding all games matching a specific genre.
#called from logic.gogGenre() line 142
def genreUI():
    picPrint("Genre Select Menu.")
    print(pcol.Blank)
    print(pcol.P + "Type in a genre. Here are some." + pcol.ENDC)
    print(pcol.Blank)
    print(pcol.B + "Action" + pcol.ENDC)
    print(pcol.B + "Shooter" + pcol.ENDC)
    print(pcol.B + "Role-playing" + pcol.ENDC)
    print(pcol.B + "Adventure" + pcol.ENDC)
    print(pcol.B + "Racing" + pcol.ENDC)
    print(pcol.B + "Strategy" + pcol.ENDC)
    print(pcol.B + "Simulation" + pcol.ENDC)
    text=input(": ")
    return text

################################################################################
#code for GOG Galaxy library queries. Called from logic.galaxyMenu()
#line 174
def galaxyMenuUI():
    picPrint("Games Library Viewer.")
    print(" ")
    print(pcol.Blank)
    print(" ")
    print(pcol.P + "Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "e: 'title'" + pcol.ENDC + " - see if you own 'title'.")
    print(pcol.B + "s: 'title'" + pcol.ENDC + " - view your stats for 'title'.")
    print(pcol.B + "t" + pcol.ENDC + " - gives you total time played ever.")
    print(pcol.B + "r" + pcol.ENDC + " - finds you a random good game to play.")
    print(pcol.B + "p: 'platform'" + pcol.ENDC + " - prints a list of all games on 'platform'.")
    print(pcol.B + "d: 'dupe'" + pcol.ENDC + " - prints list of games you have multiple times and the platforms.")
    print(pcol.B + "b" + pcol.ENDC + " - returns you back.")
    text=input(": ")
    return text

#UI function called from logic.py line 207
def statsUI(i):
    print(pcol.G + "Title: " + pcol.Y + i[0] + pcol.ENDC)
    print(pcol.G + "Summary: " + pcol.Y + i[1] + pcol.ENDC)
    print(pcol.G + "Platform: " + pcol.Y + i[2][2:-2] + pcol.ENDC)
    if(i[9]==""):
        print(pcol.G + "Time Played: " + pcol.Y + "0 minutes." + pcol.ENDC)
    else:
        print(pcol.G + "Time Played: " + pcol.Y + i[9] + " minutes." + pcol.ENDC)
    print("")
    print("")

################################################################################
#UI function for print menu from main menu.
#called from printMenu() line 321
def printUI():
    picPrint("Print Menu.")
    print(" ")
    print(pcol.Blank)
    print(" ")
    print(pcol.P + "Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "'platform'" + pcol.ENDC + " - generates a text file of all games on 'platform' -e.g. 'steam'.")
    print(pcol.B + "f" + pcol.ENDC + " - generates a text file of all steam games you own that are drm free.")
    print(pcol.B + "d" + pcol.ENDC + " - generates a text file of all games on 'platform' -e.g. 'steam'.")
    print(pcol.B + "b" + pcol.ENDC + " - return to main menu.")
    text=input(": ")
    return text

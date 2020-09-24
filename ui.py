class pcol:
    P = '\033[95m'
    B = '\033[94m'
    G = '\033[92m'
    Y = '\033[93m'
    R = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#P = purple
#B = blue
#G = green
#Y = yellow
#R = red

def picPrint(passed):
    print(pcol.Y+passed+pcol.ENDC)
    print(" ")
    print(" ")
    print(pcol.R+"                       ueeeeeu..")
    print("  "+"                ur d$$$$$$$$$$$$$$Nu")
    print("  "+"              d$$$ \"$$$$$$$$$$$$$$$$$$e.")
    print("  "+"          u$$c   \"\"   ^\"^**$$$$$$$$$$$$$b.")
    print("  "+"        z$$#\"\"\"           `!?$$$$$$$$$$$$$N.")
    print("  "+"      .$P                   ~!R$$$$$$$$$$$$$b")
    print("  "+"     x$F                 **$b. '\"R).$$$$$$$$$$")
    print("  "+"    J^\"                           #$$$$$$$$$$$$.")
    print("  "+"   z$e                      ..      \"**$$$$$$$$$")
    print("  "+"  :$P           .        .$$$$$b.    ..  \"  #$$$$")
    print("  "+"  $$            L          ^*$$$$b   \"      4$$$$L")
    print("  "+" 4$$            ^u    .e$$$$e.\"*$$$N.       @$$$$$")
    print("  "+" $$E            d$$$$$$$$$$$$$$L \"$$$$$  mu $$$$$$F")
    print("  "+" $$&            $$$$$$$$$$$$$$$$N   \"#* * ?$$$$$$$N")
    print("  "+" $$F            '$$$$$$$$$$$$$$$$$bec...z$ $$$$$$$$")
    print("  "+"'$$F             `$$$$$$$$$$$$$$$$$$$$$$$$ '$$$$E\"$")
    print("  "+" $$                  ^\"\"\"\"\"\"`       ^\"*$$$& 9$$$$N")
    print("  "+" k  u$                                  \"$$. \"$$P r")
    print("  "+" 4$$$$L                                   \"$. eeeR")
    print("  "+"  $$$$$k                                   '$e. .@")
    print("  "+"  3$$$$$b                                   '$$$$")
    print("  "+"   $$$$$$                                    3$$\"")
    print("  "+"    $$$$$  dc                                4$F")
    print("  "+"     RF** <$$                                J\"")
    print("  "+"      #bue$$$LJ$$$Nc.                        \"")
    print("  "+"       ^$$$$$$$$$$$$$r")
    print("  "+"         `\"*$$$$$$$$$")
    print(pcol.ENDC)

def mainMenu():
    print("_____________________________________________________________________________")
    print(" ")
    print(pcol.P + "Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "sdb" + pcol.ENDC + " - access generate database file.")
    print(pcol.B + "gdb" + pcol.ENDC + " - generate the GOG games database.")
    print(pcol.B + "galdb" + pcol.ENDC + " - generate database from your GOG Galaxy 2 library.")
    print(" ")
    print(pcol.B + "sdrm" + pcol.ENDC + " - check if a steam game has drm.")
    print(pcol.B + "gog" + pcol.ENDC + " - interact with GOG store database.")
    print(pcol.B + "galax" + pcol.ENDC + " - interact with your GOG Galaxy 2 library.")
    print(pcol.B + "quit" + pcol.ENDC + " - exit SteamTuuls.")
    text=input(": ")
    print("_____________________________________________________________________________")
    print(" ")
    return text

#Code for the gog store query menu. Called from gog.py second half
def gogQueryMenu():
    print(" ")
    print("_____________________________________________________________________________")
    print(" ")
    print(pcol.P+"Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "look" + pcol.ENDC + " - look up a game on GOG.")
    print(pcol.B + "sale" +pcol.ENDC +" - returns list of games on sale on GOG.")
    print(pcol.B + "bk" + pcol.ENDC + " - return to main menu.")
    text=input(": ")
    return text

def gogGameSearch(i,inner):
    print("_____________________________________________________________________________")
    print(pcol.G + "Game is on GOG: " + pcol.Y + i["title"])
    print(pcol.G + "Developer: " + pcol.Y + i["publisher"])
    print(pcol.G + "Price: " + pcol.Y + inner +pcol.ENDC)


#code for GOG Galaxy library queries. Called from library.py

def libraryUI():

    print(" ")
    print("_____________________________________________________________________________")
    print(" ")
    print(pcol.P + "Choose a command from the list below." + pcol.ENDC)
    print(pcol.B + "e: 'title'" + pcol.ENDC + " - see if you own 'title'.")
    print(pcol.B + "s: 'title'" + pcol.ENDC + " - view your stats for 'title'.")
    print(pcol.B + "p: 'title'" + pcol.ENDC + " - platform/s do you own 'title' on.")
    print(pcol.B + "t: 'total'" + pcol.ENDC + " - gives you total time played ever.")
    print(pcol.B + "bk" + pcol.ENDC + " - returns you back.")

    text=input(": ")
    return text

def galaxyUI(i):
    print(pcol.G + "Title: " + pcol.Y + i[0] + pcol.ENDC)
    print(pcol.G + "Summary: " + pcol.Y + i[1] + pcol.ENDC)
    print(pcol.G + "Platform: " + pcol.Y + i[2][2:-2] + pcol.ENDC)
    print(pcol.G + "Time Played: " + pcol.Y + i[9] + " minutes." + pcol.ENDC)
    print("")
    print("")

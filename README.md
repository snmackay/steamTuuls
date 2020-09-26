# Welcome to the steamTuuls wiki!

## About: 
Author: Sean Mackay \
Date originally created: 9/19/2020 \
Current Shipped Version: V0.2  

## Pages of this wiki:
-Setup and requirements \
-Main Menu: Covers functionality of the main menu of steamTuuls.


# Setup
Read this section carefully. This is still in beta so there is no .exe version. This will come for both \
linux and Windows in the future. 

## Notes: 
-This was developed and tested on linux using WSL2. \
-GOG Galaxy 2.0 is a major requirement for this app. Without it, many features simply do not work. \
-This is a cli application and requires python 3.5 or later to run. \
-This is a beta release so there will be issues potentially. This is untested on windows but it should work. \

## Installation: 
1: Download the codebase from github and extract to a folder. Do not modify the folder structure. \
2: Ensure python3 and pip3 is installed on your machine. \
3: Install all requirements with the requirements.txt \
-this can be done using the command 'pip3 install -r requirements.txt' from the main directory of the app. \
4: Run the program using 'python3 main.py' \
5: Follow the on screen prompts for use. \
6: For galaxy integration to work, copy the file 'galaxy-2.0.db' from the install directory of GOG Galaxy 2.\
Place this file in the dataBases folder. \
 Note: -C:\ProgramData\GOG.com\Galaxy\storage\galaxy-2.0.db is the standard path

##DISCLAIMER: The goal is to promote games that do not use DRM utilities as they
            are detrimental to the customer experience. Illegal use of this
            application is prohibited, know your local laws.

_______________________________________________________________________________
Galaxy Integration:
From their readme:
Credit to original creators.

NOTE: For galaxy integration to work, copy the file 'galaxy-2.0.db' from the
      install directory of GOG Galaxy 2.
      -C:\\ProgramData\\GOG.com\\Galaxy\\storage\\galaxy-2.0.db is the standard
      path


# GOG Galaxy 2.0 Export Script

This script helps a user export their GOG Galaxy 2.0 Library.

## Usage

Through the use of command line parameters, you can decide what data you want exported to the CSV. Some of the options include the list of platforms (`--platforms`), playtime in minutes (`--playtime`), developers, publishers, genres and much more. You can read the help manual by invoking the script without parameters, to find an up to date list of all the possible export options.

If you want to use the CSV in a different tool, such as the [HTML5 library exporter](https://github.com/Varstahl/GOG-Galaxy-HTML5-exporter), you can default to the `-a` parameter to export everything.

When a different locale wants a different CSV delimiter (such as the Italian), you can manually specify the character to use (`-D <character>`).

Also, you can manually specify the database location (`-i`) and the CSV location (`-o`), instead of using the default ones.

## Dependencies

- Python 3
  - csv
  - natsort

## Platform Support

All platforms from the [official list](https://github.com/gogcom/galaxy-integrations-python-api/blob/master/PLATFORM_IDs.md) are supported. Some are not listed at the moment but should still show up correctly in the output.

## Wiki

Check the [Wiki tab](https://github.com/AB1908/GOG-Galaxy-Export-Script/wiki).

## Roadmap

Check the [Projects tab](https://github.com/AB1908/GOG-Galaxy-Export-Script/projects).

## Contribution

Feel free to add issues and pull requests.

## License

This repository is licensed under the [MIT License](https://github.com/AB1908/GOG-Galaxy-Export-Script/blob/master/LICENSE).

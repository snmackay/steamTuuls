steamTuuls: A set of helpful tools for interacting with your games collection. Currently this program mostly interacts with GOG galaxy 2's database file. 
     Without GOG Galaxy 2 installed, there is still some level of limited functionality in the form of GOG price information, library querying, and finding
     out what steam games are drm free.

NOTE: ARGV is depricated from version 0.0.2, follow the onscreen prompts.

Author: Sean Mackay

Use:
  -prerequisites: Have python3 installed on your machine
                  Make sure urllib3 is installed by running
                    -"pip3 install urllib3"

  -DO NOT CHANGE THE FOLDER STRUCTURE FOR THE APPLICATION FOLDER. 

  -run the program with the command "python3 main.py " from the root
       directory of the application
  -argv will be your use case argument. -NOTE: Argv is currently depricated from V0.0.2 onward in favour of command line arguments in the application.

  ARGV: DEPRICATED      
    -'steamDB' : Generates a new database for the list of drm free steam games
    -'steamdrm?' : Allows you to check if a game has drm.
    -'gogDB' : Generates a new database file for all games on GOG
    -'onGog' :  Allows you to Query if games exist on GOG and whats on sale

```
                         ______                     
 _________        .---"""      """---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  steamTuuls:   | |             
|:______B:|      | |                | |             
|:______B:|      | |  Epic Tool     | |             
|         |      | |  Have Fun!     | |             
|:_____:  |      | |                | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-.
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
      fsc      .'.eeeeeeeeeeeeeeeeeeeeee.'.         
              :____________________________:
```

DISCLAIMER: The goal is to promote games that do not use DRM utilities as they
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

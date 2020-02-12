# tAnki
Corrects the .txt file with Japanese vocabulary list from tangorin.com for import into ANKI flash cards


Problem: ANKI flash cards use different file format for data import. Previously, Tangorin.com have allowed to export vocabulary list for ANKI directly creating suitable .txt file format. Recently, this option is removed and import txt file cannot be easily downloaded into the ANKI. In the simple case, the txt file is missing the "tab" between Japanese and English word.

Solution: This repository has a .py file with the code to modify the .txt file from tangorin.com and prepare file for import into the ANKI flash cards by adding missing "tab".

Option 1: Directly download the .py file and launch it with the terminal by adding additional path for the .txt file location

Option 2: Download both the .py file and tAnki.command file. Put the script file into the /usr/local/bin location as it has automatic PATH location and use chmod u+t tAnki.command to give it excecute option. Inside the tAnki.command file change the exact directory location of the python file.

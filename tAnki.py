#!/usr/bin/python3

"""
    This script takes exported vocabulary txt file from www.tangorin.com
    and adds additional \t (tab) between Japanese word and its English
    meaning. The modified text is then written in an new txt file, which
    could be easily imported into ANKI flashcard software.
"""

import sys
import os

while True:
    
    # add the path location argument
    arg = sys.argv[1] 

    try:
        # Read the file located in same directory as the code
        # Encoding utf-8 is used as otherwise it is not possible
        # to read Japanese characters
        test_tangorin = open(arg, encoding='utf-8')
        # Creates a list of strings, where every string is a one instance from
        # the Tangorine, which are separated by a new line
        tangorin = test_tangorin.readlines()
        # Close the file
        test_tangorin.close()

        # Creates new txt file where modified data will be written
        # File location should be changed by user preference is used without the tAnki.command script
        new_tangorin = open('Desktop/to_anki.txt', 'w',encoding='utf-8')

        # Scan for every instance in the file and modify it.
        # Compares every character in the string if it is unicode.
        # At the border of ascii and unicode adds \t .
        for word in tangorin:
            for idx, item in enumerate(word):
                if (ord(item) < 128) == True:
                           new_line = word[:idx] + '\t' + word[idx:]
                           new_tangorin.write(new_line)
                           break

        # Close file
        new_tangorin.close()
        print()
        print('='*75)
        print('File was modified successfully! It has a name "to_anki.txt"')
        print('It is located in the same folder as original one')
        print('='*75)
        print()
        break

    except FileNotFoundError:
        print()
        print('='*75)
        print('Incorrect file/path name. Please repeat!')
        print('='*75)
        print()
        break

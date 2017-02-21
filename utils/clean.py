#!/usr/bin/env python

"""Removes symboles, numbers and extra spaces, toLower(), all text in file"""

def save_clean(oldfile, newfile):
    try:
        with open(oldfile, 'r') as infile, open(newfile, 'w') as outfile:
            pass

    except Exception as ex:
        print(ex)    

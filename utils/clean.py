#!/usr/bin/env python

"""Removes symboles, numbers and extra spaces, toLower(), all text in file"""

import re

def save_clean(oldfile, newfile):
    try:
        with open(oldfile, 'r') as infile, open(newfile, 'w') as outfile:
            print('opened...')
            data = infile.read()
            cleandata = re.sub('[^a-zA-Z]', ' ', data).lower()
            cleandata = ' '.join(re.sub(r'\b\w{1,2}\b', '', cleandata).split())
            
            outfile.write(cleandata)
            print('complete')

    except Exception as ex:
        print(ex)    

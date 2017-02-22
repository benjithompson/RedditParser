#!/usr/bin/env python

"""Removes symboles, numbers and extra spaces, toLower()"""

import re

def clean_data(data):
    cleandata = re.sub('[^a-zA-Z]', ' ', data).lower()
    return ' '.join(re.sub(r'\b\w{1,2}\b', '', cleandata).split()) 

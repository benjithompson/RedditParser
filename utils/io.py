#  -*- coding: utf-8 -*-
"""Saves data obtained from reddit to file"""

import os
import sys
import datetime
import pprint as p
from reddit import config


RETRY = config.retry
WAIT = config.wait

def save_data_to_file(data, filename):
    """iterates through all posts and comments and writes them to specified file"""

    try:
        if __verify_write(filename):
            __write_data(data, filename)
        else:
            print('aborting file write...')
    except OSError as err:
        print(err.strerror)

def __verify_write(filename):
    """Return true if user wants to overwrite existing file"""
    
    if os.path.exists(filename):
        ans = input(filename + ' already exists. Overwrite? (y/n): ')
        return ans == 'y' or ans == 'Y'
    else:
        ans = input('Do you really want to write to ' + filename + '(y/n)?: ')
        return ans == 'y' or ans == 'Y'

def __write_data(data, filename):
    """Pulls data from posts and writes to filename"""

    time = str(datetime.datetime.now())
    print('saving to ' + filename + '...')
    with open(filename, 'w') as f:
        f.write(time + '\n')
        f.flush()
        sys.stdout.flush()
        p.pprint(data, f)
        f.flush()

def read_from_file(filename):
    text = ''
    with open(filename, 'r') as f:
        for line in f.readline():
            text += line
    return text

# -*- coding: utf-8 -*-

"""Main runner for downloading wordcounts"""

from analysis import analysis as ana
from datetime import datetime
from utils import io, args
from utils import convert as c
from reddit import reddit
import pprint as p
import time

def main():

    REDDIT = reddit.get_reddit()
    #arg = args.args()
    SUB, START, END = get_input()
    POSTS = reddit.get_posts(REDDIT, SUB, END, START)
    print('Downloading ' + SUB + ':')
    data = reddit.get_comments(POSTS)

    cleandata = c.clean_data(data)
    wordcount = ana.getdict(cleandata)
    list = ana.getsortedkv(wordcount)

    ans = input('Do you want to save file? (y/n):')
    if ans is 'y':
        filename = input('save to file: ')
        filepath = c.get_path(filename, '/data/', '.txt')
        io.save_data_to_file(list, filepath)
    else:
        p.pprint(list)

def get_input():
    sub = input('Input subreddit: ')
    start = input('Start time (yyyy-mm-dd hh:mm:ss):')
    if start == '':
        print('Setting start as current time.')
        start = c.get_UTC()
    
    end = c.time_delta(start, int(input('timedelta (hours): ')))
    ustart = c.utc_pst(c.unix_time(start))
    uend = c.utc_pst(c.unix_time(end))
    print('start:' + str(c.readable_time(ustart)) + 
          ', end: ' + str(c.readable_time(uend)))
    return sub, ustart, uend

if __name__ == '__main__':
    main()
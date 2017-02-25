# -*- coding: utf-8 -*-

"""Main runner for downloading wordcounts"""

import pprint as p
import time

from analysis import analysis as ana
from reddit import reddit
from utils import convert as c
from utils import args, io


def main():
    """Main runner to get reddit data"""

    REDDIT = reddit.get_reddit()
    #arg = args.args()
    SUB, START, END = get_input()
    POSTS = reddit.get_posts(REDDIT, SUB, END, START)
    print('Downloading ' + SUB + ':')

    comm_list = reddit.get_comments(POSTS)
    word_str = c.list_to_str(comm_list)
    cleandata = c.clean_text(word_str)
    wordcount = ana.getdict(cleandata)
    words_kv = ana.getsortedkv(wordcount)

    ans = input('Do you want to save file? (y/n):')
    if ans is 'y':
        filename = input('save to file: ')
        filepath = c.get_path(filename, '/data/', '.txt')
        io.save_data_to_file(words_kv, filepath)
    else:
        p.pprint(words_kv)

def get_input():
    """Grabs subreddit and timerange from user"""

    sub = input('Input subreddit: ')
    start = input('Start time (yyyy-mm-dd hh:mm:ss):')
    if start == '':
        print('Setting start as current time.')
        start = c.get_utc()

    end = c.time_delta(start, int(input('timedelta (hours): ')))
    ustart = c.utc_pst(c.unix_time(start))
    uend = c.utc_pst(c.unix_time(end))
    print('start:' + str(c.readable_time(ustart)) +
          ', end: ' + str(c.readable_time(uend)))
    return sub, ustart, uend

if __name__ == '__main__':
    main()

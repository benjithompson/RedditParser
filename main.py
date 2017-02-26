# -*- coding: utf-8 -*-

"""Main runner for downloading wordcounts"""

from pprint import pprint

from analysis import data
from reddit import reddit
from utils import convert as c
from utils import io


def main():
    """Main runner to get reddit data"""

    REDDIT = reddit.get_reddit()
    #arg = args.args()
    SUB, START, END = get_input()
    rd = data.RedditData(REDDIT)
    print('Downloading ' + SUB + ':')
    rd.start_query(SUB, START, END)
    rd.run_analysis()
    rd.printall()

    ans = input('Do you want to save file? (y/n): ')
    if ans is 'y':
        filename = input('filename: ')
        cntpath = c.get_path(filename, '/data/', '.cnt')
        rawpath = c.get_path(filename, '/data/', '.raw')
        io.save_data_to_file(rd.wordskv, cntpath)
        io.save_data_to_file(rd.analysis_text, rawpath)
    else:
        pprint('exitting...')

def get_input():
    """Grabs subreddit and timerange from user"""

    sub = input('Input subreddit: ')
    start = input('Start time (yyyy-mm-dd hh:mm:ss):')
    if start == '':
        print('Setting start as current time.')
        start = c.get_utc()

    ans = input('timedelta (hours): ')
    if ans is '':
        print('Default timedelta to 1hr.')
        end = c.time_delta(start, 1)
    else:
        end = c.time_delta(start, int(ans))

    ustart = c.utc_pst(c.unix_time(start))
    uend = c.utc_pst(c.unix_time(end))
    print('start:' + str(c.readable_time(ustart)) +
          ', end: ' + str(c.readable_time(uend)))
    return sub, ustart, uend

if __name__ == '__main__':
    main()

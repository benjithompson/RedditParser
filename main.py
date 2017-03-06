# -*- coding: utf-8 -*-

"""Main runner for downloading wordcounts"""

from collections import defaultdict
from pprint import pprint
from time import sleep
from analysis import data
from utils import convert as c
from utils import io

WAIT = 60

def main():
    """Main runner to get reddit data"""

    container = defaultdict(data.RedditData)

    while True:
        #SUB, START, END = get_input()
        try:
            SUB = 'the_donald'
            if SUB not in container:
                container[SUB] = data.RedditData()
            else:
                print('Instance already created.')
            print('Downloading ' + SUB + ':')
            rd = container[SUB]
            start = c.get_utc()
            rd.start_query(SUB, c.utc_pst(c.unix_time(start)), c.utc_pst(c.unix_time(c.time_delta(start, 1))))
            rd.run_analysis()
            rd.printall()

            print('waiting ' + str(WAIT) + ' mins...')
            sleep(WAIT * 60)

        except KeyboardInterrupt:
            print('exitting...')
            break

    output_reddit_data(rd)


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

def output_reddit_data(rdata):

    ans = input('Do you want to save file? (y/n): ')
    if ans is 'y':
        filename = input('filename: ')
        cntpath = c.get_path(filename, '/data/', '.cnt')
        rawpath = c.get_path(filename, '/data/', '.raw')
        statspath = c.get_path(filename, '/data/', '.txt')
        io.save_data_to_file(rdata.wordskv, cntpath)
        io.save_data_to_file(rdata.analysis_text, rawpath)
        io.save_data_to_file(rdata.stats, statspath)
    else:
        pprint('exitting...')

if __name__ == '__main__':
    main()

"""Saves data obtained from reddit to file"""

import os
import sys
import config
import datetime
import praw.exceptions as pex
from time import sleep
from urllib3 import exceptions as ex

RETRY = config.retry
WAIT = config.wait

def save(posts, filename):
    """iterates through all posts and comments and writes them to specified file"""

    try:
        if __verify_write(filename):
            __write_data(filename, posts)
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

def __write_data(filename, posts):
    """Pulls data from posts and writes to filename"""

    time = str(datetime.datetime.now())
    print('saving to ' + filename + '...')
    print('Time started: ' + time)
    with open(filename, 'w') as target:
        target.write(time + '\n')
        target.flush()
        sys.stdout.flush()
        data = __get_data(posts)
        target.write(data)
        target.flush()
        print('Complete!')

def __get_data(posts):
    """makes the request to reddit API to build the data str"""

    data = ''
    retry = 0
    while True:
        try:
            for post in posts:
                title = str(post.title.encode('ascii', 'ignore'))
                data += title
                post.comments.replace_more(limit=0)
                for comment in post.comments.list():
                    comment = str(comment.body.encode('ascii', 'ignore'))
                    data += comment
                    print('.', end = '')
                    sys.stdout.flush()
            time = str(datetime.datetime.now())
            data = ''.join(time)
            break
        except ex.HTTPError as err:
            print('HTTPError...')
            print(err.code)
            sleep(WAIT)
        except pex.ClientException:
            print('ClientException...')
            sleep(WAIT)
        except pex.APIException:
            print('APIException...')
            sleep(WAIT)
        except KeyboardInterrupt:
            print('KeyboardInterrupt...')
            break
        except:
            print('Exception...')
            sleep(WAIT)
            if retry == 100:
                break
            retry = retry + 1
            
    return data

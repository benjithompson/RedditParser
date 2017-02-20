"""Saves data obtained from reddit to file"""

import sys
import os
import datetime

def write_subreddit_text(posts, filename):
    """iterates through all posts and comments and writes them to specified file"""
    try:
        path = os.getcwd() + '/data/'
        if filename == '' or filename == None:
            filename = input("Enter name of data file: ")
        filename = os.path.join(path, filename + '.data')
        if verify_write(filename):
            __write_data(filename, posts)
        else:
            print('aborting file write...')
    except OSError as err:
        print(err.strerror)

def verify_write(filename):
    """Return true if user wants to overwrite existing file"""
    
    if os.path.exists(filename):
        ans = input('File already exists. Overwrite? (y/n): ')
        return ans == 'y' or ans == 'Y'
    else:
        ans = input('Do you really want to write to ' + filename + '(y/n)?: ')
        return ans == 'y' or ans == 'Y'

def __write_data(filename, posts):
    data = ''
    time = str(datetime.datetime.now())
    print('saving to ' + filename + '...')
    print('Time started: ' + time)
    target = open(filename, 'w')
    target.write(time + '\n')
    target.flush()
    sys.stdout.flush()

    #TODO: catch HTTP errors and using settings file
    for post in posts:
        title = str(post.title.encode('ascii', 'ignore'))
        data += title
        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            comment = str(comment.body.encode('ascii', 'ignore'))
            data += comment
            print('.', end = '')
            sys.stdout.flush()
        target.flush()

    time = str(datetime.datetime.now())
    data = ''.join(time)
    print('Compiling data complete. Writing to file...')
    target.write(data)
    target.flush()
    print('Complete!')

"""Saves data obtained from reddit to file"""
import sys
import os
import datetime


def write_subreddit_text(posts):
    """iterates through all posts and comments and writes them to specified file"""
    try:
        path = os.getcwd() + '/data/'
        filename = input("Enter name of data file: ")
        filename = os.path.join(path, filename + '.data')
        if verify_write(filename):
            __write_data(filename, posts)
        else:
            print('aborting file write...')
    except OSError as err:
        print(err.strerror)
        raise

def __write_data(filename, posts):
    time = str(datetime.datetime.now())
    print('saving to ' + filename + '...')
    print('Time started: ' + time)
    target = open(filename, 'w')
    target.write(time)
    for post in posts:
        target.write(post.title)
        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            target.write(comment.body)
    time = str(datetime.datetime.now())
    target.write(time)
    print('Complete!')
    print(time)

def verify_write(filename):
    """Return true if user wants to overwrite existing file"""
    if os.path.exists(filename):
        ans = input('File already exists. Overwrite? (y/n): ')
        return ans == 'y' or ans == 'Y'
    else:
        ans = input('Do you really want to write to ' + filename + '(y/n)?: ')
        return ans == 'y' or ans == 'Y'

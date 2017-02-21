"""Script to start writing subreddit comments to file"""
import os
import sys
sys.path.append(os.path.abspath)
from reddit import *
from utils import path

def main(argv):
    filename = getargs(argv)
    filename = path.get_path(filename, '/data/', '.data')
    REDDIT = reddit.get_reddit()
    POSTS = reddit.get_posts(REDDIT, 'The_Donald')
    io.save(POSTS, filename)

def getargs(argv):
    filename = ''
    if len(argv) is 2:
        filename = argv[1]
    else:
        print('Usage: getdata.py [filename]')
        exit(1)
    return filename
    
if __name__ == "__main__":
    print(os.path.abspath)
    main(sys.argv)
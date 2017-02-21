"""Script to start writing subreddit comments to file"""
import os
import sys
sys.path.append(os.path.abspath)
from reddit import *

def main(argv):
    filename = ''
    if len(argv) == 2:
        filename = argv[1]
    REDDIT = reddit.get_reddit()
    POSTS = reddit.get_posts(REDDIT, 'The_Donald')
    io.save(POSTS, filename)
    
if __name__ == "__main__":
    print(os.path.abspath)
    main(sys.argv)
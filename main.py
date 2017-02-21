"""Script to start writing subreddit comments to file"""

import sys
import reddit as r
from writedata import save

def main(argv):
    filename = ''
    if len(argv) == 2:
        filename = argv[1]
    REDDIT = r.get_reddit()
    POSTS = r.get_subreddit_posts(REDDIT, 'The_Donald')
    save(POSTS, filename)
    
if __name__ == "__main__":
    main(sys.argv)
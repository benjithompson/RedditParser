"""Script to start writing subreddit comments to file"""

import reddit as r
import writedata as wd
import sys

if __name__ == "__main__":
    main(sys.argv[1:])

def main(argv):
    filename = argv[1]
    REDDIT = r.get_reddit()
    POSTS = r.get_subreddit_posts(REDDIT, 'The_Donald')
    wd.write_subreddit_text(POSTS, filename)
    
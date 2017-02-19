"""Script to start writing subreddit comments to file"""

import reddit as r
import writedata as wd

REDDIT = r.get_reddit()
POSTS = r.get_subreddit_posts(REDDIT, 'The_Donald')
wd.write_subreddit_text(POSTS)

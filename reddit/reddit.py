"""Reddit authenticator and retrever of comments in specified subreddit"""

from reddit import config
from time import sleep
import praw

WAIT = config.wait
RETRY = config.retry

def get_reddit():
    """Returns Reddit instance after authentication succeeds."""
    retry = 0
    print('Authenticating reddit instance...')
    while True:
        try:   
            reddit = praw.Reddit(client_id=config.client_id,
                                 client_secret=config.client_secret,
                                 password=config.password,
                                 user_agent=config.user_agent,
                                 username=config.username)
            break           
        except KeyboardInterrupt:
            print('KeyboardInterrupt...')
            exit(1)
        except:
            print('RedditException...')
            if retry == RETRY:
                break
            retry = retry + 1
            sleep(WAIT)

    print('instance created!')
    print('Logged in as: ' + str(reddit.user.me()))
    return reddit

def get_posts(reddit, sub):
    """returns list of object submissions"""
    #flat_comments = praw.helpers.flatten_tree(submission.comments)
    subreddit = reddit.subreddit(sub)
    return subreddit.submissions()

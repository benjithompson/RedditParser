"""Reddit authenticator and retrever of comments in specified subreddit"""

from reddit import config
import praw
#debug, praw
def get_reddit():
    """Returns Reddit instance after authentication succeeds."""
    print('Authenticating reddit instance...')
    reddit = praw.Reddit(client_id=config.client_id,
                         client_secret=config.client_secret,
                         password=config.password,
                         user_agent=config.user_agent,
                         username=config.username)
    print('instance created!')
    print('Logged in as: ' + str(reddit.user.me()))
    return reddit


def get_posts(reddit, sub):
    """returns list of object submissions"""
    #flat_comments = praw.helpers.flatten_tree(submission.comments)
    subreddit = reddit.subreddit(sub)
    return subreddit.submissions()

"""Reddit authenticator and retrever of comments in specified subreddit"""

import sys
from time import sleep

import praw
import praw.exceptions as pex
from urllib3 import exceptions as ex

from reddit import config
from utils import convert as c

WAIT = 5
RETRY = 5

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

def get_posts(reddit, sub, start=None, end=None):
    """returns submissions of given subreddit between start and end times"""

    return reddit.subreddit(sub).submissions(start, end)

def get_comments(posts, submission_cnt=None, comment_cnt=None):
    """makes the request to reddit API to build the data list"""

    data = []

    while True:
        try:
            for post in posts:
                title = str(post.title)
                data.append(title)
                print(title)
                print(c.readable_time(get_submission_time(post)))
                for comment in post.comments.list():
                    comment = str(comment.body)
                    data.append(comment)
                    print('.', end='')
                    sys.stdout.flush()
            break

        except ex.HTTPError as err:
            print('HTTPError...')
            print(err)
            sleep(WAIT)
        except pex.ClientException:
            print('ClientException...')
            sleep(WAIT)
        except pex.APIException:
            print('APIException...')
            sleep(WAIT)
        except KeyboardInterrupt:
            print('\nDownload cancelled.')
            break
        except:
            print('Exception:' + sys.exc_info()[0])
            sleep(WAIT)
        finally:
            return data

def get_submission_time(submission):
    return submission.created_utc

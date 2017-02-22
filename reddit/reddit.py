"""Reddit authenticator and retrever of comments in specified subreddit"""

from urllib3 import exceptions as ex
import praw.exceptions as pex
from reddit import config
from time import sleep
import praw
import sys

WAIT = 5
START = None
END = None

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
    
    return reddit.subreddit(sub).submissions(START, END)

def get_data(posts):
    """makes the request to reddit API to build the data str"""

    data = ''
    retry = 0
    while True:
        try:
            for post in posts:
                title = str(post.title.encode('ascii', 'ignore'))
                data += title
                #post.comments.replace_more(limit=0)
                for comment in post.comments.list():
                    comment = str(comment.body.encode('ascii', 'ignore'))
                    data += comment
                    print('.', end = '')
                    sys.stdout.flush()
            break

        except ex.HTTPError as err:
            print('HTTPError...')
            print(err.code)
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
            print('Exception.')
            sleep(WAIT)

    return data

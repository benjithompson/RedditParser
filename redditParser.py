import praw
import authConfig
# import pprint

def getReddit():
    print('Authenticating reddit instance...')
    reddit = praw.Reddit(client_id=authConfig.client_id,
                         client_secret=authConfig.client_secret,
                         password=authConfig.password,
                         user_agent=authConfig.user_agent,
                         username=authConfig.username)
    print('instance created!')
    print('Logged in as: ' + str(reddit.user.me()))
    return reddit

def printPostsFeed(reddit, sub):
    for submission in reddit.subreddit(sub).stream.submissions():
        title = submission.title.encode('ascii', 'ignore')
        print(title)

def printall(items):
    for item in items:
        title = item.title.encode('ascii', 'ignore')
        print(title)

def getPostsFromSubreddit(reddit, sub):
    #flat_comments = praw.helpers.flatten_tree(submission.comments)
    subreddit = reddit.subreddit(sub)
    return subreddit.submissions()

reddit = getReddit()
posts = getPostsFromSubreddit(reddit, 'The_Donald')
printall(posts)
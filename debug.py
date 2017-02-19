
def print_posts_feed(inst, sub):
    """Prints new posts as they are posted"""
    for submission in inst.subreddit(sub).stream.submissions():
        title = submission.title.encode('ascii', 'ignore')
        print(title)

def print_posts(items):
    """Prints title from list of objects, converted to ascii"""
    for item in items:
        title = item.title.encode('ascii', 'ignore')
        print(title)

def print_post_comments(post):
    """returns all comments from given post"""
    print('Number of Comments in ' + post.title + ": " + str(post.num_comments))

    post.comments.replace_more(limit=0)
    for comment in post.comments.list():
        print(comment.body)

def print_sub_comments(posts):
    """prints all comments from list of posts"""
    for post in posts:
        print_post_comments(post)

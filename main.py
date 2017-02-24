from analysis import analysis as ana
from utils import io, convert
from reddit import reddit
import pprint as p

def main():

    REDDIT = reddit.get_reddit()
    sub = input('Input subreddit: ')
    POSTS = reddit.get_posts(REDDIT, sub)
    print('Downloading ' + sub + ':')
    data = reddit.get_data(POSTS)
    cleandata = convert.clean_data(data)
    wordcount = ana.getdict(cleandata)
    list = ana.getsortedkv(wordcount)
    ans = input('Do you want to save file? (y/n)')
    if ans is 'y':
        filename = input('save to file: ')
        filepath = convert.get_path(filename, '/data/', '.txt')
        io.save_data_to_file(list, filepath)
    else:
        p.pprint(list)

if __name__ == '__main__':
    main()
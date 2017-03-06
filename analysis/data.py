"""Analysis functions using textstat module"""

from collections import defaultdict
from pprint import pprint

from textstat import textstat as ts

from reddit import reddit
from utils import convert as c


class RedditData:

    __reddit = reddit.get_reddit()

    def __init__(self):

        self.sub = ''
        self.starttime = 0
        self.endtime = 0
        self.posts = None
        self.commlist = []
        self.rawtextstr = ''
        self.analysis_text = ''
        self.wordskv = {}
        self.stats = defaultdict(list)

    def start_query(self, sub, starttime, endtime):
        """begins retrieving reddit comments"""
        self.sub = sub
        self.starttime = starttime
        self.endtime = endtime
        self.posts = reddit.get_posts(self.__reddit, sub, endtime, starttime)
        self.commlist = reddit.get_comments(self.posts)

    def run_analysis(self):
        """Obtains useful data from comments list and saves to instance attributes"""

        if len(self.commlist) == 0:
            print('No posts/comments downloaded.')
            return
        self.rawtextstr = c.list_to_str(self.commlist)
        self.analysis_text = c.ana_text(self.rawtextstr)
        worddict = self.__getdict(c.clean_text(self.rawtextstr))
        self.wordskv = self.__getsortedkv(worddict)

        self.stats['flesch_ease'].append(ts.textstat.flesch_reading_ease(self.analysis_text))
        self.stats['flesch_grade'].append(ts.textstat.flesch_kincaid_grade(self.analysis_text))
        self.stats['dalechall'].append(ts.textstat.dale_chall_readability_score(self.analysis_text))
        self.stats['ari'].append(ts.textstat.automated_readability_index(self.analysis_text))
        self.stats['colemanliau'].append(ts.textstat.coleman_liau_index(self.analysis_text))
        self.stats['lisear'].append(ts.textstat.linsear_write_formula(self.analysis_text))

        self.stats['smog'].append(ts.textstat.smog_index(self.analysis_text))
        self.stats['difcwords'].append(ts.textstat.difficult_words(self.analysis_text))
        self.stats['sentences'].append(ts.textstat.sentence_count(self.rawtextstr))
        self.stats['lexiconcnt'].append(ts.textstat.lexicon_count(self.rawtextstr))
        self.stats['avgsyllables'].append(ts.textstat.avg_syllables_per_word(self.analysis_text))

        self.stats['stdreadability'].append(ts.textstat.text_standard(self.analysis_text))

    def printall(self):
        """Prints current class attributes"""
        print('\nSUB: ' + self.sub +
              '\nSTART: ' + str(c.readable_time(self.starttime)) +
              ', END: ' + str(c.readable_time(self.endtime)))

        pprint(self.stats)

    def __getdict(self, text):
        wordcount = defaultdict(int)
        words = text.split()
        for word in words:
            wordcount[word] += 1
        return wordcount

    def __getsortedkv(self, worddict):
        if dict is not None:
            return sorted(worddict.items(), key=lambda x: x[1], reverse=True)
        else:
            print('dict is type None')

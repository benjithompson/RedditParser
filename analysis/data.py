"""Analysis functions using textstat module"""

from pprint import pprint

from textstat import textstat as ts

from reddit import reddit
from utils import convert as c


class RedditData:
    """
    * 90-100 : Very Easy
    * 80-89 : Easy
    * 70-79 : Fairly Easy
    * 60-69 : Standard
    * 50-59 : Fairly Difficult
    * 30-49 : Difficult
    * 0-29 : Very Confusing
    """

    REDDIT = None
    sub = ''
    posts = None
    starttime = 0
    endtime = 0

    commlist = []
    rawtextstr = ''
    analysis_text = ''
    wordskv = {}

    fleschease = 0
    fleschgrade = 0
    dalechall = 0
    ari = 0
    colemanliau = 0
    lisear = 0

    smog = 0
    difcwords = 0
    sentences = 0
    lexiconcnt = 0
    avgsyllables = 0

    stdreadability = 0

    def __init__(self, REDDIT):
        self.REDDIT = REDDIT

    def start_query(self, sub, starttime, endtime):
        """begins retrieving reddit comments"""
        self.sub = sub
        self.starttime = starttime
        self.endtime = endtime
        self.posts = reddit.get_posts(self.REDDIT, self.sub, self.endtime, self.starttime)
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

        self.fleschease = ts.textstat.flesch_reading_ease(self.analysis_text)
        self.fleschgrade = ts.textstat.flesch_kincaid_grade(self.analysis_text)
        self.dalechall = ts.textstat.dale_chall_readability_score(self.analysis_text)
        self.ari = ts.textstat.automated_readability_index(self.analysis_text)
        self.colemanliau = ts.textstat.coleman_liau_index(self.analysis_text)
        self.lisear = ts.textstat.linsear_write_formula(self.analysis_text)

        self.smog = ts.textstat.smog_index(self.analysis_text)
        self.difcwords = ts.textstat.difficult_words(self.analysis_text)
        self.sentences = ts.textstat.sentence_count(self.rawtextstr)
        self.lexiconcnt = ts.textstat.lexicon_count(self.rawtextstr)
        self.avgsyllables = ts.textstat.avg_syllables_per_word(self.analysis_text)

        self.stdreadability = ts.textstat.text_standard(self.analysis_text)

    def printall(self):
        """Prints class attributes"""
        print('\nSUB: ' + self.sub +
              '\nSTART: ' + str(c.readable_time(self.starttime)) +
              ', END: ' + str(c.readable_time(self.endtime)))

        pprint('Flesch Reading EASE:    ' + str(self.fleschease))
        pprint('Flesch GRADE:           ' + str(self.fleschgrade))
        pprint('Dale Chall Readability: ' + str(self.dalechall))
        pprint('Avg Readability Idx:    ' + str(self.ari))
        pprint('Coleman Liau Idx:       ' + str(self.colemanliau))
        pprint('Lisear Formula:         ' + str(self.lisear))
        pprint('Smog Idx:               ' + str(self.smog))
        pprint('Difficult Words:        ' + str(self.difcwords))
        pprint('Sentences:              ' + str(self.sentences))
        pprint('Lexicon Count:          ' + str(self.lexiconcnt))
        pprint('Avg Syllables Per Word: ' + str(self.avgsyllables))
        pprint('ReadabilityConcensus:   ' + str(self.stdreadability))

    def __getdict(self, text):
        wordcount = {}
        words = text.split()
        for word in words:
            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1
        return wordcount

    def __getsortedkv(self, worddict):
        if dict is not None:
            return sorted(worddict.items(), key=lambda x: x[1], reverse=True)
        else:
            print('dict is type None')

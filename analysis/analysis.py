#!/usr/bin/env python

def getdict(data):
    wordcount = {}
    words = data.split()
    for word in words:
        if word in wordcount:
            wordcount[word] += 1
        else:
            wordcount[word] = 1
    return wordcount

def getsortedkv(dict):
    if dict is not None:
        return sorted(dict.items(), key=lambda x: x[1], reverse=True)
    else:
        print('dict is type None')

    
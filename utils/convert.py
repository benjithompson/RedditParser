# -*- coding: utf-8 -*-

"""Module with conversion functions to support the main program"""

import datetime as dt
import os
import re
import time

import pytz


def get_path(filename, folder='', ext=''):
    """Utility function to create file paths"""
    path = os.getcwd() + folder
    filename = os.path.join(path, filename + ext)
    return filename

def list_to_str(wlist):
    """Concatenates list entries into single string"""
    data = ''
    for entry in wlist:
        data += str(entry)
    return data

def ana_text(text):
    """Removes numbers and extra spaces, toLower()"""
    return re.sub('[^a-zA-Z.,\']', ' ', text).lower()
    #return ' '.join(re.sub(r'\b\w{1,2}\b', '', cleantext).split())

def clean_text(text):
    cleantext = re.sub('[^a-zA-Z]', ' ', text).lower()
    return ' '.join(re.sub(r'\b\w{1,2}\b', '', cleantext).split())

def unix_time(dtime):
    """Converts yyyy-mm-dd hh.mm.ss into unix time"""
    return time.mktime(dtime.timetuple())

def readable_time(utime):
    """returns readable datetime object from unix timestamp"""
    return dt.datetime.fromtimestamp(int(utime))

def time_delta(dtime, hours):
    """add hours to datetime object"""
    return dtime - dt.timedelta(hours=hours)

def get_pst():
    """returns datetime object in pacific timezone"""
    tzone = pytz.timezone('US/Pacific')
    return dt.datetime.now(tzone)

def get_utc():
    """returns current time in UTC"""
    return dt.datetime.utcnow()

def utc_pst(utime):
    """converts unix timestamp from utc to pst"""
    return utime - (8*60*60)

def pst_utc(utime):
    """converts unix timestamp from pst to utc"""
    return utime + (8*60*60)

def get_dt(stime):
    """returns datetime object from string with format yyyy-mm-dd hh:mm:ss"""
    return dt.datetime.strftime(stime, '%Y-%m-%d %H:%M:%S')

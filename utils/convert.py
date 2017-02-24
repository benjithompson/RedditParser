
#!/usr/bin/env python
import os
import re
import pytz
import time
import calendar
from pytz import timezone
import datetime as dt



def get_path(filename, folder = '', ext = ''):
    path = os.getcwd() + folder
    filename = os.path.join(path, filename + ext)
    return filename

def clean_data(data):
    """Removes symboles, numbers and extra spaces, toLower()"""
    cleandata = re.sub('[^a-zA-Z]', ' ', data).lower()
    return ' '.join(re.sub(r'\b\w{1,2}\b', '', cleandata).split()) 

def unix_time(dtime):
    """Converts yyyy-mm-dd hh.mm.ss into unix time"""
    return time.mktime(dtime.timetuple())

def readable_time(utime):
    """returns readable datetime object from unix timestamp"""
    return dt.datetime.fromtimestamp(int(utime))

def time_delta(dtime, hours):
    """add hours to datetime object"""
    return dtime - dt.timedelta(hours=hours)

def get_PST():
    """returns datetime object in pacific timezone"""
    tz = pytz.timezone('US/Pacific')
    return dt.datetime.now(tz)

def get_UTC():
    return dt.datetime.utcnow()

def utc_pst(utime):
    return utime - (8*60*60)

def pst_utc(utime):
    return utime + (8*60*60)

def get_dt(str):
    return dt.strftime(str, '%Y-%m-%d %H:%M:%S')
   


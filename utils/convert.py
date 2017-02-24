
#!/usr/bin/env python
import os
import re
import time, datetime

def get_path(filename, folder = '', ext = ''):
    path = os.getcwd() + folder
    filename = os.path.join(path, filename + ext)
    return filename

def clean_data(data):
    """Removes symboles, numbers and extra spaces, toLower()"""
    cleandata = re.sub('[^a-zA-Z]', ' ', data).lower()
    return ' '.join(re.sub(r'\b\w{1,2}\b', '', cleandata).split()) 

def get_time(date):
    """Converts d/m/y into unix time"""
    return time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())

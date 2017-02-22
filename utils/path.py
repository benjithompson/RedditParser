
#!/usr/bin/env python
import os

def get_path(filename, folder = '', ext = ''):
    path = os.getcwd() + folder
    filename = os.path.join(path, filename + ext)
    return filename
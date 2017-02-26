from analysis import analysis as ana
from utils import convert as c
from utils import io
import pprint as p

def main():

    filename = input('Input filename: ')
    filepath = c.get_path(filename, '/data/', '.txt')
    commtext = io.read_from_file(filepath)
    wordcount = ana.getdict(commtext)
    wordskv = ana.getsortedkv(wordcount)
    outpath = c.get_path(filename, '/data/', '.ana')
    io.save_data_to_file(wordskv, outpath)

if __name__ == '__main__':
    main()
from analysis import analysis
from utils import path
import pprint as p

def main():

    filename = input('Input filename: ')
    output = input('Output filename: ')
    filepath = path.get_path(filename, '/data/', '.data')
    wordcount = analysis.getdict(filepath)
    list = analysis.getsortedkv(wordcount)
    output = path.get_path(output, '/data/', '.txt')
    

if __name__ == '__main__':
    main()
from utils import clean, path

def main():
    run('test', 'testclean')

def run(oldfile, newfile):
    oldfile = path.get_path(oldfile, '/data/', '.data')
    newfile = path.get_path(newfile, '/data/', '.data')
    clean.save_clean(oldfile, newfile)

if __name__ == '__main__':
    main()
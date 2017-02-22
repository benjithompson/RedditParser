def getargs(argv):
    filename = ''
    if len(argv) is 2:
        filename = argv[1]
    else:
        print('Usage: getdata.py [filename]')
        exit(1)
    return filename
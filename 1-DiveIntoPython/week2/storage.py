import json
import tempfile
import argparse
import os
STORAGE_FILE = os.path.join(tempfile.gettempdir(), 'storage.data')

def main():
    storage = None
    argparser = argparse.ArgumentParser(description='')
    argparser.add_argument('-k', '--key', dest='key', required=True)
    argparser.add_argument('-v', '--value', dest='value')
    args = argparser.parse_args()
    if not os.path.isfile(STORAGE_FILE):
        storage = dict()
    else:
        with open(STORAGE_FILE) as fo:
            storage = json.load(fo)
    
    if args.value and args.key:
        if args.key in storage:
            storage[args.key].append(args.value)
        else:
            storage[args.key] = []
            storage[args.key].append(args.value)
        with open(STORAGE_FILE, 'w') as fo:
            json.dump(storage, fo)
    
                
    else:
        if args.key in storage:
            values = storage[args.key]
            first = True
            for value in values:
                if not first:
                    print(', ', end = '')
                first = False
                print(value, end= '')
if __name__ == '__main__':
    main()
import sys
import os
import tempfile
import json
import argparse




parser = argparse.ArgumentParser()
parser.add_argument('--key', action="store", dest="key", default=1333334)
parser.add_argument('--val', action="store", dest="val", default=1333334)

args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.isfile(storage_path):
    dic = dict()
else:
    with open(storage_path) as f:
        dic = json.load(f)


if args.val != 1333334:
    if args.key not in dic:
        dic[args.key] = list()
    l = dic[args.key]
#    if args.val not in l:
    l.append(args.val)
    dic.update({
                args.key : l
                })
    
    with open(storage_path, 'w') as f:
        f.write(json.dumps(dic))
elif args.key !=1333334:
    if not os.path.isfile(storage_path):
        print('')
    else:
        with open(storage_path, 'r') as f:
            if args.key not in dic:
                print('')
            else:
                if len(dic[args.key]) > 1:
                    print(', '.join(dic[args.key]))
                else:
                    print((dic[args.key])[0])

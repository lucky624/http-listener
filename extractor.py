#!/usr/bin/python3

import os, re
from storage import storage_set, storage_get

REDIS_STORAGE = 0 # 1 - on
                  # 0 - off

FLAG_REGEXP  = '[A-Z0-9]{31}=' 

pwd_files = []

for d, dirs, files in os.walk('data'):
    pwd_files = files
    break

if REDIS_STORAGE == 1:
    for file in pwd_files:
        if not storage_get(file):
            f = open(d + '/' + file, 'rb')
            for line in f.readlines():
                try:
                    decode_line = line.decode()
                    flags = re.findall(FLAG_REGEXP, decode_line)
                    if flags:
                        for flag in flags:
                            print(flag, flush=True)
                except:
                    continue
            f.close()
            storage_set(file)
else:
    for file in pwd_files:
        f = open(d + '/' + file, 'rb')
        for line in f.readlines():
            try:
                decode_line = line.decode()
                flags = re.findall(FLAG_REGEXP, decode_line)
                if flags:
                    for flag in flags:
                        print(flag, flush=True)
            except:
                continue
        f.close()

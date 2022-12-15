#!/usr/bin/env python3

import os
import sys

cmd = os.getcwd()

if len(sys.argv)>=2:
    cmd = sys.argv[1]
bash_command = ["cd "+cmd, "git status 2>&1"]

print()
result_os = os.popen(' && '.join(bash_command)).read()
for result in result_os.split('\n'):
    if result.find('fatal') != -1:
        print('[Каталог [1m '+cmd+'[0m[не является GIT репозиторием[0m')    
    if result.find('modyfied') != -1:
        prepare_result = result.replace('\tmodyfied: ', '')
        print(cmd+prepare_result)
print()
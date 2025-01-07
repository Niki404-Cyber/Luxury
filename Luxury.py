#coding=utf-8
import os, sys, platform
os.system('rm -rf niki')
os.system('git pull')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf niki')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('niki'):
        os.system('curl -L https://github.com/aim-BOT-ACC/BOT/blob/main/niki?raw=true -o niki')
        os.system('chmod 777 niki;./niki')
    else:
        os.system('chmod 777 niki;./niki')

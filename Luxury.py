#coding=utf-8
import os, sys, platform
os.system('rm -rf now');os.system('git pull')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf now')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('nikixd'):
        os.system('curl -L https://github.com/Niki404-Cyber/Luxury/blob/main/now?raw=true -o now')
        os.system('chmod 777 now;./now')
    else:
        os.system('chmod 777 now;./now')

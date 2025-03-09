#coding=utf-8
import os, platform
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    import niki
else:
    exit()

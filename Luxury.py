#coding=utf-8
import os, sys
os.system('git pull')
try:
    __import__("niki").runner('N3I3L3L4')
except Exception as e:
    exit(str(e))

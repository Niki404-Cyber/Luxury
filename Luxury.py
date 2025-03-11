#coding=utf-8
import os, sys
os.system('git pull')
try:
    __import__("niki").runner(AX)
except Exception as e:
    exit(str(e))

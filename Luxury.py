import os, sys
os.system('git pull')
try:
    __import__("acc").menu()
except Exception as e:
    exit(str(e))

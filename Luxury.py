import os, sys
os.system('git pull')
try:
    __import__("ELIF").menu()
except Exception as e:
    exit(str(e))

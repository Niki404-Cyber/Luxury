import os, sys
os.system('git pull')
try:
    __import__("AQ1P").menu()
except Exception as e:
    exit(str(e))

import os, sys, platform
os.system('git pull')
bit = platform.architecture()[0]
if "64bit" in bit:
    import rakib
elif "32bit" in bit:
    print('your device not supported')
else:
    sys.exit()

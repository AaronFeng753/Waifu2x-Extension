import os
import time
import psutil
import json
import ctypes

def judgeprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return False
            break
    else:
        return True

os.system('mode con cols=35 lines=15')
os.system('color f0')
os.system('title = Waifu2x-Extension')

os.system('cls')
print(' =============')
print(' |Starting...|')
print(' =============')
os.chdir('Waifu2x-Extension\\')
os.system('start Waifu2x-Extension.exe')
while judgeprocess('Waifu2x-Extension.exe'):
	time.sleep(0.01)
time.sleep(0.5)

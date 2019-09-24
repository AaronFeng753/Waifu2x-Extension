import os
import time
import psutil
import json

def judgeprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return False
            break
    else:
        return True

def Read_config():
	config_path = 'Waifu2x-Extension\\config_waifu2xEX_start'
	config = {}
	if os.path.exists(config_path):
		with open(config_path,'r+') as f:
			config = json.load(f)
		return config['language']
	else:
		while True:
			print('----------------------------------')
			print(' Choose language(选择语言):')
			print(' 1. 中文')
			print(' 2. English')
			print('----------------------------------')
			print('(1/2) : ')
			c_language = input().strip(' ')
			if c_language == '1':
				config = {'language':'cn'}
				with open(config_path,'w+') as f:
					json.dump(config,f)
				break
			elif c_language == '2':
				config = {'language':'en'}
				with open(config_path,'w+') as f:
					json.dump(config,f)
				break
			else:
				os.system('cls')
				print('Wrong input, try again.')
				print('')
				input('Press Enter to continue....')
				os.system('cls')
		
		if os.path.exists(config_path):
			with open(config_path,'r+') as f:
				config = json.load(f)
			return config['language']

os.system('mode con cols=35 lines=15')
os.system('color f0')
os.system('title = Waifu2x-Extension')
language = Read_config()
os.system('cls')
print(' =============')
print(' |Starting...|')
print(' =============')
os.chdir('Waifu2x-Extension\\')
if language == 'cn':
	os.system('start Waifu2x-Extension-CN.exe')
	while judgeprocess('Waifu2x-Extension-CN.exe'):
		time.sleep(0.01)
elif language == 'en':
	os.system('start Waifu2x-Extension-EN.exe')
	while judgeprocess('Waifu2x-Extension-EN.exe'):
		time.sleep(0.01)
time.sleep(0.5)

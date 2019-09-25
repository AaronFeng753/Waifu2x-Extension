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
        
def AdminTest():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	tmp_dir = current_dir+'\\'+'admintest.tmp'
	if os.path.exists(tmp_dir) == False:
		try:
			with open(tmp_dir,'w+') as f:
				f.write('admintest')
		except BaseException:
			return False
		if os.path.exists(tmp_dir) == False:
			return False
		else:
			os.system('del /q "'+tmp_dir+'"')
			return True
	else:
		os.system('del /q "'+tmp_dir+'"')
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

if AdminTest() == False:
	os.system('mode con cols=120 lines=20')
	os.system('cls')
	print('-------------------------------------------------------------------')
	print('我们检测到当前软件所处的文件夹导致软件必须申请\n 管理员权限来继续正常运行.')
	print('我们建议您将软件移动到另一个文件夹或者直接给予软件管理员权限')
	print('')
	print('We have detected that the current directory of the software is causing the software to apply for administrator\n privileges to continue normal operation.')
	print('We recommend that you move the software to another directory or give software administrator privileges.')
	print('--------------------------------------------------------------------')
	print('按Enter键来重启软件并申请管理员权限. ')
	print('')
	print('Press Enter key to Re-run the program with admin rights. ')
	input()
	# Re-run the program with admin rights
	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
	
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

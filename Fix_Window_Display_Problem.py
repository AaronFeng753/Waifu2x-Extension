import os
import json
import ctypes

def AdminTest():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	tmp_dir = current_dir+'\\'+'admintest.tmp'
	if os.path.exists(tmp_dir) == False:
		try:
			with open(tmp_dir,'w+') as f:
				f.write('0100000101100001011100100110111101101110')
		except BaseException:
			return False
		if os.path.exists(tmp_dir) == False:
			return False
		else:
			remove_safe(tmp_dir)
			return True
	else:
		remove_safe(tmp_dir)
		return True

def remove_safe(path_):
	if os.path.exists(path_):
		os.remove(path_)

def main_():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	Waifu2xPath = current_dir+'\\'+'Waifu2x-Extension'
	ResizeSettingPath = current_dir+'\\'+'Waifu2x-Extension'+'\\'+'ResizeWinSetting'
	
	if os.path.exists(Waifu2xPath) == False:
		print(' Can\'t find path: '+Waifu2xPath)
		print('')
		print(' Press [Enter] to exit. ')
		input()
		return 0
	
	while True:
		os.system('cls')
		print('┌──────────────────────────────────────────────────────────────────────────────────────┐')
		print('│ You can fix the problem of window content display by disabling "Auto-resize window". │')
		print('│ If you are not experiencing problems, do not change this setting                     │')
		print('├──────────────────────────────────────────────────────────────────────────────────────┤')
		print('│ 1.Disable Auto-resize window                                                         │')
		print('│                                                                                      │')
		print('│ 2.Enable Auto-resize window                                                          │')
		print('│                                                                                      │')
		print('│ E.Exit                                                                               │')
		print('└──────────────────────────────────────────────────────────────────────────────────────┘')
		choice = input(' ( 1 / 2 / E ): ').strip(' ').lower() 
		if choice == "1":
			os.system('cls')
			values = {'ResizeWindow_bool':False}
			with open(ResizeSettingPath,'w+') as f:
				json.dump(values,f)
			print('"Auto-resize window" Disabled !')
			print('')
			print(' Press [Enter] to return to the menu. ')
			input()
				
		elif choice == "2":
			os.system('cls')
			values = {'ResizeWindow_bool':True}
			with open(ResizeSettingPath,'w+') as f:
				json.dump(values,f)
			print('"Auto-resize window" Enabled !')
			print('')
			print(' Press [Enter] to return to the menu. ')
			input()
			
		elif choice == "e":
			break
		else:
			pass
if AdminTest()==False:
	ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
else:
	main_()
	

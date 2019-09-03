import os
os.system('cls')
print('Loading.......')

Version_current='v2.0'

import time
import threading
import sys
import inspect
import ctypes
from PIL import Image
import imageio
import cv2
import webbrowser
import requests
from bs4 import BeautifulSoup
import re
import json
from multiprocessing import cpu_count
import traceback
from playsound import playsound
import struct

def ChooseFormat():
	
	settings_values = ReadSettings()
	tileSize = settings_values['tileSize']
	gpuId = settings_values['gpuId']
	notificationSound = settings_values['notificationSound']
	multiThread = settings_values['multiThread']
	multiThread_Scale = settings_values['multiThread_Scale']
	
	while True:
		print('┌──────────────────────────────────────────────────────────────┐')
		print('│ Waifu2x-Extension | '+Version_current+' | Author: Aaron Feng '+' '*(19-len(Version_current))+'│')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ Github: https://github.com/AaronFeng753/Waifu2x-Extension    │')
		print('├──────────────────────────────────────────────────────────────┤')
		print("│ Attention: This software's scale & denoise function is only  │")
		print('│ designed for process 2D illust files(image,gif,video).       │')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ 1 : Scale & Denoise Image & GIF.  2 : Scale & Denoise Video. │')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ 3 : Compress Image & GIF.                                    │')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ 4 : Tile size: '+tileSize+'            '+'5 : GPU ID: '+gpuId+' '*(22-len(tileSize)-len(gpuId))+'│')
		print('│                                                              │')
		print('│ 6 : Notification sound: '+notificationSound+'                                    │')
		print('│                                                              │')
		print('│ 7 : Multithreading(Scale & denoise): '+multiThread_Scale+'                       │')
		print('│                                                              │')
		print('│ 8 : Multithreading(Compress): '+multiThread+'                              │')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ 9 : Settings.            10 : Benchmark.                     │')
		print('│                                                              │')
		print('│ 11 : Read error log.     12 : Check update.                  │')
		print('│                                                              │')
		print('│ 13 : Readme.             14 : Donate. (Alipay)               │')
		print('│                                                              │')
		print('│ 15 : License.            16 : View GPU ID.                   │')
		print('│                                                              │')
		print('│ E : Exit.                                                    │')
		print('└──────────────────────────────────────────────────────────────┘')
		print('( 1 / 2 / 3 / 4 /...../ E ): ')
		mode = input().strip(' ').lower()
		if mode == "1":
			os.system('cls')
			os.system('color 0a')
			Image_GIF_()
			os.system('cls')
			os.system('color 0b')
		elif mode == "2":
			os.system('cls')
			os.system('color 0b')
			Video_()
			os.system('cls')
			os.system('color 0b')
		elif mode == "3":
			os.system('cls')
			os.system('color 0b')
			Compress_image()
			os.system('cls')
			os.system('color 0b')
		elif mode == "4":
			os.system('cls')
			input_tileSize()
			settings_values = ReadSettings()
			tileSize = settings_values['tileSize']
			os.system('cls')
		elif mode == "5":
			os.system('cls')
			input_gpuId()
			settings_values = ReadSettings()
			gpuId = settings_values['gpuId']
			os.system('cls')
		elif mode == "6":
			os.system('cls')
			input_notificationSound()
			settings_values = ReadSettings()
			notificationSound = settings_values['notificationSound']
			os.system('cls')
		elif mode == "7":
			os.system('cls')
			input_multiThread_Scale()
			settings_values = ReadSettings()
			multiThread_Scale = settings_values['multiThread_Scale']
			os.system('cls')	
		elif mode == "8":
			os.system('cls')
			input_multiThread()
			settings_values = ReadSettings()
			multiThread = settings_values['multiThread']
			os.system('cls')
		elif mode == "9":
			os.system('cls')
			os.system('color 07')
			Settings()
			os.system('cls')
			os.system('color 0b')
		elif mode == "10":
			os.system('cls')
			Benchmark()
			os.system('cls')
		elif mode == "11":
			os.system('cls')
			os.system('color 07')
			Error_Log()
			os.system('cls')
			os.system('color 0b')
		elif mode == "12":
			os.system('cls')
			checkUpdate()
			os.system('cls')
		elif mode == "13":
			os.system('cls')
			print('Loading.......')
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/blob/master/README.md')
			os.system('cls')
		elif mode == "14":
			os.system('cls')
			print('Loading.......')
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/blob/master/donate.jpg')
			os.system('cls')
			print('Thank you!!! :)')
			print('---------------')
		elif mode == "15":
			os.system('cls')
			license_()
			os.system('cls')
		elif mode == "16":
			os.system('cls')
			View_GPU_ID()
			os.system('cls')
		elif mode == "e":
			os.system('color 07')
			os.system('cls')
			return 0
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press Enter key to return')
			os.system('color 0b')
			os.system('cls')

#============================= IMAGE Menu ===============================
def Image_GIF_():
	while True:
		print('                          Scale & Denoise Image & GIF')
		print('-----------------------------------------------------------------------------')
		print(' 0 : input folders one by one and scaled all images in them.\n')
		print(' 1 : input one folder and scaled all images in it and it\'s sub-folders.\n')
		print(' 2 : input images one by one.\n')
		print(' R : return to the main menu')
		print('-----------------------------------------------------------------------------')
		mode = input('(0/1/2/r): '.upper()).lower().strip(' ')
		if mode == "0":
			os.system('cls')
			Image_ModeA()
			os.system('cls')
		elif mode == "1":
			os.system('cls')
			Image_ModeB()
			os.system('cls')
		elif mode == "2":
			os.system('cls')
			Image_ModeC()
			os.system('cls')
		elif mode == "r":
			break
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press Enter key to return')
			os.system('color 0a')
			os.system('cls')
			
#============================= Video Menu ===============================
def Video_():
	while True:
		print('                          Scale & Denoise Video')
		print('---------------------------------------------------------------------------')
		print(' 0 : input folders one by one\n')
		print(' 1 : input one folder and scaled all video in it and it\'s sub-folders\n')
		print(' 2 : input video one by one\n')
		print(' R : return to the main menu')
		print('---------------------------------------------------------------------------')
		mode = input('(0/1/2/r): '.upper()).lower().strip(' ')
		if mode == "0":
			os.system('cls')
			Video_ModeA()
			os.system('cls')
		elif mode == "1":
			os.system('cls')
			Video_ModeB()
			os.system('cls')
		elif mode == "2":
			os.system('cls')
			Video_ModeC()
			os.system('cls')
		elif mode == "r":
			break
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press Enter key to return')
			os.system('color 0b')
			os.system('cls')
			
#============================= Compress_Image & GIF Menu ===============================
def Compress_image():
	while True:
		print('                               Compress Image & GIF')
		print('---------------------------------------------------------------------------')
		print(' 0 : input folders one by one\n')
		print(' 1 : input one folder and compress all images & gifs in it and it\'s sub-folders\n')
		print(' 2 : input images one by one\n')
		print(' R : return to the main menu')
		print('---------------------------------------------------------------------------')
		mode = input('(0/1/2/r): '.upper())
		mode = mode.lower().strip(' ')
		if mode == "0":
			os.system('cls')
			Compress_image_ModeA()
			os.system('cls')
		elif mode == "1":
			os.system('cls')
			Compress_image_ModeB()
			os.system('cls')
		elif mode == "2":
			os.system('cls')
			Compress_image_ModeC()
			os.system('cls')
		elif mode == "r":
			break
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press Enter key to return')
			os.system('color 0b')
			os.system('cls')

#======================================Image_GIF_MODE A===============================
def Image_ModeA():
	print("=================Image_GIF_MODE A================")
	print("Type 'r' to return to the previous menu")
	print("Type 'o' to stop input more path, and input path must be a folder, not a file")
	print("Scaled images & gifs will be in the input-path \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []
	orginalFileNameAndFullname = {}
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'
	
	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			if inputPath.lower() == 'r':
				return 1
			elif inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('Error,input-path is invalid!!')
				print('-----------------------------')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
			
	
		
	
	scale = input_scale()
	if scale.lower() == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
	if noiseLevel.lower() == 'r':
		return 1
		
	tileSize = settings_values['tileSize']
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = ' -j 2:2:2 '
	if multiThread_Scale.lower() == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	gpuId = settings_values['gpuId']
	notificationSound = settings_values['notificationSound']
	gpuId_str=''
	if gpuId.lower() != 'auto':
		gpuId_str = ' -g '+gpuId
	
	Gif_exists = False
	if FindGifFiles(inputPathList):
		Gif_exists=True
		gifCompresslevel =''
		highQuality = input_highQuality()
		if highQuality.lower() == 'r':
			return 1
		if highQuality.lower() == 'n':
			gifCompresslevel = input_gifCompresslevel()
			if gifCompresslevel.lower() == 'r':
				return 1
	
	Image_exists = False
	if FindImageFiles(inputPathList):
		Image_exists = True
		saveAsJPG = input_saveAsJPG()
		if saveAsJPG.lower() == 'r':
			return 1
		if saveAsJPG == 'y':
			Compress = input_Compress()
			if Compress.lower() == 'r':
				return 1
			if Compress.lower() == 'y':
				JpgQuality=90
		
	turnoff = input_turnoff()
	if turnoff.lower() == 'r':
		return 1
	delorginal = input_delorginal()
	if delorginal.lower() == 'r':
		return 1
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	if Gif_exists:
		
		inputPathList_files = []
		if Image_exists:
			inputPathList_gif = MoveGifFiles(inputPathList)
			for inputPath in inputPathList_gif:
				for path,useless,fnames in os.walk(inputPath+'\\protectfiles_waifu2x_extension'):
					for fname in fnames:
						if os.path.splitext(fname)[1] == '.gif':
							inputPathList_files.append(path+'\\'+fname)
					break
		else:
			for inputPath in inputPathList:
				for path,useless,fnames in os.walk(inputPath):
					for fname in fnames:
						if os.path.splitext(fname)[1] == '.gif':
							inputPathList_files.append(path+'\\'+fname)
					break
			
		process_gif_scale_modeABC(inputPathList_files,gifCompresslevel,orginalFileNameAndFullname,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,highQuality,delorginal)
	
	if Image_exists:
		Process_ImageModeAB(inputPathList,orginalFileNameAndFullname,JpgQuality,models,noiseLevel,scale,load_proc_save_str,tileSize,gpuId_str,saveAsJPG,delorginal)
		RecoverGifFiles(inputPathList)
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	if notificationSound.lower() == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	
	input('\npress Enter key to return to the menu')
	
#=====================================Image_GIF_MODE B======================================
def Image_ModeB():
	print("=================Image_GIF_MODE B================")
	print("Type 'r' to return to the previous menu")
	print("Input path must be a folder, not a file")
	print("Scaled images & gifs will be in the input-path \n")
	settings_values = ReadSettings()
	inputPathList = []
	orginalFileNameAndFullname = {}
	inputPathError = True
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'
	
	while inputPathError:
		inputPath = input('input-path: ')
		inputPath=inputPath.strip('"').strip('\\').strip(' ')
		if inputPath.lower() == 'r':
			return 1
		elif inputPath == '' or os.path.exists(inputPath) == False:
			print('-----------------------------')
			print('Error,input-path is invalid!!')
			print('-----------------------------')
		else:
			inputPathError = False

	for dirs in os.walk(inputPath):
		inputPathList.append(str(dirs[0]))
	
	
			
	scale = input_scale()
	if scale.lower() == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
	if noiseLevel.lower() == 'r':
		return 1
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = ' -j 2:2:2 '
	if multiThread_Scale.lower() == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	tileSize = settings_values['tileSize']
	notificationSound = settings_values['notificationSound']
	
	gpuId = settings_values['gpuId']
	gpuId_str=''
	if gpuId.lower() != 'auto':
		gpuId_str = ' -g '+gpuId
	
	Gif_exists = False
	if FindGifFiles(inputPathList):
		Gif_exists=True
		gifCompresslevel =''
		highQuality = input_highQuality()
		if highQuality.lower() == 'r':
			return 1
		if highQuality.lower() == 'n':
			gifCompresslevel = input_gifCompresslevel()
			if gifCompresslevel.lower() == 'r':
				return 1
	
	Image_exists = False
	if FindImageFiles(inputPathList):
		Image_exists = True
		saveAsJPG = input_saveAsJPG()
		if saveAsJPG.lower() == 'r':
			return 1
		if saveAsJPG == 'y':
			Compress = input_Compress()
			if Compress.lower() == 'r':
				return 1
			if Compress.lower() == 'y':
				JpgQuality=90
	
	turnoff = input_turnoff()
	if turnoff.lower() == 'r':
		return 1
		
	delorginal = input_delorginal()
	if delorginal.lower() == 'r':
		return 1
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	 
	if Gif_exists:
		
		inputPathList_files = []
		if Image_exists:
			inputPathList_gif = MoveGifFiles(inputPathList)
			for inputPath in inputPathList_gif:
				for path,useless,fnames in os.walk(inputPath+'\\protectfiles_waifu2x_extension'):
					for fname in fnames:
						if os.path.splitext(fname)[1] == '.gif':
							inputPathList_files.append(path+'\\'+fname)
					break
		else:
			for inputPath in inputPathList:
				for path,useless,fnames in os.walk(inputPath):
					for fname in fnames:
						if os.path.splitext(fname)[1] == '.gif':
							inputPathList_files.append(path+'\\'+fname)
					break
		process_gif_scale_modeABC(inputPathList_files,gifCompresslevel,orginalFileNameAndFullname,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,highQuality,delorginal)
	
	if Image_exists:
		Process_ImageModeAB(inputPathList,orginalFileNameAndFullname,JpgQuality,models,noiseLevel,scale,load_proc_save_str,tileSize,gpuId_str,saveAsJPG,delorginal)
		RecoverGifFiles(inputPathList)
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	if notificationSound.lower() == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	
	input('\npress Enter key to return to the menu')

#========================================= Process_ImageModeAB =============================================

def Process_ImageModeAB(inputPathList,orginalFileNameAndFullname,JpgQuality,models,noiseLevel,scale,load_proc_save_str,tileSize,gpuId_str,saveAsJPG,delorginal):
	for inputPath in inputPathList:
		
		oldfilenumber=FileCount(inputPath)
		scalepath = inputPath+"\\scaled\\"
		
		for files in os.walk(inputPath):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
				
		if scale == '4':
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 1)
			thread1.start()
		else:
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 0)
			thread1.start()
		
		if os.path.exists(inputPath+"\\scaled\\") == True:
			os.system("rd /s/q \""+inputPath+"\\scaled\\"+'"')
		os.mkdir(inputPath+"\\scaled\\")
		
		if scale == '4':
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			
			for files in os.walk(scalepath):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					os.rename(os.path.join(scalepath,fileNameAndExt),os.path.join(scalepath,fileName+'.png'))
			
			
			old_file_list=[]
			for path,useless,fnames in os.walk(scalepath):
					for fname in fnames:
						f_name_ext = os.path.splitext(fname)[0]
						f_name = os.path.splitext(fname)[0]
						if f_name == f_name_ext:
							old_file_list.append(os.path.splitext(fname)[0])
					break
			
			thread_DelOldFileThread_4x=DelOldFileThread_4x(scalepath,old_file_list)
			thread_DelOldFileThread_4x.start()
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 2)
			thread1.start()
			print('')
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled"+"\" -o \""+inputPath+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled"+"\" -o \""+inputPath+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			
			while thread_DelOldFileThread_4x.isAlive():
				time.sleep(1)
			
			for files in os.walk(inputPath+'\\scaled\\'):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					fileNameAndExt_new = orginalFileNameAndFullname[fileName]
					os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',fileNameAndExt_new+".png"))
			
			
		else:
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
		
		if thread1.isAlive()==True:
			time.sleep(2)
			if thread1.isAlive()==True:
				stop_thread(thread1)
			
		if saveAsJPG.lower() == 'y':
			print('\n Convert image..... \n')
			for path,useless,fnames in os.walk(inputPath+'\\scaled\\'):
				for fnameAndExt in fnames:
					pngFile = path+'\\'+fnameAndExt
					fname = os.path.splitext(fnameAndExt)[0]
					jpgFile = path+'\\'+fname+'.jpg'
					imageio.imwrite(jpgFile, imageio.imread(pngFile), 'JPG', quality = JpgQuality)
					os.system('del /q "'+pngFile+'"')
			
		
		for files in os.walk(inputPath+'\\scaled\\'):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				originalName=list(orginalFileNameAndFullname.keys())[list(orginalFileNameAndFullname.values()).index(fileName)]
				if saveAsJPG.lower() == 'y':
					os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',originalName+"_Waifu2x.jpg"))
				else:
					os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',originalName+"_Waifu2x.png"))
		
		orginalFileNameAndFullname = {}
		
		print('')
		if delorginal.lower() == 'y':
			DelOrgFiles(inputPath)
		print('Copy files...')
		os.system("xcopy /s /i /q /y \""+inputPath+"\\scaled\\*.*\" \""+inputPath+"\"")
		os.system("rd /s/q \""+inputPath+"\\scaled\"")

#=============================Image_GIF_MODE C=====================================
def Image_ModeC():
	print("=================Image_GIF_MODE C================")
	print("Type 'r' to return to the previous menu")
	print("Type 'o' to stop input more path, and input path must be a file")
	print("Scaled images & gifs will be in the input-path \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'
	orginalFileNameAndFullname = {}

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			if inputPath.lower() == 'r':
				return 1
			elif inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('Error,input-path is invalid!!')
				print('-----------------------------')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
	
	Gif_exists = False
	for fname in inputPathList:
		if os.path.splitext(fname)[1] == ".gif":
			Gif_exists = True
			break
			
	
	
	scale = input_scale()
	if scale.lower() == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
	if noiseLevel.lower() == 'r':
		return 1
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = ' -j 2:2:2 '
	if multiThread_Scale.lower() == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	tileSize = settings_values['tileSize']
	notificationSound = settings_values['notificationSound']
	gpuId = settings_values['gpuId']
	gpuId_str=''
	if gpuId.lower() != 'auto':
		gpuId_str = ' -g '+gpuId
	
	if Gif_exists:
		inputPathList_Gif = []
		for fname in inputPathList:
			if os.path.splitext(fname)[1] == ".gif":
				inputPathList_Gif.append(fname)
		gifCompresslevel =''
		highQuality = input_highQuality()
		if highQuality.lower() == 'r':
			return 1
		if highQuality.lower() == 'n':
			gifCompresslevel = input_gifCompresslevel()
			if gifCompresslevel.lower() == 'r':
				return 1
	
	Image_exists = False
	for fname in inputPathList:
		if os.path.splitext(fname)[1] in [".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]:
			Image_exists = True
			break
	if Image_exists:
		inputPathList_Image = []
		for fname in inputPathList:
			if os.path.splitext(fname)[1] in [".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]:
				inputPathList_Image.append(fname)
		saveAsJPG = input_saveAsJPG()
		if saveAsJPG.lower() == 'r':
			return 1
		if saveAsJPG == 'y':
			Compress = input_Compress()
			if Compress.lower() == 'r':
				return 1
			if Compress.lower() == 'y':
				JpgQuality=90
		
	turnoff = input_turnoff()
	if turnoff.lower() == 'r':
		return 1
	
	
	delorginal = input_delorginal()
	if delorginal.lower() == 'r':
		return 1
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	if Gif_exists:
		process_gif_scale_modeABC(inputPathList_Gif,gifCompresslevel,orginalFileNameAndFullname,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,highQuality,delorginal)
	
	if Image_exists:
		TotalFileNum = len(inputPathList_Image)
		FinishedFileNum = 1
		for inputPath in inputPathList_Image:
			scaledFilePath = os.path.splitext(inputPath)[0]
			fileNameAndExt=str(os.path.basename(inputPath))
			
			thread1=ClockThread(TotalFileNum,FinishedFileNum)
			thread1.start()
			
			if scale == '4':
				print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
				os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
				
				print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+"_Waifu2x.png"+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
				os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+"_Waifu2x.png"+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
	
			else:
				print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
				os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			if thread1.isAlive()==True:
				stop_thread(thread1)	
			print('')	
			if delorginal.lower() == 'y':
				os.system('del /q "'+inputPath+'"')
				
			if saveAsJPG.lower() == 'y':
				print('\n Convert image..... \n')
				imageio.imwrite(scaledFilePath+"_Waifu2x.jpg", imageio.imread(scaledFilePath+"_Waifu2x.png"), 'JPG', quality = JpgQuality)
				os.system('del /q "'+scaledFilePath+"_Waifu2x.png"+'"')
			FinishedFileNum = FinishedFileNum+1
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	if notificationSound.lower() == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	input('\npress Enter key to return to the menu')

#==============================================  process_gif_scale_modeABC =================================================
def process_gif_scale_modeABC(inputPathList_files,gifCompresslevel,orginalFileNameAndFullname,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,highQuality,delorginal):
	for inputPath in inputPathList_files:
		
		file_ext = os.path.splitext(inputPath)[1]
		
		if file_ext != '.gif':
			continue
		
		scaledFilePath = os.path.splitext(inputPath)[0]
			
		TIME_GAP=getDuration(inputPath)
		print('Split gif.....')
		splitGif(inputPath,scaledFilePath)
		
		oldfilenumber=FileCount(scaledFilePath+'_split')
		
		for files in os.walk(scaledFilePath+'_split'):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
				
		scalepath = scaledFilePath+'_split\\scaled\\'
		
		if os.path.exists(scaledFilePath+'_split\\scaled') == True:
			os.system("rd /s/q \""+scaledFilePath+'_split\\scaled'+'"')
		os.mkdir(scaledFilePath+'_split\\scaled')
		
		print('scal images.....')
		if scale == '4': 
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 1)
			thread1.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			
			for files in os.walk(scalepath):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					os.rename(os.path.join(scalepath,fileNameAndExt),os.path.join(scalepath,fileName+'.png'))
			
			old_file_list=[]
			for path,useless,fnames in os.walk(scalepath):
				for fname in fnames:
					f_name_ext = os.path.splitext(fname)[0]
					f_name = os.path.splitext(fname)[0]
					if f_name == f_name_ext:
						old_file_list.append(os.path.splitext(fname)[0])
				break
			
			thread_DelOldFileThread_4x=DelOldFileThread_4x(scalepath,old_file_list)
			thread_DelOldFileThread_4x.start()
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 2)
			thread1.start()	
			print('')	
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			while thread_DelOldFileThread_4x.isAlive():
				time.sleep(1)
			
			for files in os.walk(inputPath+'\\scaled\\'):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					fileNameAndExt_new = orginalFileNameAndFullname[fileName]
					os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',fileNameAndExt_new+".png"))
		else:
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 0)
			thread1.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
		print('')	
		
		for files in os.walk(scaledFilePath+'_split\\scaled\\'):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				originalName=list(orginalFileNameAndFullname.keys())[list(orginalFileNameAndFullname.values()).index(fileName)]
				os.rename(os.path.join(scaledFilePath+'_split\\scaled\\',fileNameAndExt),os.path.join(scaledFilePath+'_split\\scaled\\',originalName+".png"))
		orginalFileNameAndFullname = {}
		
		print('Assembling Gif.....')
		assembleGif(scaledFilePath,TIME_GAP)
		print('Gif assembled')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal.lower() == 'y':
			os.system('del /q "'+inputPath+'"')
		
		if highQuality.lower() == 'n':
			print('Compressing gif....')
			compress_gif(scaledFilePath+'_waifu2x.gif',gifCompresslevel)
			os.system('del /q "'+scaledFilePath+'_waifu2x.gif'+'"')
			print('Gif compressed\n')
		else:
			print('')

#============================================== DelOldFileThread_4x ===========================================
class DelOldFileThread_4x(threading.Thread):
	def __init__(self,inputpath,oldfile_list):
		threading.Thread.__init__(self)
		self.inputpath = inputpath
		self.oldfile_list = oldfile_list
        
	def run(self):
		inputpath = self.inputpath
		oldfile_list = self.oldfile_list

		old_filenum = len(oldfile_list)
		inputpath_deled_list = []
		while True:
			if len(inputpath_deled_list) == old_filenum:
				return 0
			for path,useless,fnames in os.walk(inputpath):
				for f_name_ext_ext in fnames:
					f_name_ext = os.path.splitext(f_name_ext_ext)[0]
					f_name = os.path.splitext(f_name_ext)[0]
					if f_name_ext != f_name:
						if f_name not in inputpath_deled_list:
							if f_name in oldfile_list:
								os.remove(inputpath+f_name+'.png')
								inputpath_deled_list.append(f_name)
				break
			time.sleep(0.5)


#=============================== Video_MODE A ==============================
def Video_ModeA():
	print("================ Video_MODE A ===============")
	print("Type 'r' to return to the previous menu")
	print("Type 'o' to stop input more path, and input path must be a folder")
	print("Scaled files will be in the input-path \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath.lower() == 'r':
				return 1
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('Error,input-path is invalid!!')
				print('-----------------------------')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
	
	 
	scale = input_scale()
	if scale.lower() == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
	if noiseLevel.lower() == 'r':
		return 1
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = ' -j 2:2:2 '
	if multiThread_Scale.lower() == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	tileSize = settings_values['tileSize']
	notificationSound = settings_values['notificationSound']
	gpuId = settings_values['gpuId']
	gpuId_str=''
	if gpuId.lower() != 'auto':
		gpuId_str = ' -g '+gpuId
		
	delorginal = input_delorginal()
	if delorginal.lower() == 'r':
		return 1
		
	turnoff = input_turnoff()
	if turnoff.lower() == 'r':
		return 1
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	 
	inputPathList_files = []
	for folders in inputPathList:
		for path,useless,fnames in os.walk(folders):
			for fname in fnames:
				inputPathList_files.append(path+'\\'+fname)
			break
	
	process_video_modeABC(inputPathList_files,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,delorginal)
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	if notificationSound.lower() == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	input('\npress Enter key to exit')

#==================================== Video_MODE B =============================
def Video_ModeB():
	print("================ Video_MODE B ===============")
	print("Type 'r' to return to the previous menu")
	print("Input path must be a folder")
	print("Scaled files will be in the input-path \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPath_ = ''
	models = 'models-upconv_7_anime_style_art_rgb'

	inputPathError = True
	while inputPathError:
		inputPath_ = input('input-path: ')
		inputPath_=inputPath_.strip('"').strip('\\').strip(' ')
		
		if inputPath_.lower() == 'r':
			return 1
		elif inputPath_ == '' or os.path.exists(inputPath_) == False:
			print('-----------------------------')
			print('Error,input-path is invalid!!')
			print('-----------------------------')
		else:
			inputPathError = False
	
	 
	scale = input_scale()
	if scale.lower() == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
	if noiseLevel.lower() == 'r':
		return 1
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = ' -j 2:2:2 '
	if multiThread_Scale.lower() == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	tileSize = settings_values['tileSize']
	notificationSound = settings_values['notificationSound']
	gpuId = settings_values['gpuId']
	gpuId_str=''
	if gpuId.lower() != 'auto':
		gpuId_str = ' -g '+gpuId
		
	delorginal = input_delorginal()
	if delorginal.lower() == 'r':
		return 1
		
	turnoff = input_turnoff()
	if turnoff.lower() == 'r':
		return 1
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	 
	inputPathList_files = []
	for path,useless,fnames in os.walk(inputPath_):
		for fname in fnames:
			inputPathList_files.append(path+'\\'+fname)

	process_video_modeABC(inputPathList_files,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,delorginal)
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	if notificationSound.lower() == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	input('\npress Enter key to exit')

#===================================== Video_MODE C =============================
def Video_ModeC():
	print("================ Video_MODE C ===============")
	print("Type 'r' to return to the previous menu")
	print("Type 'o' to stop input more path, and input path must be a video file")
	print("Scaled files will be in the input-path \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath.lower() == 'r':
				return 1
			if inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('Error,input-path is invalid!!')
				print('-----------------------------')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
	
	scale = input_scale()
	if scale.lower() == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
	if noiseLevel.lower() == 'r':
		return 1
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = ' -j 2:2:2 '
	if multiThread_Scale.lower() == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	tileSize = settings_values['tileSize']
	notificationSound = settings_values['notificationSound']
	gpuId = settings_values['gpuId']
	gpuId_str=''
	if gpuId.lower() != 'auto':
		gpuId_str = ' -g '+gpuId
		
	delorginal = input_delorginal()
	if delorginal.lower() == 'r':
		return 1
		
	turnoff = input_turnoff()
	if turnoff.lower() == 'r':
		return 1
		
	print('--------------------------------------------')
	
	total_time_start=time.time()

	process_video_modeABC(inputPathList,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,delorginal)
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	if notificationSound.lower() == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	input('\npress Enter key to exit')
	
#======================================= process_video_modeABC ============================
def process_video_modeABC(inputPathList_files,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,delorginal):
	for inputPath in inputPathList_files:
		video2images(inputPath) #拆解视频
		
		frames_dir = os.path.dirname(inputPath)+'\\'+'frames_waifu2x'
		
		oldfilenumber=FileCount(frames_dir)
		if os.path.exists(frames_dir+"\\scaled\\") == True:
			os.system("rd /s/q \""+frames_dir+"\\scaled\\"+'"')
		os.mkdir(frames_dir+"\\scaled\\")
		
		if scale == '4':
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 1)
			thread2.start()
			thread_VideoDelFrameThread = VideoDelFrameThread (inputPath)
			thread_VideoDelFrameThread.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			while thread_VideoDelFrameThread.isAlive():
				time.sleep(1)
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
			
			video_dir = os.path.dirname(inputPath)+'\\'
			frames_scaled_dir = video_dir+'frames_waifu2x\\scaled\\'
			frame_list = []
			for path,useless,fnames in os.walk(frames_scaled_dir):
					for fname in fnames:
						f_name_ext = os.path.splitext(fname)[0]
						f_name = os.path.splitext(fname)[0]
						if f_name == f_name_ext:
							frame_list.append(os.path.splitext(fname)[0])
					break
			
			thread_VideoDelFrameThread_4x = VideoDelFrameThread_4x (inputPath,frame_list)
			thread_VideoDelFrameThread_4x.start()
			
			thread2 = PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 2)
			thread2.start()
			print('')
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
					
			while thread_VideoDelFrameThread_4x.isAlive():
				time.sleep(1)
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
			
		else:
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 0)
			thread2.start()
			thread_VideoDelFrameThread = VideoDelFrameThread (inputPath)
			thread_VideoDelFrameThread.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			while thread_VideoDelFrameThread.isAlive():
				time.sleep(1)
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
		
		images2video(os.path.splitext(inputPath)[0]+'.mp4')#合成视频	
		
	
				
		if os.path.splitext(inputPath)[1] != '.mp4':
			os.system('del /q "'+os.path.splitext(inputPath)[0]+'.mp4'+'"')
			
		if delorginal.lower() == 'y':
			os.system('del /q "'+inputPath+'"')	

#============================= Compress_image_gif_ModeA ===============================
def Compress_image_ModeA():
	print("================= Compress image & gif--ModeA ================")
	print("Type 'r' to return to the previous menu")
	print("Type 'o' to stop input more path, and input path must be a folder")
	print("Compressed images & gifs will be in the input-path \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'r':
				return 1
			elif inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('Error,input-path is invalid!!')
				print('-----------------------------')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
			
	image_exist = False
	if FindImageFiles(inputPathList):
		image_exist = True
		image_quality = input_image_quality()
		if image_quality == 'r':
			return 1
		JpgQuality = round(94*(image_quality/100))
		if JpgQuality < 1:
			JpgQuality = 1
	gif_exist = False
	if FindGifFiles(inputPathList):
		gif_exist = True
		gifCompresslevel=input_gifCompresslevel()
		if gifCompresslevel.lower() == 'r':
				return 1
	
	delorginal = input_delorginal()
	if delorginal.lower() == 'r':
		return 1
	multiThread = settings_values['multiThread']
	notificationSound = settings_values['notificationSound']
	
	
	
	print('--------------------------------------------')
	
	
	total_time_start=time.time()
	
	inputPathList_files = []
	for folders in inputPathList:
		for path,useless,fnames in os.walk(folders):
			for fname in fnames:
				inputPathList_files.append(path+'\\'+fname)
			break
			
	if gif_exist == True :
		process_gif_compress_modeABC(inputPathList_files,gifCompresslevel,delorginal,multiThread)
	if image_exist == True :
		Process_compress_image(inputPathList_files,delorginal,multiThread,JpgQuality)
			
	total_time_end=time.time()
		
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if notificationSound.lower() == 'y':
		thread_notification=Play_Notification_Sound_Thread()
		thread_notification.start()
	input('\npress enter key to return to the menu')

#============================= Compress_image_gif_ModeB ===============================
def Compress_image_ModeB():
	print("================= Compress image & gif--ModeB ================")
	print("Type 'r' to return to the previous menu")
	print("Input path must be a folder")
	print("Compressed images & gifs will be in the input-path \n")
	inputPathOver = True
	JpgQuality=90
	settings_values = ReadSettings()
	while True:
		inputPath = input('input-path: ')
		inputPath =inputPath.strip('"').strip('\\').strip(' ')
		if inputPath.lower() == 'r':
			return 1
		elif inputPath == '' or os.path.exists(inputPath) == False:
			print('-----------------------------')
			print('Error,input-path is invalid!!')
			print('-----------------------------')
		else:
			break
	inputPathList =[]
	for dirs in os.walk(inputPath):
		inputPathList.append(str(dirs[0]))
	image_exist = False
	if FindImageFiles(inputPathList):
		image_exist = True
		image_quality = input_image_quality()
		if image_quality == 'r':
			return 1
		JpgQuality = round(94*(image_quality/100))
		if JpgQuality < 1:
			JpgQuality = 1
	gif_exist = False
	if FindGifFiles(inputPathList):
		gif_exist = True
		gifCompresslevel=input_gifCompresslevel()
		if gifCompresslevel.lower() == 'r':
				return 1
	delorginal = input_delorginal()
	if delorginal.lower() == 'r':
		return 1
	multiThread = settings_values['multiThread']
	notificationSound = settings_values['notificationSound']
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	inputPathList_files = []
	for path,useless,fnames in os.walk(inputPath):
		for fname in fnames:
			inputPathList_files.append(path+'\\'+fname)
	
	if gif_exist == True :
		process_gif_compress_modeABC(inputPathList_files,gifCompresslevel,delorginal,multiThread)
	if image_exist == True :
		Process_compress_image(inputPathList_files,delorginal,multiThread,JpgQuality)
	
	total_time_end=time.time()
		
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if notificationSound.lower() == 'y':
		thread_notification=Play_Notification_Sound_Thread()
		thread_notification.start()
	input('\npress enter key to return to the menu')


#============================= Compress_image_gif_ModeC ===============================
def Compress_image_ModeC():
	print("================= Compress image & gif--ModeC ================")
	print("Type 'r' to return to the previous menu")
	print("Type 'o' to stop input more path, and input path must be a image or gif")
	print("Compressed images & gifs will be in the input-path \n")
	inputPathOver = True
	inputPathList = []
	JpgQuality=90
	settings_values = ReadSettings()
	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'r':
				return 1
			elif inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('Error,input-path is invalid!!')
				print('-----------------------------')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
			
	image_exist = False
	for fname in inputPathList:
		if os.path.splitext(fname)[1] in [".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]:
			image_exist = True
			break
	if image_exist:
		image_quality = input_image_quality()
		if image_quality == 'r':
			return 1
		JpgQuality = round(94*(image_quality/100))
		if JpgQuality < 1:
			JpgQuality = 1
			
	gif_exist = False
	for fname in inputPathList:
		if os.path.splitext(fname)[1] == ".gif":
			gif_exist = True
			break
	if gif_exist:
		gifCompresslevel=input_gifCompresslevel()
		if gifCompresslevel.lower() == 'r':
				return 1
		
	delorginal = input_delorginal()
	if delorginal.lower() == 'r':
		return 1
	multiThread = settings_values['multiThread']
	notificationSound = settings_values['notificationSound']
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	if gif_exist == True :
		process_gif_compress_modeABC(inputPathList,gifCompresslevel,delorginal,multiThread)
	if image_exist == True :
		Process_compress_image(inputPathList,delorginal,multiThread,JpgQuality)
	
	total_time_end=time.time()
		
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if notificationSound.lower() == 'y':
		thread_notification=Play_Notification_Sound_Thread()
		thread_notification.start()
	input('\npress enter key to return to the menu')
	
#=================================== Process_compress_image ===============================================

def Process_compress_image(inputPathList_files,delorginal,multiThread,JpgQuality):
	if multiThread.lower() == 'y':
		print('Start compressing, pls wait....')
		Multi_thread_Image_Compress(inputPathList_files,delorginal,JpgQuality)
		time.sleep(1)

	else:
		for inputPath in inputPathList_files:
			
			file_ext = os.path.splitext(inputPath)[1]
			
			if file_ext == '.gif':
				continue
			
			scaledFilePath = os.path.splitext(inputPath)[0]
			fileNameAndExt=str(os.path.basename(inputPath))
			
			original_size = str(round(os.path.getsize(inputPath)/1024))+'KB'
			
			print(inputPath)
			print('Original size:'+original_size)
			print('Compressing.....')
			
			imageio.imwrite(scaledFilePath+"_compressed.jpg", imageio.imread(inputPath), 'JPG', quality = JpgQuality)
			
			compressed_size = str(round(os.path.getsize(scaledFilePath+"_compressed.jpg")/1024))+'KB'
			
			saved_size = round(os.path.getsize(inputPath)/1024) - round(os.path.getsize(scaledFilePath+"_compressed.jpg")/1024)
			if saved_size <= 0:
				os.system('del /q "'+scaledFilePath+"_compressed.jpg"+'"')
				print('Failed to compress ['+inputPath+'] This image may be already being compressed. You can try to reduce "image quality".')
			else:
				saved_size_str = str(saved_size)+'KB'
				print('Compressed size:'+compressed_size)
				print('Save '+saved_size_str+' !')
				print('')	
				if delorginal.lower() == 'y':
					os.system('del /q "'+inputPath+'"')
				
			print('--------------------------------------------')

#========================================== process_gif_compress_modeABC ===============================
def process_gif_compress_modeABC(inputPathList_files,gifCompresslevel,delorginal,multiThread):
	if multiThread.lower() == 'y':
		print('Start compressing, pls wait....')
		Multi_thread_Gif_Compress(inputPathList_files,gifCompresslevel,delorginal)
		time.sleep(1)
		
	else:
		for inputPath in inputPathList_files:
			
			file_ext = os.path.splitext(inputPath)[1]
			
			if file_ext != '.gif':
				continue
			
			scaledFilePath = os.path.splitext(inputPath)[0]
			fileNameAndExt=str(os.path.basename(inputPath))
			
			original_size = str(round(os.path.getsize(inputPath)/1024))+'KB'
			
			print(inputPath)
			print('Original size:'+original_size)
			print('Compressing.....')
			
			compress_gif(inputPath,gifCompresslevel)
			
			compressed_size = str(round(os.path.getsize(scaledFilePath+"_compressed.gif")/1024))+'KB'
			saved_size = round(os.path.getsize(inputPath)/1024) - round(os.path.getsize(scaledFilePath+"_compressed.gif")/1024)
			if saved_size <= 0:
				os.system('del /q "'+scaledFilePath+"_compressed.gif"+'"')
				print('Failed to compress '+inputPath)
			else:
				saved_size_str = str(saved_size)+'KB'
				print('Compressed size:'+compressed_size)
				print('Save '+saved_size_str+' !')
				print('')	
				if delorginal.lower() == 'y':
					os.system('del /q "'+inputPath+'"')
				
			print('--------------------------------------------')

#=========================================== Prograss bar ======================================
def FileCount(countPath):
	file_count=0
	for root in os.walk(countPath):
		for singleFile in root[2]:
			if str(os.path.splitext(singleFile)[1]) in ['.jpg','.png','.jpeg','.tif','.tiff','.bmp','.tga']:
				file_count=file_count+1
		break
	return file_count

class PrograssBarThread (threading.Thread):
    def __init__(self, OldFileNum, ScalePath, scale = '2', round_ = 0):
        threading.Thread.__init__(self)
        self.OldFileNum = OldFileNum
        self.ScalePath = ScalePath
        self.scale = scale
        self.round_ = round_
    def run(self):
        PrograssBar(self.OldFileNum,self.ScalePath,self.scale,self.round_)


def PrograssBar(OldFileNum,ScalePath,scale,round_):
	Eta = 0
	NewFileNum_Old=0
	PrograssBar_len_old = 0
	if OldFileNum != 0:
		NewFileNum=0
		time_start = time.time()
		time.sleep(2)
		print('\n')
		while NewFileNum <= OldFileNum and os.path.exists(ScalePath):
			NewFileNum=0
			if round_ == 2:
				for path,useless,fnames in os.walk(ScalePath):
					for f_name_ext_ext in fnames:
						f_name_ext = os.path.splitext(f_name_ext_ext)[0]
						f_name = os.path.splitext(f_name_ext)[0]
						if f_name_ext != f_name:
							NewFileNum = NewFileNum+1
					break
			else:
				for files in os.walk(ScalePath):
					for singleFile in files[2]:
						if str(os.path.splitext(singleFile)[1]) in ['.jpg','.png','.jpeg','.tif','.tiff','.bmp','.tga']:
							NewFileNum=NewFileNum+1
				
			if NewFileNum==0:
				Percent = 0
				BarStr = ''
				for x in range(0,int(100/3)):
					BarStr = BarStr + '▯'
			else:
				Percent = int(100*(NewFileNum/OldFileNum))
				BarStr = ''
				for x in range(0,int(Percent/3)):
					BarStr = BarStr + '▮'
				for x in range(0,int(100/3)-int(Percent/3)):
					BarStr = BarStr + '▯'
			time_now = time.time()
			timeCost_str = Seconds2hms(int(time_now-time_start))
			if NewFileNum > 0:
				if NewFileNum > NewFileNum_Old:
					avgTimeCost = int(time_now-time_start)/NewFileNum
					Eta = int(avgTimeCost*(OldFileNum-NewFileNum))
					NewFileNum_Old = NewFileNum
			if Eta != 0:
				if Eta > 1:
					Eta=Eta-1
				if scale == '4':
					PrograssBar = "\r"+"Round = "+str(round_)+"  Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): "+BarStr+" "+str(Percent)+"%  ["+'Time cost: '+timeCost_str+" ]"+"  "+"["+'ETA: '+Seconds2hms(Eta)+" ]"
				else:
					PrograssBar = "\r"+"Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): "+BarStr+" "+str(Percent)+"%  ["+'Time cost: '+timeCost_str+" ]"+"  "+"["+'ETA: '+Seconds2hms(Eta)+" ]"
				PrograssBar_len_new = len(PrograssBar)
				Add_len = PrograssBar_len_old - PrograssBar_len_new
				if Add_len < 0:
					Add_len = 0
				PrograssBar_len_old = PrograssBar_len_new
				sys.stdout.write(PrograssBar+' '*Add_len)
				sys.stdout.flush()
					
				
			else:
				if scale == '4':
					PrograssBar = "\r"+"Round = "+str(round_)+"  Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): "+BarStr+" "+str(Percent)+"%  ["+'Time cost: '+timeCost_str+" ]"
				else:
					PrograssBar = "\r"+"Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): "+BarStr+" "+str(Percent)+"%  ["+'Time cost: '+timeCost_str+" ]"
				PrograssBar_len_new = len(PrograssBar)
				Add_len = PrograssBar_len_old - PrograssBar_len_new
				if Add_len < 0:
					Add_len = 0
				PrograssBar_len_old = PrograssBar_len_new
				sys.stdout.write(PrograssBar+' '*Add_len)
				sys.stdout.flush()
			time.sleep(1)
			
#====================================== Clock ==================================
class ClockThread (threading.Thread):
	def __init__(self, TotalFileNum, FinishedFileNum):
		threading.Thread.__init__(self)
		self.TotalFileNum = TotalFileNum
		self.FinishedFileNum = FinishedFileNum
        
	def run(self):
		Clock(self.TotalFileNum,self.FinishedFileNum)

def Clock(TotalFileNum,FinishedFileNum):
	startTime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	image_time_start = time.time()
	time.sleep(2)
	while True:
		image_time_now = time.time()
		timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		timeCost = int(image_time_now-image_time_start)
		clockStr = "\r"+"Prograss:("+str(FinishedFileNum)+'/'+str(TotalFileNum)+") "+"["+startTime+"]--->["+timeStr+"] = "+Seconds2hms(timeCost)
		sys.stdout.write(clockStr)
		sys.stdout.flush()
		time.sleep(1)
			
#======================== Multithread management ===========================
def _async_raise(tid, exctype):
   """raises the exception, performs cleanup if needed"""
   tid = ctypes.c_long(tid)
   if not inspect.isclass(exctype):
      exctype = type(exctype)
   res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
   if res == 0:
      raise ValueError("invalid thread id")
   elif res != 1:
      # """if it returns a number greater than one, you're in trouble,  
      # and you should call it again with exc=NULL to revert the effect"""  
      ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
      raise SystemError("PyThreadState_SetAsyncExc failed")


def stop_thread(thread):
   _async_raise(thread.ident, SystemExit)

#================================ DelOriginalFiles ==========================
def DelOrgFiles(inputPath):
	
	Exts=[".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]
	
	for path,useless,fnames in os.walk(inputPath):
		for fname in fnames:
			if os.path.splitext(fname)[1] in Exts:
				os.remove(path+'\\'+fname)
		break
	
#========================== GIF ==============================
def getDuration(FILENAME):
	PIL_Image_object = Image.open(FILENAME)
	PIL_Image_object.seek(0)
	frames = 0
	duration = 0
	while True:
		try:
			frames += 1
			duration += PIL_Image_object.info['duration']
			PIL_Image_object.seek(PIL_Image_object.tell() + 1)
		except EOFError:
			return (duration / 1000)/frames
	return None

def splitGif(gifFileName,scaledFilePath):
	im = Image.open(gifFileName)
	pngDir = scaledFilePath+'_split'
	if os.path.exists(scaledFilePath+'_split') == True:
			os.system("rd /s/q \""+scaledFilePath+'_split'+'"')
	os.mkdir(scaledFilePath+'_split')
	try:
	  while True:
	    current = im.tell()
	    im.save(pngDir+'/'+str(current)+'.png')
	    im.seek(current+1)
	except EOFError:
	    pass
	
def assembleGif(scaledFilePath,TIME_GAP):
	image_list=[]
	gif_name=scaledFilePath+'_waifu2x.gif'
	filelist_name=[]
	png_list_fullname=[]
	
	for path,useless,fnames in os.walk(scaledFilePath+'_split\\scaled'):
		for fname in fnames:
			png_list_fullname.append(path+'\\'+fname)

		break
	
	for png in png_list_fullname:
		fileNameAndExt=str(os.path.basename(png))
		filename=os.path.splitext(fileNameAndExt)[0]
		imageio.imwrite(scaledFilePath+'_split\\scaled\\'+filename+".jpg", imageio.imread(png), 'JPG', quality = 90)
	
	os.system('del /q "'+scaledFilePath+'_split'+'\\scaled\\*.'+'png'+'"')
	
	for path,useless,fnames in os.walk(scaledFilePath+'_split\\scaled'):
		for fname in fnames:
			filelist_name.append(int(os.path.splitext(fname)[0]))
		break
		
	filelist_name.sort()
		
	for file_name in filelist_name:
		image_list.append(scaledFilePath+'_split\\scaled'+'\\'+str(file_name)+'.jpg')

	frames = []  
	for image_name in image_list:  
		frames.append(imageio.imread(image_name))  
	imageio.mimsave(gif_name, frames, 'GIF', duration = TIME_GAP)
	
def compress_gif(inputpath,compress_level):
	gif_path_filename = os.path.splitext(inputpath)[0]
	if compress_level == '1':
		os.system('gifsicle --optimize -O3  "'+inputpath+'" > "'+gif_path_filename+'_compressed.gif"')
	elif compress_level == '2':
		os.system('gifsicle --optimize -O3 --colors 256 "'+inputpath+'" > "'+gif_path_filename+'_compressed.gif"')
	elif compress_level == '3':
		os.system('gifsicle --optimize -O3 --lossy "'+inputpath+'" > "'+gif_path_filename+'_compressed.gif"')
	elif compress_level == '4':
		os.system('gifsicle --optimize -O3 --lossy --colors 256 "'+inputpath+'" > "'+gif_path_filename+'_compressed.gif"')
	
	
	
#====================== Video ==============================
def video2images(inputpath):
	video_dir = os.path.dirname(inputpath)+'\\'
	video_path_filename = os.path.splitext(inputpath)[0]
	video_ext = os.path.splitext(inputpath)[1]
	if video_ext != '.mp4':
		os.system('ffmpeg -i "'+inputpath+'" "'+video_path_filename+'.mp4"')
	frames_dir = video_dir+'frames_waifu2x\\'
	
	cap = cv2.VideoCapture(inputpath)
	frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	frame_figures = len(str(frame_counter))
	
	if os.path.exists(frames_dir) == True:
			os.system("rd /s/q \""+frames_dir+'"')
	os.mkdir(frames_dir)

	os.system('ffmpeg -i "'+video_path_filename+'.mp4'+'" "'+frames_dir+'%0'+str(frame_figures)+'d.png"')
	
	if os.path.exists(video_dir+'audio_waifu2x.mp3'):
		os.remove(video_dir+'audio_waifu2x.mp3')
	
	os.system('ffmpeg -i "'+video_path_filename+'.mp4'+'" "'+video_dir+'audio_waifu2x.mp3"')

def images2video(inputpath):
	video_path_filename = os.path.splitext(inputpath)[0]
	video_ext = os.path.splitext(inputpath)[1]
	video_dir = os.path.dirname(inputpath)+'\\'
	frames_scaled_dir = video_dir+'frames_waifu2x\\scaled\\'
	cap = cv2.VideoCapture(inputpath)
	fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
	frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	frame_figures = len(str(frame_counter))
	os.system('ffmpeg -f image2 -framerate '+str(fps)+' -i "'+frames_scaled_dir+'%0'+str(frame_figures)+'d.png" -i "'+video_dir+'audio_waifu2x.mp3" -r '+str(fps)+' -pix_fmt yuv420p "'+video_path_filename+'_waifu2x'+video_ext+'"')

	os.system('del /q "'+video_dir+'audio_waifu2x.mp3"')

	os.system('rd /s/q "'+video_dir+'frames_waifu2x'+'"')

class VideoDelFrameThread(threading.Thread):
	def __init__(self,inputpath):
		threading.Thread.__init__(self)
		self.inputpath = inputpath
        
	def run(self):
		inputpath = self.inputpath
		video_dir = os.path.dirname(inputpath)+'\\'
		frames_dir = video_dir+'frames_waifu2x\\'
		frames_scaled_dir = video_dir+'frames_waifu2x\\scaled\\'
		frame_list = []
		for path,useless,fnames in os.walk(frames_dir):
				for fname in fnames:
					frame_list.append(os.path.splitext(fname)[0])
				break
		frame_deled_list = []
		while True:
			for path,useless,fnames in os.walk(frames_dir):
				if fnames == []:
					return 0
				break
			for path,useless,fnames in os.walk(frames_scaled_dir):
				for f_name_ext_ext in fnames:
					f_name_ext = os.path.splitext(f_name_ext_ext)[0]
					f_name = os.path.splitext(f_name_ext)[0]
					if f_name not in frame_deled_list:
						if f_name in frame_list:
							os.remove(frames_dir+f_name+'.png')
							frame_deled_list.append(f_name)
				break
			time.sleep(0.5)

class VideoDelFrameThread_4x(threading.Thread):
	def __init__(self,inputpath,frame_list):
		threading.Thread.__init__(self)
		self.inputpath = inputpath
		self.frame_list = frame_list
        
	def run(self):
		inputpath = self.inputpath
		frame_list = self.frame_list
		video_dir = os.path.dirname(inputpath)+'\\'
		frames_scaled_dir = video_dir+'frames_waifu2x\\scaled\\'
		old_filenum = len(frame_list)
		frame_deled_list = []
		while True:
			if len(frame_deled_list) == old_filenum:
				return 0
			for path,useless,fnames in os.walk(frames_scaled_dir):
				for f_name_ext_ext in fnames:
					f_name_ext = os.path.splitext(f_name_ext_ext)[0]
					f_name = os.path.splitext(f_name_ext)[0]
					if f_name_ext != f_name:
						if f_name not in frame_deled_list:
							if f_name in frame_list:
								os.remove(frames_scaled_dir+f_name+'.png')
								frame_deled_list.append(f_name)
				break
			time.sleep(0.5)
	
#====================== input ============================
def input_scale():
	settings_values = ReadSettings()
	default_value = settings_values['scale']

	while True:
		scale = input('Upscale ratio(1/2/4, default='+default_value+'): ')
		if scale in ['1','2','4','','r','R']:
			break
		else:
			print('Error : wrong input, pls input again')
	
	if scale == '':
		scale = default_value
	elif scale == '1':
		models = 'models-cunet'
	return scale
	
def input_tileSize():
	settings_values = ReadSettings()
	default_value = '200'
	print('You can run the benchmark to determine the best value of "tile size" for your computer.')
	print('--------------------------------------------------------------------------------------')
	while True:
		tileSize = input('Tile size(>=32, default='+default_value+'): ')
		if tileSize.isdigit():
			if int(tileSize) > 0:
				break
			else:
				print('wrong input, pls input again')
		elif tileSize == '':
			break
		else:
			os.system('cls')
			print('wrong input, pls input again')
		
	if tileSize == '':
		tileSize = default_value
	
	settings_values['tileSize']=str(int(tileSize))
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)
	
def input_noiseLevel():
	settings_values = ReadSettings()
	default_value = settings_values['noiseLevel']
	while True:
		noiseLevel = input('Denoise level(-1/0/1/2/3, default='+default_value+'): ')
		if noiseLevel in ['-1','0','1','2','3','','r','R']:
			break
		else:
			print('wrong input, pls input again')
	
	if noiseLevel == '':
		noiseLevel = default_value
	return noiseLevel
		
def input_delorginal():
	settings_values = ReadSettings()
	default_value = settings_values['delorginal']
	while True:
		delorginal = input('Delete original files?(y/n, default='+default_value+'): ')
		if delorginal in ['y','n','Y','N','','r','R']:
			break
		else:
			print('wrong input, pls input again')
	
	if delorginal == '':
		delorginal = default_value
	return delorginal
	
def input_turnoff():
	while True:
		turnoff = input('turn off computer when finished?(y/n, default=n): ')
		if turnoff in ['y','n','Y','N','','r','R']:
			break
		else:
			print('wrong input, pls input again')
	
	if turnoff == '':
		turnoff = 'n'
	return turnoff

def input_saveAsJPG():
	settings_values = ReadSettings()
	default_value = settings_values['saveAsJPG']
	while True:
		saveAsJPG = input('Save as .jpg? (y/n, default='+default_value+'): ')
		if saveAsJPG in ['y','n','Y','N','','r','R']:
			break
		else:
			print('wrong input, pls input again')
	
	if saveAsJPG == '':
		saveAsJPG = default_value
	return saveAsJPG
	
def input_Compress():
	settings_values = ReadSettings()
	default_value = settings_values['Compress']
	while True:
		Compress = input('Compress the .jpg file?(Almost lossless) (y/n, default='+default_value+'): ')
		if Compress in ['y','n','Y','N','','r','R']:
			break
		else:
			print('wrong input, pls input again')
	if Compress == '':
		Compress = default_value
	return Compress

def input_highQuality():
	settings_values = ReadSettings()
	default_value = settings_values['highQuality']
	while True:
		highQuality = input('Save high quality gif? (y/n, default='+default_value+'): ')
		if highQuality in ['y','n','Y','N','','r','R']:
			break
		else:
			print('wrong input, pls input again')
	
	if highQuality == '':
		highQuality = default_value
		
	return highQuality
	
def input_gifCompresslevel():
	settings_values = ReadSettings()
	default_value = settings_values['gifCompresslevel']
	while True:
		gifCompresslevel = input('Compress level(1/2/3/4, default='+default_value+'): ')
		if gifCompresslevel in ['1','2','3','4','','r','R']:
			break
		else:
			print('wrong input, pls input again')
	
	if gifCompresslevel == '':
		gifCompresslevel = default_value
		
	return gifCompresslevel
	
def input_multiThread():
	settings_values = ReadSettings()
	default_value = 'y'
	while True:
		multiThread = input('Enable multithreading(Compress)? (y/n, default='+default_value+'): ')
		if multiThread in ['y','n','Y','N','']:
			break
		else:
			print('wrong input, pls input again')
	
	if multiThread == '':
		multiThread = default_value
	
	settings_values['multiThread']=str(multiThread)
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)
	
def input_gpuId():
	settings_values = ReadSettings()
	default_value = 'auto'
	while True:
		gpuId = input('GPU ID (auto (Automatic)/0/1/2/..., default='+default_value+'): ')
		if gpuId.isdigit():
			if int(gpuId) >= 0:
				break
			else:
				print('wrong input, pls input again')
		elif gpuId == '':
			break
		elif gpuId.lower() == 'auto':
			gpuId = gpuId.lower()
			break
		else:
			os.system('cls')
			print('wrong input, pls input again')
		
	if gpuId == '':
		gpuId = default_value
	settings_values['gpuId']=str(gpuId)
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)

def input_notificationSound():
	settings_values = ReadSettings()
	default_value = 'y'
	while True:
		notificationSound = input('Enable notification sound? (y/n, default='+default_value+'): ')
		if notificationSound in ['y','n','Y','N','']:
			break
		else:
			os.system('cls')
			print('wrong input, pls input again')
	
	if notificationSound == '':
		notificationSound = default_value
		
	settings_values['notificationSound']=str(notificationSound)
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)

def input_multiThread_Scale():
	settings_values = ReadSettings()
	default_value = 'y'
	while True:
		multiThread_Scale = input('Enable multithreading(Scale & denoise)? (y/n, default='+default_value+'): ')
		if multiThread_Scale in ['y','n','Y','N','']:
			break
		else:
			print('wrong input, pls input again')
	
	if multiThread_Scale == '':
		multiThread_Scale = default_value
	
	settings_values['multiThread_Scale']=str(multiThread_Scale)
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)

def input_image_quality():
	settings_values = ReadSettings()
	default_value = settings_values['image_quality']
	while True:
		image_quality = input('Image quality ( 100 (Almost lossless) ~ 1 (Most lossy) , defalut = '+str(default_value)+' ):').strip(' ')
		if image_quality.isdigit():
			if int(image_quality) >= 1 and int(image_quality) <= 100:
				return int(image_quality)
				break
			else:
				print('wrong input, pls input again')
		elif image_quality.lower() == 'r':
			return 'r'
		elif image_quality == '':
			return default_value
		else:
			os.system('cls')
			print('wrong input, pls input again')

#======================== Seconds 2 h:m:s =========================
def Seconds2hms(seconds):
	if seconds > 59 and seconds < 3600:
		minutes = int(seconds/60)
		seconds = seconds - (60*minutes)
		return str(minutes)+'m : '+str(seconds)+'s'
	elif seconds > 3599:
		hours = int(seconds/3600)
		seconds = seconds - (3600*hours)
		minutes = int(seconds/60)
		seconds = seconds - (60*minutes)
		return str(hours)+'h : '+str(minutes)+'m : '+str(seconds)+'s'
	else:
		return str(seconds)+'s'
#============================= Check Update =====================
def checkUpdate():
	print('Checking update....')
	try:
		headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
		r1=requests.get('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest',headers=headers)
		
		soup = BeautifulSoup(r1.text,'lxml')
		
		title = soup.title.string
		p_split_name = re.compile(r' ')
		
		Version_latest = p_split_name.split(title)[1]
		
		if Version_current != Version_latest:
			os.system('cls')
			print('New update : '+Version_latest)
			while True:
				download_update = input('Do you wanna download the update?(y/n): ')
				if download_update in ['y','n','Y','N']:
					break
				else:
					print('wrong input, pls input again')
			if download_update.lower() == 'y':
				webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest')
		else:
			os.system('cls')
			print('No new update')
			input('press Enter key to return')
	except BaseException:
		os.system('cls')
		input('Failed to establish connection, pls check your internet, press Enter key to return....')
		os.system('cls')
	
		
def checkUpdate_start(Version_current):
	print('Checking update....')
	try:
		headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
		r1=requests.get('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest',headers=headers)
		
		soup = BeautifulSoup(r1.text,'lxml')
				
		title = soup.title.string
		p_split_name = re.compile(r' ')
		
		Version_latest = p_split_name.split(title)[1]
		
		if Version_current != Version_latest:
			os.system('cls')
			print('New update : '+Version_latest)
			while True:
				print('If you don\'t wanna check for updates at startup. You can change the settings.')
				download_update = input('Do you wanna download the update?(y/n): ')
				if download_update in ['y','n','Y','N']:
					break
				else:
					print('wrong input, pls input again')
			if download_update.lower() == 'y':
				webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest')
		else:
			os.system('cls')
	except BaseException:
		os.system('cls')

#========================Verify Files=====================

def VerifyFiles():
	FilesList = ['ffmpeg.exe', 'msvcp140.dll', 'vcomp140.dll', 
	'vcruntime140.dll', 'vulkan-1.dll', 'waifu2x-ncnn-vulkan.exe', 
	'noise0_model.bin', 'noise0_model.param', 'noise0_scale2.0x_model.bin', 
	'noise0_scale2.0x_model.param', 'noise1_model.bin', 'noise1_model.param', 
	'noise1_scale2.0x_model.bin', 'noise1_scale2.0x_model.param', 'noise2_model.bin', 
	'noise2_model.param', 'noise2_scale2.0x_model.bin', 'noise2_scale2.0x_model.param', 
	'noise3_model.bin', 'noise3_model.param', 'noise3_scale2.0x_model.bin', 
	'noise3_scale2.0x_model.param', 'scale2.0x_model.bin', 'scale2.0x_model.param', 
	'noise0_scale2.0x_model.bin', 'noise0_scale2.0x_model.param', 'noise1_scale2.0x_model.bin', 
	'noise1_scale2.0x_model.param', 'noise2_scale2.0x_model.bin', 'noise2_scale2.0x_model.param', 
	'noise3_scale2.0x_model.bin', 'noise3_scale2.0x_model.param', 'scale2.0x_model.bin', 'scale2.0x_model.param','gifsicle.exe',
	'NotificationSound_waifu2xExtension.mp3','Benchmark_Image_waifu2x_extension_1.png','Benchmark_Image_waifu2x_extension_2.png',
	'Benchmark_Image_waifu2x_extension_3.png','Benchmark_Image_waifu2x_extension_4.png','Benchmark_Image_waifu2x_extension_5.png',
	'Benchmark_Image_waifu2x_extension_6.png','Benchmark_Image_waifu2x_extension_7.png','Benchmark_Image_waifu2x_extension_8.png','vgi_waifu2x_extension.jpg']
	
	current_dir = os.path.dirname(os.path.abspath(__file__))
	FilesList_current = []
	for path,useless,fnames in os.walk(current_dir):
		for fname in fnames:
			FilesList_current.append(fname)
	FileNotFound = False
	for fname in FilesList:
		if fname not in FilesList_current:
			FileNotFound = True
			print('Error: "'+fname+'" not found.')
	if FileNotFound == True:
		return 'error'
	else:
		return 'verified'

#=================  Settings  ================

def Settings():
	while True:
		settings_values = {}
		with open('waifu2x-extension-setting','r+') as f:
			settings_values = json.load(f)
		print('                                  Settings')
		print('-----------------------------------------------------------------------------')
		print(' 1: Check for updates at startup. Current value: '+settings_values['CheckUpdate']+'\n')
		print(' 2: Default value of "Upscale ratio". Current value: '+settings_values['scale']+'\n')
		print(' 3: Default value of "Denoise Level". Current value: '+settings_values['noiseLevel']+'\n')
		print(' 4: Save the result image as .jpg file? Current default value: '+settings_values['saveAsJPG']+'\n')
		print(' 5: Compress the result image?(when saved as .jpg) Current default value: '+settings_values['Compress']+'\n')
		print(' 6: Delete original files when finished? Current default value: '+settings_values['delorginal']+'\n')
		print(' 7: Save high quality gif? Current default value: '+settings_values['highQuality']+'\n')
		print(' 8: Gif compress level. Current default value: '+settings_values['gifCompresslevel']+'\n')
		print(' 9: Image quality ( When compress images ). Current default value: ',settings_values['image_quality'],'\n')
		print(' 10: Reset error log.\n')
		print(' R : Return to the main menu.')
		print('-----------------------------------------------------------------------------')
		mode = input('(1/2/3/4/5/6/7/8/9/r): '.upper())
		mode = mode.lower()
		if mode == "1":
			os.system('cls')
			
			while True:
				value_ = input('New value(y/n): ').lower()
				if value_ in ['y','n']:
					break
				else:
					print('invalid value, pls input again')
					
			settings_values['CheckUpdate']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode== "2":
			os.system('cls')
			
			while True:
				value_ = input('New value(1/2/4): ').lower()
				if value_ in ['1','2','4']:
					break
				else:
					print('invalid value, pls input again')
					
			settings_values['scale']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
			
		elif mode == "3":
			os.system('cls')
			
			while True:
				value_ = input('New value(-1/0/1/2/3): ').lower()
				if value_ in ['-1','0','1','2','3']:
					break
				else:
					print('invalid value, pls input again')
					
			settings_values['noiseLevel']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
			
		elif mode == "4":
			os.system('cls')
			
			while True:
				value_ = input('New value(y/n): ').lower()
				if value_ in ['y','n']:
					break
				else:
					print('invalid value, pls input again')
					
			settings_values['saveAsJPG']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
			
		elif mode == "5":
			os.system('cls')
			
			while True:
				value_ = input('New value(y/n): ').lower()
				if value_ in ['y','n']:
					break
				else:
					print('invalid value, pls input again')
					
			settings_values['Compress']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
			
		elif mode == "6":
			os.system('cls')
			
			while True:
				value_ = input('New value(y/n): ').lower()
				if value_ in ['y','n']:
					break
				else:
					print('invalid value, pls input again')
					
			settings_values['delorginal']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
			
		elif mode == "7":
			os.system('cls')
			
			while True:
				value_ = input('New value(y/n): ').lower()
				if value_ in ['y','n']:
					break
				else:
					print('invalid value, pls input again')
					
			settings_values['highQuality']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode== "8":
			os.system('cls')
			
			while True:
				value_ = input('New value(1/2/3/4): ').lower()
				if value_ in ['1','2','3','4']:
					break
				else:
					print('invalid value, pls input again')
					
			settings_values['gifCompresslevel']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode == "9":
			os.system('cls')
			while True:
				image_quality = input('New value ( 100 ~ 1 ): ').strip(' ')
				if image_quality.isdigit():
					if int(image_quality) >= 1 and int(image_quality) <= 100:
						break
					else:
						print('wrong input, pls input again')
				else:
					print('wrong input, pls input again')
			settings_values['image_quality']=int(image_quality)
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode == "10":
			os.system('cls')
			
			with open('Error_Log_Waifu2x-Extension.log','w+') as f:
				f.write('')
				
			with open('Error_Log_Waifu2x-Extension.log','a+') as f:
				timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
				f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Error log reseted by user.\n')
			
			input('Error log reseted, press Enter key to return.')
			
			os.system('cls')
		
		
		
		elif mode == "r":
			break
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press Enter key to return')
			os.system('color 07')
			os.system('cls')

def ReadSettings():
	default_values = {'CheckUpdate':'y','scale':'2','tileSize':'200',
						'noiseLevel':'2','saveAsJPG':'y',
						'Compress':'n','delorginal':'n','highQuality':'n','gifCompresslevel':'1',
						'multiThread':'y','gpuId':'auto','notificationSound':'y','multiThread_Scale':'y','image_quality':'95'}
	current_dir = os.path.dirname(os.path.abspath(__file__))
	settingPath = current_dir+'\\'+'waifu2x-extension-setting'
	if os.path.exists(settingPath) == False:
		with open('waifu2x-extension-setting','w+') as f:
			json.dump(default_values,f)
		return default_values
	else:
		settings_values = {}
		with open('waifu2x-extension-setting','r+') as f:
			settings_values = json.load(f)
		if len(settings_values) != len(default_values):
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(default_values,f)
			return default_values
		else:
			return settings_values

#==========================================  Init  ==================================================================

def init():		#初始化函数
	Window_Title('')	#更改控制台标题
	os.system('color 0b')	#更改文字颜色
	
	sys.stderr = Logger('Error_Log_Waifu2x-Extension.log', sys.stderr)
	with open('Error_Log_Waifu2x-Extension.log','a+') as f:
		timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Start running\n')
		
	settings_values = ReadSettings()
	
	if settings_values['CheckUpdate'] == 'y':
		checkUpdate_start(Version_current)
		
	if VerifyFiles() == 'verified':
		os.system('cls')
		thread_resizeWindow=ResizeWindow_Thread()
		thread_resizeWindow.start()
		time.sleep(0.2)
		ChooseFormat()
		if thread_resizeWindow.isAlive()==True:
			stop_thread(thread_resizeWindow)
	else:
		os.system('cls')
		os.system('color 0c')
		print('-'*40)
		download_latest = input('Some files are missing. Do you wanna download the latest package?(y/n): ')
		if download_latest.lower() == 'y':
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest')
		os.system('cls')
		input('Press Enter key to exit.')
		os.system('cls')
		os.system('color 07')
		
#======================== Logger =============================

class Logger(object):
	def __init__(self, filename='default.log', stream=sys.stdout):
		self.terminal = stream
		self.log = open(filename, 'a')

	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def flush(self):
		pass

#==================== Admin ===========================
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
#============================= Error_Log ====================================

def Error_Log():	#读取错误日志
	if os.path.exists('Error_Log_Waifu2x-Extension.log') == True:	#判断错误日志文件是否存在
		webbrowser.open('Error_Log_Waifu2x-Extension.log')
		log_size = round(os.path.getsize('Error_Log_Waifu2x-Extension.log')/1024)
		if log_size > 200:
			del_log = input('The error log is too large (>200KB). Do you want to reset the error log?(Y/N): ')
			if del_log.lower() == 'y':
				with open('Error_Log_Waifu2x-Extension.log','w+') as f:
					f.write('')
				with open('Error_Log_Waifu2x-Extension.log','a+') as f:
					timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
					f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Error log reseted by user.\n')
				
	else:
		print('Error : error log file is missing.')	#提示错误日志文件丢失
		input('Press Enter key to return.')

#===================== Multi-thread Gif Compress =======================
class GifCompressThread (threading.Thread):
	def __init__(self,inputPath,gifCompresslevel,delorginal):
		threading.Thread.__init__(self)
		self.inputPath = inputPath
		self.gifCompresslevel = gifCompresslevel
		self.delorginal =delorginal
        
	def run(self):
		inputPath = self.inputPath
		gifCompresslevel = self.gifCompresslevel
		delorginal = self.delorginal
		scaledFilePath = os.path.splitext(inputPath)[0]
		compress_gif(inputPath,gifCompresslevel)
		saved_size = round(os.path.getsize(inputPath)/1024) - round(os.path.getsize(scaledFilePath+"_compressed.gif")/1024)
		if saved_size <= 0:
			os.system('del /q "'+scaledFilePath+"_compressed.gif"+'"')
			print('\nFailed to compress '+inputPath)
		else:
			saved_size_str = str(saved_size)+'KB'
			print('\nFinished to compress '+inputPath)
			if delorginal.lower() == 'y':
				os.system('del /q "'+inputPath+'"')

def Multi_thread_Gif_Compress(inputPathList_files,gifCompresslevel,delorginal):
	
	max_threads = cpu_count()
	
	thread_files = []
	
	for inputPath in inputPathList_files:
		file_ext = os.path.splitext(inputPath)[1]
		if file_ext != '.gif':
			continue
		thread_files.append(inputPath)
		if len(thread_files) == max_threads:
			for inputPath in thread_files:
				thread1=GifCompressThread(inputPath,gifCompresslevel,delorginal)
				thread1.start()
			while True:
				if thread1.isAlive()== False:
					break
			thread_files = []
	if thread_files != []:
		for inputPath in thread_files:
			thread1=GifCompressThread(inputPath,gifCompresslevel,delorginal)
			thread1.start()
		while True:
			if thread1.isAlive()== False:
				break
		thread_files = []
		
#===================== Multi-thread Image Compress =======================
class ImageCompressThread (threading.Thread):
	def __init__(self,inputPath,delorginal,JpgQuality):
		threading.Thread.__init__(self)
		self.inputPath = inputPath
		self.delorginal =delorginal
		self.JpgQuality =JpgQuality
        
	def run(self):
		inputPath = self.inputPath
		delorginal = self.delorginal
		JpgQuality=self.JpgQuality
		
		scaledFilePath = os.path.splitext(inputPath)[0]
		imageio.imwrite(scaledFilePath+"_compressed.jpg", imageio.imread(inputPath), 'JPG', quality = JpgQuality)
		saved_size = round(os.path.getsize(inputPath)/1024) - round(os.path.getsize(scaledFilePath+"_compressed.jpg")/1024)
		if saved_size <= 0:
			os.system('del /q "'+scaledFilePath+"_compressed.jpg"+'"')
			print('Failed to compress ['+inputPath+'] This image may be already being compressed.\nYou can try to reduce "image quality".')
		else:
			print('\nFinished to compress '+inputPath)
			if delorginal.lower() == 'y':
				os.system('del /q "'+inputPath+'"')

def Multi_thread_Image_Compress(inputPathList_files,delorginal,JpgQuality):
	
	max_threads = cpu_count()
	
	thread_files = []
	
	for inputPath in inputPathList_files:
		file_ext = os.path.splitext(inputPath)[1]
		if file_ext == '.gif':
			continue
		thread_files.append(inputPath)
		if len(thread_files) == max_threads:
			for inputPath in thread_files:
				thread1=ImageCompressThread(inputPath,delorginal,JpgQuality)
				thread1.start()
			while True:
				if thread1.isAlive()== False:
					break
			thread_files = []
	if thread_files != []:
		for inputPath in thread_files:
			thread1=ImageCompressThread(inputPath,delorginal,JpgQuality)
			thread1.start()
		while True:
			if thread1.isAlive()== False:
				break
		thread_files = []

#================================= Play Notification Sound====================

class Play_Notification_Sound_Thread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
        
	def run(self):
		playsound('NotificationSound_waifu2xExtension.mp3')

#================================ Resize Window ==========================

class ResizeWindow_Thread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
        
	def run(self):
		ResizeWindow()

def ResizeWindow():
	cols = 145
	lines = 38
	while True:
		h = ctypes.windll.kernel32.GetStdHandle(-12)
		csbi = ctypes.create_string_buffer(22)
		res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
		
		if res:
			(bufx, bufy, curx, cury, wattr,
			 left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
			sizex = right - left + 1
			sizey = bottom - top + 1
			if sizex != cols or sizey != lines:
				os.system('Resize-window.exe 145 38')
		else:
			os.system('Resize-window.exe 145 38')
		time.sleep(0.1)
	
#=============================== Benchmark =============================
def Benchmark():
	print('============================== Benchmark ==============================================')
	print('This benchmark will help you to determine the best value of "tile size".')
	print('In order to get the accurate result, pls do not use your computer during the benchmark.')
	print('---------------------------------------------------------------------------------------')
	if input('Do you wanna start the benchmark now? (y/n): ').lower().strip(' ') != 'y':
		return 0
	Window_Title('[Running benchmark]')
	print('-------------------------------------------------------')
	print('This benchmark is gonna take a while, pls wait.....')
	print('-------------------------------------------------------')
	print('Wait 60 seconds to cool the computer.')
	time.sleep(60)
	settings_values = ReadSettings()
	notificationSound = settings_values['notificationSound']
	models = 'models-upconv_7_anime_style_art_rgb'
	scale = '2'
	noiseLevel = '3'
	gpuId = settings_values['gpuId']
	gpuId_str=''
	if gpuId.lower() != 'auto':
		gpuId_str = ' -g '+gpuId
	current_dir = os.path.dirname(os.path.abspath(__file__))
	inputPath = current_dir+'\\'+'benchmark-files-waifu2x-extension'
	scaledFilePath = inputPath+'\\scaled'
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = ' -j 2:2:2 '
	if multiThread_Scale.lower() == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	tileSize = 50
	old_time_cost = 100000
	old_tileSize = 0
	
	if os.path.exists(scaledFilePath) == True:
		os.system("rd /s/q \""+scaledFilePath+"\"")
	
	for x in range(0,50):
		os.mkdir(scaledFilePath)
		time_start=time.time()
		print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+str(tileSize)+" -m "+models+gpuId_str+load_proc_save_str)
		os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+str(tileSize)+" -m "+models+gpuId_str+load_proc_save_str)
		time_end=time.time()
		os.system("rd /s/q \""+scaledFilePath+"\"")
		new_time_cost = time_end - time_start
		print('---------------------------------')
		print('Tile size: ',tileSize)
		print('Time cost: ',new_time_cost)
		print('---------------------------------')
		if new_time_cost <= old_time_cost:
			old_time_cost = new_time_cost
			old_tileSize = tileSize
		else:
			break
		tileSize=tileSize+50
		print('Wait 60 seconds to cool the computer.')
		time.sleep(60)
	if notificationSound.lower() == 'y':
			thread_Notification=Play_Notification_Sound_Thread()
			thread_Notification.start()
	Window_Title('')
	print('==================================================================')
	print('The best value of "tile size" of your computer is:',old_tileSize)
	if input('Do you wanna use the result value? (y/n): ').lower().strip(' ') != 'y':
		return 0
	settings_values['tileSize']=str(old_tileSize)
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)
		
#============================= license_ ========================
def license_():
	print('English:')
	print('------------------------------------------')
	print('Copyright 2019 Aaron Feng\n')
	print('Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n')
	print('The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n')
	print('THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n')
	print('------------------------------------------')
	print('中文:')
	print('注意:中文版本由机器翻译生成, 仅供无法阅读英语者参考, 可能包含错误, 一切以英文原版许可证为准.')
	print('---------------------------------------------')
	print('版权所有 2019 Aaron Feng\n')
	print('特此授予任何获得本软件和相关文档文件（“软件”）副本的人免费许可，以无限制地交易本软件，包括但不限于使用，复制，修改，合并的权利在符合以下条件的前提下，发布，分发，再许可，并允许向其提供软件的人员这样做：\n')
	print('上述版权声明和本许可声明应包含在本软件的所有副本或实质部分中。\n')
	print('本软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于适销性，特定用途的适用性和不侵权的保证。在任何情况下，作者或版权所有者均不对任何索赔，损害或其他责任承担任何责任，无论是在合同，侵权行为还是其他方面的行为，由本软件引起或与之相关，或与本软件的使用或其他交易有关。软件。\n')
	print('------------------------------------------')
	input('Press Enter key to return to the main menu.')

#================= Protect files ================
def FindGifFiles(inputPathList):
	Gif_exist = False
	for inputPath in inputPathList:
		for path,useless,fnames in os.walk(inputPath):
			for fname in fnames:
				if os.path.splitext(fname)[1] == ".gif":
					return True
			break
	return False

def MoveGifFiles(inputPathList):
	inputPathList_gif = []
	path_gif_exist = False
	for inputPath in inputPathList:
		for path,useless,fnames in os.walk(inputPath):
			for fname in fnames:
				if os.path.splitext(fname)[1] == ".gif":
					path_gif_exist = True
					old_path = path+'\\'+fname
					if os.path.exists(inputPath+'\\protectfiles_waifu2x_extension') == False:
						os.mkdir(inputPath+'\\protectfiles_waifu2x_extension')
					new_path = path+'\\protectfiles_waifu2x_extension\\'+fname
					os.system('copy /y "'+old_path+'" "'+new_path+'"')
					os.system('del /q "'+old_path+'"')
			if path_gif_exist:
				inputPathList_gif.append(inputPath)
				path_gif_exist = False
			break
	return inputPathList_gif

def RecoverGifFiles(inputPathList):
	Exts=[".gif"]
	for inputPath in inputPathList:
		for path,useless,fnames in os.walk(inputPath+'\\protectfiles_waifu2x_extension'):
			for fname in fnames:
				if os.path.splitext(fname)[1] in Exts:
					old_path = path+'\\'+fname
					new_path = inputPath+'\\'+fname
					os.system('copy /y "'+old_path+'" "'+new_path+'"')
					os.system('del /q "'+old_path+'"')
			if os.path.exists(inputPath+'\\protectfiles_waifu2x_extension') == True:
				os.system('rd /s/q "'+inputPath+'\\protectfiles_waifu2x_extension'+'"')
			break
			
def FindImageFiles(inputPathList):
	Exts=[".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]
	Image_exist = False
	for inputPath in inputPathList:
		for path,useless,fnames in os.walk(inputPath):
			for fname in fnames:
				if os.path.splitext(fname)[1] in Exts:
					return True
			break
	return False

#======================================= View_GPU_ID() ===========================
def View_GPU_ID():
	print('============================View_GPU_ID =======================')
	print('This will tell you the available GPU ID.')
	print('----------------------------------------')
	gpuId = 0
	gpuId_list = []
	for x in range(0,10):
		gpuId_str = ' -g '+str(gpuId)
		settings_values = ReadSettings()
		current_dir = os.path.dirname(os.path.abspath(__file__))
		models = 'models-upconv_7_anime_style_art_rgb'
		scale = '2'
		noiseLevel = '0'
		tileSize = settings_values['tileSize']
		multiThread_Scale = settings_values['multiThread_Scale']
		load_proc_save_str = ' -j 2:2:2 '
		if multiThread_Scale.lower() == 'n':
			load_proc_save_str = ' -j 1:1:1 '
		inputPath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension.jpg'
		scaledFilePath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension_waifu2x.png'
		if os.path.exists(scaledFilePath) == True:
			os.system("del /q \""+scaledFilePath+"\"")
		os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+str(tileSize)+" -m "+models+gpuId_str+load_proc_save_str)
		if os.path.exists(scaledFilePath)==True:
			gpuId_list.append(gpuId)
			os.system("del /q \""+scaledFilePath+"\"")
		else:
			break
		gpuId = gpuId+1
	if len(gpuId_list) > 0:
		print('---------------------------------------------')
		print(' Available GPU ID: ',gpuId_list)
		print('---------------------------------------------')
	else:
		print('---------------------------------------------------------------')
		print(' No GPU ID availabel. Pls upgrade or reinstall your GPU driver.')
		print('---------------------------------------------------------------')
	input('Press Enter key to return to the main menu.')
	
#=============================== Default Window Title =================
def Window_Title(Add_str = ''):
	os.system('title = Waifu2x-Extension '+Version_current+' by Aaron Feng '+Add_str)
	
	
#======================== Start ========================
        
if __name__ == '__main__':
	#检查所处文件夹是否需要管理员权限
	if AdminTest():
		try:
			init()
		except BaseException as e:
			print()
			print('---------------------------------------------------')
			print('                   !!! Error !!!')
			print('---------------------------------------------------')
			ErrorStr = str(traceback.print_exc())
			
			with open('Error_Log_Waifu2x-Extension.log','a+') as f:
				f.write(ErrorStr)
			
			print('---------------------------------------------------')
			input('An error occurred, pls report this to the developer.\nPress Enter key to restart the software.\n')
			os.system('color 07')
			os.system('cls')
			python = sys.executable
			os.execl(python, python, * sys.argv)
	else:
		# Re-run the program with admin rights
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

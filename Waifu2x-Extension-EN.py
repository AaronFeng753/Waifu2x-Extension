#!/usr/bin/python  
# -*- coding: utf-8 -*- 

'''

What is Waifu2x-Extension ?

Image & GIF & Video Super-Resolution for Anime-style art using Deep Convolutional Neural Networks.
Based on waifu2x-ncnn-vulkan (version 20190712).
Thanks to waifu2x-ncnn-vulkan, Waifu2x-Extension could use any kind of gpu that support Vulakn, even Intel GPU.
Already been tested on AMD RX 550, NVIDIA GeForce GTX 1070 and Intel UHD 620.

-----------------------------------------------

waifu2x-ncnn-vulkan version 20190712

Anime4K Java v0.9 Beta

ffmpeg version 4.2.1

gifsicle version 1.92

Waifu2x-converter version: 2015-11-30T02:17:24

ImageMagick 7.0.8-68 Q16 x64 2019-10-05

-----------------------------------------------

Update log

- Fix bugs
- Some improvements


------------------------------------------------

To do:





'''

print('''
		____    __    ____  ___       __   _______  __    __      ___   ___   ___ 
		\   \  /  \  /   / /   \     |  | |   ____||  |  |  |    |__ \  \  \ /  / 
		 \   \/    \/   / /  ^  \    |  | |  |__   |  |  |  |       ) |  \  V  /  
		  \            / /  /_\  \   |  | |   __|  |  |  |  |      / /    >   <   
		   \    /\    / /  _____  \  |  | |  |     |  `--'  |     / /_   /  .  \  
		    \__/  \__/ /__/     \__\ |__| |__|      \______/     |____| /__/ \__\
	
	
	 __________   ___ .___________. _______ .__   __.      _______. __    ______   .__   __. 
	|   ____\  \ /  / |           ||   ____||  \ |  |     /       ||  |  /  __  \  |  \ |  | 
	|  |__   \  V  /  `---|  |----`|  |__   |   \|  |    |   (----`|  | |  |  |  | |   \|  | 
	|   __|   >   <       |  |     |   __|  |  . `  |     \   \    |  | |  |  |  | |  . `  | 
	|  |____ /  .  \      |  |     |  |____ |  |\   | .----)   |   |  | |  `--'  | |  |\   | 
	|_______/__/ \__\     |__|     |_______||__| \__| |_______/    |__|  \______/  |__| \__| 

                                           Loading.......
''')

import os
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
import psutil

Version_current='v3.6'

#======================================================== MAIN MENU ==============================================================

def MainMenu():
	
	settings_values = ReadSettings()
	
	if settings_values['CheckUpdate'] == 'y':
		thread_CheckUpdate=CheckUpdate_start_thread()
		thread_CheckUpdate.start()
	
	tileSize = '[ '+settings_values['tileSize']+' ]'
	
	gpuId = '[ '+settings_values['gpuId']+' ]'
	
	notificationSound = '[ '+settings_values['notificationSound']+' ]'
	
	multiThread = '[ '+settings_values['multiThread']+' ]'
	
	multiThread_Scale = '[ '+settings_values['multiThread_Scale']+' ]' 
	
	saveAsJPG = '[ '+settings_values['saveAsJPG']+' ]' 
	Compress = ''
	if settings_values['saveAsJPG'].lower() == 'y':
		Compress = '   Compress: [ '+settings_values['Compress']+' ]' 
	
	optimizeGif = '[ '+settings_values['optimizeGif']+' ]' 
	
	Video_str = 'Scale & Denoise Video.'
	
	if settings_values['Video_scale_mode'] == 'anime4k':
		Video_str = 'Scale Video.(Anime4k) '
	else:
		Video_str = 'Scale & Denoise Video.'
	
	Error_log_clean()
	
	while True:
		Set_cols_lines(65,35)
		Set_cols_lines(66,36)
		Window_Title('')
		print('┌──────────────────────────────────────────────────────────────┐')
		print('│       Waifu2x-Extension | '+Version_current+' | Author: Aaron Feng '+' '*(13-len(Version_current))+'│')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ Github: https://github.com/AaronFeng753/Waifu2x-Extension    │')
		print('├──────────────────────────────────────────────────────────────┤')
		print("│ Attention: This software's scale & denoise function is only  │")
		print('│ designed for process Anime-style art (Image,GIF,Video).      │')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ 1 : Scale & Denoise Image & GIF.  2 : '+Video_str+' │')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ 3 : Compress Image & GIF.                                    │')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ 4 : Tile size: '+tileSize+'           '+'5 : GPU ID: '+gpuId+' '*(22-len(tileSize)-len(gpuId))+' │')
		print('│                                                              │')
		print('│ 6 : Notification sound: '+notificationSound+'                                │')
		print('│                                                              │')
		print('│ 7 : Multithreading(Compress): '+multiThread+'                          │')
		print('│                                                              │')
		print('│ 8 : Multithreading(Scale & denoise): '+multiThread_Scale+'                   │')
		print('│                                                              │')
		print('│ 9 : Save as .jpg?(Scale & Denoise): '+saveAsJPG+Compress+' '*(19-len(Compress))+' │')
		print('│                                                              │')
		print('│ 10 : Optimize .gif?(Scale & Denoise): '+optimizeGif+'                  │')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ 11 : Settings.            12 : Benchmark.                    │')
		print('│                                                              │')
		print('│ 13 : Read error log.      14 : Check update.                 │')
		print('│                                                              │')
		print('│ 15 : Readme.              16 : License.                      │')
		print('│                                                              │')
		print('│ 17 : Compatibility test   E : Exit.                          │')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│ D : Donate. (Alipay)      R : Report Bugs & Suggestions      │')
		print('└──────────────────────────────────────────────────────────────┘')
		mode = input('( 1 / 2 / 3 /.../ E / D / R ): ').strip(' ').lower()
			
		Set_cols_lines(120,38)
		
		if mode == "1":
			os.system('cls')
			settings_values = ReadSettings()
			if settings_values['Image_GIF_scale_mode'] == 'waifu2x-ncnn-vulkan':
				Image_Gif_Scale_Denoise()
			elif settings_values['Image_GIF_scale_mode'] == 'waifu2x-converter':
				Image_Gif_Scale_Denoise_waifu2x_converter()
			os.system('cls')
			
		elif mode == "2":
			os.system('cls')
			
			settings_values = ReadSettings()
			
			if settings_values['Video_scale_mode'] == 'anime4k':
				Scale_Denoise_Video_Anime4K()
			elif settings_values['Video_scale_mode'] == 'waifu2x-ncnn-vulkan':
				Scale_Denoise_Video()
			elif settings_values['Video_scale_mode'] == 'waifu2x-converter':
				Scale_Denoise_Video_waifu2x_converter()
				
			os.system('cls')
			
		elif mode == "3":
			os.system('cls')
			Compress_image_gif()
			os.system('cls')
			
		elif mode == "4":
			os.system('cls')
			input_tileSize()
			settings_values = ReadSettings()
			tileSize = '[ '+settings_values['tileSize']+' ]'
			os.system('cls')
		elif mode == "5":
			os.system('cls')
			input_gpuId()
			settings_values = ReadSettings()
			gpuId = '[ '+settings_values['gpuId']+' ]'
			os.system('cls')
		elif mode == "6":
			os.system('cls')
			input_notificationSound()
			settings_values = ReadSettings()
			notificationSound = '[ '+settings_values['notificationSound']+' ]'
			os.system('cls')
		elif mode == "7":
			os.system('cls')
			input_multiThread()
			settings_values = ReadSettings()
			multiThread = '[ '+settings_values['multiThread']+' ]'
			os.system('cls')
		elif mode == "8":
			os.system('cls')
			input_multiThread_Scale()
			settings_values = ReadSettings()
			multiThread_Scale = '[ '+settings_values['multiThread_Scale']+' ]' 
			os.system('cls')
		elif mode == "9":
			os.system('cls')
			input_saveAsJPG()
			settings_values = ReadSettings()
			saveAsJPG = '[ '+settings_values['saveAsJPG']+' ]' 
			Compress = ''
			if settings_values['saveAsJPG'].lower() == 'y':
				Compress = '   Compress: [ '+settings_values['Compress']+' ]' 
			os.system('cls')
		elif mode == "10":
			os.system('cls')
			input_optimizeGif()
			settings_values = ReadSettings()
			optimizeGif = '[ '+settings_values['optimizeGif']+' ]' 
			os.system('cls')
		elif mode == "11":
			os.system('cls')
			Settings()
			settings_values = ReadSettings()
			if settings_values['Video_scale_mode'] == 'anime4k':
				Video_str = 'Scale Video.          '
			else:
				Video_str = 'Scale & Denoise Video.'
				
			os.system('cls')
			
		elif mode == "12":
			os.system('cls')
			Benchmark()
			os.system('cls')
		elif mode == "13":
			os.system('cls')
			Error_Log()
			os.system('cls')
			
		elif mode == "14":
			os.system('cls')
			checkUpdate()
			os.system('cls')
		elif mode == "15":
			os.system('cls')
			print('Loading.......')
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/blob/master/README.md')
			os.system('cls')
		
		elif mode == "16":
			os.system('cls')
			Set_cols_lines(120,43)
			license_()
			os.system('cls')
		
		elif mode == "17":
			os.system('cls')
			Compatibility_Test(False)
			os.system('cls')
			
		elif mode == "e":
			ChangeColor_cmd_original()
			os.system('cls')
			return 0
		elif mode == "d":
			os.system('cls')
			print('Loading.......')
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension#donate')
			os.system('cls')
			print('                     Thank you!!!  :)')
		elif mode == "r":
			os.system('cls')
			print('Loading.......')
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/issues/new')
			os.system('cls')
		else:
			os.system('cls')
			ChangeColor_warning()
			print('-'*52)
			print(' Error : wrong input,pls press Enter key to return')
			print('-'*52)
			input()
			ChangeColor_default()
			os.system('cls')

#===================================================== Scale & Denoise Image & GIF ========================================
def Image_Gif_Scale_Denoise():
	print(' Note: The input path must not contain special characters,')
	print(' which will cause compatibility problems.')
	print('─'*80)
	print("               Scale & Denoise Image & GIF - Waifu2x-ncnn-vulkan")
	print('─'*80)
	print(" Type 'r' to return to the previous menu.")
	print(" Type 'o' to stop input more path, and input path must be a folder or a file.")
	print(" Scaled images & gifs will be in the input path.")
	print('─'*80)
	
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []
	orginalFileNameAndFullname = {}
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'
	Image_GIF_scale_mode = settings_values['Image_GIF_scale_mode']
	inputPathError = True
	inputPath = ''
	
	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input(' Input path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			if inputPath.lower() == 'r':
				return 1
			elif inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-'*32)
				print(' Error,input path is invalid !!')
				print('-'*32)
			else:
				inputPathError = False
		if inputPathOver :
			inputPathList.append(inputPath)
			
	inputPathList = Deduplicate_list(inputPathList)
	
	pathlist_files_folder = Separate_files_folder(inputPathList)
	
	inputPathList_files = pathlist_files_folder[0]
	inputPathList_folders = pathlist_files_folder[1]
	scan_subfolders = 'n'
	if inputPathList_folders != []:
		scan_subfolders = input_scan_subfolders()
		if scan_subfolders == 'r':
			return 1
	
	if scan_subfolders == 'y':
		subfolders_list = []
		for inputPathList_folders_folder_scan in inputPathList_folders:
			for path_scansub,useless,filename in os.walk(inputPathList_folders_folder_scan):
				for dirs in os.walk(path_scansub):
					subfolders_list.append(str(dirs[0]))
				break
		inputPathList_folders = subfolders_list
	
	scale = input_scale()
	if scale == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
	if noiseLevel == 'r':
		return 1
		
	tileSize = settings_values['tileSize']
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = settings_values['load_proc_save_str']
	if multiThread_Scale == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	gpuId = settings_values['gpuId']
	gpuId_str=''
	if gpuId != 'auto':
		gpuId_str = ' -g '+gpuId
	
	Gif_exists = False
	for file_ in inputPathList_files:
		if os.path.splitext(file_)[1] == '.gif':
			Gif_exists=True
			break
	if FindGifFiles(inputPathList_folders):
		Gif_exists=True
	if Gif_exists:
		optimizeGif = settings_values['optimizeGif']
	
	Image_exists = False
	for file_ in inputPathList_files:
		if os.path.splitext(file_)[1] in ['.jpg','.png','.jpeg','.tif','.tiff','.bmp','.tga']:
			Image_exists=True
			break
	if FindImageFiles(inputPathList_folders):
		Image_exists = True
	if Image_exists:
		saveAsJPG = settings_values['saveAsJPG']
		Compress = settings_values['Compress']
		if Compress.lower() == 'y':
			JpgQuality=90
	
	delorginal = input_delorginal()
	if delorginal == 'r':
		return 1
	
	turnoff = input_turnoff()
	if turnoff == 'r':
		return 1
	
	sleepMode = input_sleepMode()
	if sleepMode == 'r':
		return 1
	elif sleepMode == 'y':
		load_proc_save_str = ' -j 1:1:1 '
		
	print('-'*50)
	
	total_time_start=time.time()
	
	#======================== 同文件夹下的单个文件合并到一个文件夹内 ==========================
	Dict_New_folder_Old_folder_RemoveList = Image_File_2_Folder(inputPathList_files)
	Dict_New_folder_Old_folder = Dict_New_folder_Old_folder_RemoveList[0]
	RemoveList = Dict_New_folder_Old_folder_RemoveList[1]
	if RemoveList != []:
		for key in Dict_New_folder_Old_folder:
			inputPathList_folders.append(key)
		for path in RemoveList:
			inputPathList_files.remove(path)
	
	#=================================== 文件夹 =========================
	if inputPathList_folders != []:
		if Gif_exists:
			
			inputPathList_files_gif = []
			if Image_exists:
				inputPathList_gif = MoveGifFiles(inputPathList_folders)
				for inputPath in inputPathList_gif:
					for path,useless,fnames in os.walk(inputPath+'\\protectfiles_waifu2x_extension'):
						fnames = dict.fromkeys(fnames,'')
						for fname in fnames:
							if os.path.splitext(fname)[1] == '.gif':
								inputPathList_files_gif.append(path+'\\'+fname)
						break
			else:
				for inputPath in inputPathList_folders:
					for path,useless,fnames in os.walk(inputPath):
						fnames = dict.fromkeys(fnames,'')
						for fname in fnames:
							if os.path.splitext(fname)[1] == '.gif':
								inputPathList_files_gif.append(path+'\\'+fname)
						break
				
			process_gif_scale_modeABC(inputPathList_files_gif,orginalFileNameAndFullname,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,optimizeGif,delorginal)
		
		if Image_exists:
			Process_ImageModeAB(inputPathList_folders,orginalFileNameAndFullname,JpgQuality,models,noiseLevel,scale,load_proc_save_str,tileSize,gpuId_str,saveAsJPG,delorginal)
			RecoverGifFiles(inputPathList_folders)
			
	if RemoveList != []:
		Remove_File_2_Folder(Dict_New_folder_Old_folder)
	#======================= 单文件 =========================
	if inputPathList_files != []:
		if Gif_exists:
			inputPathList_files_gif = []
			for file_ in inputPathList_files:
				if os.path.splitext(file_)[1] == '.gif':
					inputPathList_files_gif.append(file_)
			process_gif_scale_modeABC(inputPathList_files_gif,orginalFileNameAndFullname,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,optimizeGif,delorginal)
		
		if Image_exists:
			inputPathList_files_images = []
			for file_ in inputPathList_files:
				if os.path.splitext(file_)[1] in [".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]:
					inputPathList_files_images.append(file_)
			Process_ImageModeC(inputPathList_files_images,orginalFileNameAndFullname,JpgQuality,models,noiseLevel,scale,load_proc_save_str,tileSize,gpuId_str,saveAsJPG,delorginal)
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff=='y':
		ShutDown()
	Play_Notification_Sound()
	
	input('\npress Enter key to return to the menu')

#========================================= Process_ImageModeAB =============================================

def Process_ImageModeAB(inputPathList,orginalFileNameAndFullname,JpgQuality,models,noiseLevel,scale,load_proc_save_str,tileSize,gpuId_str,saveAsJPG,delorginal):
	Total_folder_num = len(inputPathList)
	Finished_folder_num = 1
	for inputPath in inputPathList:
		Window_Title('  [Scale Images]  Folder: ('+str(Finished_folder_num)+'/'+str(Total_folder_num)+')')
		oldfilenumber=FileCount(inputPath)
		scalepath = inputPath+"\\scaled_waifu2x\\"
		orginalFileNameAndFullname = {}
		for files in os.walk(inputPath):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
			break
		
		if os.path.exists(inputPath+"\\scaled_waifu2x\\") :
			os.system("rd /s/q \""+inputPath+"\\scaled_waifu2x\\"+'"')
		os.mkdir(inputPath+"\\scaled_waifu2x\\")
		
		if scale in ['4','8']:
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 1)
			thread1.start()
		else:
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 0)
			thread1.start()
		
		if scale in ['4','8']:
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread1.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
			
			for files in os.walk(scalepath):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					os.rename(os.path.join(scalepath,fileNameAndExt),os.path.join(scalepath,fileName+'.png'))
			
			
			old_file_list=[]
			for path,useless,fnames in os.walk(scalepath):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					f_name_ext = os.path.splitext(fname)[0]
					f_name = os.path.splitext(fname)[0]
					if f_name == f_name_ext:
						old_file_list.append(os.path.splitext(fname)[0])
				break
			
			old_file_list_prograsssbar=[]
			for path,useless,fnames in os.walk(scalepath):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					old_file_list_prograsssbar.append(fname)
				break
			
			thread_DelOldFileThread_4x=DelOldFileThread_4x(scalepath,old_file_list)
			thread_DelOldFileThread_4x.start()
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 2,old_file_list_prograsssbar = old_file_list_prograsssbar)
			thread1.start()
			print('')
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled_waifu2x"+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled_waifu2x"+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread1.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
			
			while thread_DelOldFileThread_4x.isAlive():
				time.sleep(1)
			
			for files in os.walk(inputPath+'\\scaled_waifu2x\\'):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					fileNameAndExt_new = orginalFileNameAndFullname[fileName]
					os.rename(os.path.join(inputPath+'\\scaled_waifu2x\\',fileNameAndExt),os.path.join(inputPath+'\\scaled_waifu2x\\',fileNameAndExt_new+".png"))
		
		if scale == '8':
			
			old_file_list=[]
			for path,useless,fnames in os.walk(scalepath):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					f_name_ext = os.path.splitext(fname)[0]
					f_name = os.path.splitext(fname)[0]
					if f_name == f_name_ext:
						old_file_list.append(os.path.splitext(fname)[0])
				break
			old_file_list_prograsssbar=[]
			for path,useless,fnames in os.walk(scalepath):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					old_file_list_prograsssbar.append(fname)
				break
			
			thread_DelOldFileThread_4x=DelOldFileThread_4x(scalepath,old_file_list)
			thread_DelOldFileThread_4x.start()
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 3,old_file_list_prograsssbar=old_file_list_prograsssbar)
			thread1.start()
			
			print('')
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled_waifu2x"+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled_waifu2x"+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread1.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
			
			while thread_DelOldFileThread_4x.isAlive():
				time.sleep(1)
			
			for files in os.walk(inputPath+'\\scaled_waifu2x\\'):
				for fileNameAndExt in files[2]:
					fileName_new = os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(inputPath+'\\scaled_waifu2x\\',fileNameAndExt),os.path.join(inputPath+'\\scaled_waifu2x\\',fileName_new))
			
			
		if scale in ['2','1']:
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
		
		time_wait_prograssbar = 0
		while thread1.isAlive():
			time_wait_prograssbar = time_wait_prograssbar+1
			time.sleep(1.1)
			if time_wait_prograssbar == 2:
				break
			
		if saveAsJPG == 'y':
			print('\n Convert image..... \n')
			for path,useless,fnames in os.walk(inputPath+'\\scaled_waifu2x\\'):
				for fnameAndExt in fnames:
					pngFile = path+'\\'+fnameAndExt
					fname = os.path.splitext(fnameAndExt)[0]
					jpgFile = path+'\\'+fname+'.jpg'
					imageio.imwrite(jpgFile, imageio.imread(pngFile), 'JPG', quality = JpgQuality)
					remove_safe(pngFile)
		settings_values = ReadSettings()
		Rename_result_images = settings_values['Rename_result_images']
		if Rename_result_images.lower() == 'y':
			for files in os.walk(inputPath+'\\scaled_waifu2x\\'):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					originalName=list(orginalFileNameAndFullname.keys())[list(orginalFileNameAndFullname.values()).index(fileName)]
					if saveAsJPG == 'y':
						os.rename(os.path.join(inputPath+'\\scaled_waifu2x\\',fileNameAndExt),os.path.join(inputPath+'\\scaled_waifu2x\\',originalName+"_Waifu2x.jpg"))
					else:
						os.rename(os.path.join(inputPath+'\\scaled_waifu2x\\',fileNameAndExt),os.path.join(inputPath+'\\scaled_waifu2x\\',originalName+"_Waifu2x.png"))
		elif Rename_result_images.lower() == 'n':
			for files in os.walk(inputPath+'\\scaled_waifu2x\\'):
				for fileNameAndExt in files[2]:
					fileName_new = os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(inputPath+'\\scaled_waifu2x\\',fileNameAndExt),os.path.join(inputPath+'\\scaled_waifu2x\\',fileName_new))
			
			
		orginalFileNameAndFullname = {}
		
		print('')
		if delorginal == 'y':
			files_num_inputPath = 0
			files_num_inputPath_scaled = 0
			for path,useless,fnames in os.walk(inputPath):
				files_num_inputPath = len(fnames)
				break
			for path,useless,fnames in os.walk(inputPath+"\\scaled_waifu2x"):
				files_num_inputPath_scaled = len(fnames)
				break
			if files_num_inputPath == files_num_inputPath_scaled:
				DelOrgFiles(inputPath)
			else:
				list_Content=[
					'echo ------------------------------------------------------------------------------\n',
					'echo Error occured, in order to save your files, the original files in this folder:\n',
					'echo '+inputPath+'\n'
					'echo will not be deleted.\n'
					'echo ------------------------------------------------------------------------------\n'
				]
				
				Pop_up_window('Error_file_not_del','Error',list_Content,'')

		print('Copy files...')
		if Rename_result_images.lower() == 'y':
			os.system("xcopy /s /i /q /y \""+inputPath+"\\scaled_waifu2x\\*.*\" \""+inputPath+"\"")
			os.system("rd /s/q \""+inputPath+"\\scaled_waifu2x\"")
		Finished_folder_num = Finished_folder_num + 1
	Window_Title('')

#=============================================  Process_ImageModeC  ======================================================

def Process_ImageModeC(inputPathList_Image,orginalFileNameAndFullname,JpgQuality,models,noiseLevel,scale,load_proc_save_str,tileSize,gpuId_str,saveAsJPG,delorginal):
	TotalFileNum = len(inputPathList_Image)
	FinishedFileNum = 1
	for inputPath in inputPathList_Image:
		scaledFilePath = os.path.splitext(inputPath)[0]
		fileNameAndExt=str(os.path.basename(inputPath))
		
		thread1=ClockThread(TotalFileNum,FinishedFileNum)
		thread1.start()
		
		if scale in ['4','8']:
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			print('')
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+"_Waifu2x.png"+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+"_Waifu2x.png"+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
		
		if scale == '8':	
			print('')
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+"_Waifu2x.png"+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+"_Waifu2x.png"+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
	
		if scale in ['2','1']:
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
		
		if thread1.isAlive():
			stop_thread(thread1)	
		print('')	
		
			
		if saveAsJPG == 'y':
			if os.path.exists(scaledFilePath+"_Waifu2x.png"):
				print('\n Convert image..... \n')
				imageio.imwrite(scaledFilePath+"_Waifu2x.jpg", imageio.imread(scaledFilePath+"_Waifu2x.png"), 'JPG', quality = JpgQuality)
				remove_safe(scaledFilePath+"_Waifu2x.png")
		
		
		if delorginal == 'y':
			if os.path.exists(scaledFilePath+"_Waifu2x.png") or os.path.exists(scaledFilePath+"_Waifu2x.jpg"):
				os.system('del /q "'+inputPath+'"')
			else:
				list_Content=[
					'echo --------------------------------------------------------------\n',
					'echo Error occured, in order to save your files, the original file :\n',
					'echo '+inputPath+'\n'
					'echo will not be deleted.\n'
					'echo --------------------------------------------------------------\n'
				]
				
				Pop_up_window('Error_file_not_del','Error',list_Content,'')
		FinishedFileNum = FinishedFileNum+1
		
#==============================================  process_gif_scale_modeABC =================================================
def process_gif_scale_modeABC(inputPathList_files,orginalFileNameAndFullname,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,optimizeGif,delorginal):
	Gif_inputPathList_files = []
	for inputPath in inputPathList_files:
		file_ext = os.path.splitext(inputPath)[1]
		if file_ext != '.gif':
			continue
		else:
			Gif_inputPathList_files.append(inputPath)
	
	Total_num = len(Gif_inputPathList_files)
	finished_num = 1
	for inputPath in Gif_inputPathList_files:
		Window_Title('  [Scale GIF]  Files: '+'('+str(finished_num)+'/'+str(Total_num)+')')
		scaledFilePath = os.path.splitext(inputPath)[0]
			
		Duration_gif=getDuration(inputPath)
		print('Split gif.....')
		splitGif(inputPath,scaledFilePath)
		
		oldfilenumber=FileCount(scaledFilePath+'_split')
				
		scalepath = scaledFilePath+'_split\\scaled\\'
		
		if os.path.exists(scaledFilePath+'_split\\scaled') :
			os.system("rd /s/q \""+scaledFilePath+'_split\\scaled'+'"')
		os.mkdir(scaledFilePath+'_split\\scaled')
		
		print('scale images.....')
		if scale in ['4','8']: 
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 1)
			thread1.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread1.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
			
			for files in os.walk(scalepath):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					os.rename(os.path.join(scalepath,fileNameAndExt),os.path.join(scalepath,fileName+'.png'))
			
			old_file_list=[]
			for path,useless,fnames in os.walk(scalepath):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					f_name_ext = os.path.splitext(fname)[0]
					f_name = os.path.splitext(fname)[0]
					if f_name == f_name_ext:
						old_file_list.append(os.path.splitext(fname)[0])
				break
			
			old_file_list_prograsssbar=[]
			for path,useless,fnames in os.walk(scalepath):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					old_file_list_prograsssbar.append(fname)
				break
			
			thread_DelOldFileThread_4x=DelOldFileThread_4x(scalepath,old_file_list)
			thread_DelOldFileThread_4x.start()
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 2,old_file_list_prograsssbar=old_file_list_prograsssbar)
			thread1.start()	
			
			print('')	
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread1.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
				
			while thread_DelOldFileThread_4x.isAlive():
				time.sleep(1)
			
			for files in os.walk(scalepath):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					os.rename(os.path.join(scalepath,fileNameAndExt),os.path.join(scalepath,fileName+'.png'))
			print('')
		if scale == '8':
			old_file_list=[]
			for path,useless,fnames in os.walk(scalepath):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					f_name_ext = os.path.splitext(fname)[0]
					f_name = os.path.splitext(fname)[0]
					if f_name == f_name_ext:
						old_file_list.append(os.path.splitext(fname)[0])
				break
			old_file_list_prograsssbar=[]
			for path,useless,fnames in os.walk(scalepath):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					old_file_list_prograsssbar.append(fname)
				break
			thread_DelOldFileThread_4x=DelOldFileThread_4x(scalepath,old_file_list)
			thread_DelOldFileThread_4x.start()
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 3,old_file_list_prograsssbar = old_file_list_prograsssbar)
			thread1.start()	
			print('')	
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread1.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
				
			while thread_DelOldFileThread_4x.isAlive():
				time.sleep(1)
			for files in os.walk(scalepath):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					os.rename(os.path.join(scalepath,fileNameAndExt),os.path.join(scalepath,fileName+'.png'))
			
			
		if scale in ['2','1']:
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 0)
			thread1.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread1.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
				
			for files in os.walk(scalepath):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					os.rename(os.path.join(scalepath,fileNameAndExt),os.path.join(scalepath,fileName+'.png'))
		print('')	
		
		print('Assembling Gif.....')
		assembleGif(scaledFilePath,Duration_gif)
		print('Gif assembled')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal == 'y':
			gif_name=scaledFilePath+'_waifu2x.gif'
			if os.path.exists(gif_name):
				if os.path.getsize(gif_name)>0:
					os.system('del /q "'+inputPath+'"')
			else:
				list_Content=[
					'echo --------------------------------------------------------------\n',
					'echo Error occured, in order to save your files, the original file :\n',
					'echo '+inputPath+'\n'
					'echo will not be deleted.\n'
					'echo --------------------------------------------------------------\n'
				]
				
				Pop_up_window('Error_file_not_del','Error',list_Content,'')
			
		if optimizeGif == 'y':
			print('Compressing gif....')
			compress_gif(scaledFilePath+'_waifu2x.gif','1')
			remove_safe(scaledFilePath+'_waifu2x.gif')
			print('Gif compressed\n')
		else:
			print('')
		finished_num = finished_num+1
	Window_Title('')

#================================================= Image_Gif_Scale_Denoise_waifu2x_converter ===========================================
def Image_Gif_Scale_Denoise_waifu2x_converter():
	print(' Note: The input path must not contain special characters,')
	print(' which will cause compatibility problems.')
	print('─'*80)
	print("                Scale & Denoise Image & GIF - Waifu2x-converter")
	print('─'*80)
	print(" Type 'r' to return to the previous menu.")
	print(" Type 'o' to stop input more path, and input path must be a folder or a file.")
	print(" Scaled images & gifs will be in the input path.")
	print('─'*80)
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []
	JpgQuality=100
	Image_GIF_scale_mode = settings_values['Image_GIF_scale_mode']
	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input(' Input path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			if inputPath.lower() == 'r':
				return 1
			elif inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-'*32)
				print(' Error,input path is invalid !!')
				print('-'*32)
			else:
				inputPathError = False
		if inputPathOver :
			inputPathList.append(inputPath)
			
	inputPathList = Deduplicate_list(inputPathList)
	
	pathlist_files_folder = Separate_files_folder(inputPathList)
	
	inputPathList_files = pathlist_files_folder[0]
	inputPathList_folders = pathlist_files_folder[1]
	scan_subfolders = 'n'
	if inputPathList_folders != []:
		scan_subfolders = input_scan_subfolders()
		if scan_subfolders == 'r':
			return 1
	
	if scan_subfolders == 'y':
		subfolders_list = []
		for inputPathList_folders_folder_scan in inputPathList_folders:
			for path_scansub,useless,filename in os.walk(inputPathList_folders_folder_scan):
				for dirs in os.walk(path_scansub):
					subfolders_list.append(str(dirs[0]))
				break
		inputPathList_folders = subfolders_list
	
	for folder in inputPathList_folders:
		for path,useless,fnames in os.walk(folder):
			fnames = dict.fromkeys(fnames,'')
			for fname in fnames:
				inputPathList_files.append(path+'\\'+fname)
			break
			
	
	scale = input_scale_Anime4k_waifu2x_converter()
	if scale == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel_waifu2x_converter()
	if noiseLevel == 'r':
		return 1
	
	Gif_exists = False
	for file_ in inputPathList_files:
		if os.path.splitext(file_)[1] == '.gif':
			Gif_exists=True
			break
	if Gif_exists:
		optimizeGif = settings_values['optimizeGif']
	
	Image_exists = False
	for file_ in inputPathList_files:
		if os.path.splitext(file_)[1] in ['.jpg','.png','.jpeg','.tif','.tiff','.bmp','.tga']:
			Image_exists=True
			break
	if Image_exists:
		saveAsJPG = settings_values['saveAsJPG']
		Compress = settings_values['Compress']
		if Compress.lower() == 'y':
			JpgQuality=90
	
	delorginal = input_delorginal()
	if delorginal == 'r':
		return 1
	
	turnoff = input_turnoff()
	if turnoff == 'r':
		return 1
		
	print('-'*50)
	
	total_time_start=time.time()
	
	#======================= 单文件 =========================
	if inputPathList_files != []:
		if Gif_exists:
			inputPathList_files_gif = []
			for file_ in inputPathList_files:
				if os.path.splitext(file_)[1] == '.gif':
					inputPathList_files_gif.append(file_)
			process_gif_scale_modeABC_waifu2x_converter(inputPathList_files_gif,scale,noiseLevel,optimizeGif,delorginal)
		
		if Image_exists:
			inputPathList_files_images = []
			for file_ in inputPathList_files:
				if os.path.splitext(file_)[1] in [".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]:
					inputPathList_files_images.append(file_)
			Process_ImageModeC_waifu2x_converter(inputPathList_files_images,JpgQuality,noiseLevel,scale,saveAsJPG,delorginal)
	total_time_end=time.time()
	
	print('\n Total time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff=='y':
		ShutDown()
	Play_Notification_Sound()
	
	input('\n Press Enter key to return to the menu.')
	Window_Title('')

#=================================================  waifu2x_converter_Thread  ============================================

class waifu2x_converter_Thread(threading.Thread):
	def __init__(self,inputPath,outputPath,scale,noiseLevel):
		threading.Thread.__init__(self)
		self.inputPath = inputPath
		self.outputPath = outputPath
		self.scale = scale
		self.noiseLevel = noiseLevel
        
	def run(self):
		inputPath = self.inputPath  
		outputPath = self.outputPath 
		scale = self.scale 
		noiseLevel = self.noiseLevel 

		model_dir = 'waifu2x-converter\\models_rgb'
		os.system('waifu2x-converter\\waifu2x-converter_x64.exe -i "'+inputPath+'" -o "'+outputPath+'" --scale_ratio '+scale+' --noise_level '+noiseLevel+' --model_dir '+model_dir)


class waifu2x_converter_Thread_ImageModeC(threading.Thread):
	def __init__(self,inputPath,JpgQuality,noiseLevel,scale,saveAsJPG,delorginal):
		threading.Thread.__init__(self)
		self.inputPath = inputPath
		self.JpgQuality = JpgQuality
		self.noiseLevel = noiseLevel
		self.scale = scale
		self.saveAsJPG = saveAsJPG
		self.delorginal = delorginal
        
	def run(self):
		inputPath = self.inputPath 
		JpgQuality = self.JpgQuality 
		noiseLevel = self.noiseLevel 
		scale = self.scale
		saveAsJPG = self.saveAsJPG 
		delorginal = self.delorginal 

		scaledFilePath = os.path.splitext(inputPath)[0]
		fileNameAndExt=str(os.path.basename(inputPath))
		
		model_dir = 'waifu2x-converter\\models_rgb'
		os.system('waifu2x-converter\\waifu2x-converter_x64.exe -i "'+inputPath+'" -o "'+scaledFilePath+"_Waifu2x.png"+'" --scale_ratio '+scale+' --noise_level '+noiseLevel+' --model_dir '+model_dir)
		print('')	
		if saveAsJPG == 'y':
			if os.path.exists(scaledFilePath+"_Waifu2x.png"):
				print('\n Convert image..... \n')
				imageio.imwrite(scaledFilePath+"_Waifu2x.jpg", imageio.imread(scaledFilePath+"_Waifu2x.png"), 'JPG', quality = JpgQuality)
				remove_safe(scaledFilePath+"_Waifu2x.png")
		
		
		if delorginal == 'y':
			if os.path.exists(scaledFilePath+"_Waifu2x.png") or os.path.exists(scaledFilePath+"_Waifu2x.jpg"):
				os.system('del /q "'+inputPath+'"')
			else:
				list_Content=[
					'echo --------------------------------------------------------------\n',
					'echo Error occured, in order to save your files, the original file :\n',
					'echo '+inputPath+'\n'
					'echo will not be deleted.\n'
					'echo --------------------------------------------------------------\n'
				]
				
				Pop_up_window('Error_file_not_del','Error',list_Content,'')
		return 0


#=============================================  Process_ImageModeC_waifu2x_converter  ======================================================

def Process_ImageModeC_waifu2x_converter(inputPathList_Image,JpgQuality,noiseLevel,scale,saveAsJPG,delorginal):
	settings_values = ReadSettings()
	TotalFileNum = len(inputPathList_Image)
	max_threads = settings_values['Number_of_threads_Waifu2x_converter']
	FinishedFileNum = 0
	thread_files = []
	ETA = 'Null'
	time_start_scale = time.time()
	
	for inputPath in inputPathList_Image:
		Window_Title('  [Scale Imgae]  Files: '+'('+str(FinishedFileNum)+'/'+str(TotalFileNum)+')  ETA: '+ETA)
		
		thread_files.append(inputPath)
		if len(thread_files) == max_threads:
			for fname_ in thread_files:
				thread_image=waifu2x_converter_Thread_ImageModeC(fname_,JpgQuality,noiseLevel,scale,saveAsJPG,delorginal)
				thread_image.start()
			while True:
				if thread_image.isAlive()== False:
					break
				else:
					time.sleep(0.02)
			FinishedFileNum = FinishedFileNum+len(thread_files)
			
			remain_frames = TotalFileNum - FinishedFileNum
			time_cost = time.time()-time_start_scale
			time_remain = (time_cost/FinishedFileNum)*remain_frames
			ETA = time.strftime('%H:%M:%S', time.localtime(time.time()+time_remain))
			
			thread_files = []
			
	if thread_files != []:
		#FinishedFileNum = TotalFileNum
		Window_Title('  [Scale Imgae]  Files: '+'('+str(FinishedFileNum)+'/'+str(TotalFileNum)+')  ETA: '+ETA)
		for fname_ in thread_files:
			thread_image=waifu2x_converter_Thread_ImageModeC(fname_,JpgQuality,noiseLevel,scale,saveAsJPG,delorginal)
			thread_image.start()
		thread_files = []
		while True:
			if thread_image.isAlive()== False:
				break
			else:
				time.sleep(0.02)
	while True:
		if Process_exist('waifu2x-converter_x64.exe')== False:
			break
		else:
			time.sleep(0.02)
	Window_Title('')
	

#==============================================  process_gif_scale_modeABC_waifu2x_converter =================================================
def process_gif_scale_modeABC_waifu2x_converter(inputPathList_files,scale,noiseLevel,optimizeGif,delorginal):
	settings_values = ReadSettings()
	Gif_inputPathList_files = []
	for inputPath in inputPathList_files:
		file_ext = os.path.splitext(inputPath)[1]
		if file_ext != '.gif':
			continue
		else:
			Gif_inputPathList_files.append(inputPath)
	
	Total_num = len(Gif_inputPathList_files)
	finished_num = 1
	for inputPath in Gif_inputPathList_files:
		scaledFilePath = os.path.splitext(inputPath)[0]
			
		Duration_gif=getDuration(inputPath)
		print('Split gif.....')
		splitGif(inputPath,scaledFilePath)
		
		
		time_start_scale = time.time()
		
		oldfilenumber=FileCount(scaledFilePath+'_split')
				
		scalepath = scaledFilePath+'_split\\scaled\\'
		
		if os.path.exists(scaledFilePath+'_split\\scaled') :
			os.system("rd /s/q \""+scaledFilePath+'_split\\scaled'+'"')
		os.mkdir(scaledFilePath+'_split\\scaled')
		
		print('scale images.....')
		
		input_folder = scaledFilePath+'_split'
		output_folder = scaledFilePath+'_split\\scaled'
		model_dir = 'waifu2x-converter\\models_rgb'
		for path,useless,fnames in os.walk(input_folder):
			total_frame = len(fnames)
			
			max_threads = settings_values['Number_of_threads_Waifu2x_converter']
			finished_frame = 0
			thread_files = []
			fnames = dict.fromkeys(fnames,'')
			ETA = 'Null'
			
			for fname in fnames:
				Window_Title('  [Scale GIF]  Files: '+'('+str(finished_num)+'/'+str(Total_num)+')  Frames: ('+str(finished_frame)+'/'+str(total_frame)+')  ETA: '+ETA)
				thread_files.append(fname)
				if len(thread_files) == max_threads:
					for fname_ in thread_files:
						thread1=waifu2x_converter_Thread(path+'\\'+fname_,output_folder+'\\'+fname_,scale,noiseLevel)
						thread1.start()
					while True:
						if thread1.isAlive()== False:
							break
					finished_frame = finished_frame+len(thread_files)
					
					remain_frames = total_frame - finished_frame
					time_cost = time.time()-time_start_scale
					time_remain = (time_cost/finished_frame)*remain_frames
					ETA = time.strftime('%H:%M:%S', time.localtime(time.time()+time_remain))
					
					thread_files = []
					
			if thread_files != []:
				#finished_frame = total_frame
				Window_Title('  [Scale GIF]  Files: '+'('+str(finished_num)+'/'+str(Total_num)+')  Frames: ('+str(finished_frame)+'/'+str(total_frame)+')  ETA: '+ETA)
				for fname_ in thread_files:
					thread1=waifu2x_converter_Thread(path+'\\'+fname_,output_folder+'\\'+fname_,scale,noiseLevel)
					thread1.start()
				while True:
					if thread1.isAlive()== False:
						break
				thread_files = []
				while True:
					if Process_exist('waifu2x-converter_x64.exe')== False:
						break
					else:
						time.sleep(0.02)
			break
		
		print('')	
		print('Assembling Gif.....')
		assembleGif(scaledFilePath,Duration_gif)
		print('Gif assembled')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal == 'y':
			gif_name=scaledFilePath+'_waifu2x.gif'
			if os.path.exists(gif_name):
				if os.path.getsize(gif_name)>0:
					os.system('del /q "'+inputPath+'"')
			else:
				list_Content=[
					'echo --------------------------------------------------------------\n',
					'echo Error occured, in order to save your files, the original file :\n',
					'echo '+inputPath+'\n'
					'echo will not be deleted.\n'
					'echo --------------------------------------------------------------\n'
				]
				
				Pop_up_window('Error_file_not_del','Error',list_Content,'')
			
		
		if optimizeGif == 'y':
			print('Compressing gif....')
			compress_gif(scaledFilePath+'_waifu2x.gif','1')
			remove_safe(scaledFilePath+'_waifu2x.gif')
			print('Gif compressed\n')
		else:
			print('')
		finished_num = finished_num+1
	Window_Title('')

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
								remove_safe(inputpath+f_name+'.png')
								inputpath_deled_list.append(f_name)
				break
			time.sleep(0.5)

#=============================================  Scale & Denoise Video_waifu2x_converter  ====================================
def Scale_Denoise_Video_waifu2x_converter():
	print(' Note: The input path must not contain special characters,')
	print(' which will cause compatibility problems.')
	print('─'*83)
	print("                       Scale & Denoise Video - waifu2x-converter")
	print('─'*83)
	print(" Type 'r' to return to the previous menu.")
	print(" Type 'o' to stop input more path, and input path must be a folder or a video file.")
	print(" Scaled files will be in the input-path.")
	print('─'*83)
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input(' Input path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath.lower() == 'r':
				return 1
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-'*32)
				print(' Error,input path is invalid !!')
				print('-'*32)
			else:
				inputPathError = False
		if inputPathOver :
			inputPathList.append(inputPath)
	inputPathList = Deduplicate_list(inputPathList)
	
	pathlist_files_folder = Separate_files_folder(inputPathList)
	
	inputPathList_files = pathlist_files_folder[0]
	inputPathList_folders = pathlist_files_folder[1]
	scan_subfolders = 'n'
	if inputPathList_folders != []:
		scan_subfolders = input_scan_subfolders()
		if scan_subfolders == 'r':
			return 1
	
	if scan_subfolders == 'y':
		subfolders_list = []
		for inputPathList_folders_folder_scan in inputPathList_folders:
			for path_scansub,useless,filename in os.walk(inputPathList_folders_folder_scan):
				for dirs in os.walk(path_scansub):
					subfolders_list.append(str(dirs[0]))
				break
		inputPathList_folders = subfolders_list
	
	scale = input_scale_Anime4k_waifu2x_converter()
	if scale == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel_waifu2x_converter()
	if noiseLevel == 'r':
		return 1
			
	delorginal = input_delorginal()
	if delorginal == 'r':
		return 1
		
	turnoff = input_turnoff()
	if turnoff == 'r':
		return 1
	
		
	print('-'*50)
	
	total_time_start=time.time()
	 
	inputPathList_file_video = []
	for folders in inputPathList_folders:
		for path,useless,fnames in os.walk(folders):
			fnames = dict.fromkeys(fnames,'')
			for fname in fnames:
				inputPathList_file_video.append(path+'\\'+fname)
			break
	inputPathList_files = inputPathList_file_video + inputPathList_files
	process_video_modeABC_waifu2x_converter(inputPathList_files,scale,noiseLevel,delorginal)
	total_time_end=time.time()
	
	print('\n Total time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff=='y':
		ShutDown()
	Play_Notification_Sound()
	input('\n Press Enter key to exit')

#======================================= process_video_modeABC_waifu2x_converter ============================
def process_video_modeABC_waifu2x_converter(inputPathList_files,scale,noiseLevel,delorginal):
	settings_values = ReadSettings()
	total_num = len(inputPathList_files)
	finished_num = 1
	for inputPath in inputPathList_files:
		
		#========================== 拆解视频 ====================
		video2images(inputPath) #拆解视频
		
		time_start_scale = time.time()
		
		frames_dir = os.path.dirname(inputPath)+'\\'+'frames_waifu2x'.replace("\\\\", "\\")
		
		oldfilenumber=FileCount(frames_dir)
		if os.path.exists(frames_dir+"\\scaled\\") :
			os.system("rd /s/q \""+frames_dir+"\\scaled\\"+'"')
		os.mkdir(frames_dir+"\\scaled\\")
		
		thread_VideoDelFrameThread = VideoDelFrameThread (inputPath)
		thread_VideoDelFrameThread.start()
		
		input_folder = frames_dir
		output_folder = frames_dir+"\\scaled"
		model_dir = 'waifu2x-converter\\models_rgb'
		for path,useless,fnames in os.walk(input_folder):
			total_frames = len(fnames)
			max_threads = settings_values['Number_of_threads_Waifu2x_converter']
			finished_frames = 0
			thread_files = []
			fnames = dict.fromkeys(fnames,'')
			ETA = 'Null'
			for fname in fnames:
				Window_Title('  [Scale Video]  Video: '+'('+str(finished_num)+'/'+str(total_num)+')  Frames:('+str(finished_frames)+'/'+str(total_frames)+')  ETA: '+ETA)
				thread_files.append(fname)
				if len(thread_files) == max_threads:
					for fname_ in thread_files:
						thread1=waifu2x_converter_Thread(path+'\\'+fname_,output_folder+'\\'+fname_+'.png',scale,noiseLevel)
						thread1.start()
					while True:
						if thread1.isAlive()== False:
							break
					finished_frames = finished_frames+len(thread_files)
					
					remain_frames = total_frames - finished_frames
					time_cost = time.time()-time_start_scale
					time_remain = (time_cost/finished_frames)*remain_frames
					ETA = time.strftime('%H:%M:%S', time.localtime(time.time()+time_remain))
					
					thread_files = []
				
			if thread_files != []:
				#finished_frames = total_frames
				Window_Title('  [Scale Video]  Video: '+'('+str(finished_num)+'/'+str(total_num)+')  Frames: ('+str(finished_frames)+'/'+str(total_frames)+')  ETA: '+ETA)
				for fname_ in thread_files:
					thread1=waifu2x_converter_Thread(path+'\\'+fname_,output_folder+'\\'+fname_+'.png',scale,noiseLevel)
					thread1.start()
				while True:
					if thread1.isAlive()== False:
						break
				thread_files = []
			while True:
				if Process_exist('waifu2x-converter_x64.exe')== False:
					break
				else:
					time.sleep(0.02)
			break
		
		while thread_VideoDelFrameThread.isAlive():
			time.sleep(1)
		
		for files in os.walk(frames_dir+"\\scaled"):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
		
		
		#====================== 合成视频 ====================
		images2video(os.path.splitext(inputPath)[0]+'.mp4')#合成视频	
		
		if os.path.splitext(inputPath)[1] != '.mp4':
			remove_safe(os.path.splitext(inputPath)[0]+'.mp4')
		
		res_video = os.path.splitext(inputPath)[0]+'_waifu2x.mp4'
	
		if delorginal == 'y':
			if os.path.exists(res_video):
				if os.path.getsize(res_video) > 0:
					os.system('del /q "'+inputPath+'"')	
				else:
					print(' Error occured, failed to generate result video.')
			else:
				print(' Error occured, failed to generate result video.')
		finished_num = finished_num+1
	Window_Title('')

#=============================================  Scale & Denoise Video  ====================================
def Scale_Denoise_Video():
	print(' Note: The input path must not contain special characters,')
	print(' which will cause compatibility problems.')
	print('─'*83)
	print("                     Scale & Denoise Video - Waifu2x-ncnn-vulkan")
	print('─'*83)
	print(" Type 'r' to return to the previous menu.")
	print(" Type 'o' to stop input more path, and input path must be a folder or a video file.")
	print(" Scaled files will be in the input-path.")
	print('─'*83)
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input(' Input path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath.lower() == 'r':
				return 1
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-'*32)
				print(' Error,input path is invalid !!')
				print('-'*32)
			else:
				inputPathError = False
		if inputPathOver :
			inputPathList.append(inputPath)
	inputPathList = Deduplicate_list(inputPathList)
	
	pathlist_files_folder = Separate_files_folder(inputPathList)
	
	inputPathList_files = pathlist_files_folder[0]
	inputPathList_folders = pathlist_files_folder[1]
	scan_subfolders = 'n'
	if inputPathList_folders != []:
		scan_subfolders = input_scan_subfolders()
		if scan_subfolders == 'r':
			return 1
	
	if scan_subfolders == 'y':
		subfolders_list = []
		for inputPathList_folders_folder_scan in inputPathList_folders:
			for path_scansub,useless,filename in os.walk(inputPathList_folders_folder_scan):
				for dirs in os.walk(path_scansub):
					subfolders_list.append(str(dirs[0]))
				break
		inputPathList_folders = subfolders_list
	
	scale = input_scale()
	if scale == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
	if noiseLevel == 'r':
		return 1
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = settings_values['load_proc_save_str']
	if multiThread_Scale == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	tileSize = settings_values['tileSize']
	gpuId = settings_values['gpuId']
	gpuId_str=''
	if gpuId != 'auto':
		gpuId_str = ' -g '+gpuId
		
	delorginal = input_delorginal()
	if delorginal == 'r':
		return 1
		
	turnoff = input_turnoff()
	if turnoff == 'r':
		return 1
	
	sleepMode = input_sleepMode()
	if sleepMode == 'r':
		return 1
	elif sleepMode == 'y':
		load_proc_save_str = ' -j 1:1:1 '
		
	print('-'*50)
	
	total_time_start=time.time()
	 
	inputPathList_file_video = []
	for folders in inputPathList_folders:
		for path,useless,fnames in os.walk(folders):
			fnames = dict.fromkeys(fnames,'')
			for fname in fnames:
				inputPathList_file_video.append(path+'\\'+fname)
			break
	inputPathList_files = inputPathList_file_video + inputPathList_files
	process_video_modeABC(inputPathList_files,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,delorginal)
	total_time_end=time.time()
	
	print('\n Total time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff=='y':
		ShutDown()
	Play_Notification_Sound()
	input('\n Press Enter key to exit')
	
#======================================= process_video_modeABC ============================
def process_video_modeABC(inputPathList_files,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,delorginal):
	total_num = len(inputPathList_files)
	finished_num = 1
	for inputPath in inputPathList_files:
		Window_Title('  [Scale Video]  Video: '+'('+str(finished_num)+'/'+str(total_num)+')')
		video2images(inputPath) #拆解视频
		
		frames_dir = os.path.dirname(inputPath)+'\\'+'frames_waifu2x'.replace("\\\\", "\\")
		
		oldfilenumber=FileCount(frames_dir)
		if os.path.exists(frames_dir+"\\scaled\\") :
			os.system("rd /s/q \""+frames_dir+"\\scaled\\"+'"')
		os.mkdir(frames_dir+"\\scaled\\")
		
		if scale in ['4','8']:
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 1)
			thread2.start()
			thread_VideoDelFrameThread = VideoDelFrameThread (inputPath)
			thread_VideoDelFrameThread.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread2.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
					
			while thread_VideoDelFrameThread.isAlive():
				time.sleep(1)
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
			
			video_dir = os.path.dirname(inputPath)+'\\'.replace("\\\\", "\\")
			frames_scaled_dir = video_dir+'frames_waifu2x\\scaled\\'
			frame_list = []
			for path,useless,fnames in os.walk(frames_scaled_dir):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					f_name_ext = os.path.splitext(fname)[0]
					f_name = os.path.splitext(fname)[0]
					if f_name == f_name_ext:
						frame_list.append(os.path.splitext(fname)[0])
				break
			
			thread_VideoDelFrameThread_4x = VideoDelFrameThread_4x (inputPath,frame_list)
			thread_VideoDelFrameThread_4x.start()
			
			old_file_list_prograsssbar=[]
			for path,useless,fnames in os.walk(video_dir+'frames_waifu2x\\scaled\\'):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					old_file_list_prograsssbar.append(fname)
				break
					
			thread2 = PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 2,old_file_list_prograsssbar=old_file_list_prograsssbar)
			thread2.start()
			print('')
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread2.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
					
			while thread_VideoDelFrameThread_4x.isAlive():
				time.sleep(1)
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
		if scale == '8':
			video_dir = os.path.dirname(inputPath)+'\\'.replace("\\\\", "\\")
			frames_scaled_dir = video_dir+'frames_waifu2x\\scaled\\'
			frame_list = []
			for path,useless,fnames in os.walk(frames_scaled_dir):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					f_name_ext = os.path.splitext(fname)[0]
					f_name = os.path.splitext(fname)[0]
					if f_name == f_name_ext:
						frame_list.append(os.path.splitext(fname)[0])
				break
			
			thread_VideoDelFrameThread_4x = VideoDelFrameThread_4x (inputPath,frame_list)
			thread_VideoDelFrameThread_4x.start()
			
			old_file_list_prograsssbar=[]
			for path,useless,fnames in os.walk(video_dir+'frames_waifu2x\\scaled\\'):
				fnames = dict.fromkeys(fnames,'')
				for fname in fnames:
					old_file_list_prograsssbar.append(fname)
				break
					
			thread2 = PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 3,old_file_list_prograsssbar=old_file_list_prograsssbar)
			thread2.start()
			print('')
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'-1'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread2.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
					
			while thread_VideoDelFrameThread_4x.isAlive():
				time.sleep(1)
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
			
		if scale in ['2','1']:
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 0)
			thread2.start()
			thread_VideoDelFrameThread = VideoDelFrameThread (inputPath)
			thread_VideoDelFrameThread.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			time_wait_prograssbar = 0
			while thread2.isAlive():
				time_wait_prograssbar = time_wait_prograssbar+1
				time.sleep(1.1)
				if time_wait_prograssbar == 2:
					break
			
			while thread_VideoDelFrameThread.isAlive():
				time.sleep(1)
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
		
		images2video(os.path.splitext(inputPath)[0]+'.mp4')#合成视频	
		
	
				
		if os.path.splitext(inputPath)[1] != '.mp4':
			remove_safe(os.path.splitext(inputPath)[0]+'.mp4')
			
		res_video = os.path.splitext(inputPath)[0]+'_waifu2x.mp4'
	
		if os.path.splitext(inputPath)[1] != '.mp4':
			os.system('del /q "'+os.path.splitext(inputPath)[0]+'.mp4'+'"')
		if delorginal == 'y':
			if os.path.exists(res_video):
				if os.path.getsize(res_video) > 0:
					os.system('del /q "'+inputPath+'"')	
				else:
					print('Error occured, failed to generate result video.')
			else:
				print('Error occured, failed to generate result video.')
		finished_num = finished_num+1
	Window_Title('')

#=============================================  Scale Video - Anime4K  ====================================
def Scale_Denoise_Video_Anime4K():
	print(' Note: The input path must not contain special characters,')
	print(' which will cause compatibility problems.')
	print('─'*83)
	print("                              Scale Video - Anime4K")
	print('─'*83)
	print(" Type 'r' to return to the previous menu.")
	print(" Type 'o' to stop input more path, and input path must be a folder or a video file.")
	print(" Scaled files will be in the input-path.")
	print('─'*83)
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input(' Input path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath.lower() == 'r':
				return 1
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-'*31)
				print(' Error,input path is invalid!!')
				print('-'*31)
			else:
				inputPathError = False
		if inputPathOver :
			inputPathList.append(inputPath)
	inputPathList = Deduplicate_list(inputPathList)
	
	pathlist_files_folder = Separate_files_folder(inputPathList)
	
	inputPathList_files = pathlist_files_folder[0]
	inputPathList_folders = pathlist_files_folder[1]
	scan_subfolders = 'n'
	if inputPathList_folders != []:
		scan_subfolders = input_scan_subfolders()
		if scan_subfolders == 'r':
			return 1
	
	if scan_subfolders == 'y':
		subfolders_list = []
		for inputPathList_folders_folder_scan in inputPathList_folders:
			for path_scansub,useless,filename in os.walk(inputPathList_folders_folder_scan):
				for dirs in os.walk(path_scansub):
					subfolders_list.append(str(dirs[0]))
				break
		inputPathList_folders = subfolders_list
	
	scale = input_scale_Anime4k_waifu2x_converter()
	if scale == 'r':
		return 1
		
	delorginal = input_delorginal()
	if delorginal == 'r':
		return 1
		
	turnoff = input_turnoff()
	if turnoff == 'r':
		return 1
		
	print('-'*50)
	
	total_time_start=time.time()
	 
	inputPathList_file_video = []
	for folders in inputPathList_folders:
		for path,useless,fnames in os.walk(folders):
			fnames = dict.fromkeys(fnames,'')
			for fname in fnames:
				inputPathList_file_video.append(path+'\\'+fname)
			break
	inputPathList_files = inputPathList_file_video + inputPathList_files
	process_video_modeABC_Anime4K(inputPathList_files,scale,delorginal)
	total_time_end=time.time()
	
	print('\n Total time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff=='y':
		ShutDown()
	Play_Notification_Sound()
	input('\n Press Enter key to exit')

#======================================= process_video_modeABC_Anime4K ============================

class Video_scale_Anime4K_Thread (threading.Thread):
	def __init__(self,frame,out_path,scale):
		threading.Thread.__init__(self)
		self.frame = frame
		self.out_path =out_path
		self.scale =scale
        
	def run(self):
		frame = self.frame
		out_path = self.out_path
		scale=self.scale
		
		fram_fname = frame.split("\\")[-1]
		os.system('java -jar Anime4K\\Anime4K.jar "'+frame+'" "'+out_path+'\\'+fram_fname+'.png" '+scale)

def Video_scale_Anime4K(in_path,out_path,scale):
	settings_values = ReadSettings()
	max_threads = settings_values['Number_of_threads_Anime4k']
	
	thread_files = []
	
	Frame_list = []
	for path,useless,fnames in os.walk(in_path):
		fnames = dict.fromkeys(fnames,'')
		for fname in fnames:
			Frame_list.append(path+'\\'+fname)
		break
	for frame in Frame_list:
		thread_files.append(frame)
		if len(thread_files) == max_threads:
			for frame in thread_files:
				thread1=Video_scale_Anime4K_Thread(frame,out_path,scale)
				thread1.start()
			while True:
				if thread1.isAlive()== False:
					break
			thread_files = []
	if thread_files != []:
		for frame in thread_files:
			thread1=Video_scale_Anime4K_Thread(frame,out_path,scale)
			thread1.start()
		while True:
			if thread1.isAlive()== False:
				break
		thread_files = []

def process_video_modeABC_Anime4K(inputPathList_files,scale,delorginal):
	total_num = len(inputPathList_files)
	finished_num = 1
	for inputPath in inputPathList_files:
		Window_Title('  [Scale Video]  Video: '+'('+str(finished_num)+'/'+str(total_num)+')')
		video2images(inputPath) #拆解视频
		
		frames_dir = os.path.dirname(inputPath)+'\\'+'frames_waifu2x'.replace("\\\\", "\\")
		
		oldfilenumber=FileCount(frames_dir)
		if os.path.exists(frames_dir+"\\scaled\\") :
			os.system("rd /s/q \""+frames_dir+"\\scaled\\"+'"')
		os.mkdir(frames_dir+"\\scaled\\")
			
		thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 0)
		thread2.start()
		thread_VideoDelFrameThread = VideoDelFrameThread (inputPath)
		thread_VideoDelFrameThread.start()
		Video_scale_Anime4K(frames_dir,frames_dir+"\\scaled",scale)
		
		time_wait_prograssbar = 0
		while thread2.isAlive():
			time_wait_prograssbar = time_wait_prograssbar+1
			time.sleep(1.1)
			if time_wait_prograssbar == 2:
				break
		
		while thread_VideoDelFrameThread.isAlive():
			time.sleep(1)
		
		for files in os.walk(frames_dir+"\\scaled"):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
		
		images2video(os.path.splitext(inputPath)[0]+'.mp4')#合成视频	
		
	
				
		if os.path.splitext(inputPath)[1] != '.mp4':
			os.system('del /q "'+os.path.splitext(inputPath)[0]+'.mp4'+'"')
			
		res_video = os.path.splitext(inputPath)[0]+'_waifu2x.mp4'
	
		if os.path.splitext(inputPath)[1] != '.mp4':
			remove_safe(os.path.splitext(inputPath)[0]+'.mp4')
		if delorginal == 'y':
			if os.path.exists(res_video):
				if os.path.getsize(res_video) > 0:
					os.system('del /q "'+inputPath+'"')	
				else:
					print('Error occured, failed to generate result video.')
			else:
				print('Error occured, failed to generate result video.')
		finished_num = finished_num+1
	Window_Title('')

#===================================================== Compress_image_gif ====================================================
def Compress_image_gif():
	print(' Path and file name contains special characters may cause compatibility problems,')
	print(' change the file name and folder name if something goes wrong.')
	print('─'*83)
	print("                                 Compress image & gif")
	print('─'*83)
	print(" Type 'r' to return to the previous menu.")
	print(" Type 'o' to stop input more path, and input path must be a folder or a file.")
	print(" Compressed images & gifs will be in the input-path.")
	print('─'*83)
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input(' Input path: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'r':
				return 1
			elif inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-'*32)
				print(' Error,input path is invalid !!')
				print('-'*32)
			else:
				inputPathError = False
		if inputPathOver :
			inputPathList.append(inputPath)
	inputPathList = Deduplicate_list(inputPathList)
	
	pathlist_files_folder = Separate_files_folder(inputPathList)
	
	inputPathList_files_input = pathlist_files_folder[0]
	inputPathList_folders = pathlist_files_folder[1]
	scan_subfolders = 'n'
	if inputPathList_folders != []:
		scan_subfolders = input_scan_subfolders()
		if scan_subfolders == 'r':
			return 1
	
	if scan_subfolders == 'y':
		subfolders_list = []
		for inputPathList_folders_folder_scan in inputPathList_folders:
			for path_scansub,useless,filename in os.walk(inputPathList_folders_folder_scan):
				for dirs in os.walk(path_scansub):
					subfolders_list.append(str(dirs[0]))
				break
		inputPathList_folders = subfolders_list
	
	image_exist = False
	for file_ in inputPathList_files_input:
		if os.path.splitext(file_)[1] in ['.jpg','.png','.jpeg','.tif','.tiff','.bmp','.tga']:
			image_exist=True
			break
	if FindImageFiles(inputPathList_folders):
		image_exist = True
	if image_exist:
		image_quality = input_image_quality()
		if image_quality == 'r':
			return 1
		JpgQuality = round(94*(image_quality/100))
		if JpgQuality < 1:
			JpgQuality = 1
	gif_exist = False
	for file_ in inputPathList_files_input:
		if os.path.splitext(file_)[1] == '.gif':
			gif_exist=True
			break
	if FindGifFiles(inputPathList_folders):
		gif_exist = True
	if gif_exist:
		gifCompresslevel=input_gifCompresslevel()
		if gifCompresslevel == 'r':
				return 1
	
	delorginal = input_delorginal()
	if delorginal == 'r':
		return 1
	multiThread = settings_values['multiThread']
	
	print('-'*50)
	
	total_time_start=time.time()
	
	inputPathList_files = []
	for folders in inputPathList_folders:
		for path,useless,fnames in os.walk(folders):
			fnames = dict.fromkeys(fnames,'')
			for fname in fnames:
				inputPathList_files.append(path+'\\'+fname)
			break
	inputPathList_files = inputPathList_files+inputPathList_files_input
			
	if gif_exist  :
		process_gif_compress_modeABC(inputPathList_files,gifCompresslevel,delorginal,multiThread)
	if image_exist  :
		Process_compress_image(inputPathList_files,delorginal,multiThread,JpgQuality)
			
	total_time_end=time.time()
		
	print('\n Total time cost: ',total_time_end-total_time_start,'s\n')
	Play_Notification_Sound()
	input('\n Press enter key to return to the menu')
	
#========================================================== Process_compress_image ======================================================

def Process_compress_image(inputPathList_files,delorginal,multiThread,JpgQuality):
	if multiThread == 'y':
		print('Start compressing images, pls wait....')
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
				remove_safe(scaledFilePath+"_compressed.jpg")
				print('Failed to compress ['+inputPath+'] This image may be already being compressed. You can try to reduce "image quality".')
			else:
				saved_size_str = str(saved_size)+'KB'
				print('Compressed size:'+compressed_size)
				print('Save '+saved_size_str+' !')
				print('')	
				if delorginal == 'y':
					os.system('del /q "'+inputPath+'"')
				
			print('-'*50)

#============================================================= process_gif_compress_modeABC ===================================================

def process_gif_compress_modeABC(inputPathList_files,gifCompresslevel,delorginal,multiThread):
	if multiThread == 'y':
		print('Start compressing .gif, pls wait....')
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
				remove_safe(scaledFilePath+"_compressed.gif")
				print('Failed to compress '+inputPath)
			else:
				saved_size_str = str(saved_size)+'KB'
				print('Compressed size:'+compressed_size)
				print('Save '+saved_size_str+' !')
				print('')	
				if delorginal == 'y':
					os.system('del /q "'+inputPath+'"')
				
			print('-'*50)

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
    def __init__(self, OldFileNum, ScalePath, scale = '2', round_ = 0, old_file_list_prograsssbar = []):
        threading.Thread.__init__(self)
        self.OldFileNum = OldFileNum
        self.ScalePath = ScalePath
        self.scale = scale
        self.round_ = round_
        self.old_file_list_prograsssbar = old_file_list_prograsssbar
    def run(self):
        PrograssBar(self.OldFileNum,self.ScalePath,self.scale,self.round_,self.old_file_list_prograsssbar)


def PrograssBar(OldFileNum,ScalePath,scale,round_,old_file_list_prograsssbar):
	
	ETA = 0
	NewFileNum_Old=0
	PrograssBar_len_old = 0
	
	if OldFileNum != 0:
		
		NewFileNum=0
		time_start = time.time()
		time.sleep(2.5)
		print('\n')
		
		while NewFileNum <= OldFileNum and os.path.exists(ScalePath):
			NewFileNum=0
			if round_ > 1:
				for path,useless,fnames in os.walk(ScalePath):
					fnames = dict.fromkeys(fnames,'')
					for fname in fnames:
						if fname not in old_file_list_prograsssbar:
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
					ETA = int(avgTimeCost*(OldFileNum-NewFileNum))
					NewFileNum_Old = NewFileNum
			
			if ETA != 0:
				if ETA > 1:
					ETA=ETA-1
				ETA_str = time.strftime('%H:%M:%S', time.localtime(time.time()+ETA))
				if scale in ['4','8'] and round_ != 0:
					PrograssBar = "\r"+"Round = "+str(round_)+"  Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): "+BarStr+" "+str(Percent)+"%  ["+'Time Cost: '+timeCost_str+" ]"+" "+"["+'Time Remaining: '+Seconds2hms(ETA)+" ] "+'[ETA: '+ETA_str+' ]'
				else:
					PrograssBar = "\r"+"Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): "+BarStr+" "+str(Percent)+"%  ["+'Time Cost: '+timeCost_str+" ]"+"  "+"["+'Time Remaining: '+Seconds2hms(ETA)+" ] "+'[ETA: '+ETA_str+' ]'
				
				PrograssBar_len_new = len(PrograssBar)
				current_cols = Get_cols_lines()[0]
				if PrograssBar_len_new > current_cols:
					Set_cols_lines(cols = PrograssBar_len_new,lines=38)
				current_cols = Get_cols_lines()[0]
				Add_len = current_cols-PrograssBar_len_new
				if Add_len < 0:
					Add_len = 0
				sys.stdout.write(PrograssBar+' '*Add_len)
				sys.stdout.flush()
					
				
			else:
				if scale in ['4','8'] and round_ != 0:
					PrograssBar = "\r"+"Round = "+str(round_)+"  Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): "+BarStr+" "+str(Percent)+"%  ["+'Time Cost: '+timeCost_str+" ]"
				else:
					PrograssBar = "\r"+"Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): "+BarStr+" "+str(Percent)+"%  ["+'Time Cost: '+timeCost_str+" ]"
				
				PrograssBar_len_new = len(PrograssBar)
				current_cols = Get_cols_lines()[0]
				if PrograssBar_len_new > current_cols:
					Set_cols_lines(cols = PrograssBar_len_new,lines=38)
				current_cols = Get_cols_lines()[0]
				Add_len = current_cols-PrograssBar_len_new
				if Add_len < 0:
					Add_len = 0
				sys.stdout.write(PrograssBar+' '*Add_len)
				sys.stdout.flush()
			if NewFileNum == OldFileNum:
				return 0
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
	clockStr_len_old = 0
	timeStr = ''
	timeCost = ''
	clockStr = ''
	
	
	while True:
		image_time_now = time.time()
		timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		timeCost = int(image_time_now-image_time_start)
		clockStr = "\r"+"Prograss:("+str(FinishedFileNum)+'/'+str(TotalFileNum)+") "+"["+startTime+"]--->["+timeStr+"] = "+Seconds2hms(timeCost)
		
		clockStr_len_new = len(clockStr)
		Add_len = clockStr_len_old - clockStr_len_new
		if Add_len < 0:
			Add_len = 0
		clockStr_len_old = clockStr_len_new
		
		current_cols = Get_cols_lines()[0]
		if (clockStr_len_new+Add_len) > current_cols:
			Set_cols_lines(cols = clockStr_len_new+Add_len+1,lines=38)		
		sys.stdout.write(clockStr+' '*Add_len)
		sys.stdout.flush()
		time.sleep(1)
			
#===================================================== Multithread management ==================================================
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

#======================================================= DelOriginalFiles =======================================
def DelOrgFiles(inputPath):
	
	Exts=[".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]
	Exts = dict.fromkeys(Exts,'')
	for path,useless,fnames in os.walk(inputPath):
		fnames = dict.fromkeys(fnames,'')
		for fname in fnames:
			if os.path.splitext(fname)[1] in Exts:
				remove_safe(path+'\\'+fname)
		break
	
#======================================================= GIF ======================================================

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
			return (duration / 1000)/frames * 100
	return None

def get_frames_gif(FILENAME):
	
	frame_current = 0
	im = Image.open(FILENAME)
	try:
	  while True:
	    frame_current = im.tell()
	    im.seek(frame_current+1)
	except EOFError:
	    pass
	
	frames = len(str(frame_current))
	if frames == 0 :
		frames=1
	return frames

def splitGif(gifFileName,scaledFilePath):
	
	frames = get_frames_gif(gifFileName)
	
	if os.path.exists(scaledFilePath+'_split') :
			os.system("rd /s/q \""+scaledFilePath+'_split'+'"')
	os.mkdir(scaledFilePath+'_split')
	
	os.system('ffmpeg -i "'+gifFileName+'" "'+scaledFilePath+'_split\\%0'+str(frames)+'d.png"')	
	

def assembleGif(scaledFilePath,Duration):
	
	gif_name=scaledFilePath+'_waifu2x.gif'
	
	os.system('convert -delay '+str(Duration)+' -loop 0 "'+scaledFilePath+'_split\\scaled\\'+'*png" "'+gif_name+'"')
	
	
# ~ def assembleGif(scaledFilePath,frames,gifFileName):
	
	# ~ cap = cv2.VideoCapture(gifFileName)
	# ~ fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
	
	# ~ gif_name=scaledFilePath+'_waifu2x.gif'
	
	# ~ os.system('ffmpeg -f image2 -framerate '+str(fps)+' -i "'+scaledFilePath+'_split\\scaled\\'+'%0'+str(frames)+'d.png" "'+gif_name+'"')
	
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
	
	
	
#=========================================================== Video =========================================================
def video2images(inputpath):
	video_dir = os.path.dirname(inputpath)+'\\'.replace("\\\\", "\\")
	video_path_filename = os.path.splitext(inputpath)[0]
	video_ext = os.path.splitext(inputpath)[1]
	if video_ext != '.mp4':
		os.system('ffmpeg -i "'+inputpath+'" "'+video_path_filename+'.mp4"')
	frames_dir = video_dir+'frames_waifu2x\\'
	
	cap = cv2.VideoCapture(inputpath)
	frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	frame_figures = len(str(frame_counter))
	
	if os.path.exists(frames_dir) :
			os.system("rd /s/q \""+frames_dir+'"')
	os.mkdir(frames_dir)

	os.system('ffmpeg -i "'+video_path_filename+'.mp4'+'" "'+frames_dir+'%0'+str(frame_figures)+'d.png"')
	
	remove_safe(video_dir+'audio_waifu2x.wav')
	
	os.system('ffmpeg -i "'+video_path_filename+'.mp4'+'" "'+video_dir+'audio_waifu2x.wav"')

def images2video(inputpath):
	video_path_filename = os.path.splitext(inputpath)[0]
	video_ext = os.path.splitext(inputpath)[1]
	video_dir = os.path.dirname(inputpath)+'\\'.replace("\\\\", "\\")
	frames_scaled_dir = video_dir+'frames_waifu2x\\scaled\\'
	frames_scaled_dir = frames_scaled_dir.replace("\\\\", "\\")
	cap = cv2.VideoCapture(inputpath)
	fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
	frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	frame_figures = len(str(frame_counter))
	
	
	if os.path.exists(video_dir+'audio_waifu2x.wav'):
		os.system('ffmpeg -f image2 -framerate '+str(fps)+' -i "'+frames_scaled_dir+'%0'+str(frame_figures)+'d.png" -i "'+video_dir+'audio_waifu2x.wav" -r '+str(fps)+' -pix_fmt yuv420p "'+video_path_filename+'_waifu2x'+video_ext+'"')
		remove_safe(video_dir+'audio_waifu2x.wav')
	else:
		os.system('ffmpeg -f image2 -framerate '+str(fps)+' -i "'+frames_scaled_dir+'%0'+str(frame_figures)+'d.png" -r '+str(fps)+' -pix_fmt yuv420p "'+video_path_filename+'_waifu2x'+video_ext+'"')
	
	
	os.system('rd /s/q "'+video_dir+'frames_waifu2x'+'"')

class VideoDelFrameThread(threading.Thread):
	def __init__(self,inputpath):
		threading.Thread.__init__(self)
		self.inputpath = inputpath
        
	def run(self):
		inputpath = self.inputpath
		video_dir = os.path.dirname(inputpath)+'\\'.replace("\\\\", "\\")
		frames_dir = video_dir+'frames_waifu2x\\'
		frames_scaled_dir = video_dir+'frames_waifu2x\\scaled\\'
		frame_list = []
		for path,useless,fnames in os.walk(frames_dir):
			fnames = dict.fromkeys(fnames,'')
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
				fnames = dict.fromkeys(fnames,'')
				for f_name_ext_ext in fnames:
					f_name_ext = os.path.splitext(f_name_ext_ext)[0]
					f_name = os.path.splitext(f_name_ext)[0]
					if f_name not in frame_deled_list:
						if f_name in frame_list:
							remove_safe(frames_dir+f_name+'.png')
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
		video_dir = os.path.dirname(inputpath)+'\\'.replace("\\\\", "\\")
		frames_scaled_dir = video_dir+'frames_waifu2x\\scaled\\'
		old_filenum = len(frame_list)
		frame_deled_list = []
		while True:
			if len(frame_deled_list) == old_filenum:
				return 0
			for path,useless,fnames in os.walk(frames_scaled_dir):
				fnames = dict.fromkeys(fnames,'')
				for f_name_ext_ext in fnames:
					f_name_ext = os.path.splitext(f_name_ext_ext)[0]
					f_name = os.path.splitext(f_name_ext)[0]
					if f_name_ext != f_name:
						if f_name not in frame_deled_list:
							if f_name in frame_list:
								remove_safe(frames_scaled_dir+f_name+'.png')
								frame_deled_list.append(f_name)
				break
			time.sleep(0.5)
	
#===================================================== input ====================================================
def input_scale():
	settings_values = ReadSettings()
	default_value = settings_values['scale']

	while True:
		scale = input(' Scale ratio(1/2/4/8/help, default='+default_value+'): ').strip(' ').lower()
		if scale in ['1','2','4','8','','r']:
			break
		elif scale == 'help':
			print('------------------------------------------')
			print('Scale ratio : Magnification of the image')
			print('------------------------------------------')
			print('')
		else:
			print('Error : wrong input, pls input again')
	
	if scale == '':
		scale = default_value

	return scale

def input_scale_Anime4k_waifu2x_converter():
	settings_values = ReadSettings()
	default_value = settings_values['scale']

	while True:
		scale = input(' Scale ratio(2/3/4/.../help, default='+default_value+'): ').strip(' ').lower()
		if scale.isdigit():
			if int(scale) > 1:
				return str(int(scale))
		elif scale == 'r':
			break
		elif scale == '':
			scale = default_value
			break
		elif scale == 'help':
			print('------------------------------------------')
			print('Scale ratio : Magnification of the image')
			print('------------------------------------------')
			print('')
		else:
			print('Error : wrong input, pls input again')
	
	if scale == '':
		scale = default_value
	return scale
	
def input_tileSize():
	settings_values = ReadSettings()
	default_value = '200'
	print('You can run the benchmark to determine the best value of "tile size" for your computer.')
	print('--------------------------------------------------------------------------------------')
	while True:
		tileSize = input(' Tile size(for waifu2x-ncnn-vulkan)( >=32 / help, default='+default_value+'): ').strip(' ').lower()
		if tileSize.isdigit():
			if int(tileSize) > 0:
				break
			else:
				os.system('cls')
				print('wrong input, pls input again')
		elif tileSize == '':
			break
		elif tileSize == 'help':
			os.system('cls')
			print('-'*91)
			print(' Tile size : This value will affacts GPU memory usage.')
			print(' Larger tile size means waifu2x will use more GPU memory and run faster.')
			print(' Smaller tile size means waifu2x will use less GPU memory and run slower.')
			print(' The "Benchmark" in the main menu can help you to determine the best value of "tile size".')
			print('-'*91)
			print('')
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
		noiseLevel = input(' Denoise level(-1/0/1/2/3/help, default='+default_value+'): ').strip(' ').lower()
		if noiseLevel in ['-1','0','1','2','3','','r']:
			break
		elif noiseLevel == 'help':
			print('-'*72)
			print(' Denoise level: large value means strong denoise effect, -1 = no effect')
			print('-'*72)
			print('')
		else:
			print('wrong input, pls input again')
	
	if noiseLevel == '':
		noiseLevel = default_value
	return noiseLevel

def input_noiseLevel_waifu2x_converter():
	settings_values = ReadSettings()
	while True:
		noiseLevel = input(' Denoise level(1/2, default= 2): ').strip(' ').lower()
		if noiseLevel in ['1','2','','r']:
			break
		elif noiseLevel == 'help':
			print('-'*57)
			print(' Denoise level: large value means strong denoise effect')
			print('-'*57)
			print('')
		else:
			print('wrong input, pls input again')
	
	if noiseLevel == '':
		noiseLevel = '2'
	return noiseLevel
		
def input_delorginal():
	settings_values = ReadSettings()
	default_value = settings_values['delorginal']
	while True:
		delorginal = input(' Delete original files?(y/n, default='+default_value+'): ').strip(' ').lower()
		if delorginal in ['y','n','','r']:
			break
		else:
			print('wrong input, pls input again')
	
	if delorginal == '':
		delorginal = default_value
	return delorginal
	
def input_turnoff():
	while True:
		turnoff = input(' Turn off computer when finished?(y/n, default=n): ').strip(' ').lower()
		if turnoff in ['y','n','','r']:
			break
		else:
			print('wrong input, pls input again')
	
	if turnoff == '':
		turnoff = 'n'
	return turnoff

def input_saveAsJPG():
	settings_values = ReadSettings()
	while True:
		saveAsJPG = input(' Save as .jpg? (y/n, default=y): ').strip(' ').lower()
		if saveAsJPG in ['y','n','']:
			break
		else:
			print('wrong input, pls input again')
	
	if saveAsJPG == '':
		saveAsJPG = 'y'
		
	settings_values['saveAsJPG']=saveAsJPG
	
	if saveAsJPG == 'y':
		while True:
			Compress = input(' Compress the .jpg file?(Almost lossless) (y/n, default=y): ').strip(' ')
			if Compress in ['y','n','Y','N','',]:
				break
			else:
				print('wrong input, pls input again')
		if Compress == '':
			Compress = 'y'
		settings_values['Compress']=Compress
		
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)

def input_optimizeGif():
	settings_values = ReadSettings()
		
	if settings_values['optimizeGif'] == 'n':
		settings_values['optimizeGif'] = 'y'
	elif settings_values['optimizeGif'] == 'y':
		settings_values['optimizeGif'] = 'n'
	
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)
	
def input_gifCompresslevel():
	settings_values = ReadSettings()
	default_value = settings_values['gifCompresslevel']
	while True:
		gifCompresslevel = input(' GIF Compress level(1/2/3/4/help, default='+default_value+'): ').strip(' ').lower()
		if gifCompresslevel in ['1','2','3','4','','r']:
			break
		elif gifCompresslevel == 'help':
			print('-----------------------------------------------------------')
			print('GIF Compress level : higher level means strong compress effect.')
			print('-----------------------------------------------------------')
			print('')
		else:
			print('wrong input, pls input again')
	
	if gifCompresslevel == '':
		gifCompresslevel = default_value
		
	return gifCompresslevel
	
def input_multiThread():
	settings_values = ReadSettings()
	if settings_values['multiThread']=='n':
		settings_values['multiThread']='y'
	elif settings_values['multiThread']=='y':
		settings_values['multiThread']='n'
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)
	
def input_gpuId():
	settings_values = ReadSettings()
	default_value = 'auto'
	gpuId_list = View_GPU_ID()
	if gpuId_list == []:
		input(' Press Enter key to return')
		return 0
	gpuId_list_str = ''
	for id_ in gpuId_list:
		gpuId_list_str = gpuId_list_str+'/'+str(id_)
	while True:
		gpuId = input(' GPU ID (auto (Automatic)'+gpuId_list_str+', default='+default_value+'): ').strip(' ').lower()
		if gpuId.isdigit():
			if int(gpuId) in gpuId_list:
				break
			else:
				os.system('cls')
				print(' Wrong input, pls input again')
				print('-'*30)
		elif gpuId == '':
			break
		elif gpuId == 'auto':
			break
		else:
			os.system('cls')
			print(' Wrong input, pls input again')
			print('-'*30)
		
	if gpuId == '':
		gpuId = default_value
	settings_values['gpuId']=str(gpuId)
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)

def input_notificationSound():
	settings_values = ReadSettings()
	if settings_values['notificationSound']=='y':
		settings_values['notificationSound']='n'
	elif settings_values['notificationSound']=='n':
		settings_values['notificationSound']='y'
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)

def input_multiThread_Scale():
	settings_values = ReadSettings()
	
	if settings_values['multiThread_Scale']=='n':
		settings_values['multiThread_Scale']='y'
	
	elif settings_values['multiThread_Scale']=='y':
		settings_values['multiThread_Scale']='n'
	
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)

def input_image_quality():
	settings_values = ReadSettings()
	default_value = settings_values['image_quality']
	while True:
		image_quality = input(' Image quality ( 100 (Almost lossless) ~ 1 (Most lossy) , defalut = '+str(default_value)+' ):').strip(' ').lower()
		if image_quality.isdigit():
			if int(image_quality) >= 1 and int(image_quality) <= 100:
				return int(image_quality)
				break
			else:
				print(' Wrong input, pls input again')
		elif image_quality == 'r':
			return 'r'
		elif image_quality == '':
			return default_value
		else:
			print(' Wrong input, pls input again')
			
def input_scan_subfolders():
	while True:
		scan_subfolders = input(' Scan subfolders? ( y/n, default= n ): ').strip(' ').lower()
		if scan_subfolders in ['y','n','r','']:
			break
		else:
			print(' Wrong input, pls input again')
	
	if scan_subfolders == '':
		scan_subfolders = 'n'
		
	return scan_subfolders

def input_sleepMode():
	sleepMode = ''
	while True:
		sleepMode = input(' Enable sleep mode?( y / n / help , default = n ): ').strip(' ').lower()
		if sleepMode in ['y','n','','r','help']:
			if sleepMode == 'help':
				print('')
				print('-'*95)
				print(' When "sleep mode" is enabled, the software will attempts to reduce performance requirements,')
				print(' thereby reducing the computer\'s operating pressure and thus minimizing noise.')
				print(' Enabling this mode will lengthen the time it takes for the program to complete its task.')
				print('-'*95)
			else:
				break
		else:
			print(' Wrong input, pls input again')
	
	if sleepMode == '':
		sleepMode = 'n'
	return sleepMode
	

#======================================================= Seconds 2 h:m:s =======================================================
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
#=========================================================== Check Update ============================================================
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
			print(' No new update')
			input(' Press Enter key to return')
	except BaseException:
		os.system('cls')
		print(' Failed to establish connection, pls check your internet or try again, press Enter key to return....\n')
		input()
		os.system('cls')

class CheckUpdate_start_thread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
        
	def run(self):
		CheckUpdate_start()

		
def CheckUpdate_start():
	try:
		headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
		r1=requests.get('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest',headers=headers)
		
		soup = BeautifulSoup(r1.text,'lxml')
				
		title = soup.title.string
		p_split_name = re.compile(r' ')
		
		Version_latest = p_split_name.split(title)[1]
		
		if Version_current != Version_latest:
			
			settings_values = ReadSettings()
			
			update_bat_str=[
			'@echo off \n',
			'color '+settings_values['default_color']+' \n',
			'title = Waifu2x-Extension '+Version_current+' by Aaron Feng  [ New Update Available ] \n',
			'echo Current version : '+Version_current+'\n',
			'echo New update : '+Version_latest+'\n',
			'echo If you don\'t wanna check for updates at startup. You can change the settings. \n',
			'echo Do you wanna download the update?(y/n): \n',
			'set user_input=N\n',
			'set /p user_input= \n',
			'if %user_input%==Y goto update \n',
			'if %user_input%==N goto exit \n',
			'if %user_input%==y goto update \n',
			'if %user_input%==n goto exit \n',
			'EXIT \n'
			':update \n',
			'start https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest \n',
			'goto exit \n',
			':exit \n',
			'EXIT \n'
			]
			
			with open('update_bat.bat','w+',encoding='ANSI') as f:
				f.writelines(update_bat_str)
			os.system('start update_bat.bat')
			
			return 0
			
		else:
			return 0
	except BaseException:
		return 0
	

#=====================================================  Settings  =============================================================

def Settings():
	while True:
		Set_cols_lines(90,37)
		Set_cols_lines(92,41)
		
		settings_values = {}
		with open('waifu2x-extension-setting','r+') as f:
			settings_values = json.load(f)
		print('─'*90)
		print(' '*41+'Settings')
		print('─'*90)
		print(' 1: Check for updates at startup. Current value: [ '+settings_values['CheckUpdate']+' ]\n')
		print(' 2: Default value of "Scale ratio". Current value: [ '+settings_values['scale']+' ]\n')
		print(' 3: Default value of "Denoise Level". Current value: [ '+settings_values['noiseLevel']+' ]\n')
		print(' 4: Delete original files when finished? Current default value: [ '+settings_values['delorginal']+' ]\n')
		print(' 5: Rename result images. Current value: [ ',settings_values['Rename_result_images'],' ]')
		print('─'*90)
		print(' 6: Gif compress level. Current default value: [ '+settings_values['gifCompresslevel']+' ]\n')
		print(' 7: Image quality ( When compress images ). Current default value: [ ',settings_values['image_quality'],' ]')
		print('─'*90)
		print(' 8: Number of threads ( Scale & Denoise (Waifu2x-ncnn-vulkan) ). Current value: [ ',settings_values['Number_of_threads'],' ]\n')
		print(' 9: Number of threads ( Scale Video (Anime4k) ). Current value: [ ',settings_values['Number_of_threads_Anime4k'],' ]\n')
		print(' 10: Number of threads ( Scale & Denoise (Waifu2x-converter) ). Current value: [ ',settings_values['Number_of_threads_Waifu2x_converter'],' ]')
		print('─'*90)
		print(' 11: Video scale mode. Current value: [ ',settings_values['Video_scale_mode'],' ]\n')
		print(' 12: Image & GIF scale mode. Current value: [ ',settings_values['Image_GIF_scale_mode'],' ]')
		print('─'*90)
		print(' 13: Change interface color.\n')
		print(' 14: Reset error log.\n')
		print(' 15: Reset settings.\n')
		print(' 16: Reset language setting for launcher.\n')
		print(' 17: Show settings_values.\n')
		print(' R: Return to the main menu.')
		print('─'*90)
		
		mode = input('( 1 / 2 / 3 /.../ R ): ').strip(' ').lower()
		
		if mode == "1":
			os.system('cls')
			print('------------------------------------------------------------------------------------------')
			print(' The software\'s update strategy is to use multiple small updates')
			print(' to continuously improve all aspects of the software,')
			print(' rather than releasing a major update every once in a while.')
			print(' So we recommend that you turn on automatic check for updates to improve your experience.')
			print('------------------------------------------------------------------------------------------')
			while True:
				value_ = input(' Check for updates at startup? (y/n): ').strip(' ').lower()
				if value_ in ['y','n']:
					break
				elif value_ == '':
					value_ = settings_values['CheckUpdate']
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
				value_ = input('Default value of "Scale ratio" (1/2/4): ').strip(' ').lower()
				if value_ in ['1','2','4']:
					break
				elif value_ == '':
					value_ = settings_values['scale']
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
				value_ = input('Default value of "Denoise Level" (-1/0/1/2/3): ').strip(' ').lower()
				if value_ in ['-1','0','1','2','3']:
					break
				elif value_ == '':
					value_ = settings_values['noiseLevel']
					break
				else:
					print('invalid value, pls input again')
					
			settings_values['noiseLevel']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
			
		elif mode == "4":
			
			os.system('cls')
			
			print('Loading...')
			
			if settings_values['delorginal'] == 'y':
				settings_values['delorginal'] = 'n'
			elif settings_values['delorginal'] == 'n':
				settings_values['delorginal'] = 'y'
			
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode == '5':
			os.system('cls')
			print('------------------------------------------------------------------')
			print('If the value of "Rename result images" == "n":')
			print('The result images will stay in input-path\\scaled_waifu2x')
			print('and we won\'t rename them, no "_waifu2x" at the end of file name')
			print('')
			print('If the value of "Rename result images" == "y":')
			print('The result images will stay in input-path')
			print('and we will rename them, add "_waifu2x" at the end of file name')
			print('------------------------------------------------------------------')
			while True:
				Rename_result_images = input(' Rename result images?(y/n): ').lower().strip(' ')
				if Rename_result_images in ['y','n']:
					break
				elif Rename_result_images == '':
					Rename_result_images = settings_values['Rename_result_images']
					break
				else:
					print('--------------')
					print(' Wrong input.')
					print('--------------')
			settings_values['Rename_result_images']=Rename_result_images
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
			os.system('cls')
		
		elif mode== "6":
			os.system('cls')
			
			while True:
				value_ = input('Default value of gif compress level (1/2/3/4): ').strip(' ').lower()
				if value_ in ['1','2','3','4']:
					break
				elif value_ == '':
					value_ = settings_values['gifCompresslevel']
					break
				else:
					print('invalid value, pls input again')
					
			settings_values['gifCompresslevel']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode == "7":
			os.system('cls')
			while True:
				image_quality = input('Default value of image quality ( When compress images ) ( 100 ~ 1 ): ').strip(' ').lower()
				if image_quality.isdigit():
					if int(image_quality) >= 1 and int(image_quality) <= 100:
						break
					else:
						print('wrong input, pls input again')
				elif image_quality == '':
					image_quality = settings_values['image_quality']
					break
				else:
					print('wrong input, pls input again')
			settings_values['image_quality']=int(image_quality)
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode== "8":
			os.system('cls')
			Number_of_threads=''
			print('-----------------------------------------------------------------')
			print('Change this setting may cause performance issues.\n')
			print('We recommend you to use the default setting.\n')
			print('This setting option only takes effect in waifu2x-ncnn-vulkan mode')
			print('-----------------------------------------------------------------')
			while True:
				Number_of_threads = input('Number of threads(Scale&Denoise) ( 2 / 3 / 4 /.... ; default = 2 ): ').strip(' ').lower()
				if Number_of_threads.isdigit():
					if int(Number_of_threads) >= 2:
						break
					else:
						print('wrong input, pls input again')
				elif Number_of_threads == '':
					Number_of_threads = '2'
					break
				else:
					print('invalid value, pls input again')
			settings_values['Number_of_threads']=Number_of_threads
			load_proc_save_str = ' -j '+Number_of_threads+':'+Number_of_threads+':'+Number_of_threads+' '
			settings_values['load_proc_save_str']=load_proc_save_str	
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode == "9":
			os.system('cls')
			cpu_num = int(cpu_count() / 2)
			if cpu_num < 1 :
				cpu_num = 1
			print('------------------------------')
			print('Recommanded value:',cpu_num)
			print('------------------------------')
			while True:
				Number_of_threads_Anime4k = input('Number of threads ( Scale Video (Anime4k) ) (1/2/3/4...):').lower().strip(' ')
				if Number_of_threads_Anime4k.isdigit():
					if int(Number_of_threads_Anime4k) > 0:
						Number_of_threads_Anime4k = int(Number_of_threads_Anime4k)
						break
					else:
						print('Wrong input.')
				elif Number_of_threads_Anime4k == '':
					Number_of_threads_Anime4k = settings_values['Number_of_threads_Anime4k']
					break
				else:
					print('Wrong input.')
			settings_values['Number_of_threads_Anime4k']=Number_of_threads_Anime4k
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
			os.system('cls')
		
		elif mode == "10":
			os.system('cls')
			print('-----------')
			print('Default: 1')
			print('-----------')
			while True:
				Number_of_threads_Waifu2x_converter = input('Number of threads ( Scale & Denoise (Waifu2x-converter) ) (1/2/3/4...):').lower().strip(' ')
				if Number_of_threads_Waifu2x_converter.isdigit():
					if int(Number_of_threads_Waifu2x_converter) > 0:
						Number_of_threads_Waifu2x_converter = int(Number_of_threads_Waifu2x_converter)
						break
					else:
						print('Wrong input.')
				elif Number_of_threads_Waifu2x_converter == '':
					Number_of_threads_Waifu2x_converter = settings_values['Number_of_threads_Waifu2x_converter']
					break
				else:
					print('Wrong input.')
			settings_values['Number_of_threads_Waifu2x_converter']=Number_of_threads_Waifu2x_converter
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
			os.system('cls')
		
		elif mode == "11":
			
			vulkan_compat = '[Incompatible] '
			converter_compat = '[Incompatible] '
			Anime4k_compat = '[Incompatible] '
			
			if settings_values['Compatibility_waifu2x_ncnn_vulkan']:
				vulkan_compat = ''
			if settings_values['Compatibility_waifu2x_converter']:
				converter_compat = ''
			if settings_values['Compatibility_Anime4k']:
				Anime4k_compat = ''
			
			os.system('cls')
				
			print('------------------------------------------------------------------')
			print('We recommand you to use "waifu2x-ncnn-vulkan".')
			print('')
			print('If "waifu2x-ncnn-vulkan" does not work properly on your computer,')
			print('you should try "waifu2x-converter"')
			print('')
			print('If "waifu2x-converter" also does not work properly on your computer,')
			print('or you think waifu2x is too slow, you should try "Anime4k"')
			print('------------------------------------------------------------------')
			print(vulkan_compat+'1. waifu2x-ncnn-vulkan  [ Speed:★★  Image Quality:★★★ ]\n')
			print(converter_compat+'2. waifu2x-converter  [ Speed:★  Image Quality:★★ ]\n')
			print(Anime4k_compat+'3. Anime4k  [ Speed:★★★  Image Quality:★ ]')
			print('------------------------------------------------------------------')
			while True:
				value_ = input('Video scale mode (1/2/3): ').lower().strip(' ')
				if value_ in ['1','2','3']:
					if value_ == '1':
						value_ = 'waifu2x-ncnn-vulkan'
					elif value_ == '2':
						value_ = 'waifu2x-converter'
					elif value_ == '3':
						value_ = 'anime4k'
					break
				elif value_ == '':
					value_ = settings_values['Video_scale_mode']
					break
				else:
					print('invalid value, pls input again')
			if value_ == 'anime4k':
				os.system('cls')
				ChangeColor_warning()
				print('                               !! ATTENTION !!\n')
				print('=========================================================================================\n')
				print('Anime4k dosen\'t support denoise and won\'t improve image quilty as much as Waifu2x.\n')
				print('Therefore, even this program support Anime4k, we don\'t recommand you to use it.\n')
				print('But Anime4k is faster than Waifu2x, so if you think speed is more important then quality,\n')
				print('then feel free to use it.\n')
				print('=========================================================================================\n')
				input('Press Enter to continue')
				
				os.system('cls')
				print('                               !! ATTENTION !!\n')
				print('=========================================================================================\n')
				print('This program uses the Java version of Anime4k.\n')
				print('So there may be compatibility issues.\n')
				print('To solve these issues, we recommend that you follow these steps:\n')
				print('(if compatibility issues occured)\n')
				print('1. Install the latest version of JDK and JRE\n')
				print('2. Try to enlarge the video using Anime4k mode\n')
				print('3. If Anime4k still doesn\'t work, re-compile Anime4k yourself and try again\n')
				print('Installation of the JDK and the JRE on Microsoft Windows Platforms:')
				print('https://docs.oracle.com/javase/10/install/installation-jdk-and-jre-microsoft-windows-platforms.htm \n')
				print('Anime4K :')
				print('https://github.com/bloc97/Anime4K \n')
				print('=========================================================================================\n')
				input('Press Enter to continue')
				ChangeColor_default()
			settings_values['Video_scale_mode']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode == '12':
			
			vulkan_compat = '[Incompatible] '
			converter_compat = '[Incompatible] '
			
			if settings_values['Compatibility_waifu2x_ncnn_vulkan']:
				vulkan_compat = ''
			if settings_values['Compatibility_waifu2x_converter']:
				converter_compat = ''
			
			os.system('cls')
			print('------------------------------------------------------------------')
			print('We recommand you to use "waifu2x-ncnn-vulkan".')
			print('')
			print('If "waifu2x-ncnn-vulkan" does not work properly on your computer,')
			print('you should try "waifu2x-converter"')
			print('------------------------------------------------------------------')
			print(vulkan_compat+'1. waifu2x-ncnn-vulkan  [ Speed:★★★★  Image Quality:★★★★ ]\n')
			print(converter_compat+'2. waifu2x-converter  [ Speed:★  Image Quality:★★★ ]')
			print('------------------------------------------------------------------')
			while True:
				Image_GIF_scale_mode = input('Image & GIF scale mode (1 / 2): ').lower().strip(' ')
				if Image_GIF_scale_mode in ['1','2']:
					if Image_GIF_scale_mode == '1':
						Image_GIF_scale_mode = 'waifu2x-ncnn-vulkan'
					elif Image_GIF_scale_mode == '2':
						Image_GIF_scale_mode = 'waifu2x-converter'
					break
				elif Image_GIF_scale_mode=='':
					Image_GIF_scale_mode = settings_values['Image_GIF_scale_mode']
					break
				else:
					print('Wrong input.')
			settings_values['Image_GIF_scale_mode']=Image_GIF_scale_mode
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
			os.system('cls')
		
		
		elif mode == "13":
			os.system('cls')
			Set_default_color()
			os.system('cls')
			

		elif mode == "14":
			os.system('cls')
			
			with open('Error_Log_Waifu2x-Extension.log','w+') as f:
				f.write('')
				
			with open('Error_Log_Waifu2x-Extension.log','a+') as f:
				timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
				f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Error log reseted by user.\n')
			
			input('Error log reseted, press Enter key to return.')
			
			os.system('cls')
		
		elif mode == "15":
			os.system('cls')
			
			remove_safe('config_waifu2xEX_start')
			
			remove_safe('waifu2x-extension-setting')
			ReadSettings()
			
			input('Setting reseted, press Enter key to return.')
			
			os.system('cls')
		
		elif mode == "16":
			os.system('cls')
			
			print('loading....')
			remove_safe('config_waifu2xEX_start')
			os.system('cls')
			input(' Language setting reseted, press Enter key to return.')
			
			os.system('cls')
		
		elif mode == "17":
			os.system('cls')
			
			for key,val in settings_values.items():
				print(str(key)+' : '+str(val))
			print('')
			print('--------------------------------------')
			input('press Enter key to return.')
			
			os.system('cls')

		elif mode == "r":
			break
		else:
			os.system('cls')
			ChangeColor_warning()
			print(' -------------------------------------------------')
			print(' Error : wrong input,pls press Enter key to return')
			print(' -------------------------------------------------')
			input()
			ChangeColor_default()
			os.system('cls')

def ReadSettings():
	cpu_num = int(cpu_count() / 2)
	if cpu_num < 1 :
		cpu_num = 1
	default_values = {'SettingVersion':'10','CheckUpdate':'y','scale':'2','First_Time_Boot_Up':'y',
						'noiseLevel':'2','saveAsJPG':'y','tileSize':'200','default_color':'0b',
						'Compress':'y','delorginal':'n','optimizeGif':'y','gifCompresslevel':'1',
						'multiThread':'y','gpuId':'auto','notificationSound':'y','multiThread_Scale':'y',
						'image_quality':95,'load_proc_save_str':' -j 2:2:2 ','Number_of_threads':'2',
						'Video_scale_mode':'waifu2x-ncnn-vulkan','Number_of_threads_Anime4k':cpu_num,
						'Rename_result_images':'y','Image_GIF_scale_mode':'waifu2x-ncnn-vulkan','Number_of_threads_Waifu2x_converter':1,
						'Compatibility_waifu2x_ncnn_vulkan':True,'Compatibility_waifu2x_converter':True,'Compatibility_Anime4k':True}
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
		if len(settings_values) != len(default_values) or settings_values['SettingVersion'] != default_values['SettingVersion']:
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(default_values,f)
			return default_values
		else:
			return settings_values


		
#==================================================== Logger =====================================================

class Logger(object):
	def __init__(self, filename='default.log', stream=sys.stdout):
		self.terminal = stream
		self.log = open(filename, 'a')

	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def flush(self):
		pass

#=================================================== Admin ===================================================
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
#==================================================== Error_Log ==================================================

def Error_Log():	#读取错误日志
	if os.path.exists('Error_Log_Waifu2x-Extension.log') :	#判断错误日志文件是否存在
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

def Error_log_clean():
	if os.path.exists('Error_Log_Waifu2x-Extension.log') :	#判断错误日志文件是否存在
		log_size = round(os.path.getsize('Error_Log_Waifu2x-Extension.log')/1024)
		if log_size > 500:
			os.system('cls')
			del_log = input('错误日志文件过大 (>500KB). 你想要重置错误日志吗?(Y/N): ')
			if del_log.lower() == 'y':
				with open('Error_Log_Waifu2x-Extension.log','w+') as f:
					f.write('')
				with open('Error_Log_Waifu2x-Extension.log','a+') as f:
					timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
					f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Error log reseted by user.\n')
				
	else:
		os.system('cls')
	os.system('cls')

#============================================= Multi-thread Gif Compress =================================================
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
			remove_safe(scaledFilePath+"_compressed.gif")
			print('\n'+'Failed to compress '+inputPath+'\n')
		else:
			saved_size_str = str(saved_size)+'KB'
			print('\n'+'Finished to compress '+inputPath+'\n')
			if delorginal == 'y':
				os.system('del /q "'+inputPath+'"')

def Multi_thread_Gif_Compress(inputPathList_files,gifCompresslevel,delorginal):
	
	max_threads = cpu_count()
	file_ext = ''
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
		
#=============================================== Multi-thread Image Compress ======================================
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
			remove_safe(scaledFilePath+"_compressed.jpg")
			print('\n'+'Failed to compress ['+inputPath+'] This image may be already being compressed.\nYou can try to reduce "image quality".'+'\n')
		else:
			print('\n'+'Finished to compress '+inputPath+'\n')
			if delorginal == 'y':
				os.system('del /q "'+inputPath+'"')

def Multi_thread_Image_Compress(inputPathList_files,delorginal,JpgQuality):
	
	max_threads = cpu_count()
	thread_files = []
	file_ext = ''
	
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

#=============================================== Play Notification Sound======================================

class Play_Notification_Sound_Thread (threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
        
	def run(self):
		playsound('NotificationSound_waifu2xExtension.mp3')

def Play_Notification_Sound():
	
	settings_values = ReadSettings()
	
	if settings_values['notificationSound'] == 'y':
		
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	

#=================================================== Resize Window ===============================================

class ResizeWindow_Thread(threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
        
	def run(self):
		ResizeWindow()

def ResizeWindow():
	while True:
		cols = 120
		lines = 38
		
		try:
			settings_values = Read_ResizeFile()
			cols = settings_values['cols_resize']
			lines = settings_values['lines_resize']
		except BaseException:
			time.sleep(0.02)
			settings_values = Read_ResizeFile()
			cols = settings_values['cols_resize']
			lines = settings_values['lines_resize']

		h = ctypes.windll.kernel32.GetStdHandle(-12)
		csbi = ctypes.create_string_buffer(22)
		res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
		
		if res:
			(bufx, bufy, curx, cury, wattr,
			 left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
			sizex = right - left + 1
			sizey = bottom - top + 1
			if sizex != cols or sizey != lines:
				os.system('Resize-window.exe '+str(cols)+' '+str(lines))
		else:
			os.system('Resize-window.exe '+str(cols)+' '+str(lines))
		time.sleep(0.05)

def Set_cols_lines(cols,lines):
	settings_values = Read_ResizeFile()
	settings_values['cols_resize'] = cols
	settings_values['lines_resize'] = lines
	with open('ResizeFile-waifu2xEX','w+') as f:
		json.dump(settings_values,f)
	while Complete_ResizeWindow(cols,lines):
		time.sleep(0.01)
	return 0

def Get_cols_lines():
	settings_values = Read_ResizeFile()
	cols = settings_values['cols_resize']
	lines = settings_values['lines_resize']
	return [cols,lines]

def Complete_ResizeWindow(cols,lines):
	h = ctypes.windll.kernel32.GetStdHandle(-12)
	csbi = ctypes.create_string_buffer(22)
	res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(h, csbi)
	
	if res:
		(bufx, bufy, curx, cury, wattr,
		 left, top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh", csbi.raw)
		sizex = right - left + 1
		sizey = bottom - top + 1
		if sizex == cols and sizey == lines:
			return False
		else:
			return True
	else:
		return True

def Read_ResizeFile():
	
	default_values = {"cols_resize": 20, "lines_resize": 20}
	current_dir = os.path.dirname(os.path.abspath(__file__))
	settingPath = current_dir+'\\'+'ResizeFile-waifu2xEX'
	if os.path.exists(settingPath) == False:
		with open(settingPath,'w+') as f:
			json.dump(default_values,f)
		return default_values
	else:
		settings_values = {}
		with open(settingPath,'r+') as f:
			settings_values = json.load(f)
		if len(settings_values) != len(default_values):
			with open(settingPath,'w+') as f:
				json.dump(default_values,f)
			return default_values
		else:
			return settings_values

	
#=============================== Benchmark =============================
def Benchmark():
	print('================ Benchmark ==========================')
	print(' 1.Tile size(for waifu2x-ncnn-vulkan)')
	print('')
	print(' 2.Number of threads(for waifu2x-converter) ( Beta )')
	print('')
	print(' 3.Number of threads(for Anime4K) ( Beta )')
	print('=====================================================')
	print('( 1 / 2 / 3 )')
	choice_ = input().strip(' ')
	if choice_ == '1':
		os.system('cls')
		Benchmark_vulkan()
		os.system('cls')
	elif choice_ == '2':
		os.system('cls')
		Benchmark_converter()
		os.system('cls')
	elif choice_ == '3':
		os.system('cls')
		Benchmark_Anime4K()
		os.system('cls')
	else:
		os.system('cls')

def Benchmark_Anime4K():
	print('This benchmark will help you to determine the right number of threads for Anime4K.')
	print('In order to get the accurate result, pls do not use your computer during the benchmark.')
	print('---------------------------------------------------------------------------------------')
	if input('Do you wanna start the benchmark now? (y/n): ').lower().strip(' ') != 'y':
		return 0
	wait_to_cool_time=int(input('How many seconds do you wanna wait to cool your computer during the test: '))
	
	Window_Title('[Running benchmark]')
	print('-------------------------------------------------------')
	print('This benchmark is gonna take a while, pls wait.....')
	print('-------------------------------------------------------')
	print('Wait '+str(wait_to_cool_time)+' seconds to cool the computer.')
	
	time.sleep(wait_to_cool_time)
	settings_values = ReadSettings()
	
	current_dir = os.path.dirname(os.path.abspath(__file__))
	input_folder = current_dir+'\\'+'benchmark-files-anime4k-waifu2x-extension'
	output_folder = input_folder+'\\'+'waifu2x_'
	
	scale = '2'
	noiseLevel = '2'
	Number_of_threads = 1
	
	old_time_cost = 1999999
	old_Number_of_threads = 0
	
	if os.path.exists(output_folder):
		os.system("rd /s/q \""+output_folder+"\"")
	
	for x in range(1,129):
		
		os.mkdir(output_folder)
		
		Number_of_threads = x
		
		settings_values['Number_of_threads_Anime4k'] = Number_of_threads
		with open('waifu2x-extension-setting','w+') as f:
			json.dump(settings_values,f)
		
		
		time_start=time.time()
		
		Video_scale_Anime4K(input_folder,output_folder,scale)
		
		time_end=time.time()
		os.system("rd /s/q \""+output_folder+"\"")
		new_time_cost = time_end - time_start
		print('---------------------------------')
		print('Number of threads: ',Number_of_threads)
		print('Time cost: ',new_time_cost)
		print('---------------------------------')
		if new_time_cost <= old_time_cost:
			old_time_cost = new_time_cost
			old_Number_of_threads = Number_of_threads
		else:
			break
		print('Wait '+str(wait_to_cool_time)+' seconds to cool the computer.')
		time.sleep(wait_to_cool_time)
		
	Play_Notification_Sound()
	Window_Title('')
	os.system('cls')
	print('=======================================================================')
	print('The right number of threads for your computer is:',old_Number_of_threads)
	if input('Do you wanna use the result value? (y/n): ').lower().strip(' ') != 'y':
		settings_values['Number_of_threads_Anime4k']=Original_Number_of_threads
	else:
		settings_values['Number_of_threads_Anime4k']=old_Number_of_threads
		
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)



def Benchmark_converter():
	print('This benchmark will help you to determine the right number of threads for waifu2x-converter.')
	print('In order to get the accurate result, pls do not use your computer during the benchmark.')
	print('---------------------------------------------------------------------------------------')
	if input('Do you wanna start the benchmark now? (y/n): ').lower().strip(' ') != 'y':
		return 0
	wait_to_cool_time=int(input('How many seconds do you wanna wait to cool your computer during the test: '))
	
	Window_Title('[Running benchmark]')
	print('-------------------------------------------------------')
	print('This benchmark is gonna take a while, pls wait.....')
	print('-------------------------------------------------------')
	print('Wait '+str(wait_to_cool_time)+' seconds to cool the computer.')
	
	time.sleep(wait_to_cool_time)
	settings_values = ReadSettings()
	
	current_dir = os.path.dirname(os.path.abspath(__file__))
	input_folder = current_dir+'\\'+'benchmark-files-converter-waifu2x-extension'
	output_folder = input_folder+'\\'+'waifu2x_'
	
	scale = '2'
	noiseLevel = '2'
	Number_of_threads = 1
	
	old_time_cost = 1999999
	old_Number_of_threads = 0
	
	if os.path.exists(output_folder):
		os.system("rd /s/q \""+output_folder+"\"")
	
	for x in range(1,129):
		
		os.mkdir(output_folder)
		
		Number_of_threads = x
		
		time_start=time.time()
		
		for path,useless,fnames in os.walk(input_folder):
			total_frame = len(fnames)
			
			max_threads = Number_of_threads
			thread_files = []
			fnames = dict.fromkeys(fnames,'')
			
			for fname in fnames:
				thread_files.append(fname)
				if len(thread_files) == max_threads:
					for fname_ in thread_files:
						thread1=waifu2x_converter_Thread(path+'\\'+fname_,output_folder+'\\'+fname_,scale,noiseLevel)
						thread1.start()
					while True:
						if thread1.isAlive()== False:
							break
	
					thread_files = []
	
			if thread_files != []:
				for fname_ in thread_files:
					thread1=waifu2x_converter_Thread(path+'\\'+fname_,output_folder+'\\'+fname_,scale,noiseLevel)
					thread1.start()
				while True:
					if thread1.isAlive()== False:
						break
				thread_files = []
				while True:
					if Process_exist('waifu2x-converter_x64.exe')== False:
						break
					else:
						time.sleep(0.02)
			break
		
		time_end=time.time()
		os.system("rd /s/q \""+output_folder+"\"")
		new_time_cost = time_end - time_start
		print('---------------------------------')
		print('Number of threads: ',Number_of_threads)
		print('Time cost: ',new_time_cost)
		print('---------------------------------')
		if new_time_cost <= old_time_cost:
			old_time_cost = new_time_cost
			old_Number_of_threads = Number_of_threads
		else:
			break
		print('Wait '+str(wait_to_cool_time)+' seconds to cool the computer.')
		time.sleep(wait_to_cool_time)
		
	Play_Notification_Sound()
	Window_Title('')
	os.system('cls')
	print('=======================================================================')
	print('The right number of threads for your computer is:',old_Number_of_threads)
	if input('Do you wanna use the result value? (y/n): ').lower().strip(' ') != 'y':
		return 0
	settings_values['Number_of_threads_Waifu2x_converter']=old_Number_of_threads
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)



def Benchmark_vulkan():
	print('This benchmark will help you to determine the best value of "tile size".')
	print('In order to get the accurate result, pls do not use your computer during the benchmark.')
	print('---------------------------------------------------------------------------------------')
	if input('Do you wanna start the benchmark now? (y/n): ').lower().strip(' ') != 'y':
		return 0
	wait_to_cool_time=int(input('How many seconds do you wanna wait to cool your computer during the test: '))
	
	Window_Title('[Running benchmark]')
	print('-------------------------------------------------------')
	print('This benchmark is gonna take a while, pls wait.....')
	print('-------------------------------------------------------')
	print('Wait '+str(wait_to_cool_time)+' seconds to cool the computer.')
	time.sleep(wait_to_cool_time)
	settings_values = ReadSettings()
	models = 'models-upconv_7_anime_style_art_rgb'
	scale = '2'
	noiseLevel = '3'
	gpuId = settings_values['gpuId']
	gpuId_str=''
	if gpuId != 'auto':
		gpuId_str = ' -g '+gpuId
	current_dir = os.path.dirname(os.path.abspath(__file__))
	inputPath = current_dir+'\\'+'benchmark-files-vulkan-waifu2x-extension'
	scaledFilePath = inputPath+'\\scaled'
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = settings_values['load_proc_save_str']
	if multiThread_Scale == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	tileSize = 50
	old_time_cost = 100000
	old_tileSize = 0
	
	if os.path.exists(scaledFilePath) :
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
		print('Wait '+str(wait_to_cool_time)+' seconds to cool the computer.')
		time.sleep(wait_to_cool_time)
	Play_Notification_Sound()
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
	print('Icons made by : Freepik (https://www.flaticon.com/authors/freepik)')
	print('From Flaticon : https://www.flaticon.com/')
	print('------------------------------------------')
	input('Press Enter key to return to the main menu.')

#================= Protect files ================
def FindGifFiles(inputPathList):
	inputPathList=dict.fromkeys(inputPathList,'')
	Gif_exist = False
	for inputPath in inputPathList:
		for path,useless,fnames in os.walk(inputPath):
			fnames = dict.fromkeys(fnames,'')
			for fname in fnames:
				if os.path.splitext(fname)[1] == ".gif":
					return True
			break
	return False

def MoveGifFiles(inputPathList):
	
	inputPathList=dict.fromkeys(inputPathList,'')
	inputPathList_gif = []
	path_gif_exist = False
	old_path=''
	new_path=''
	
	for inputPath in inputPathList:
		for path,useless,fnames in os.walk(inputPath):
			fnames = dict.fromkeys(fnames,'')
			for fname in fnames:
				if os.path.splitext(fname)[1] == ".gif":
					path_gif_exist = True
					old_path = path+'\\'+fname
					if os.path.exists(inputPath+'\\protectfiles_waifu2x_extension') == False:
						os.mkdir(inputPath+'\\protectfiles_waifu2x_extension')
					new_path = path+'\\protectfiles_waifu2x_extension\\'+fname
					os.system('copy /y "'+old_path+'" "'+new_path+'"')
					remove_safe(old_path)
			if path_gif_exist:
				inputPathList_gif.append(inputPath)
				path_gif_exist = False
			break
			
	return inputPathList_gif

def RecoverGifFiles(inputPathList):
	inputPathList=dict.fromkeys(inputPathList,'')
	
	old_path =''
	new_path =''
	
	for inputPath in inputPathList:
		for path,useless,fnames in os.walk(inputPath+'\\protectfiles_waifu2x_extension'):
			for fname in fnames:
				if os.path.splitext(fname)[1] == ".gif":
					old_path = path+'\\'+fname
					new_path = inputPath+'\\'+fname
					os.system('copy /y "'+old_path+'" "'+new_path+'"')
					os.system('del /q "'+old_path+'"')
			if os.path.exists(inputPath+'\\protectfiles_waifu2x_extension') :
				os.system('rd /s/q "'+inputPath+'\\protectfiles_waifu2x_extension'+'"')
			break
			
def FindImageFiles(inputPathList):
	Exts=[".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]
	
	Exts=dict.fromkeys(Exts,'')
	inputPathList=dict.fromkeys(inputPathList,'')
	
	Image_exist = False
	for inputPath in inputPathList:
		for path,useless,fnames in os.walk(inputPath):
			for fname in fnames:
				if os.path.splitext(fname)[1] in Exts:
					return True
			break
	return False

#======================================= View_GPU_ID() ==================================
def View_GPU_ID():
	print('----------------------------')
	print('        Loading....')
	print('----------------------------')
	gpuId = 0
	gpuId_list = []
	
	current_dir = os.path.dirname(os.path.abspath(__file__))
	models = 'models-upconv_7_anime_style_art_rgb'
	scale = '2'
	noiseLevel = '0'
	tileSize = '50'
	load_proc_save_str = ' -j 1:1:1 '
	inputPath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension.jpg'
	scaledFilePath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension_waifu2x.png'
	
	gpuId_str = ''
	
	for x in range(0,10):
		gpuId_str = ' -g '+str(gpuId)
		
		if os.path.exists(scaledFilePath) :
			os.system("del /q \""+scaledFilePath+"\"")
		os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+str(tileSize)+" -m "+models+gpuId_str+load_proc_save_str)
		if os.path.exists(scaledFilePath):
			gpuId_list.append(gpuId)
			os.system("del /q \""+scaledFilePath+"\"")
		else:
			break
		gpuId = gpuId+1
	os.system('cls')
	if len(gpuId_list) > 0:
		print('---------------------------------------------------------')
		print(' Available GPU ID for waifu2x-ncnn-vulkan: ',gpuId_list)
		print('---------------------------------------------------------')
	else:
		print('------------------------------------------')
		print(' No GPU availabel for waifu2x-ncnn-vulkan.')
		print(' Pls upgrade or reinstall your GPU driver.')
		print('------------------------------------------')
	return gpuId_list

#======================================================  Compatibility_Test =============================================================

def Compatibility_Test(Init):
	
	waifu2x_ncnn_vulkan_avaliable = False
	waifu2x_converter_avaliable = False
	Anime4k_avaliable = False
	
	os.system('cls')
	print('----------------------------------------------')
	print('  Running compatibility test, please wait...')
	print('----------------------------------------------')
	
	waifu2x_ncnn_vulkan_avaliable = Compatibility_Test_waifu2x_ncnn_vulkan()
	waifu2x_converter_avaliable = Compatibility_Test_waifu2x_converter()
	Anime4k_avaliable = Compatibility_Test_Anime4k()
	
	settings_values = ReadSettings()
	
	settings_values['Compatibility_waifu2x_ncnn_vulkan'] = waifu2x_ncnn_vulkan_avaliable
	settings_values['Compatibility_waifu2x_converter'] = waifu2x_converter_avaliable
	settings_values['Compatibility_Anime4k'] = Anime4k_avaliable
	
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)
	
	#====================== 输出测试结果 =======================
	os.system('cls')
	if waifu2x_ncnn_vulkan_avaliable:
		str_waifu2x_ncnn_vulkan_avaliable = 'YES'
	else:
		str_waifu2x_ncnn_vulkan_avaliable = 'NO'
		
	if waifu2x_converter_avaliable:
		str_waifu2x_converter_avaliable = 'YES'
	else:
		str_waifu2x_converter_avaliable = 'NO'
	
	if Anime4k_avaliable:
		str_Anime4k_avaliable = 'YES'
	else:
		str_Anime4k_avaliable = 'NO'
		
		
	print('------------------------------------------------')
	print('Compatible with waifu2x-ncnn-vulkan : ',str_waifu2x_ncnn_vulkan_avaliable)
	print('')
	print('Compatible with waifu2x-converter : ',str_waifu2x_converter_avaliable)
	print('')
	print('Compatible with Anime4k : ',str_Anime4k_avaliable)
	print('------------------------------------------------')
	print('')
	if waifu2x_ncnn_vulkan_avaliable and waifu2x_converter_avaliable and Anime4k_avaliable:
		if Init:
			time.sleep(3)
		else:
			input('Press Enter key to continue.')
	else:
		ChangeColor_warning()
		print('When waifu2x-ncnn-vulkan or waifu2x-converter is avaliable,')
		print('You can use all the features in the software without fixing compatibility issues.')
		print('---------------------------------------------------------------------------------')
		print('Warning, there is a compatibility issue on the current computer.') 
		print('Please follow the suggestions below to fix compatibility issues:')
		print('----------------------------------------------------------------')
		print('First of all, check update, make sure you are using the latest Waifu2x-Extension.')
		if waifu2x_ncnn_vulkan_avaliable == False:
			print('')
			print('-------------------------------------------------')
			print('Waifu2x-ncnn-vulkan:')
			print('Re-install gpu driver or update it to the latest.')
			print('And make sure your GPU support Vulkan.')
			print('-------------------------------------------------')
			print('')
			
		if waifu2x_converter_avaliable == False:
			print('')
			print('-------------------------------------------------------------------')
			print('Waifu2x-converter:')
			print('Check update, make sure you are using the latest Waifu2x-Extension.')
			print('If this won\'t fix the problem, then buy a new computer.')
			print('-------------------------------------------------------------------')
			print('')
			
		if Anime4k_avaliable == False:
			print('')
			print('------------------------------')
			print('Anime4k:')
			print('Install the latest JDK and JRE')
			print('------------------------------')
			print('')
		
		
		print('If the compatibility issue is still not resolved, enable the compatible components in the settings.')
		print('')
		print('----------------------------')
		print('Press Enter key to continue.')
		print('----------------------------')
		input()
		os.system('cls')
		ChangeColor_default()
		
		if waifu2x_ncnn_vulkan_avaliable == False and waifu2x_converter_avaliable == True:
			print('We have detected that waifu2x-converter is available on your computer, do you wanna enable it now??\n')
			print('Waifu2x-converter can enlarge image,video,GIF')
			print('')
			print('(Y/N): ')
			enable_waifu2x_converter = input().strip(' ').lower()
			if enable_waifu2x_converter == 'y':
				settings_values = ReadSettings()
				settings_values['Video_scale_mode'] = 'waifu2x-converter'
				settings_values['Image_GIF_scale_mode'] = 'waifu2x-converter'
				with open('waifu2x-extension-setting','w+') as f:
					json.dump(settings_values,f)
			os.system('cls')

def Compatibility_Test_waifu2x_ncnn_vulkan():
	
	current_dir = os.path.dirname(os.path.abspath(__file__))
	inputPath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension.jpg'
	scaledFilePath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension_waifu2x.jpg'
	
	gpuId = 0
	gpuId_list = []
	models = 'models-upconv_7_anime_style_art_rgb'
	scale = '2'
	noiseLevel = '0'
	tileSize = '50'
	load_proc_save_str = ' -j 1:1:1 '
	gpuId_str = ''
	
	if os.path.exists(scaledFilePath):
		os.system("del /q \""+scaledFilePath+"\"")
	
	for x in range(0,10):
		gpuId_str = ' -g '+str(gpuId)
		
		os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+str(tileSize)+" -m "+models+gpuId_str+load_proc_save_str)
		if os.path.exists(scaledFilePath):
			remove_safe(scaledFilePath)
			return True
		else:
			break
		gpuId = gpuId+1
		
	return False

def Compatibility_Test_waifu2x_converter():
	
	current_dir = os.path.dirname(os.path.abspath(__file__))
	inputPath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension.jpg'
	scaledFilePath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension_waifu2x.jpg'
	
	
	if os.path.exists(scaledFilePath):
		os.system("del /q \""+scaledFilePath+"\"")
		
	os.system('waifu2x-converter\\waifu2x-converter_x64.exe -i "'+inputPath+'" -o "'+scaledFilePath+'" --scale_ratio '+'2'+' --noise_level '+'2'+' --model_dir waifu2x-converter\\models_rgb')
	
	if os.path.exists(scaledFilePath):
		return True
		os.system("del /q \""+scaledFilePath+"\"")
	else:
		return False

def Compatibility_Test_Anime4k():
	
	current_dir = os.path.dirname(os.path.abspath(__file__))
	inputPath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension.jpg'
	scaledFilePath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension_waifu2x.jpg'
	
	
	if os.path.exists(scaledFilePath):
		os.system("del /q \""+scaledFilePath+"\"")
	
	os.system('java -jar Anime4K\\Anime4K.jar "'+inputPath+'" "'+scaledFilePath+'" '+'2')
	
	if os.path.exists(scaledFilePath):
		return True
		os.system("del /q \""+scaledFilePath+"\"")
	else:
		return False
		
	
#=============================== Default Window Title =================
def Window_Title(Add_str = ''):
	os.system('title = Waifu2x-Extension '+Version_current+' by Aaron Feng '+Add_str)

#============================================  Deduplicate_list  ===================================

def Deduplicate_list(The_List):
	New_List = sorted(list(set(The_List)))
	return New_List
	
#=========================================================  Separate_files_folder  ======================================================
def Separate_files_folder(paths_list):
	list_folders = []
	list_files = []
	paths_list = dict.fromkeys(paths_list,'')
	for path in paths_list:
		if os.path.isdir(path):
		    list_folders.append(path)
		elif os.path.isfile(path):
		    list_files.append(path)
	return [list_files,list_folders]
#============================================================= Change Color =============================================================
def ChangeColor_default():
	settings_values = ReadSettings()
	os.system('color '+settings_values['default_color'])

def ChangeColor_warning():
	os.system('color 0c')

def ChangeColor_cmd_original():
	os.system('color 07')

def Set_default_color():
	settings_values = ReadSettings()
	Color_dict = {'0':'0b','1':'09','2':'0a','3':'0c','4':'0d','5':'0e','6':'0f'}
	while True:
		print('''Set default color
----------------------
 0.Aqua (Default)
 1.Blue
 2.Green
 3.Red
 4.Purple
 5.Yellow
 6.White
----------------------
(0/1/2...../6)''')
		color = input().strip(' ')
		if color.isdigit():
			if color in ['0','1','2','3','4','5','6']:
				settings_values['default_color'] = Color_dict[color]
				with open('waifu2x-extension-setting','w+') as f:
					json.dump(settings_values,f)
				ChangeColor_default()
				return 0
			else:
				os.system('cls')
				input('Wrong input,press Enter to continue.')
				os.system('cls')
		elif color == '':
			return 0
		else:
			os.system('cls')
			input('Wrong input,press Enter to continue.')
			os.system('cls')

#===================================================== MOVE FILE =========================================================
def Move_file_org_new(org_path,new_path):
	if os.path.exists(os.path.dirname(new_path)) == False:
		os.mkdir(os.path.dirname(new_path))
	remove_safe(new_path)
	os.system('copy /y "'+org_path+'" "'+new_path+'"')
	if os.path.exists(new_path):
		remove_safe(org_path)
	else:
		print('Error: Move_file_org_new() -  new_path doesn\'t exists')

#=================================================== Image_File_2_Folder ==========================================================
def Image_File_2_Folder(FileList):
	File_folder_full_dict = {}
	File_folder_final_dict = {}
	
	for file_ in FileList:
		if os.path.splitext(file_)[1] in [".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]:
			File_folder_full_dict[os.path.dirname(file_)] = []
			
	for file_ in FileList:
		if os.path.splitext(file_)[1] in [".png",".jpg",".jpeg",".tif",".tiff",".bmp",".tga"]:
			File_folder_full_dict[os.path.dirname(file_)].append(file_)
			
	for key in File_folder_full_dict:
		if len(File_folder_full_dict[key]) > 1:
			File_folder_final_dict[key] = File_folder_full_dict[key]
	
	
	RemoveList = []
	for vals in File_folder_final_dict.values():
		for val in vals:
			RemoveList.append(val)
	
	Dict_New_folder_Old_folder={}
	New_folder = ''
	Old_folder = ''
	New_file = ''
	for key in File_folder_final_dict:
		New_folder = key+'\\waifu2x_image_folder'
		Old_folder = key
		Dict_New_folder_Old_folder[New_folder] = Old_folder
		for Org_file in File_folder_final_dict[key]:
			New_file = New_folder+'\\'+Org_file.split('\\')[-1]
			Move_file_org_new(Org_file,New_file)
			
	return [Dict_New_folder_Old_folder,RemoveList]


def Remove_File_2_Folder(Dict_New_folder_Old_folder):
	for key,val in Dict_New_folder_Old_folder.items():
		os.system('copy /y "'+key+"\\*.*\" \""+val+'"')
		os.system("rd /s/q \""+key+'"')


#================================================ Pop-up window ===============================================
def Pop_up_window(str_FileName,str_Title,list_Content,str_wait_time):
	settings_values = ReadSettings()
	str_FileName = str_FileName.strip(' ')
	start_bat_str=[
		'@echo off \n',
		'color '+settings_values['default_color']+' \n',
		'title = Waifu2x扩展 '+Version_current+' 作者: Aaron Feng  [ '+str_Title+' ] \n',
		]
	
	end_bat_str=[
		'\necho. \n'
		'pause \n'
		'EXIT \n',
		]
	
	wait_time_str = [
	'\necho. \n'
	'TIMEOUT /T '+str(str_wait_time)+' /NOBREAK \n',
	'EXIT \n'
	]
	
	if str_wait_time == '':
		Full_bat_str= start_bat_str+list_Content+end_bat_str
	else:
		Full_bat_str= start_bat_str+list_Content+wait_time_str
	
	with open(str_FileName+'.bat','w+',encoding='ANSI') as f:
		f.writelines(Full_bat_str)
	
	os.system('start '+str_FileName+'.bat')
	
	return 0 

#================================= 判断进程是否存在 ================================
def Process_exist(str_processname):
	pl = psutil.pids()
	for pid in pl:
		try:
			if psutil.Process(pid).name() == str_processname:
				return True
		except BaseException:
			pass

	else:
		return False

#==================================== 安全删除 ====================================
def remove_safe(path_):
	if os.path.exists(path_):
		os.remove(path_)

#============================================== Shut Down ==============================
def ShutDown():
	shutdown_time_str = time.strftime('%H:%M:%S', time.localtime(time.time()+30))
	print('-'*52)
	print(' The computer will be turned off at '+shutdown_time_str+' ! !')
	print('-'*52)
	time.sleep(30)
	os.system('shutdown -s')

#==========================================  Init  ==================================================================

def init():		#初始化函数
	Window_Title('')	#更改控制台标题
	ChangeColor_default()	#更改文字颜色
	
	sys.stderr = Logger('Error_Log_Waifu2x-Extension.log', sys.stderr)
	with open('Error_Log_Waifu2x-Extension.log','a+') as f:
		timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Start running\n')
		
	settings_values = ReadSettings()
		
	if settings_values['First_Time_Boot_Up'] == 'y':
		settings_values['First_Time_Boot_Up'] = 'n'
		with open('waifu2x-extension-setting','w+') as f:
			json.dump(settings_values,f)
		Compatibility_Test(True)
					
	os.system('cls')
	
	thread_resizeWindow=ResizeWindow_Thread()
	thread_resizeWindow.start()
	
	MainMenu()
	
	if thread_resizeWindow.isAlive():
		stop_thread(thread_resizeWindow)
		

#======================== Start ========================
        
if __name__ == '__main__':
	#检查所处文件夹是否需要管理员权限
	if AdminTest():
		try:
			init()
		except BaseException as e:
			os.system('cls')
			ChangeColor_warning()
			print('---------------------------------------------------')
			print('                   !!! Error !!!')
			print('---------------------------------------------------')
			ErrorStr = traceback.format_exc()
			print(ErrorStr)
			
			with open('Error_Log_Waifu2x-Extension.log','a+') as f:
				f.write(ErrorStr)
			
			print('---------------------------------------------------')
			print('An error occurred, pls report this to the developer.')
			print('')
			print('Report link:')
			print('https://github.com/AaronFeng753/Waifu2x-Extension/issues')
			print('')
			print('You can download the Latest release here, maybe the bug is already fixed:')
			print('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest')
			print('----------------------------------------')
			print('Press Enter key to restart the software.')
			input()
			os.system('cls')
			ChangeColor_default()
			python = sys.executable
			os.execl(python, python, * sys.argv)
	else:
		os.system('cls')
		print('--------------------------------------------------------------------------------------------------------------')
		print('We have detected that the current directory of the software is causing the software to apply for administrator\n privileges to continue normal operation.')
		print('We recommend that you move the software to another directory or give software administrator privileges.')
		print('--------------------------------------------------------------------------------------------------------------')
		print('Press Enter key to Re-run the program with admin rights. ')
		input()
		# Re-run the program with admin rights
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

#!/usr/bin/python  
# -*- coding: utf-8 -*- 

'''

什么是"Waifu2x扩展" ?

借助深度卷积神经网络进行超分辨率放大动漫风格的艺术作品, 包括图片,gif动态图片以及视频.

基于waifu2x-ncnn-vulkan (version 20190712) 和 Waifu2x-converter.

借助于waifu2x-ncnn-vulkan, Waifu2x-Extension可以借助任何支持Vulkan的显卡进行运算, 即便是Intel集成显卡.

如果你的GPU不支持vulkan, 你也可以使用集成在扩展中的Waifu2x-converter.

已经在 AMD RX 550, Intel UHD 620 和 NVIDIA GeForce GTX 1070 上通过测试.

-----------------------------------------------

waifu2x-ncnn-vulkan version 20190712

Anime4K Java v0.9 Beta

ffmpeg version 4.2

gifsicle version 1.92

-----------------------------------------------

更新日志
- converter 视频放大增加ETA
- converter GIF放大增加ETA
- converter 图片放大增加ETA
- 修复 converter代码内 无法正常检测线程的bug
- 更改设置逻辑, 单变量的直接切换(y/n那种)


------------------------------------------------

To do:
- 加入, anime4k线程数量测试, converter线程数量测试, 统一到benchmark里
- 完善汉化修复,错误翻译

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


                                           载入中.......
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

Version_current='v3.351'

#======================================================== MAIN MENU ==============================================================

def ChooseFormat():
	
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
		Compress = '   压缩: [ '+settings_values['Compress']+' ]' 
	
	optimizeGif = '[ '+settings_values['optimizeGif']+' ]' 
	
	Video_str = ''
	
	if settings_values['Video_scale_mode'] == 'anime4k':
		Video_str = '放大视频.(Anime4k) '
	else:
		Video_str = '放大与降噪视频.'
	
	while True:
		Set_cols_lines(65,37)
		Set_cols_lines(66,38)
		Window_Title('')
		print('-'*65)
		print(' Waifu2x扩展   '+Version_current+'   作者: Aaron Feng')
		print('-'*65)
		print(' Github主页: https://github.com/AaronFeng753/Waifu2x-Extension')
		print('-'*65)
		print(" 注意: 本软件的放大与降噪功能仅适用于处理动漫风格的艺术作品")
		print(" (包括图片,GIF动态图,视频)")
		print('-'*65)
		print(' 1 : 放大与降噪图片和GIF.  2 : '+Video_str)
		print('-'*65)
		print(' 3 : 压缩图片与GIF')
		print('-'*65)
		print(' 4 : Tile size(块大小): '+tileSize+'   '+'5 : GPU ID: '+gpuId)
		print('')
		print(' 6 : 提示音: '+notificationSound)
		print('')
		print(' 7 : 多线程(压缩): '+multiThread)
		print('')
		print(' 8 : 多线程(放大与降噪): '+multiThread_Scale)
		print('')
		print(' 9 : 目标另存为 .jpg?(放大与降噪): '+saveAsJPG+Compress)
		print('')
		print(' 10 : 优化 .gif?(放大与降噪): '+optimizeGif)
		print('-'*65)
		print(' 11 : 设置.              12 : 基准测试.')
		print('')
		print(' 13 : 阅读错误日志.      14 : 检查更新.')
		print('')
		print(' 15 : 说明文档.          16 : 用户协议.')
		print('')
		print(' 17 : 兼容性测试         E : 退出.')
		print('-'*65)
		print(' D : 捐赠. (支付宝)      R : 提交反馈')
		print('-'*65)
		print('( 1 / 2 / 3 / 4 /...../ E / D / R ): ')
		mode = input().strip(' ').lower()
			
		Set_cols_lines(120,40)
		
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
				Video_str = '放大视频(Anime4k)'
			else:
				Video_str = '放大与降噪视频'
				
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
			print('载入中.......')
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
			print('载入中.......')
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/blob/master/donate.jpg')
			os.system('cls')
			print(' 谢谢您 !!!  :)')
		elif mode == "r":
			os.system('cls')
			print('Loading.......')
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/issues/new')
			os.system('cls')
		else:
			os.system('cls')
			ChangeColor_warning()
			input('错误 : 输入无效, 请按 Enter 键返回')
			ChangeColor_default()
			os.system('cls')

#===================================================== Scale & Denoise Image & GIF ========================================
def Image_Gif_Scale_Denoise():
	print("================= 放大与降噪图片和GIF - Waifu2x-ncnn-vulkan ================")
	print("输入 'r' 返回上一级菜单")
	print("输入 'o' 来停止输入更多路径, 输入的路径必须是一个有效的文件或者文件夹")
	print("放大后的图片和GIF会保存在原输入路径中 \n")
	
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
			inputPath = input('输入路径: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			if inputPath.lower() == 'r':
				return 1
			elif inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('错误,输入路径无效!!')
				print('-----------------------------')
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
	notificationSound = settings_values['notificationSound']
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
		if Compress == 'y':
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
		notificationSound = 'n'
		
	print('--------------------------------------------')
	
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
	
	print('\n 总共用时: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff=='y':
		os.system('shutdown -s')
	if notificationSound == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	
	input('\n 按下 Enter 键返回上一级菜单')

#========================================= Process_ImageModeAB =============================================

def Process_ImageModeAB(inputPathList,orginalFileNameAndFullname,JpgQuality,models,noiseLevel,scale,load_proc_save_str,tileSize,gpuId_str,saveAsJPG,delorginal):
	Total_folder_num = len(inputPathList)
	Finished_folder_num = 1
	for inputPath in inputPathList:
		Window_Title('  [放大图片]  文件夹: ('+str(Finished_folder_num)+'/'+str(Total_folder_num)+')')
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
			print('\n 转换图片中..... \n')
			for path,useless,fnames in os.walk(inputPath+'\\scaled_waifu2x\\'):
				for fnameAndExt in fnames:
					pngFile = path+'\\'+fnameAndExt
					fname = os.path.splitext(fnameAndExt)[0]
					jpgFile = path+'\\'+fname+'.jpg'
					imageio.imwrite(jpgFile, imageio.imread(pngFile), 'JPG', quality = JpgQuality)
					os.remove(pngFile)
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
					'echo --------------------------------------------\n',
					'echo 发生错误, 为了保护您的文件, 该文件夹内的原文件:\n',
					'echo '+inputPath+'\n'
					'echo 不会被删除.\n'
					'echo --------------------------------------------\n'
				]
				
				Pop_up_window('Error_file_not_del','错误',list_Content,'')

		print('复制文件中...')
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
				os.remove(scaledFilePath+"_Waifu2x.png")
		
		
		if delorginal == 'y':
			if os.path.exists(scaledFilePath+"_Waifu2x.png") or os.path.exists(scaledFilePath+"_Waifu2x.jpg"):
				os.system('del /q "'+inputPath+'"')
			else:
				list_Content=[
					'echo -------------------------------------\n',
					'echo 发生错误, 为了保护您的文件, 该原文件 :\n',
					'echo '+inputPath+'\n'
					'echo 不会被删除.\n'
					'echo -------------------------------------\n',
				]
				
				Pop_up_window('Error_file_not_del','错误',list_Content,'')

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
		Window_Title('  [放大 GIF]  文件: '+'('+str(finished_num)+'/'+str(Total_num)+')')
		scaledFilePath = os.path.splitext(inputPath)[0]
			
		TIME_GAP=getDuration(inputPath)
		print('拆分GIF中.....')
		splitGif(inputPath,scaledFilePath)
		
		oldfilenumber=FileCount(scaledFilePath+'_split')
				
		scalepath = scaledFilePath+'_split\\scaled\\'
		
		if os.path.exists(scaledFilePath+'_split\\scaled') :
			os.system("rd /s/q \""+scaledFilePath+'_split\\scaled'+'"')
		os.mkdir(scaledFilePath+'_split\\scaled')
		
		print('放大图像中.....')
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
		
		print('组装GIF.....')
		assembleGif(scaledFilePath,TIME_GAP)
		print('GIF组装完成')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal == 'y':
			gif_name=scaledFilePath+'_waifu2x.gif'
			if os.path.exists(gif_name):
				if os.path.getsize(gif_name)>0:
					os.system('del /q "'+inputPath+'"')
			else:
				list_Content=[
					'echo -------------------------------------\n',
					'echo 发生错误, 为了保护您的文件, 该原文件 :\n',
					'echo '+inputPath+'\n'
					'echo 不会被删除.\n'
					'echo -------------------------------------\n',
				]
				
				Pop_up_window('Error_file_not_del','错误',list_Content,'')
			
		
		if optimizeGif == 'y':
			print('压缩 gif....')
			compress_gif(scaledFilePath+'_waifu2x.gif','1')
			os.remove(scaledFilePath+'_waifu2x.gif')
			print('Gif 压缩成功\n')
		else:
			print('')
		finished_num = finished_num+1
	Window_Title('')

#================================================= Image_Gif_Scale_Denoise_waifu2x_converter ===========================================
def Image_Gif_Scale_Denoise_waifu2x_converter():
	print("================= 降噪与放大图片和GIF - Waifu2x-converter  ================")
	print("输入 'r' 返回上一级菜单")
	print("输入 'o' 来停止输入更多路径, 注意:输入的路径必须是合法的文件或者文件夹")
	print("放大后的图片和GIF会保存在原路径中 \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []
	JpgQuality=100
	Image_GIF_scale_mode = settings_values['Image_GIF_scale_mode']
	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('输入路径: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			if inputPath.lower() == 'r':
				return 1
			elif inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('错误,输入路径无效 !!')
				print('-----------------------------')
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

	notificationSound = settings_values['notificationSound']
	
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
		if Compress == 'y':
			JpgQuality=90
	
	delorginal = input_delorginal()
	if delorginal == 'r':
		return 1
	
	turnoff = input_turnoff()
	if turnoff == 'r':
		return 1
		
	print('--------------------------------------------')
	
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
	print('')
	print(' 总消耗时间: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff=='y':
		os.system('shutdown -s')
	if notificationSound == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	
	input('\n 按下Enter键来以返回上一级菜单')

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
				print('\n 转换图片..... \n')
				imageio.imwrite(scaledFilePath+"_Waifu2x.jpg", imageio.imread(scaledFilePath+"_Waifu2x.png"), 'JPG', quality = JpgQuality)
				os.remove(scaledFilePath+"_Waifu2x.png")
		
		
		if delorginal == 'y':
			if os.path.exists(scaledFilePath+"_Waifu2x.png") or os.path.exists(scaledFilePath+"_Waifu2x.jpg"):
				os.system('del /q "'+inputPath+'"')
			else:
				list_Content=[
					'echo -------------------------------------\n',
					'echo 发生错误, 为了保护您的文件, 该原文件 :\n',
					'echo '+inputPath+'\n'
					'echo 不会被删除.\n'
					'echo -------------------------------------\n',
				]
				
				Pop_up_window('Error_file_not_del','错误',list_Content,'')

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
		Window_Title('  [放大图片]  文件: '+'('+str(FinishedFileNum)+'/'+str(TotalFileNum)+')  预计完成时间: '+ETA)
		
		thread_files.append(inputPath)
		if len(thread_files) == max_threads:
			for fname_ in thread_files:
				thread1=waifu2x_converter_Thread_ImageModeC(fname_,JpgQuality,noiseLevel,scale,saveAsJPG,delorginal)
				thread1.start()
			while True:
				if thread1.isAlive()== False:
					break
			FinishedFileNum = FinishedFileNum+len(thread_files)
			
			remain_frames = TotalFileNum - FinishedFileNum
			time_cost = time.time()-time_start_scale
			time_remain = (time_cost/FinishedFileNum)*remain_frames
			ETA = time.strftime('%H:%M:%S', time.localtime(time.time()+time_remain))
			
			thread_files = []
	if thread_files != []:
		#FinishedFileNum = TotalFileNum
		Window_Title('  [放大图片]  文件: '+'('+str(FinishedFileNum)+'/'+str(TotalFileNum)+')  预计完成时间: '+ETA)
		for fname_ in thread_files:
				thread1=waifu2x_converter_Thread_ImageModeC(fname_,JpgQuality,noiseLevel,scale,saveAsJPG,delorginal)
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
			
		TIME_GAP=getDuration(inputPath)
		print('拆分GIF.....')
		splitGif(inputPath,scaledFilePath)
		
		time_start_scale = time.time()
		
		oldfilenumber=FileCount(scaledFilePath+'_split')
				
		scalepath = scaledFilePath+'_split\\scaled\\'
		
		if os.path.exists(scaledFilePath+'_split\\scaled') :
			os.system("rd /s/q \""+scaledFilePath+'_split\\scaled'+'"')
		os.mkdir(scaledFilePath+'_split\\scaled')
		
		print('放大图像.....')
		
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
				Window_Title('  [放大 GIF]  文件: '+'('+str(finished_num)+'/'+str(Total_num)+')  视频帧: ('+str(finished_frame)+'/'+str(total_frame)+')  预计完成时间: '+ETA)
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
				Window_Title('  [放大 GIF]  文件: '+'('+str(finished_num)+'/'+str(Total_num)+')  视频帧: ('+str(finished_frame)+'/'+str(total_frame)+')  预计完成时间: '+ETA)
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
		print('组装 Gif.....')
		assembleGif(scaledFilePath,TIME_GAP)
		print('Gif 组装完毕')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal == 'y':
			gif_name=scaledFilePath+'_waifu2x.gif'
			if os.path.exists(gif_name):
				if os.path.getsize(gif_name)>0:
					os.system('del /q "'+inputPath+'"')
			else:
				list_Content=[
					'echo -------------------------------------\n',
					'echo 发生错误, 为了保护您的文件, 该原文件 :\n',
					'echo '+inputPath+'\n'
					'echo 不会被删除.\n'
					'echo -------------------------------------\n',
				]
				
				Pop_up_window('Error_file_not_del','错误',list_Content,'')
			
		
		if optimizeGif == 'y':
			print('压缩 gif....')
			compress_gif(scaledFilePath+'_waifu2x.gif','1')
			os.remove(scaledFilePath+'_waifu2x.gif')
			print('Gif 压缩完成\n')
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
								os.remove(inputpath+f_name+'.png')
								inputpath_deled_list.append(f_name)
				break
			time.sleep(0.5)

#=============================================  Scale & Denoise Video_waifu2x_converter  ====================================
def Scale_Denoise_Video_waifu2x_converter():
	print('注意 : 输入路径中不得包含中文字符或者其他特殊字符,会造成兼容性问题.')
	print('')
	print("================ 放大与降噪视频 - waifu2x-converter ===============")
	print("输入 'r' 返回上一级菜单")
	print("输入 'o' 以停止输入更多路径, 注意:输入路径必须是一个合法的视频文件或者文件夹")
	print("放大后的视频文件会保存在原路径中 \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('输入路径: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath.lower() == 'r':
				return 1
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('错误,输入路径无效!!')
				print('-----------------------------')
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
	
	notificationSound = settings_values['notificationSound']
		
	delorginal = input_delorginal()
	if delorginal == 'r':
		return 1
		
	turnoff = input_turnoff()
	if turnoff == 'r':
		return 1
	
		
	print('--------------------------------------------')
	
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
	
	print('\n 总共消耗时间: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff=='y':
		os.system('shutdown -s')
	if notificationSound == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	input('\n 按下 Enter 键以退出')

#======================================= process_video_modeABC_waifu2x_converter ============================
def process_video_modeABC_waifu2x_converter(inputPathList_files,scale,noiseLevel,delorginal):
	settings_values = ReadSettings()
	total_num = len(inputPathList_files)
	finished_num = 1
	for inputPath in inputPathList_files:
		
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
				Window_Title('  [放大视频]  视频: '+'('+str(finished_num)+'/'+str(total_num)+')  帧:('+str(finished_frames)+'/'+str(total_frames)+')  预计完成时间: '+ETA)
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
				Window_Title('  [放大视频]  视频: '+'('+str(finished_num)+'/'+str(total_num)+')  帧: ('+str(finished_frames)+'/'+str(total_frames)+')  预计完成时间: '+ETA)
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
		
		images2video(os.path.splitext(inputPath)[0]+'.mp4')#合成视频	
		
		if os.path.splitext(inputPath)[1] != '.mp4':
			os.remove(os.path.splitext(inputPath)[0]+'.mp4')
		
		res_video = os.path.splitext(inputPath)[0]+'_waifu2x.mp4'
	
		if delorginal == 'y':
			if os.path.exists(res_video):
				if os.path.getsize(res_video) > 0:
					os.system('del /q "'+inputPath+'"')	
				else:
					print('发生错误, 无法生成视频.')
			else:
				print('发生错误, 无法生成视频.')
		finished_num = finished_num+1
	Window_Title('')

#=============================================  Scale & Denoise Video  ====================================
def Scale_Denoise_Video():
	print('注意 : 输入路径中不得包含中文字符或者其他特殊字符,会造成兼容性问题.')
	print('')
	print("================ 放大与降噪视频 - Waifu2x-ncnn-vulkan ===============")
	print("输入 'r' 以返回上一级菜单")
	print("输入 'o' 以停止输入更多路径, 注意, 输入的路径必须是一个文件夹或者一个视频文件")
	print("处理后的文件会存放在原文件夹内 \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('输入路径: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath.lower() == 'r':
				return 1
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('错误,输入路径无效!!')
				print('-----------------------------')
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
	notificationSound = settings_values['notificationSound']
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
		notificationSound = 'n'
		
	print('--------------------------------------------')
	
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
	
	print('\n总共消耗时间: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff=='y':
		os.system('shutdown -s')
	if notificationSound == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	input('\n按下 Enter 键以退出')
	
#======================================= process_video_modeABC ============================
def process_video_modeABC(inputPathList_files,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,delorginal):
	total_num = len(inputPathList_files)
	finished_num = 1
	for inputPath in inputPathList_files:
		Window_Title('  [放大视频]  视频: '+'('+str(finished_num)+'/'+str(total_num)+')')
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
			os.remove(os.path.splitext(inputPath)[0]+'.mp4')
			
		res_video = os.path.splitext(inputPath)[0]+'_waifu2x.mp4'
	
		if os.path.splitext(inputPath)[1] != '.mp4':
			os.system('del /q "'+os.path.splitext(inputPath)[0]+'.mp4'+'"')
		if delorginal == 'y':
			if os.path.exists(res_video):
				if os.path.getsize(res_video) > 0:
					os.system('del /q "'+inputPath+'"')	
				else:
					print('发生错误, 无法生成视频.')
			else:
				print('发生错误, 无法生成视频.')
		finished_num = finished_num+1
	Window_Title('')

#=============================================  Scale & Denoise Video - Anime4K  ====================================
def Scale_Denoise_Video_Anime4K():
	print('注意 : 输入路径中不得包含中文字符或者其他特殊字符,会造成兼容性问题.')
	print('')
	print("======================== 放大视频 - Anime4K =======================")
	print("输入 'r' 以返回上一级菜单")
	print("输入 'o' 以停止输入更多路径, 注意, 输入的路径必须是一个文件夹或者一个视频文件")
	print("处理后的文件会存放在原文件夹内 \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('输入路径: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath.lower() == 'r':
				return 1
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('错误,输入路径无效!!')
				print('-----------------------------')
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

	notificationSound = settings_values['notificationSound']
		
	delorginal = input_delorginal()
	if delorginal == 'r':
		return 1
		
	turnoff = input_turnoff()
	if turnoff == 'r':
		return 1
		
	print('--------------------------------------------')
	
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
	
	print('\n总共消耗时间: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff=='y':
		os.system('shutdown -s')
	if notificationSound == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	input('\n按下 Enter 键以退出')

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
		Window_Title('  [放大视频]  视频: '+'('+str(finished_num)+'/'+str(total_num)+')')
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
			os.remove(os.path.splitext(inputPath)[0]+'.mp4')
		if delorginal == 'y':
			if os.path.exists(res_video):
				if os.path.getsize(res_video) > 0:
					os.system('del /q "'+inputPath+'"')	
				else:
					print('发生错误, 无法生成视频.')
			else:
				print('发生错误, 无法生成视频.')
		finished_num = finished_num+1
	Window_Title('')

#===================================================== Compress_image_gif ====================================================
def Compress_image_gif():
	print("================= 压缩图片与GIF ================")
	print("输入 'r' 以返回上一级菜单")
	print("输入 'o' 以停止输入更多路径, 注意, 输入的路径必须是一个文件夹或者一个文件")
	print("压缩后的图片和GIF会保存在原文件夹内 \n")
	settings_values = ReadSettings()
	inputPathOver = True
	inputPathList = []

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('输入路径: ')
			inputPath=inputPath.strip('"').strip('\\').strip(' ')
			
			if inputPath.lower() == 'r':
				return 1
			elif inputPath.lower() == 'o':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('-----------------------------')
				print('错误,输入路径无效!!')
				print('-----------------------------')
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
	if FindImageFiles(inputPathList):
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
	if FindGifFiles(inputPathList):
		gif_exist = True
	if gif_exist:
		gifCompresslevel=input_gifCompresslevel()
		if gifCompresslevel == 'r':
				return 1
	
	delorginal = input_delorginal()
	if delorginal == 'r':
		return 1
	multiThread = settings_values['multiThread']
	notificationSound = settings_values['notificationSound']
	
	
	
	print('--------------------------------------------')
	
	
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
		
	print('\n总共消耗时间: ',total_time_end-total_time_start,'s\n')
	if notificationSound == 'y':
		thread_notification=Play_Notification_Sound_Thread()
		thread_notification.start()
	input('\n按下 Enter 键来返回主菜单')
	
#========================================================== Process_compress_image ======================================================

def Process_compress_image(inputPathList_files,delorginal,multiThread,JpgQuality):
	if multiThread == 'y':
		print('开始压缩图片, 请稍等....')
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
			print('原文件大小:'+original_size)
			print('压缩中.....')
			
			imageio.imwrite(scaledFilePath+"_compressed.jpg", imageio.imread(inputPath), 'JPG', quality = JpgQuality)
			
			compressed_size = str(round(os.path.getsize(scaledFilePath+"_compressed.jpg")/1024))+'KB'
			
			saved_size = round(os.path.getsize(inputPath)/1024) - round(os.path.getsize(scaledFilePath+"_compressed.jpg")/1024)
			if saved_size <= 0:
				os.remove(scaledFilePath+"_compressed.jpg")
				print('无法压缩 ['+inputPath+'] 这个图片可能已经被压缩过了. 你可以尝试减小 "image quality" 的值.')
			else:
				saved_size_str = str(saved_size)+'KB'
				print('压缩后大小:'+compressed_size)
				print('节省了 '+saved_size_str+' !')
				print('')	
				if delorginal == 'y':
					os.system('del /q "'+inputPath+'"')
				
			print('--------------------------------------------')

#============================================================= process_gif_compress_modeABC ===================================================

def process_gif_compress_modeABC(inputPathList_files,gifCompresslevel,delorginal,multiThread):
	if multiThread == 'y':
		print('开始压缩 .gif, 请稍等....')
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
			print('原文件大小:'+original_size)
			print('压缩中.....')
			
			compress_gif(inputPath,gifCompresslevel)
			
			compressed_size = str(round(os.path.getsize(scaledFilePath+"_compressed.gif")/1024))+'KB'
			saved_size = round(os.path.getsize(inputPath)/1024) - round(os.path.getsize(scaledFilePath+"_compressed.gif")/1024)
			if saved_size <= 0:
				os.remove(scaledFilePath+"_compressed.gif")
				print('无法压缩 '+inputPath)
			else:
				saved_size_str = str(saved_size)+'KB'
				print('压缩后大小:'+compressed_size)
				print('节省了 '+saved_size_str+' !')
				print('')	
				if delorginal == 'y':
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
      raise ValueError("无效的线程ID")
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
				os.remove(path+'\\'+fname)
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
			return (duration / 1000)/frames
	return None

def splitGif(gifFileName,scaledFilePath):
	im = Image.open(gifFileName)
	pngDir = scaledFilePath+'_split'
	if os.path.exists(scaledFilePath+'_split') :
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

	for path,useless,fnames in os.walk(scaledFilePath+'_split\\scaled'):
		fnames = dict.fromkeys(fnames,'')
		for fname in fnames:
			filelist_name.append(int(os.path.splitext(fname)[0]))
		break
		
	filelist_name.sort()
	filelist_name = dict.fromkeys(filelist_name,'')
	for file_name in filelist_name:
		image_list.append(scaledFilePath+'_split\\scaled'+'\\'+str(file_name)+'.png')
	frames = []  
	image_list = dict.fromkeys(image_list,'')
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
	
	if os.path.exists(video_dir+'audio_waifu2x.wav'):
		os.remove(video_dir+'audio_waifu2x.wav')
	
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
	os.system('ffmpeg -f image2 -framerate '+str(fps)+' -i "'+frames_scaled_dir+'%0'+str(frame_figures)+'d.png" -i "'+video_dir+'audio_waifu2x.wav" -r '+str(fps)+' -pix_fmt yuv420p "'+video_path_filename+'_waifu2x'+video_ext+'"')
	os.remove(video_dir+'audio_waifu2x.wav')
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
								os.remove(frames_scaled_dir+f_name+'.png')
								frame_deled_list.append(f_name)
				break
			time.sleep(0.5)
	
#===================================================== 输 入 ====================================================
def input_scale():
	settings_values = ReadSettings()
	default_value = settings_values['scale']

	while True:
		scale = input('放大比例(1/2/4/8/help, 默认值='+default_value+'): ').strip(' ').lower()
		if scale in ['1','2','4','8','','r']:
			break
		elif scale == 'help':
			print('------------------------------------------')
			print('放大比例 : 该值决定了要将图片放大几倍')
			print('------------------------------------------')
			print('')
		else:
			print('错误 : 错误的输入,请在此输入')
	
	if scale == '':
		scale = default_value

	return scale

def input_scale_Anime4k_waifu2x_converter():
	settings_values = ReadSettings()
	default_value = settings_values['scale']

	while True:
		scale = input('放大比例(2/3/4/.../help, 默认值='+default_value+'): ').strip(' ').lower()
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
			print('放大比例 : 该值决定了要将图片放大几倍')
			print('------------------------------------------')
			print('')
		else:
			print('错误 : 输入无效, 请再次输入')
	
	if scale == '':
		scale = default_value
	return scale
	
def input_tileSize():
	settings_values = ReadSettings()
	default_value = '200'
	print('你可以通过基准测试来确定 "tile size" 的最佳值.')
	print('--------------------------------------------------------------------------------------')
	while True:
		tileSize = input('Tile size(对于 waifu2x-ncnn-vulkan)( >=32 / help, 默认='+default_value+'): ').strip(' ').lower()
		if tileSize.isdigit():
			if int(tileSize) > 0:
				break
			else:
				os.system('cls')
				print('输入无效,请再次尝试')
		elif tileSize == '':
			break
		elif tileSize == 'help':
			os.system('cls')
			print('-----------------------------------------------------------------------------------------')
			print('Tile size : 这个值会影响本软件放大时使用多少显存.')
			print('更大的 tile size 表示 waifu2x 会使用更大显存并运行的更快.')
			print('更小的 tile size 表示 waifu2x 会使用更少的显存并运行的更慢.')
			print('主菜单内的基准测试可以帮助您确定Tile size的最佳值')
			print('-----------------------------------------------------------------------------------------')
			print('')
		else:
			os.system('cls')
			print('输入无效, 请再次尝试')
		
	if tileSize == '':
		tileSize = default_value
	
	settings_values['tileSize']=str(int(tileSize))
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)
	
def input_noiseLevel():
	settings_values = ReadSettings()
	default_value = settings_values['noiseLevel']
	while True:
		noiseLevel = input('降噪等级(-1/0/1/2/3/help, 默认值='+default_value+'): ').strip(' ').lower()
		if noiseLevel in ['-1','0','1','2','3','','r']:
			break
		elif noiseLevel == 'help':
			print('----------------------------------------------------------------------')
			print('降噪等级: 更大的值代表更强的降噪效果, -1 代表不降噪')
			print('----------------------------------------------------------------------')
			print('')
		else:
			print('输入无效, 请再次输入')
	
	if noiseLevel == '':
		noiseLevel = default_value
	return noiseLevel

def input_noiseLevel_waifu2x_converter():
	settings_values = ReadSettings()
	while True:
		noiseLevel = input('降噪等级(1/2, 默认= 2): ').strip(' ').lower()
		if noiseLevel in ['1','2','','r']:
			break
		elif noiseLevel == 'help':
			print('---------------------------------------------------------')
			print('降噪等级: 更大的值代表更强的降噪效果')
			print('---------------------------------------------------------')
			print('')
		else:
			print('输入无效, 请再次输入')
	
	if noiseLevel == '':
		noiseLevel = '2'
	return noiseLevel
		
def input_delorginal():
	settings_values = ReadSettings()
	default_value = settings_values['delorginal']
	while True:
		delorginal = input('删除原文件?(y/n, 默认='+default_value+'): ').strip(' ').lower()
		if delorginal in ['y','n','','r']:
			break
		else:
			print('输入无效, 请再次输入')
	
	if delorginal == '':
		delorginal = default_value
	return delorginal
	
def input_turnoff():
	while True:
		turnoff = input('完成任务后关闭电脑?(y/n, 默认=n): ').strip(' ').lower()
		if turnoff in ['y','n','','r']:
			break
		else:
			print('输入无效, 请再次输入')
	
	if turnoff == '':
		turnoff = 'n'
	return turnoff

def input_saveAsJPG():
	settings_values = ReadSettings()
	while True:
		saveAsJPG = input('目标另存为.jpg? (y/n, 默认=y): ').strip(' ').lower()
		if saveAsJPG in ['y','n','']:
			break
		else:
			print('输入无效, 请再次输入')
	
	if saveAsJPG == '':
		saveAsJPG = 'y'
		
	settings_values['saveAsJPG']=saveAsJPG
	
	if saveAsJPG == 'y':
		while True:
			Compress = input('压缩 .jpg 文件?(近乎无损) (y/n, 默认=y): ').strip(' ').lower()
			if Compress in ['y','n','Y','N','',]:
				break
			else:
				print('输入无效, 请再次输入')
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
		gifCompresslevel = input('GIF压缩等级(1/2/3/4/help, 默认='+default_value+'): ').strip(' ').lower()
		if gifCompresslevel in ['1','2','3','4','','r']:
			break
		elif gifCompresslevel == 'help':
			print('-----------------------------------------------------------')
			print('GIF压缩等级 : 更高的等级意味着更强力的压缩.')
			print('-----------------------------------------------------------')
			print('')
		else:
			print('输入无效, 请再次输入')
	
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
		input('按Enter返回')
		return 0
	gpuId_list_str = ''
	for id_ in gpuId_list:
		gpuId_list_str = gpuId_list_str+'/'+str(id_)
	while True:
		gpuId = input('GPU ID (auto (自动)'+gpuId_list_str+', 默认='+default_value+'): ').strip(' ').lower()
		if gpuId.isdigit():
			if int(gpuId) in gpuId_list:
				break
			else:
				os.system('cls')
				print('输入无效, 请再次输入')
				print('----------------------------')
		elif gpuId == '':
			break
		elif gpuId == 'auto':
			break
		else:
			os.system('cls')
			print('输入无效, 请再次输入')
		
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
		image_quality = input('图像质量 ( 100 (几乎无损) ~ 1 (损失最大) , 默认 = '+str(default_value)+' ):').strip(' ').lower()
		if image_quality.isdigit():
			if int(image_quality) >= 1 and int(image_quality) <= 100:
				return int(image_quality)
				break
			else:
				print('输入无效, 请再次输入')
		elif image_quality == 'r':
			return 'r'
		elif image_quality == '':
			return default_value
		else:
			print('输入无效, 请再次输入')
			
def input_scan_subfolders():
	while True:
		scan_subfolders = input('扫描子文件夹? ( y/n, 默认= n ): ').strip(' ').lower()
		if scan_subfolders in ['y','n','r','']:
			break
		else:
			print('输入无效, 请再次输入')
	
	if scan_subfolders == '':
		scan_subfolders = 'n'
		
	return scan_subfolders

def input_sleepMode():
	sleepMode = ''
	while True:
		sleepMode = input('启用睡眠模式?( y / n / help , 默认 = n ): ').strip(' ').lower()
		if sleepMode in ['y','n','','r','help']:
			if sleepMode == 'help':
				print('')
				print('------------------------------------------------')
				print('当睡眠模式启用时, 软件会尝试减少性能需求,')
				print('以此来减少电脑的运行压力并减少噪音.')
				print('同时还会关闭提示音.')
				print('启用该选项会延长程序完成放大与降噪任务的时间')
				print('-------------------------------------------------')
			else:
				break
		else:
			print('输入无效, 请再次输入')
	
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
	print('检查更新中....')
	try:
		headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}
		r1=requests.get('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest',headers=headers)
		
		soup = BeautifulSoup(r1.text,'lxml')
		
		title = soup.title.string
		p_split_name = re.compile(r' ')
		
		Version_latest = p_split_name.split(title)[1]
		
		if Version_current != Version_latest:
			os.system('cls')
			print(' 检测到新版本 : '+Version_latest)
			print(' 通过修改hosts加速github访问：https://share.weiyun.com/5u4OPP3 ')
			print(' -----------------------------------------------------------')
			while True:
				download_update = input(' 你想现在下载更新吗?(y/n): ')
				if download_update in ['y','n','Y','N']:
					break
				else:
					print('输入无效, 请再次输入')
			if download_update.lower() == 'y':
				webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest')
		else:
			os.system('cls')
			print('没有更新')
			input('按下Enter返回')
	except BaseException:
		os.system('cls')
		print('无法与github建立连接, 请检查你的网络或重试, 按 Enter 键返回....\n')
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
			'title = Waifu2x扩展 '+Version_current+' 作者: Aaron Feng  [ 检测到新版本 ] \n',
			'echo 当前版本 : '+Version_current+'\n',
			'echo 新版本 : '+Version_latest+'\n',
			'echo 如果你不想在启动时检查更新, 你可以在设置内手动关闭. \n',
			'echo 通过修改hosts加速github访问：https://share.weiyun.com/5u4OPP3 \n',
			'echo ------------------------------------------------------------ \n',
			'echo 你想现在下载更新吗?(y/n): \n',
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
		settings_values = {}
		with open('waifu2x-extension-setting','r+') as f:
			settings_values = json.load(f)
		print('                                   设置')
		print('-----------------------------------------------------------------------------')
		print(' 1: 启动时后台检查更新. 当前值: [ '+settings_values['CheckUpdate']+' ]\n')
		print(' 2: "放大倍数"的默认值. 当前默认值: [ '+settings_values['scale']+' ]\n')
		print(' 3: "降噪等级"的默认值. 当前默认值: [ '+settings_values['noiseLevel']+' ]\n')
		print(' 4: 完成后删除原文件? 当前默认值: [ '+settings_values['delorginal']+' ]\n')
		print(' 5: Gif 压缩等级. 当前默认值: [ '+settings_values['gifCompresslevel']+' ]\n')
		print(' 6: 图像质量 ( 当压缩图片时 ). 当前默认值: [ ',settings_values['image_quality'],' ]\n')
		print(' 7: 线程数 ( 放大与降噪 (Waifu2x-ncnn-vulkan) ). 当前值: [ ',settings_values['Number_of_threads'],' ]\n')
		print(' 8: 更改交互界面颜色.\n')
		print(' 9: 线程数 ( 放大视频 (Anime4k) ). 当前值: [ ',settings_values['Number_of_threads_Anime4k'],' ]\n')
		print(' 10: 重命名放大后的图片. 当前值: [ ',settings_values['Rename_result_images'],' ]\n')
		print(' 11: 视频放大模式. 当前值: [ ',settings_values['Video_scale_mode'],' ]\n')
		print(' 12: 图片与GIF放大模式. 当前值: [ ',settings_values['Image_GIF_scale_mode'],' ]\n')
		print(' 13: 线程数 ( 放大与降噪 (Waifu2x-converter) ). 当前值: [ ',settings_values['Number_of_threads_Waifu2x_converter'],' ]\n')
		print(' RE: 重置错误日志.\n')
		print(' RS: 重置设置.\n')
		print(' RL: 重置语言设置 (Waifu2x-Extension-Start.exe).\n')
		print(' S: 显示 settings_values.\n')
		print(' R: 返回主菜单.')
		print('-----------------------------------------------------------------------------')
		mode = input('(1/2/3/..../RE/RS/RL/S/R): ').strip(' ').lower()
		if mode == "1":
			os.system('cls')
			print('------------------------------------------------------------------')
			print('本软件的更新策略是通过频繁且多次的小更新, 来逐渐改善软件使用体验\n')
			print('而不是每隔一大段时间发布一次大更新.\n')
			print('所以我们强烈建议您打开自动更新检查来保证您的使用体验.')
			print('------------------------------------------------------------------')
			while True:
				value_ = input('启动时检查更新? (y/n): ').strip(' ').lower()
				if value_ in ['y','n']:
					break
				elif value_ == '':
					value_ = settings_values['CheckUpdate']
					break
				else:
					print('无效值, 请再次输入')
					
			settings_values['CheckUpdate']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode== "2":
			os.system('cls')
			
			while True:
				value_ = input('"放大比例"的默认值 (1/2/4): ').strip(' ').lower()
				if value_ in ['1','2','4']:
					break
				elif value_ == '':
					value_ = settings_values['scale']
					break
				else:
					print('无效值, 请再次输入')
					
			settings_values['scale']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
			
		elif mode == "3":
			os.system('cls')
			
			while True:
				value_ = input('"降噪等级"的默认值 (-1/0/1/2/3): ').strip(' ').lower()
				if value_ in ['-1','0','1','2','3']:
					break
				elif value_ == '':
					value_ = settings_values['noiseLevel']
					break
				else:
					print('无效值, 请再次输入')
					
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
		
		elif mode== "5":
			os.system('cls')
			
			while True:
				value_ = input('GIF压缩等级的默认值 (1/2/3/4): ').strip(' ').lower()
				if value_ in ['1','2','3','4']:
					break
				elif value_ == '':
					value_ = settings_values['gifCompresslevel']
					break
				else:
					print('无效值, 请再次输入')
					
			settings_values['gifCompresslevel']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode == "6":
			os.system('cls')
			while True:
				image_quality = input('图像质量的默认值 ( 压缩静态图像时 ) ( 100 ~ 1 ): ').strip(' ').lower()
				if image_quality.isdigit():
					if int(image_quality) >= 1 and int(image_quality) <= 100:
						break
					else:
						print('输入无效, 请再次输入')
				elif image_quality == '':
					image_quality = settings_values['image_quality']
					break
				else:
					print('输入无效, 请再次输入')
			settings_values['image_quality']=int(image_quality)
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode== "7":
			os.system('cls')
			Number_of_threads=''
			print('--------------------------------------------------')
			print('改变这项设置可能会导致性能问题.\n')
			print('我们建议您使用默认值.\n')
			print('这个设置选项只在 waifu2x-ncnn-vulkan 模式内生效')
			print('--------------------------------------------------')
			while True:
				Number_of_threads = input('线程数(放大与降噪) ( 2 / 3 / 4 /.... ; default = 2 ): ').strip(' ').lower()
				if Number_of_threads.isdigit():
					if int(Number_of_threads) >= 2:
						break
					else:
						print('输入无效, 请再次输入')
				elif Number_of_threads == '':
					Number_of_threads = '2'
					break
				else:
					print('无效值, 请再次输入')
			settings_values['Number_of_threads']=Number_of_threads
			load_proc_save_str = ' -j '+Number_of_threads+':'+Number_of_threads+':'+Number_of_threads+' '
			settings_values['load_proc_save_str']=load_proc_save_str	
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		
		elif mode == "8":
			os.system('cls')
			Set_default_color()
			os.system('cls')
			
		elif mode == "9":
			os.system('cls')
			cpu_num = int(cpu_count() / 2)
			if cpu_num < 1 :
				cpu_num = 1
			print('------------------------------')
			print('推荐值:',cpu_num)
			print('------------------------------')
			while True:
				Number_of_threads_Anime4k = input('线程数 ( 放大视频 (Anime4k) ) (1/2/3/4...):').lower().strip(' ')
				if Number_of_threads_Anime4k.isdigit():
					if int(Number_of_threads_Anime4k) > 0:
						Number_of_threads_Anime4k = int(Number_of_threads_Anime4k)
						break
					else:
						print('输入错误.')
				else:
					print('输入错误.')
			settings_values['Number_of_threads_Anime4k']=Number_of_threads_Anime4k
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
			os.system('cls')
		
		elif mode == '10':
			os.system('cls')
			print('----------------------------------------------------')
			print('如果 "Rename result images" 的值 == "n":')
			print('生成的图片会保存在 输入路径\\scaled_waifu2x')
			print('并且我们不会重命名这些图片, 不会在文件末尾添加 "_waifu2x"')
			print('')
			print('如果 "Rename result images" 的值 == "y":')
			print('生成的图片会保存在 输入路径')
			print('并且我们会重命名这些图片, 在图片末尾添加 "_waifu2x"')
			print('-----------------------------------------------------')
			while True:
				Rename_result_images = input('重命名生成的图片?(y/n): ').lower().strip(' ')
				if Rename_result_images in ['y','n']:
					break
				else:
					print('错误的输入.')
			settings_values['Rename_result_images']=Rename_result_images
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
			os.system('cls')
		
		elif mode == "11":
			os.system('cls')
			print('------------------------------------------------------------------')
			print('我们推荐你使用 "waifu2x-ncnn-vulkan".')
			print('')
			print('如果 "waifu2x-ncnn-vulkan" 无法兼容你的电脑,')
			print('你可以尝试启用 "waifu2x-converter"')
			print('')
			print('如果 "waifu2x-converter" 也无法兼容你的电脑,')
			print('或者你认为 waifu2x 过于缓慢, 你可以尝试启用 "Anime4k"')
			print('------------------------------------------------------------------')
			print('1. waifu2x-ncnn-vulkan  [ 速度:★★  图像质量:★★★ ]\n')
			print('2. waifu2x-converter  [ 速度:★  图像质量:★★ ]\n')
			print('3. Anime4k  [ 速度:★★★  图像质量:★ ]')
			print('------------------------------------------------------------------')
			while True:
				value_ = input('视频放大模式 (1/2/3): ').lower().strip(' ')
				if value_ in ['1','2','3']:
					if value_ == '1':
						value_ = 'waifu2x-ncnn-vulkan'
					elif value_ == '2':
						value_ = 'waifu2x-converter'
					elif value_ == '3':
						value_ = 'anime4k'
					break
				else:
					print('无效值, 请再次输入')
			if value_ == 'anime4k':
				os.system('cls')
				ChangeColor_warning()
				print('                                   !! 注意 !!\n')
				print('=========================================================================================\n')
				print('Anime4k 不支持降噪并且无法像waifu2x那样对图像质量有很大提升.\n')
				print('所以, 尽管本程序支持Anime4k, 我们依旧极为不推荐您使用它(恕我直言,真的垃圾).\n')
				print('但是 Anime4k 运行速度比 Waifu2x 更快, 所以如果你认为速度远比图像质量更重要,\n')
				print('那么请自便.\n')
				print('=========================================================================================\n')
				input('按下 Enter 以继续')
				
				os.system('cls')
				print('                                   !! 注意 !!\n')
				print('=========================================================================================\n')
				print('本软件集成的是java版本的 Anime4k.\n')
				print('所以可能会出现兼容性问题.\n')
				print('为了解决这些问题, 我们建议您遵循以下步骤:\n')
				print('(如果出现兼容性问题的话)\n')
				print('1. 安装最新版本的 JDK and JRE\n')
				print('2. 尝试使用Anime4k模式放大视频\n')
				print('3. 如果Anime4k依旧无法正常工作, 自己重新编译Anime4k然后替换软件内自带的\n')
				print('在微软Windows平台安装JAR和JDK的步骤(英文文档):')
				print('https://docs.oracle.com/javase/10/install/installation-jdk-and-jre-microsoft-windows-platforms.htm \n')
				print('Anime4K的GITHUB :')
				print('https://github.com/bloc97/Anime4K \n')
				print('=========================================================================================\n')
				input('按下 Enter 以继续')
				ChangeColor_default()
			settings_values['Video_scale_mode']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode == '12':
			os.system('cls')
			print('------------------------------------------------------------------')
			print('我们推荐您使用 "waifu2x-ncnn-vulkan".')
			print('')
			print('如果 "waifu2x-ncnn-vulkan" 无法在您的电脑上正常工作,')
			print('你可以尝试 "waifu2x-converter"')
			print('------------------------------------------------------------------')
			print('1. waifu2x-ncnn-vulkan  [ 速度:★★★★  图像质量:★★★★ ]\n')
			print('2. waifu2x-converter  [ 速度:★  图像质量:★★★ ]')
			print('------------------------------------------------------------------')
			while True:
				Image_GIF_scale_mode = input('图片和GIF的放大模式 (1 / 2): ').lower().strip(' ')
				if Image_GIF_scale_mode in ['1','2']:
					if Image_GIF_scale_mode == '1':
						Image_GIF_scale_mode = 'waifu2x-ncnn-vulkan'
					elif Image_GIF_scale_mode == '2':
						Image_GIF_scale_mode = 'waifu2x-converter'
					break
				else:
					print('输入错误.')
			settings_values['Image_GIF_scale_mode']=Image_GIF_scale_mode
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
			os.system('cls')
		
		elif mode == "13":
			os.system('cls')
			print('-----------')
			print('默认值: 1')
			print('-----------')
			while True:
				Number_of_threads_Waifu2x_converter = input('线程数量 ( 放大与降噪 (Waifu2x-converter) ) (1/2/3/4...):').lower().strip(' ')
				if Number_of_threads_Waifu2x_converter.isdigit():
					if int(Number_of_threads_Waifu2x_converter) > 0:
						Number_of_threads_Waifu2x_converter = int(Number_of_threads_Waifu2x_converter)
						break
					else:
						print('输入错误.')
				else:
					print('输入错误.')
			settings_values['Number_of_threads_Waifu2x_converter']=Number_of_threads_Waifu2x_converter
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
			os.system('cls')
		
		elif mode == "re":
			os.system('cls')
			
			with open('Error_Log_Waifu2x-Extension.log','w+') as f:
				f.write('')
				
			with open('Error_Log_Waifu2x-Extension.log','a+') as f:
				timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
				f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Error log reseted by user.\n')
			
			input('错误日志已经重置, 按下Enter返回.')
			
			os.system('cls')
		
		elif mode == "rs":
			os.system('cls')
			
			cpu_num = int(cpu_count() / 2)
			if cpu_num < 1 :
				cpu_num = 1
			default_values = {'SettingVersion':'8','CheckUpdate':'y','scale':'2','First_Time_Boot_Up':'y',
								'noiseLevel':'2','saveAsJPG':'y','tileSize':'200','default_color':'0b',
								'Compress':'y','delorginal':'n','optimizeGif':'y','gifCompresslevel':'1',
								'multiThread':'y','gpuId':'auto','notificationSound':'y','multiThread_Scale':'y',
								'image_quality':'95','load_proc_save_str':' -j 2:2:2 ','Number_of_threads':'2',
								'cols_resize':140,'lines_resize':38,'Video_scale_mode':'waifu2x-ncnn-vulkan','Number_of_threads_Anime4k':cpu_num,
								'Rename_result_images':'y','Image_GIF_scale_mode':'waifu2x-ncnn-vulkan','Number_of_threads_Waifu2x_converter':1}
			current_dir = os.path.dirname(os.path.abspath(__file__))
			settingPath = current_dir+'\\'+'waifu2x-extension-setting'
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(default_values,f)
			
				
			
			input('设置已重置, 按下Enter返回.')
			
			os.system('cls')
		
		elif mode == "rl":
			os.system('cls')
			
			print('请稍等....')
			if os.path.exists('config_waifu2xEX_start'):
				os.remove('config_waifu2xEX_start')
			os.system('cls')
			input('设置已重置, 按下Enter返回.')
			
			os.system('cls')
		
		elif mode == "s":
			os.system('cls')
			
			for key,val in settings_values.items():
				print(str(key)+' : '+str(val))
			print('')
			print('--------------------------------------')
			input('按下Enter返回.')
			
			os.system('cls')

		elif mode == "r":
			break
		else:
			os.system('cls')
			ChangeColor_warning()
			print(' -------------------------------------------------')
			print(' 错误 : 非法的输入,请按下 Enter 以返回')
			print(' -------------------------------------------------')
			input()
			ChangeColor_default()
			os.system('cls')

def ReadSettings():
	cpu_num = int(cpu_count() / 2)
	if cpu_num < 1 :
		cpu_num = 1
	default_values = {'SettingVersion':'8','CheckUpdate':'y','scale':'2','First_Time_Boot_Up':'y',
						'noiseLevel':'2','saveAsJPG':'y','tileSize':'200','default_color':'0b',
						'Compress':'y','delorginal':'n','optimizeGif':'y','gifCompresslevel':'1',
						'multiThread':'y','gpuId':'auto','notificationSound':'y','multiThread_Scale':'y',
						'image_quality':'95','load_proc_save_str':' -j 2:2:2 ','Number_of_threads':'2',
						'cols_resize':140,'lines_resize':38,'Video_scale_mode':'waifu2x-ncnn-vulkan','Number_of_threads_Anime4k':cpu_num,
						'Rename_result_images':'y','Image_GIF_scale_mode':'waifu2x-ncnn-vulkan','Number_of_threads_Waifu2x_converter':1}
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
			del_log = input('错误日志文件过大 (>200KB). 你想要重置错误日志吗?(Y/N): ')
			if del_log.lower() == 'y':
				with open('Error_Log_Waifu2x-Extension.log','w+') as f:
					f.write('')
				with open('Error_Log_Waifu2x-Extension.log','a+') as f:
					timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
					f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Error log reseted by user.\n')
				
	else:
		print('错误 : 找不到错误日志文件.')	#提示错误日志文件丢失
		input('按Enter返回')

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
			os.remove(scaledFilePath+"_compressed.gif")
			print('\n'+'无法压缩 '+inputPath+'\n')
		else:
			saved_size_str = str(saved_size)+'KB'
			print('\n'+'成功压缩 '+inputPath+'\n')
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
			os.remove(scaledFilePath+"_compressed.jpg")
			print('\n'+'无法压缩 ['+inputPath+'] 该图片或许已经被压缩过了.\n你可以尝试减少 "图像质量" 的值.'+'\n')
		else:
			print('\n'+'压缩完成 '+inputPath+'\n')
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
			settings_values = ReadSettings()
			cols = settings_values['cols_resize']
			lines = settings_values['lines_resize']
		except BaseException:
			time.sleep(0.02)
			settings_values = ReadSettings()
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
	settings_values = ReadSettings()
	settings_values['cols_resize'] = cols
	settings_values['lines_resize'] = lines
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)
	while Complete_ResizeWindow(cols,lines):
		time.sleep(0.01)
	return 0

def Get_cols_lines():
	settings_values = ReadSettings()
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

	
	
#=============================== Benchmark =============================
def Benchmark():
	print('================ 基准测试 ===================')
	print(' 1.Tile size块大小(对于 waifu2x-ncnn-vulkan)')
	print('')
	print(' 2.线程数量(对于 waifu2x-converter)')
	print('')
	print(' 3.线程数量(对于 Anime4K)')
	print('==============================================')
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
	print('这个基准测试会帮助你确定你的电脑可以同时运行多少个 Anime4k 线程.')
	print('为了获得准确的结果, 请不要在测试期间使用电脑或者在后台运行占用资源的程式.')
	print('---------------------------------------------------------------------')
	if input('你想现在开始运行基准测试吗? (y/n): ').lower().strip(' ') != 'y':
		return 0
	wait_to_cool_time=int(input('你想要等待多少秒以使你的电脑冷却: '))
	
	Window_Title('[运行基准测试中]')
	print('-------------------------------------------------------')
	print('这个基准测试需要运行一段时间,请稍等.....')
	print('-------------------------------------------------------')
	print('等待 '+str(wait_to_cool_time)+' 秒以使电脑冷却.')
	
	time.sleep(wait_to_cool_time)
	
	print('运行中....')
	
	settings_values = ReadSettings()
	notificationSound = settings_values['notificationSound']
	
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
		print('线程数: ',Number_of_threads)
		print('消耗时间: ',new_time_cost)
		print('---------------------------------')
		if new_time_cost <= old_time_cost:
			old_time_cost = new_time_cost
			old_Number_of_threads = Number_of_threads
		else:
			break
		print('等待 '+str(wait_to_cool_time)+' 秒以使电脑冷却.')
		time.sleep(wait_to_cool_time)
		
	if notificationSound == 'y':
			thread_Notification=Play_Notification_Sound_Thread()
			thread_Notification.start()
	Window_Title('')
	os.system('cls')
	print('=================================================')
	print('适合您的电脑的线程数量是:',old_Number_of_threads)
	if input('是否现在启用结果值? (y/n): ').lower().strip(' ') != 'y':
		return 0
	settings_values['Number_of_threads_Anime4k']=old_Number_of_threads
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)



def Benchmark_converter():
	print('这个基准测试会帮助您确定您的电脑可以运行多少个 waifu2x-converter 线程.')
	print('为了获得准确的结果,请不要在测试运气期间使用电脑或者在后台运行占用资源的程式')
	print('-------------------------------------------------------------------------')
	if input('你想要现在开始运行基准测试吗? (y/n): ').lower().strip(' ') != 'y':
		return 0
	wait_to_cool_time=int(input('你想要等待多少秒以使你的电脑冷却: '))
	
	Window_Title('[运行基准测试中]')
	print('-------------------------------------------------------')
	print('个基准测试需要运行一段时间,请稍等.....')
	print('-------------------------------------------------------')
	print('等待 '+str(wait_to_cool_time)+' 秒以使电脑冷却.')
	
	time.sleep(wait_to_cool_time)
	settings_values = ReadSettings()
	notificationSound = settings_values['notificationSound']
	
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
		print('线程数 ',Number_of_threads)
		print('消耗时间: ',new_time_cost)
		print('---------------------------------')
		if new_time_cost <= old_time_cost:
			old_time_cost = new_time_cost
			old_Number_of_threads = Number_of_threads
		else:
			break
		print('等待 '+str(wait_to_cool_time)+' 秒以使电脑冷却.')
		time.sleep(wait_to_cool_time)
		
	if notificationSound == 'y':
			thread_Notification=Play_Notification_Sound_Thread()
			thread_Notification.start()
	Window_Title('')
	os.system('cls')
	print('==================================================')
	print('适合您的电脑的线程数量是:',old_Number_of_threads)
	if input('你想要现在启用结果值吗? (y/n): ').lower().strip(' ') != 'y':
		return 0
	settings_values['Number_of_threads_Waifu2x_converter']=old_Number_of_threads
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)



def Benchmark_vulkan():
	print('基准测试可以帮助你确定 "tile size(块大小)" 的最佳值.')
	print('为了获得准确的结果, 请在基准测试运行期间不要使用你的电脑或者在后台运行占用大量资源的任务.')
	print('---------------------------------------------------------------------------------------')
	if input('你想现在开始基准测试吗? (y/n): ').lower().strip(' ') != 'y':
		return 0
	wait_to_cool_time=int(input('你想要等待多少秒以冷却你的电脑: '))
	
	Window_Title('[运行基准测试中]')
	print('-------------------------------------------------------')
	print('基准测试需要运行一段时间,请稍等.....')
	print('-------------------------------------------------------')
	print('等待 '+str(wait_to_cool_time)+' 秒来冷却您的电脑.')
	time.sleep(wait_to_cool_time)
	settings_values = ReadSettings()
	notificationSound = settings_values['notificationSound']
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
		print('消耗时间: ',new_time_cost)
		print('---------------------------------')
		if new_time_cost <= old_time_cost:
			old_time_cost = new_time_cost
			old_tileSize = tileSize
		else:
			break
		tileSize=tileSize+50
		print('等待 '+str(wait_to_cool_time)+' 秒来冷却你的电脑.')
		time.sleep(wait_to_cool_time)
	if notificationSound == 'y':
			thread_Notification=Play_Notification_Sound_Thread()
			thread_Notification.start()
	Window_Title('')
	print('==================================================================')
	print('对于您的电脑, "tile size" 的最佳值是:',old_tileSize)
	if input('你想现在启用结果值吗? (y/n): ').lower().strip(' ') != 'y':
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
	print('中文:')
	print('注意:中文版本由机器翻译生成, 仅供无法阅读英语者参考, 可能包含错误, 一切以英文原版许可证为准.')
	print('---------------------------------------------')
	print('版权所有 2019 Aaron Feng\n')
	print('特此授予任何获得本软件和相关文档文件（“软件”）副本的人免费许可，以无限制地交易本软件，包括但不限于使用，复制，修改，合并的权利在符合以下条件的前提下，发布，分发，再许可，并允许向其提供软件的人员这样做：\n')
	print('上述版权声明和本许可声明应包含在本软件的所有副本或实质部分中。\n')
	print('本软件按“原样”提供，不提供任何明示或暗示的保证，包括但不限于适销性，特定用途的适用性和不侵权的保证。在任何情况下，作者或版权所有者均不对任何索赔，损害或其他责任承担任何责任，无论是在合同，侵权行为还是其他方面的行为，由本软件引起或与之相关，或与本软件的使用或其他交易有关。软件。\n')
	print('------------------------------------------')
	print('图标作者 : Freepik ( https://www.flaticon.com/authors/freepik )')
	print('来自 Flaticon : https://www.flaticon.com/')
	print('------------------------------------------')
	input('按Enter键返回')

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
					os.remove(old_path)
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
	print('       载入中....')
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
		print(' 可用的 GPU ID (对于 waifu2x-ncnn-vulkan): ',gpuId_list)
		print('---------------------------------------------------------')
	else:
		print('------------------------------------------')
		print(' 没有支持waifu2x-ncnn-vulkan的显卡.')
		print(' 请升级或者重装你的显卡驱动.')
		print('------------------------------------------')
	return gpuId_list

#======================================================  Compatibility_Test =============================================================

def Compatibility_Test(Init):
	
	waifu2x_ncnn_vulkan_avaliable = False
	waifu2x_converter_avaliable = False
	Anime4k_avaliable = False
	
	current_dir = os.path.dirname(os.path.abspath(__file__))
	inputPath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension.jpg'
	scaledFilePath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension_waifu2x.jpg'
	
	os.system('cls')
	print('----------------------------')
	print('        载入中....')
	print('----------------------------')
	
	#============== 测试waifu2x-ncnn-vulkan ==============
	
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
			waifu2x_ncnn_vulkan_avaliable = True
			os.remove(scaledFilePath)
			break
		else:
			break
		gpuId = gpuId+1
	
	#=========================== 测试waifu2x-converter ===================
	if os.path.exists(scaledFilePath):
		os.system("del /q \""+scaledFilePath+"\"")
		
	os.system('waifu2x-converter\\waifu2x-converter_x64.exe -i "'+inputPath+'" -o "'+scaledFilePath+'" --scale_ratio '+'2'+' --noise_level '+'2'+' --model_dir waifu2x-converter\\models_rgb')
	
	if os.path.exists(scaledFilePath):
		waifu2x_converter_avaliable = True
		os.system("del /q \""+scaledFilePath+"\"")
	
	#======================== 测试 Anime4k ===============================
	if os.path.exists(scaledFilePath):
		os.system("del /q \""+scaledFilePath+"\"")
	
	os.system('java -jar Anime4K\\Anime4K.jar "'+inputPath+'" "'+scaledFilePath+'" '+'2')
	
	if os.path.exists(scaledFilePath):
		Anime4k_avaliable = True
		os.system("del /q \""+scaledFilePath+"\"")
	
	#====================== 输出测试结果 =======================
	os.system('cls')
	
	if waifu2x_ncnn_vulkan_avaliable:
		str_waifu2x_ncnn_vulkan_avaliable = '是'
	else:
		str_waifu2x_ncnn_vulkan_avaliable = '否'
		
	if waifu2x_converter_avaliable:
		str_waifu2x_converter_avaliable = '是'
	else:
		str_waifu2x_converter_avaliable = '否'
	
	if Anime4k_avaliable:
		str_Anime4k_avaliable = '是'
	else:
		str_Anime4k_avaliable = '否'
	
	print('------------------------------------------------')
	print('是否兼容 waifu2x-ncnn-vulkan : ',str_waifu2x_ncnn_vulkan_avaliable)
	print('')
	print('是否兼容 waifu2x-converter : ',str_waifu2x_converter_avaliable)
	print('')
	print('是否兼容 Anime4k : ',str_Anime4k_avaliable)
	print('------------------------------------------------')
	print('')
	if waifu2x_ncnn_vulkan_avaliable and waifu2x_converter_avaliable and Anime4k_avaliable:
		if Init:
			time.sleep(3)
		else:
			input('按Enter键以继续')
	else:
		ChangeColor_warning()
		print('当 waifu2x-ncnn-vulkan 或 waifu2x-converter 可用时,')
		print('您无需修复兼容性问题也可以正常使用软件内的功能')
		print('-----------------------------------------------------')
		print('警告,在当前电脑上出现了兼容性问题') 
		print('请按照以下建议来修复兼容性问题:')
		print('----------------------------------------------------------------')
		print('首先, 检查更新, 确保你在使用最新版本的Waifu2x-Extension.')
		if waifu2x_ncnn_vulkan_avaliable == False:
			print('')
			print('-------------------------------------------------')
			print('Waifu2x-ncnn-vulkan:')
			print('重装或者更新显卡驱动')
			print('并确认你的显卡支持Vulkan.')
			print('-------------------------------------------------')
			print('')
			
		if waifu2x_converter_avaliable == False:
			print('')
			print('-------------------------------------------------------------------')
			print('Waifu2x-converter:')
			print('检查更新,确认你在使用最新版')
			print('如果这样依旧不兼容, 看在上帝的份上, 换个新电脑吧')
			print('-------------------------------------------------------------------')
			print('')
			
		if Anime4k_avaliable == False:
			print('')
			print('------------------------------')
			print('Anime4k:')
			print('安装最新版本的JDK和JRE')
			print('------------------------------')
			print('')
		
		
		print('如果按照上面的建议操作后依旧无法修复兼容问题, 请在 设置 中启用当前兼容的组件.')
		print('')
		print('--------------------')
		print('按 Enter 键以继续.')
		print('--------------------')
		input()
		os.system('cls')
		ChangeColor_default()
		
		if waifu2x_ncnn_vulkan_avaliable == False and waifu2x_converter_avaliable == True:
			print('我们检测到waifu2x-converter在您的电脑上可用, 是否现在启用??\n')
			print('waifu2x-converter支持放大 图片,视频,GIF')
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

	
#=============================== Default Window Title =================
def Window_Title(Add_str = ''):
	os.system('title = Waifu2x扩展 '+Version_current+' 作者: Aaron Feng '+Add_str)

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
		print('''设置界面颜色
------------------
0.湖绿色(初始值)
1.蓝色
2.绿色
3.红色
4.紫色
5.黄色
6.白色
------------------
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
				input('输入错误,按Enter键以继续')
				os.system('cls')
		else:
			os.system('cls')
			input('输入错误,按Enter键以继续')
			os.system('cls')

#===================================================== MOVE FILE =========================================================
def Move_file_org_new(org_path,new_path):
	if os.path.exists(os.path.dirname(new_path)) == False:
		os.mkdir(os.path.dirname(new_path))
	if os.path.exists(new_path):
		os.remove(new_path)
	os.system('copy /y "'+org_path+'" "'+new_path+'"')
	if os.path.exists(new_path):
		os.remove(org_path)
	else:
		print('错误: Move_file_org_new() -  new_path doesn\'t exists')

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

#================================================ Pop-up window ====================================================================
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
        if psutil.Process(pid).name() == str_processname:
            return True
    else:
        return False

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
	
	ChooseFormat()
	
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
			print('                   !!! 错误 !!!')
			print('---------------------------------------------------')
			ErrorStr = str(traceback.print_exc())
			
			with open('Error_Log_Waifu2x-Extension.log','a+') as f:
				f.write(ErrorStr)
			
			print('---------------------------------------------------')
			print('发生了一个错误, 请报告给开发者.')
			print('')
			print('反馈链接:')
			print('https://github.com/AaronFeng753/Waifu2x-Extension/issues')
			print('')
			print('你可以在这里下载最新版,或许该错误已经在最新版中被修复了:')
			print('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest')
			print('----------------------------------------')
			print('按Enter以重新启动程序')
			input()
			os.system('cls')
			python = sys.executable
			os.execl(python, python, * sys.argv)
	else:
		os.system('cls')
		print('--------------------------------------------------------------------------------------------------------------')
		print('我们检测到当前软件所处的文件夹导致软件必须申请\n 管理员权限来继续正常运行.')
		print('我们建议您将软件移动到另一个文件夹或者直接给予软件管理员权限')
		print('--------------------------------------------------------------------------------------------------------------')
		print('按Enter键来重启软件并申请管理员权限. ')
		input()
		# Re-run the program with admin rights
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

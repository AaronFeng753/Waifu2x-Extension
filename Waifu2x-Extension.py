#!/usr/bin/python  
# -*- coding: utf-8 -*- 

import os
os.system('cls')
print('Loading.......')

Version_current='v2.75'

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
		print('│ 11 : Settings.           12 : Benchmark.                     │')
		print('│                                                              │')
		print('│ 13 : Read error log.     14 : Check update.                  │')
		print('│                                                              │')
		print('│ 15 : Readme.             16 : License.                       │')
		print('│                                                              │')
		print('│ E : Exit.                                                    │')
		print('├──────────────────────────────────────────────────────────────┤')
		print('│                D : Donate 捐赠. (Alipay 支付宝)              │')
		print('└──────────────────────────────────────────────────────────────┘')
		print('( 1 / 2 / 3 / 4 /...../ E / D ): ')
		mode = input().strip(' ').lower()
		if mode == "1":
			os.system('cls')
			Image_Gif_Scale_Denoise()
			os.system('cls')
			
		elif mode == "2":
			os.system('cls')
			Scale_Denoise_Video()
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
			license_()
			os.system('cls')
		elif mode == "e":
			ChangeColor_cmd_original()
			os.system('cls')
			return 0
		elif mode == "d":
			os.system('cls')
			print('Loading.......')
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/blob/master/donate.jpg')
			os.system('cls')
			print('                     Thank you!!!  :)')
		else:
			os.system('cls')
			ChangeColor_warning()
			input('Error : wrong input,pls press Enter key to return')
			ChangeColor_default()
			os.system('cls')

#===================================================== Scale & Denoise Image & GIF ========================================
def Image_Gif_Scale_Denoise():
	print('PS:In the new version, we merged the previous three modes.')
	print('----------------------------------------------------------')
	print("================= Scale & Denoise Image & GIF ================")
	print("Type 'r' to return to the previous menu")
	print("Type 'o' to stop input more path, and input path must be a folder or a file")
	print("Scaled images & gifs will be in the input path \n")
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
			
	inputPathList = Deduplicate_list(inputPathList)
	
	pathlist_files_folder = Separate_files_folder(inputPathList)
	
	inputPathList_files = pathlist_files_folder[0]
	inputPathList_folders = pathlist_files_folder[1]
	scan_subfolders = 'n'
	if inputPathList_folders != []:
		scan_subfolders = input_scan_subfolders()
		if scan_subfolders.lower() == 'r':
			return 1
	
	if scan_subfolders.lower() == 'y':
		subfolders_list = []
		for inputPathList_folders_folder_scan in inputPathList_folders:
			for path_scansub,useless,filename in os.walk(inputPathList_folders_folder_scan):
				for dirs in os.walk(path_scansub):
					subfolders_list.append(str(dirs[0]))
				break
		inputPathList_folders = subfolders_list
		
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
	load_proc_save_str = settings_values['load_proc_save_str']
	if multiThread_Scale.lower() == 'n':
		load_proc_save_str = ' -j 1:1:1 '
	gpuId = settings_values['gpuId']
	notificationSound = settings_values['notificationSound']
	gpuId_str=''
	if gpuId.lower() != 'auto':
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
	if delorginal.lower() == 'r':
		return 1
	
	turnoff = input_turnoff()
	if turnoff.lower() == 'r':
		return 1
	
	sleepMode = input_sleepMode()
	if sleepMode.lower() == 'r':
		return 1
	elif sleepMode.lower() == 'y':
		load_proc_save_str = ' -j 1:1:1 '
		notificationSound = 'n'
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	#=================================== 文件夹 =========================
	if inputPathList_folders != []:
		if Gif_exists:
			
			inputPathList_files_gif = []
			if Image_exists:
				inputPathList_gif = MoveGifFiles(inputPathList_folders)
				for inputPath in inputPathList_gif:
					for path,useless,fnames in os.walk(inputPath+'\\protectfiles_waifu2x_extension'):
						for fname in fnames:
							if os.path.splitext(fname)[1] == '.gif':
								inputPathList_files_gif.append(path+'\\'+fname)
						break
			else:
				for inputPath in inputPathList_folders:
					for path,useless,fnames in os.walk(inputPath):
						for fname in fnames:
							if os.path.splitext(fname)[1] == '.gif':
								inputPathList_files_gif.append(path+'\\'+fname)
						break
				
			process_gif_scale_modeABC(inputPathList_files_gif,orginalFileNameAndFullname,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,optimizeGif,delorginal)
		
		if Image_exists:
			Process_ImageModeAB(inputPathList_folders,orginalFileNameAndFullname,JpgQuality,models,noiseLevel,scale,load_proc_save_str,tileSize,gpuId_str,saveAsJPG,delorginal)
			RecoverGifFiles(inputPathList_folders)
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
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	if notificationSound.lower() == 'y':
		thread_Notification=Play_Notification_Sound_Thread()
		thread_Notification.start()
	
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
		if scale == '4':
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 1)
			thread1.start()
		else:
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 0)
			thread1.start()
		
		if os.path.exists(inputPath+"\\scaled_waifu2x\\") == True:
			os.system("rd /s/q \""+inputPath+"\\scaled_waifu2x\\"+'"')
		os.mkdir(inputPath+"\\scaled_waifu2x\\")
		
		if scale == '4':
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
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
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled_waifu2x"+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled_waifu2x"+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			
			while thread_DelOldFileThread_4x.isAlive():
				time.sleep(1)
			
			for files in os.walk(inputPath+'\\scaled_waifu2x\\'):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(os.path.splitext(fileNameAndExt)[0])[0]
					fileNameAndExt_new = orginalFileNameAndFullname[fileName]
					os.rename(os.path.join(inputPath+'\\scaled_waifu2x\\',fileNameAndExt),os.path.join(inputPath+'\\scaled_waifu2x\\',fileNameAndExt_new+".png"))
			
			
		else:
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled_waifu2x\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models+gpuId_str+load_proc_save_str)
		
		if thread1.isAlive()==True:
			time.sleep(2)
			if thread1.isAlive()==True:
				stop_thread(thread1)
			
		if saveAsJPG.lower() == 'y':
			print('\n Convert image..... \n')
			for path,useless,fnames in os.walk(inputPath+'\\scaled_waifu2x\\'):
				for fnameAndExt in fnames:
					pngFile = path+'\\'+fnameAndExt
					fname = os.path.splitext(fnameAndExt)[0]
					jpgFile = path+'\\'+fname+'.jpg'
					imageio.imwrite(jpgFile, imageio.imread(pngFile), 'JPG', quality = JpgQuality)
					os.remove(pngFile)
			
		
		for files in os.walk(inputPath+'\\scaled_waifu2x\\'):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				originalName=list(orginalFileNameAndFullname.keys())[list(orginalFileNameAndFullname.values()).index(fileName)]
				if saveAsJPG.lower() == 'y':
					os.rename(os.path.join(inputPath+'\\scaled_waifu2x\\',fileNameAndExt),os.path.join(inputPath+'\\scaled_waifu2x\\',originalName+"_Waifu2x.jpg"))
				else:
					os.rename(os.path.join(inputPath+'\\scaled_waifu2x\\',fileNameAndExt),os.path.join(inputPath+'\\scaled_waifu2x\\',originalName+"_Waifu2x.png"))
		
		orginalFileNameAndFullname = {}
		
		print('')
		if delorginal.lower() == 'y':
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
				print('------------------------------------------------------------------------------')
				print('Error occured, in order to save your files, the original files in this folder:')
				print(inputPath)
				print('will not be deleted.')
				print('------------------------------------------------------------------------------')
		print('Copy files...')
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
		
			
		if saveAsJPG.lower() == 'y':
			if os.path.exists(scaledFilePath+"_Waifu2x.png"):
				print('\n Convert image..... \n')
				imageio.imwrite(scaledFilePath+"_Waifu2x.jpg", imageio.imread(scaledFilePath+"_Waifu2x.png"), 'JPG', quality = JpgQuality)
				os.remove(scaledFilePath+"_Waifu2x.png")
		
		
		if delorginal.lower() == 'y':
			if os.path.exists(scaledFilePath+"_Waifu2x.png") or os.path.exists(scaledFilePath+"_Waifu2x.jpg"):
				os.system('del /q "'+inputPath+'"')
			else:
				print('----------------------------------------------------------------')
				print(' Error occured, in order to save your files, the original file :')
				print(' '+inputPath)
				print(' will not be deleted.')
				print('----------------------------------------------------------------')
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
			
		TIME_GAP=getDuration(inputPath)
		print('Split gif.....')
		splitGif(inputPath,scaledFilePath)
		
		oldfilenumber=FileCount(scaledFilePath+'_split')
		
		orginalFileNameAndFullname = {}
		for files in os.walk(scaledFilePath+'_split'):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
			break
				
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
			gif_name=scaledFilePath+'_waifu2x.gif'
			if os.path.exists(gif_name):
				if os.path.getsize(gif_name)>0:
					os.system('del /q "'+inputPath+'"')
			else:
				print('----------------------------------------------------------------')
				print(' Error occured, in order to save your files, the original file :')
				print(' '+inputPath)
				print(' will not be deleted.')
				print('----------------------------------------------------------------')
			
		
		if optimizeGif.lower() == 'y':
			print('Compressing gif....')
			compress_gif(scaledFilePath+'_waifu2x.gif','1')
			os.remove(scaledFilePath+'_waifu2x.gif')
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
								os.remove(inputpath+f_name+'.png')
								inputpath_deled_list.append(f_name)
				break
			time.sleep(0.5)

#=============================================  Scale & Denoise Video  ====================================
def Scale_Denoise_Video():
	print('PS:In the new version, we merged the previous three modes.')
	print('----------------------------------------------------------')
	print("================ Scale & Denoise Video ===============")
	print("Type 'r' to return to the previous menu")
	print("Type 'o' to stop input more path, and input path must be a folder or a video file")
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
	inputPathList = Deduplicate_list(inputPathList)
	
	pathlist_files_folder = Separate_files_folder(inputPathList)
	
	inputPathList_files = pathlist_files_folder[0]
	inputPathList_folders = pathlist_files_folder[1]
	scan_subfolders = 'n'
	if inputPathList_folders != []:
		scan_subfolders = input_scan_subfolders()
		if scan_subfolders.lower() == 'r':
			return 1
	
	if scan_subfolders.lower() == 'y':
		subfolders_list = []
		for inputPathList_folders_folder_scan in inputPathList_folders:
			for path_scansub,useless,filename in os.walk(inputPathList_folders_folder_scan):
				for dirs in os.walk(path_scansub):
					subfolders_list.append(str(dirs[0]))
				break
		inputPathList_folders = subfolders_list
	
	scale = input_scale()
	if scale.lower() == 'r':
		return 1
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
	if noiseLevel.lower() == 'r':
		return 1
	multiThread_Scale = settings_values['multiThread_Scale']
	load_proc_save_str = settings_values['load_proc_save_str']
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
	
	sleepMode = input_sleepMode()
	if sleepMode.lower() == 'r':
		return 1
	elif sleepMode.lower() == 'y':
		load_proc_save_str = ' -j 1:1:1 '
		notificationSound = 'n'
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	 
	inputPathList_file_video = []
	for folders in inputPathList_folders:
		for path,useless,fnames in os.walk(folders):
			for fname in fnames:
				inputPathList_file_video.append(path+'\\'+fname)
			break
	inputPathList_files = inputPathList_file_video + inputPathList_files
	process_video_modeABC(inputPathList_files,models,scale,noiseLevel,load_proc_save_str,tileSize,gpuId_str,delorginal)
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
	total_num = len(inputPathList_files)
	finished_num = 1
	for inputPath in inputPathList_files:
		Window_Title('  [Scale Video]  Video: '+'('+str(finished_num)+'/'+str(total_num)+')')
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
		finished_num = finished_num+1
	Window_Title('')
#============================= Compress_image_gif ===============================
def Compress_image_gif():
	print('PS:In the new version, we merged the previous three modes.')
	print('----------------------------------------------------------')
	print("================= Compress image & gif ================")
	print("Type 'r' to return to the previous menu")
	print("Type 'o' to stop input more path, and input path must be a folder or a file")
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
	inputPathList = Deduplicate_list(inputPathList)
	
	pathlist_files_folder = Separate_files_folder(inputPathList)
	
	inputPathList_files_input = pathlist_files_folder[0]
	inputPathList_folders = pathlist_files_folder[1]
	scan_subfolders = 'n'
	if inputPathList_folders != []:
		scan_subfolders = input_scan_subfolders()
		if scan_subfolders.lower() == 'r':
			return 1
	
	if scan_subfolders.lower() == 'y':
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
	for folders in inputPathList_folders:
		for path,useless,fnames in os.walk(folders):
			for fname in fnames:
				inputPathList_files.append(path+'\\'+fname)
			break
	inputPathList_files = inputPathList_files+inputPathList_files_input
			
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
	
#=================================== Process_compress_image ===============================================

def Process_compress_image(inputPathList_files,delorginal,multiThread,JpgQuality):
	if multiThread.lower() == 'y':
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
				os.remove(scaledFilePath+"_compressed.jpg")
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
				os.remove(scaledFilePath+"_compressed.gif")
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
		imageio.imwrite(scaledFilePath+'_split\\scaled\\'+filename+".jpg", imageio.imread(png), 'JPG', quality = 100)
	
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
	
	if os.path.exists(video_dir+'audio_waifu2x.wav'):
		os.remove(video_dir+'audio_waifu2x.wav')
	
	os.system('ffmpeg -i "'+video_path_filename+'.mp4'+'" "'+video_dir+'audio_waifu2x.wav"')

def images2video(inputpath):
	video_path_filename = os.path.splitext(inputpath)[0]
	video_ext = os.path.splitext(inputpath)[1]
	video_dir = os.path.dirname(inputpath)+'\\'
	frames_scaled_dir = video_dir+'frames_waifu2x\\scaled\\'
	cap = cv2.VideoCapture(inputpath)
	fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
	frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	frame_figures = len(str(frame_counter))
	os.system('ffmpeg -f image2 -framerate '+str(fps)+' -i "'+frames_scaled_dir+'%0'+str(frame_figures)+'d.png" -i "'+video_dir+'audio_waifu2x.wav" -r '+str(fps)+' -pix_fmt yuv420p "'+video_path_filename+'_waifu2x'+video_ext+'"')
	
	os.remove(video_dir+'audio_waifu2x.wav')
	#os.system('del /q "'+video_dir+'audio_waifu2x.wav"')

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
		scale = input('Scale ratio(1/2/4, default='+default_value+'): ').strip(' ')
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
		tileSize = input('Tile size(>=32, default='+default_value+'): ').strip(' ')
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
		noiseLevel = input('Denoise level(-1/0/1/2/3, default='+default_value+'): ').strip(' ')
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
		delorginal = input('Delete original files?(y/n, default='+default_value+'): ').strip(' ')
		if delorginal in ['y','n','Y','N','','r','R']:
			break
		else:
			print('wrong input, pls input again')
	
	if delorginal == '':
		delorginal = default_value
	return delorginal
	
def input_turnoff():
	while True:
		turnoff = input('turn off computer when finished?(y/n, default=n): ').strip(' ')
		if turnoff in ['y','n','Y','N','','r','R']:
			break
		else:
			print('wrong input, pls input again')
	
	if turnoff == '':
		turnoff = 'n'
	return turnoff

def input_saveAsJPG():
	settings_values = ReadSettings()
	while True:
		saveAsJPG = input('Save as .jpg? (y/n, default=y): ').strip(' ')
		if saveAsJPG in ['y','n','Y','N','']:
			break
		else:
			print('wrong input, pls input again')
	
	if saveAsJPG == '':
		saveAsJPG = 'y'
		
	settings_values['saveAsJPG']=saveAsJPG
	
	if saveAsJPG.lower() == 'y':
		while True:
			Compress = input('Compress the .jpg file?(Almost lossless) (y/n, default=y): ').strip(' ')
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
	print('''This will slightly affect the quality of the GIF, but it will save a lot of space.
----------------------------------------------------------------------------------''')
	while True:
		optimizeGif = input('Optimize .gif? (y/n, default=y): ').strip(' ')
		if optimizeGif in ['y','n','Y','N','']:
			break
		else:
			print('wrong input, pls input again')
	
	if optimizeGif == '':
		optimizeGif = 'y'
		
	settings_values['optimizeGif'] = optimizeGif
	with open('waifu2x-extension-setting','w+') as f:
		json.dump(settings_values,f)
	
def input_gifCompresslevel():
	settings_values = ReadSettings()
	default_value = settings_values['gifCompresslevel']
	while True:
		gifCompresslevel = input('Compress level(1/2/3/4, default='+default_value+'): ').strip(' ')
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
		multiThread = input('Enable multithreading(Compress)? (y/n, default='+default_value+'): ').strip(' ')
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
	gpuId_list = View_GPU_ID()
	if gpuId_list == []:
		input('Press Enter key to return')
	gpuId_list_str = ''
	for id_ in gpuId_list:
		gpuId_list_str = gpuId_list_str+'/'+str(id_)
	while True:
		gpuId = input('GPU ID (auto (Automatic)'+gpuId_list_str+', default='+default_value+'): ').strip(' ')
		if gpuId.isdigit():
			if int(gpuId) in gpuId_list:
				break
			else:
				os.system('cls')
				print('wrong input, pls input again')
				print('----------------------------')
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
		notificationSound = input('Enable notification sound? (y/n, default='+default_value+'): ').strip(' ')
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
			
def input_scan_subfolders():
	while True:
		scan_subfolders = input('Scan subfolders? ( y/n, default= n ): ').strip(' ')
		if scan_subfolders in ['y','n','Y','N','R','r','']:
			break
		else:
			print('wrong input, pls input again')
	
	if scan_subfolders == '':
		scan_subfolders = 'n'
		
	return scan_subfolders

def input_sleepMode():
	while True:
		
		sleepMode = input('Enable sleep mode?( y / n / help , default = n ): ').strip(' ').lower()
		if sleepMode in ['y','n','','r','help']:
			if sleepMode == 'help':
				print('')
				print('--------------------------------------------------------------------------------------------')
				print('When "sleep mode" is enabled, the software will attempts to reduce performance requirements,')
				print('thereby reducing the computer\'s operating pressure and thus minimizing noise.')
				print('And turn off notification sound.')
				print('Enabling this mode will lengthen the time it takes for the program to complete its task.')
				print('--------------------------------------------------------------------------------------------')
			else:
				break
		else:
			print('wrong input, pls input again')
	
	if sleepMode == '':
		sleepMode = 'n'
	return sleepMode
	

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
		print('Failed to establish connection, pls check your internet or try again, press Enter key to return....\n')
		input()
		os.system('cls')
	
		
def checkUpdate_start(Version_current):
	os.system('cls')
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
	'Benchmark_Image_waifu2x_extension_6.png','Benchmark_Image_waifu2x_extension_7.png','Benchmark_Image_waifu2x_extension_8.png',
	'vgi_waifu2x_extension.jpg','Resize-window.exe']
	
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
		print(' 2: Default value of "Scale ratio". Current value: '+settings_values['scale']+'\n')
		print(' 3: Default value of "Denoise Level". Current value: '+settings_values['noiseLevel']+'\n')
		print(' 4: Delete original files when finished? Current default value: '+settings_values['delorginal']+'\n')
		print(' 5: Gif compress level. Current default value: '+settings_values['gifCompresslevel']+'\n')
		print(' 6: Image quality ( When compress images ). Current default value: ',settings_values['image_quality'],'\n')
		print(' 7: Number of threads ( Scale & Denoise ). Current default value: ',settings_values['Number_of_threads'],'\n')
		print(' 8: Reset error log.\n')
		print(' 9: Show settings_values.\n')
		print(' 10: Change interface color.\n')
		print(' R : Return to the main menu.')
		print('-----------------------------------------------------------------------------')
		mode = input('(1/2/3/..../r): '.upper())
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
					
			settings_values['delorginal']=value_
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
		
		elif mode== "5":
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
		
		elif mode == "6":
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
		
		elif mode== "7":
			os.system('cls')
			Number_of_threads=''
			print('Change this setting may cause performance issues.')
			print('We recommend you to use the default setting.')
			print('-------------------------------------------------')
			while True:
				Number_of_threads = input('Number of threads(Scale&Denoise) ( 2 / 3 / 4 /.... ; default = 2 ): ').strip(' ')
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
		
		elif mode == "8":
			os.system('cls')
			
			with open('Error_Log_Waifu2x-Extension.log','w+') as f:
				f.write('')
				
			with open('Error_Log_Waifu2x-Extension.log','a+') as f:
				timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
				f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Error log reseted by user.\n')
			
			input('Error log reseted, press Enter key to return.')
			
			os.system('cls')
		
		elif mode == "9":
			os.system('cls')
			
			for key,val in settings_values.items():
				print(key+' : '+val)
			print('--------------------------')
			input('press Enter key to return.')
			
			os.system('cls')
			
		elif mode == "10":
			os.system('cls')
			Set_default_color()
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
	default_values = {'SettingVersion':'3','CheckUpdate':'y','scale':'2','First_Time_Boot_Up':'y',
						'noiseLevel':'2','saveAsJPG':'y','tileSize':'200','default_color':'0b',
						'Compress':'y','delorginal':'n','optimizeGif':'y','gifCompresslevel':'1',
						'multiThread':'y','gpuId':'auto','notificationSound':'y','multiThread_Scale':'y',
						'image_quality':'95','load_proc_save_str':' -j 2:2:2 ','Number_of_threads':'2'}
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
			os.remove(scaledFilePath+"_compressed.gif")
			print('\n'+'Failed to compress '+inputPath+'\n')
		else:
			saved_size_str = str(saved_size)+'KB'
			print('\n'+'Finished to compress '+inputPath+'\n')
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
			os.remove(scaledFilePath+"_compressed.jpg")
			print('\n'+'Failed to compress ['+inputPath+'] This image may be already being compressed.\nYou can try to reduce "image quality".'+'\n')
		else:
			print('\n'+'Finished to compress '+inputPath+'\n')
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
		time.sleep(0.2)

	
#=============================== Benchmark =============================
def Benchmark():
	print('============================== Benchmark ==============================================')
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
	load_proc_save_str = settings_values['load_proc_save_str']
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
		print('Wait '+str(wait_to_cool_time)+' seconds to cool the computer.')
		time.sleep(wait_to_cool_time)
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
	print('----------------------------')
	print('        Loading....')
	print('----------------------------')
	gpuId = 0
	gpuId_list = []
	for x in range(0,10):
		gpuId_str = ' -g '+str(gpuId)
		settings_values = ReadSettings()
		current_dir = os.path.dirname(os.path.abspath(__file__))
		models = 'models-upconv_7_anime_style_art_rgb'
		scale = '2'
		noiseLevel = '0'
		tileSize = '50'
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
	os.system('cls')
	if len(gpuId_list) > 0:
		print('---------------------------------------------')
		print(' Available GPU ID: ',gpuId_list)
		print('---------------------------------------------')
	else:
		print('---------------------------------------------------------------')
		print(' No GPU availabel. Pls upgrade or reinstall your GPU driver.')
		print('---------------------------------------------------------------')
	return gpuId_list

def View_GPU_ID_start():
	os.system('cls')
	print('----------------------------')
	print('        Loading....')
	print('----------------------------')
	gpuId = 0
	gpuId_list = []
	for x in range(0,10):
		gpuId_str = ' -g '+str(gpuId)
		settings_values = ReadSettings()
		current_dir = os.path.dirname(os.path.abspath(__file__))
		models = 'models-upconv_7_anime_style_art_rgb'
		scale = '2'
		noiseLevel = '0'
		tileSize = '50'
		load_proc_save_str = ' -j 1:1:1 '
		inputPath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension.jpg'
		scaledFilePath = current_dir+'\\viewGpuId-files-waifu2x-extension\\vgi_waifu2x_extension_waifu2x.jpg'
		if os.path.exists(scaledFilePath) == True:
			os.system("del /q \""+scaledFilePath+"\"")
		os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+str(tileSize)+" -m "+models+gpuId_str+load_proc_save_str)
		if os.path.exists(scaledFilePath)==True:
			gpuId_list.append(gpuId)
			os.system("del /q \""+scaledFilePath+"\"")
			break
		else:
			break
		gpuId = gpuId+1
	os.system('cls')
	return gpuId_list
	
#=============================== Default Window Title =================
def Window_Title(Add_str = ''):
	os.system('title = Waifu2x-Extension '+Version_current+' by Aaron Feng '+Add_str)

#============================================  Deduplicate_list  ===================================

def Deduplicate_list(The_List):
	New_List = sorted(list(set(The_List)))
	return New_List
	
#============================================  Separate_files_folder  ===================================
def Separate_files_folder(paths_list):
	list_folders = []
	list_files = []
	for path in paths_list:
		if os.path.isdir(path):
		    list_folders.append(path)
		elif os.path.isfile(path):
		    list_files.append(path)
	return [list_files,list_folders]
#================================================ Change Color ======================
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
		print('''Set_default_color
------------------
0.Aqua
1.Blue
2.Green
3.Red
4.Purple
5.Yellow
6.White
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
				input('Wrong input,press Enter to continue.')
				os.system('cls')
		else:
			os.system('cls')
			input('Wrong input,press Enter to continue.')
			os.system('cls')

#==========================================  Init  ==================================================================

def init():		#初始化函数
	Window_Title('')	#更改控制台标题
	ChangeColor_default()	#更改文字颜色
	
	sys.stderr = Logger('Error_Log_Waifu2x-Extension.log', sys.stderr)
	with open('Error_Log_Waifu2x-Extension.log','a+') as f:
		timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Start running\n')
		
	settings_values = ReadSettings()
	
	if settings_values['CheckUpdate'] == 'y':
		checkUpdate_start(Version_current)
		
	if VerifyFiles() == 'verified':
		if settings_values['First_Time_Boot_Up'] == 'y':
			settings_values['First_Time_Boot_Up'] = 'n'
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
			if View_GPU_ID_start() == []:
				os.system('cls')
				print('------------------------------------------------------------')
				print(' No GPU availabel. Pls upgrade or reinstall your GPU driver.')
				print('------------------------------------------------------------')
				input('Press Enter to continue.')
		os.system('cls')
		thread_resizeWindow=ResizeWindow_Thread()
		thread_resizeWindow.start()
		time.sleep(0.2)
		ChooseFormat()
		if thread_resizeWindow.isAlive()==True:
			stop_thread(thread_resizeWindow)
	else:
		os.system('cls')
		print('-'*40)
		download_latest = input('Some files are missing. Do you wanna download the latest package?(y/n): ')
		if download_latest.lower() == 'y':
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest')
		os.system('cls')
		input('Press Enter key to exit.')
		ChangeColor_cmd_original()
		os.system('cls')
		

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
			ErrorStr = str(traceback.print_exc())
			
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

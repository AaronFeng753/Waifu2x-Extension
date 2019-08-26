print('Loading.......')

Version_current='v1.4'

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

def ChooseFormat(Version_current):
	while True:
		print('Waifu2x-Extension | '+Version_current+' | 2019/8/26 | Author: Aaron Feng')
		print('Github: https://github.com/AaronFeng753/Waifu2x-Extension')
		print('------------------------------------------')
		print(' I : Scale image.\n')
		print(' G : Scale gif.\n')
		print(' V : Scale video.\n')
		print(' C : Compress image (Lossless).')
		print('------------------------------------------')
		print(' S : Settings.\n')
		print(' L : Read error log.\n')
		print(' U : Check update.\n')
		print(' R : Readme.\n')
		print('\033[1;31;40m'+' ---------------------------------'+'\033[0m')
		print('\033[1;31;40m'+' |D : Donate 捐赠 (Alipay 支付宝)|'+'\033[0m')
		print('\033[1;31;40m'+' ---------------------------------\n'+'\033[0m')
		print(' E : Exit.')
		print('------------------------------------------')
		mode = input('( i / g / v / c / s / l / u / r / d / e ): '.upper())
		mode = mode.lower().strip(' ')
		if mode == "i":
			os.system('cls')
			os.system('color 0a')
			Image_()
			os.system('cls')
			os.system('color 0b')
		elif mode == "g":
			os.system('cls')
			os.system('color 0e')
			Gif_()
			os.system('cls')
			os.system('color 0b')
		elif mode == "v":
			os.system('cls')
			os.system('color 09')
			Video_()
			os.system('cls')
			os.system('color 0b')
		elif mode == "c":
			os.system('cls')
			os.system('color 09')
			Compress_()
			os.system('cls')
			os.system('color 0b')
		elif mode == "s":
			os.system('cls')
			os.system('color 07')
			Settings()
			os.system('cls')
			os.system('color 0b')
		elif mode == "e":
			os.system('color 07')
			os.system('cls')
			return 0
		elif mode == "l":
			os.system('cls')
			os.system('color 07')
			Error_Log()
			os.system('cls')
			os.system('color 0b')
		elif mode == "u":
			os.system('cls')
			checkUpdate(Version_current)
			os.system('cls')
		elif mode == "r":
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/blob/master/README.md')
			os.system('cls')
		elif mode == "d":
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/blob/master/donate.jpg')
			os.system('cls')
			print('Thank you!!! :)')
			print('---------------')
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press any key to return')
			os.system('color 0b')
			os.system('cls')

#============================= IMAGE Menu ===============================
def Image_():
	while True:
		print('Image')
		print('-----------------------------------------------------------------------------')
		print(' Mode A: input folders one by one and scaled all images in them.\n')
		print(' Mode B: input one folder and scaled all images in it and it\'s sub-folders.\n')
		print(' Mode C: input images one by one.\n')
		print(' R : return to the main menu')
		print('-----------------------------------------------------------------------------')
		mode = input('(a/b/c/r): '.upper())
		mode = mode.lower().strip(' ')
		if mode == "a":
			os.system('cls')
			Image_ModeA()
			os.system('cls')
		elif mode == "b":
			os.system('cls')
			Image_ModeB()
			os.system('cls')
		elif mode == "c":
			os.system('cls')
			Image_ModeC()
			os.system('cls')
		elif mode == "r":
			break
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press any key to return')
			os.system('color 0a')
			os.system('cls')
			
#============================= GIF Menu ===============================
def Gif_():
	while True:
		print('GIF')
		print('---------------------------------------------------------------------------')
		print(' Mode A: input folders one by one\n')
		print(' Mode B: input one folder and scaled all gif in it and it\'s sub-folders\n')
		print(' Mode C: input gif one by one\n')
		print(' R : return to the main menu')
		print('---------------------------------------------------------------------------')
		mode = input('(a/b/c/r): '.upper())
		mode = mode.lower().strip(' ')
		if mode == "a":
			os.system('cls')
			Gif_ModeA()
			os.system('cls')
		elif mode == "b":
			os.system('cls')
			Gif_ModeB()
			os.system('cls')
		elif mode == "c":
			os.system('cls')
			Gif_ModeC()
			os.system('cls')
		elif mode == "r":
			break
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press any key to return')
			os.system('color 0e')
			os.system('cls')
			
#============================= Video Menu ===============================
def Video_():
	while True:
		print('Video')
		print('---------------------------------------------------------------------------')
		print(' Mode A: input folders one by one\n')
		print(' Mode B: input one folder and scaled all video in it and it\'s sub-folders\n')
		print(' Mode C: input video one by one\n')
		print(' R : return to the main menu')
		print('---------------------------------------------------------------------------')
		mode = input('(a/b/c/r): '.upper())
		mode = mode.lower().strip(' ')
		if mode == "a":
			os.system('cls')
			Video_ModeA()
			os.system('cls')
		elif mode == "b":
			os.system('cls')
			Video_ModeB()
			os.system('cls')
		elif mode == "c":
			os.system('cls')
			Video_ModeC()
			os.system('cls')
		elif mode == "r":
			break
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press any key to return')
			os.system('color 09')
			os.system('cls')
			
#============================= Compress Menu ===============================
def Compress_():
	while True:
		print('Compress image')
		print('---------------------------------------------------------------------------')
		print(' Mode A: input folders one by one\n')
		print(' Mode B: input one folder and compress all images in it and it\'s sub-folders\n')
		print(' Mode C: input images one by one\n')
		print(' R : return to the main menu')
		print('---------------------------------------------------------------------------')
		mode = input('(a/b/c/r): '.upper())
		mode = mode.lower().strip(' ')
		if mode == "a":
			os.system('cls')
			Compress_ModeA()
			os.system('cls')
		elif mode == "b":
			os.system('cls')
			Compress_ModeB()
			os.system('cls')
		elif mode == "c":
			os.system('cls')
			Compress_ModeC()
			os.system('cls')
		elif mode == "r":
			break
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press any key to return')
			os.system('color 09')
			os.system('cls')
		
#=============================Image_MODE A===============================
def Image_ModeA():
	print("=================Image_MODE A================")
	print("Type 'return' to return to the previous menu")
	print("Type 'over' to stop input more path, and input path must be a folder, not a file")
	print("Scaled images will be in the input-path \n")
	inputPathOver = True
	inputPathList = []
	orginalFileNameAndFullname = {}
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'
	
	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\')
			if inputPath.lower() == 'return':
				return 1
			elif inputPath.lower() == 'over':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('error,input-path is invalid\n')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
	 
	scale = input_scale()
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
		
	tileSize = input_tileSize()
		
	saveAsJPG = input_saveAsJPG()
	
	if saveAsJPG == 'y':
		Compress = input_Compress()
		if Compress.lower() == 'y':
			JpgQuality=90
		
	turnoff = input_turnoff()
		
	delorginal = input_delorginal()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
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
				
		os.mkdir(inputPath+"\\scaled\\")
		
		if scale == '4':
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			
			File_x2=[]
			for path,useless,filenames in os.walk(inputPath+"\\scaled\\"):
				for filename in filenames:
					File_x2.append(path+'\\'+filename)
			
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 2)
			thread1.start()
			
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled"+"\" -o \""+inputPath+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled"+"\" -o \""+inputPath+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			
			for f in File_x2:
				os.system('del /q "'+f+'"')
				
			for files in os.walk(inputPath+'\\scaled\\'):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',fileName))
			
		else:
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
		
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
		os.system("xcopy /s /i /q /y \""+inputPath+"\\scaled\\*.*\" \""+inputPath+"\"")
		os.system("rd /s/q \""+inputPath+"\\scaled\"")
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	
	input('\npress any key to return to the menu')
	
#=====================================Image_MODE B======================================
def Image_ModeB():
	print("=================Image_MODE B================")
	print("Type 'return' to return to the previous menu")
	print("Input path must be a folder, not a file")
	print("Scaled images will be in the input-path \n")
	inputPathList = []
	orginalFileNameAndFullname = {}
	inputPathError = True
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'
	
	while inputPathError:
		inputPath = input('input-path: ')
		inputPath=inputPath.strip('"').strip('\\')
		if inputPath.lower() == 'return':
			return 1
		elif inputPath == '' or os.path.exists(inputPath) == False:
			print('error,input-path is invalid\n')
		else:
			inputPathError = False

	
	 
	scale = input_scale()
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
		
	tileSize = input_tileSize()
		
	saveAsJPG = input_saveAsJPG()
	
	if saveAsJPG == 'y':
		Compress = input_Compress()
		if Compress.lower() == 'y':
			JpgQuality=90
		
	turnoff = input_turnoff()
		
	delorginal = input_delorginal()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	for dirs in os.walk(inputPath):
		inputPathList.append(str(dirs[0]))
		
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
				
		os.mkdir(inputPath+"\\scaled\\")
		
		if scale == '4':
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
				
			File_x2=[]
			for path,useless,filenames in os.walk(inputPath+"\\scaled\\"):
				for filename in filenames:
					File_x2.append(path+'\\'+filename)
			
			thread1=PrograssBarThread(oldfilenumber,scalepath,scale,round_ = 2)
			thread1.start()
			
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled"+"\" -o \""+inputPath+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\\scaled"+"\" -o \""+inputPath+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			
			for f in File_x2:
				os.system('del /q "'+f+'"')
			
			for files in os.walk(inputPath+'\\scaled\\'):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',fileName))
			
		else:
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+inputPath+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
		
		
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
		os.system("xcopy /s /i /q /y \""+inputPath+"\\scaled\\*.*\" \""+inputPath+"\"")
		os.system("rd /s/q \""+inputPath+"\\scaled\"")
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	
	input('\npress any key to return to the menu')
	
#=============================Image_MODE C=====================================
def Image_ModeC():
	print("=================Image_MODE C================")
	print("Type 'return' to return to the previous menu")
	print("Type 'over' to stop input more path, and input path must be a file")
	print("Scaled images will be in the input-path \n")
	inputPathOver = True
	inputPathList = []
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\')
			
			if inputPath.lower() == 'return':
				return 1
			elif inputPath.lower() == 'over':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('error,input-path is invalid\n')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
	
	 
	scale = input_scale()
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
		
	tileSize = input_tileSize()
		
	saveAsJPG = input_saveAsJPG()
		
	if saveAsJPG == 'y':
		Compress = input_Compress()
		if Compress.lower() == 'y':
			JpgQuality=90
		
	turnoff = input_turnoff()
	
	
	delorginal = input_delorginal()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()

	TotalFileNum = len(inputPathList)
	FinishedFileNum = 1
	for inputPath in inputPathList:
		scaledFilePath = os.path.splitext(inputPath)[0]
		fileNameAndExt=str(os.path.basename(inputPath))
		
		thread1=ClockThread(TotalFileNum,FinishedFileNum)
		thread1.start()
		
		if scale == '4':
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+"_Waifu2x.png"+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+"_Waifu2x.png"+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)

		else:
			print("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+inputPath+"\" -o \""+scaledFilePath+"_Waifu2x.png\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
		
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
	
	input('\npress any key to return to the menu')


#======================================Gif_MODE A========================================
def Gif_ModeA():
	print("====================== Gif_MODE A =====================")
	print("Type 'return' to return to the previous menu")
	print("Type 'over' to stop input more path, and input path must be a folder")
	print("Scaled images will be in the input-path \n")
	inputPathOver = True
	inputPathList = []
	gifQuality = False
	orginalFileNameAndFullname = {}
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\')
			
			if inputPath.lower() == 'return':
				return 1
			elif inputPath.lower() == 'over':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('error,input-path is invalid\n')
			else:
				inputPathError = False
		if inputPathOver == True:

			inputPathList.append(inputPath)
	
	 
	scale = input_scale()
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
		
	tileSize = input_tileSize()
		
	highQuality = input_highQuality()
		
	turnoff = input_turnoff()
	
	delorginal = input_delorginal()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	inputPathList_files = []
	for folders in inputPathList:
		for path,useless,fnames in os.walk(folders):
			for fname in fnames:
				if os.path.splitext(fname)[1] == '.gif':
					inputPathList_files.append(path+'\\'+fname)
			break
	
	for inputPath in inputPathList_files:
		scaledFilePath = os.path.splitext(inputPath)[0]
			
		TIME_GAP=getDuration(inputPath)
		print('Split gif.....')
		splitGif(inputPath,scaledFilePath)
		
		oldfilenumber=FileCount(scaledFilePath+'_split')
		
		for files in os.walk(scaledFilePath+'_split'):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
				
	
		os.mkdir(scaledFilePath+'_split\\scaled')
		print('scal images.....')
		if scale == '4': 
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 1)
			thread1.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			File_x2=[]
			for path,useless,filenames in os.walk(scaledFilePath+'_split\\scaled\\'):
				for filename in filenames:
					File_x2.append(path+'\\'+filename)
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 2)
			thread1.start()		
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			for f in File_x2:
				os.system('del /q "'+f+'"')
			
			for files in os.walk(scaledFilePath+'_split\\scaled\\'):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(scaledFilePath+'_split\\scaled\\',fileNameAndExt),os.path.join(scaledFilePath+'_split\\scaled\\',fileName))
			
		else:
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 0)
			thread1.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
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
		
		
		if highQuality.lower() == 'y':
			gifQuality = False
		else:
			gifQuality = True
		
		print('Assembling Gif.....')
		assembleGif(scaledFilePath,TIME_GAP,gifQuality)
		print('Gif assembled')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal.lower() == 'y':
			os.system('del /q "'+inputPath+'"')
		
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')

#===================================Gif_MODE B========================================
def Gif_ModeB():
	print("====================== Gif_MODE B =====================")
	print("Type 'return' to return to the previous menu")
	print("Input path must be a folder")
	print("Scaled images will be in it's original path \n")
	inputPathOver = True
	inputPath_ = ''
	gifQuality = False
	orginalFileNameAndFullname = {}
	models = 'models-upconv_7_anime_style_art_rgb'
	inputPathError = True
	while inputPathError:
		inputPath_ = input('input-path: ')
		
		if inputPath_.lower() == 'return':
			return 1
		elif inputPath_ == '' or os.path.exists(inputPath_) == False:
			print('error,input-path is invalid\n')
		else:
			inputPath_=inputPath_.strip('"').strip('\\')
			inputPathError = False
	
	 
	scale = input_scale()
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
		
	tileSize = input_tileSize()
		
	highQuality = input_highQuality()
		
	turnoff = input_turnoff()
	
	delorginal = input_delorginal()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	inputPathList_files = []
	for path,useless,fnames in os.walk(inputPath_):
		for fname in fnames:
			if os.path.splitext(fname)[1] == '.gif':
				inputPathList_files.append(path+'\\'+fname)
	
	for inputPath in inputPathList_files:
		scaledFilePath = os.path.splitext(inputPath)[0]
			
		TIME_GAP=getDuration(inputPath)
		print('Split gif.....')
		splitGif(inputPath,scaledFilePath)
		
		oldfilenumber=FileCount(scaledFilePath+'_split')
		
		for files in os.walk(scaledFilePath+'_split'):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
				
	
		os.mkdir(scaledFilePath+'_split\\scaled')
		print('scal images.....')
		if scale == '4': 
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 1)
			thread1.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			File_x2=[]
			for path,useless,filenames in os.walk(scaledFilePath+'_split\\scaled\\'):
				for filename in filenames:
					File_x2.append(path+'\\'+filename)
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 2)
			thread1.start()		
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			for f in File_x2:
				os.system('del /q "'+f+'"')
			
			for files in os.walk(scaledFilePath+'_split\\scaled\\'):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(scaledFilePath+'_split\\scaled\\',fileNameAndExt),os.path.join(scaledFilePath+'_split\\scaled\\',fileName))
			
		else:
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 0)
			thread1.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
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
		
		
		if highQuality.lower() == 'y':
			gifQuality = False
		else:
			gifQuality = True
		
		print('Assembling Gif.....')
		assembleGif(scaledFilePath,TIME_GAP,gifQuality)
		print('Gif assembled')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal.lower() == 'y':
			os.system('del /q "'+inputPath+'"')
		
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')


#===================================Gif_MODE C======================================
def Gif_ModeC():
	print("====================== Gif_MODE C =====================")
	print("Type 'return' to return to the previous menu")
	print("Type 'over' to stop input more path, and input path must be a .gif file")
	print("Scaled images will be in the input-path \n")
	inputPathOver = True
	inputPathList = []
	gifQuality = False
	orginalFileNameAndFullname = {}
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\')
			
			if inputPath.lower() == 'return':
				return 1
			elif inputPath.lower() == 'over':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('error,input-path is invalid\n')
			else:
				inputPathError = False
		if inputPathOver == True:

			inputPathList.append(inputPath)
	
	 
	scale = input_scale()
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
		
	tileSize = input_tileSize()
		
	highQuality = input_highQuality()
		
	turnoff = input_turnoff()
	
	delorginal = input_delorginal()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	for inputPath in inputPathList:
		scaledFilePath = os.path.splitext(inputPath)[0]
			
		TIME_GAP=getDuration(inputPath)
		print('Split gif.....')
		splitGif(inputPath,scaledFilePath)
		
		oldfilenumber=FileCount(scaledFilePath+'_split')
		
		for files in os.walk(scaledFilePath+'_split'):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
				
	
		os.mkdir(scaledFilePath+'_split\\scaled')
		print('scal images.....')
		if scale == '4': 
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 1)
			thread1.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			File_x2=[]
			for path,useless,filenames in os.walk(scaledFilePath+'_split\\scaled\\'):
				for filename in filenames:
					File_x2.append(path+'\\'+filename)
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 2)
			thread1.start()		
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split\\scaled'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			if thread1.isAlive()==True:
				time.sleep(2)
				if thread1.isAlive()==True:
					stop_thread(thread1)
			for f in File_x2:
				os.system('del /q "'+f+'"')
			
			for files in os.walk(scaledFilePath+'_split\\scaled\\'):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(scaledFilePath+'_split\\scaled\\',fileNameAndExt),os.path.join(scaledFilePath+'_split\\scaled\\',fileName))
			
		else:
			thread1=PrograssBarThread(oldfilenumber,scaledFilePath+'_split\\scaled\\',scale,round_ = 0)
			thread1.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+scaledFilePath+'_split'+"\" -o \""+scaledFilePath+'_split\\scaled'+"\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
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
		
		
		if highQuality.lower() == 'y':
			gifQuality = False
		else:
			gifQuality = True
		
		print('Assembling Gif.....')
		assembleGif(scaledFilePath,TIME_GAP,gifQuality)
		print('Gif assembled')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal.lower() == 'y':
			os.system('del /q "'+inputPath+'"')
		
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')


#=============================== Video_MODE A ==============================
def Video_ModeA():
	print("================ Video_MODE A ===============")
	print("Type 'return' to return to the previous menu")
	print("Type 'over' to stop input more path, and input path must be a folder")
	print("Scaled files will be in the input-path \n")
	inputPathOver = True
	inputPathList = []
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\')
			
			if inputPath.lower() == 'over':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath.lower() == 'return':
				return 1
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('error,input-path is invalid\n')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
	
	 
	scale = input_scale()
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
		
	tileSize = input_tileSize()
		
	delorginal = input_delorginal()
		
	turnoff = input_turnoff()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	inputPathList_files = []
	for folders in inputPathList:
		for path,useless,fnames in os.walk(folders):
			for fname in fnames:
				inputPathList_files.append(path+'\\'+fname)
			break
	
	for inputPath in inputPathList_files:
		
		video2images(inputPath) #拆解视频
		
		frames_dir = os.path.dirname(inputPath)+'\\'+'frames'
		
		oldfilenumber=FileCount(frames_dir)
		
		os.mkdir(frames_dir+"\\scaled\\")
		
		if scale == '4':
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 1)
			thread2.start()
			
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
					
			File_x2=[]
			for path,useless,filenames in os.walk(frames_dir+"\\scaled"):
				for filename in filenames:
					File_x2.append(path+'\\'+filename)
			
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 2)
			thread2.start()
			
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			
			for f in File_x2:
				os.system('del /q "'+f+'"')
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
			
		else:
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 0)
			thread2.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
		
		images2video(os.path.splitext(inputPath)[0]+'.mp4')#合成视频	
		

				
		if os.path.splitext(inputPath)[1] != '.mp4':
			os.system('del /q "'+os.path.splitext(inputPath)[0]+'.mp4'+'"')
			
		if delorginal.lower() == 'y':
			os.system('del /q "'+inputPath+'"')	
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')

#================== Video_MODE B =============================
def Video_ModeB():
	print("================ Video_MODE B ===============")
	print("Type 'return' to return to the previous menu")
	print("Input path must be a folder")
	print("Scaled files will be in the input-path \n")
	inputPathOver = True
	inputPath_ = ''
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'

	inputPathError = True
	while inputPathError:
		inputPath_ = input('input-path: ')
		inputPath_=inputPath_.strip('"').strip('\\')
		
		if inputPath_.lower() == 'return':
			return 1
		elif inputPath_ == '' or os.path.exists(inputPath_) == False:
			print('error,input-path is invalid\n')
		else:
			inputPathError = False
	
	 
	scale = input_scale()
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
		
	tileSize = input_tileSize()
		
	delorginal = input_delorginal()
		
	turnoff = input_turnoff()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	inputPathList_files = []
	for path,useless,fnames in os.walk(inputPath_):
		for fname in fnames:
			inputPathList_files.append(path+'\\'+fname)

	
	for inputPath in inputPathList_files:
		
		video2images(inputPath) #拆解视频
		
		frames_dir = os.path.dirname(inputPath)+'\\'+'frames'
		
		oldfilenumber=FileCount(frames_dir)
		
		os.mkdir(frames_dir+"\\scaled\\")
		
		if scale == '4':
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 1)
			thread2.start()
			
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
					
			File_x2=[]
			for path,useless,filenames in os.walk(frames_dir+"\\scaled"):
				for filename in filenames:
					File_x2.append(path+'\\'+filename)
			
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 2)
			thread2.start()
			
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			
			for f in File_x2:
				os.system('del /q "'+f+'"')
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
			
		
		else:
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 0)
			thread2.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
		
		images2video(os.path.splitext(inputPath)[0]+'.mp4')#合成视频	
		

				
		if os.path.splitext(inputPath)[1] != '.mp4':
			os.system('del /q "'+os.path.splitext(inputPath)[0]+'.mp4'+'"')
			
		if delorginal.lower() == 'y':
			os.system('del /q "'+inputPath+'"')	
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')

#================== Video_MODE C =============================
def Video_ModeC():
	print("================ Video_MODE C ===============")
	print("Type 'return' to return to the previous menu")
	print("Type 'over' to stop input more path, and input path must be a video file")
	print("Scaled files will be in the input-path \n")
	inputPathOver = True
	inputPathList = []
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\')
			
			if inputPath.lower() == 'over':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath.lower() == 'return':
				return 1
			if inputPath == '' or os.path.exists(inputPath) == False:
				print('error,input-path is invalid\n')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
	
	scale = input_scale()
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input_noiseLevel()
		
	tileSize = input_tileSize()
		
	delorginal = input_delorginal()
		
	turnoff = input_turnoff()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()

	
	for inputPath in inputPathList:
		
		video2images(inputPath) #拆解视频
		
		frames_dir = os.path.dirname(inputPath)+'\\'+'frames'
		
		oldfilenumber=FileCount(frames_dir)
		
		os.mkdir(frames_dir+"\\scaled\\")
		
		if scale == '4':
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 1)
			thread2.start()
			
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
					
			File_x2=[]
			for path,useless,filenames in os.walk(frames_dir+"\\scaled"):
				for filename in filenames:
					File_x2.append(path+'\\'+filename)
			
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 2)
			thread2.start()
			
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\\scaled"+"\" -o \""+frames_dir+"\\scaled\""+" -n "+'0'+ " -s "+'2'+" -t "+tileSize+" -m "+models)
			
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			
			for f in File_x2:
				os.system('del /q "'+f+'"')
			
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
			
		
		else:
			thread2=PrograssBarThread(oldfilenumber,frames_dir+"\\scaled\\",scale,round_ = 0)
			thread2.start()
			print("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			os.system("waifu2x-ncnn-vulkan.exe -i \""+frames_dir+"\" -o \""+frames_dir+"\\scaled\""+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
			if thread2.isAlive()==True:
				time.sleep(2)
				if thread2.isAlive()==True:
					stop_thread(thread2)
			for files in os.walk(frames_dir+"\\scaled"):
				for fileNameAndExt in files[2]:
					fileName=os.path.splitext(fileNameAndExt)[0]
					os.rename(os.path.join(frames_dir+"\\scaled\\",fileNameAndExt),os.path.join(frames_dir+"\\scaled\\",fileName))
		
		images2video(os.path.splitext(inputPath)[0]+'.mp4')#合成视频	
		

				
		if os.path.splitext(inputPath)[1] != '.mp4':
			os.system('del /q "'+os.path.splitext(inputPath)[0]+'.mp4'+'"')
			
		if delorginal.lower() == 'y':
			os.system('del /q "'+inputPath+'"')	
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',Seconds2hms(round(total_time_end-total_time_start)),'\n')
	if turnoff.lower()=='y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')

#============================= Compress_ModeA ===============================
def Compress_ModeA():
	print("================= Compress_ModeA ================")
	print("Type 'return' to return to the previous menu")
	print("Type 'over' to stop input more path, and input path must be a folder")
	print("Compressed images will be in the input-path \n")
	inputPathOver = True
	inputPathList = []
	JpgQuality=90

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\')
			
			if inputPath.lower() == 'return':
				return 1
			elif inputPath.lower() == 'over':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('error,input-path is invalid\n')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
	
	delorginal = input_delorginal()
	
	
	
	print('--------------------------------------------')
	
	
	total_time_start=time.time()
	
	inputPathList_files = []
	for folders in inputPathList:
		for path,useless,fnames in os.walk(folders):
			for fname in fnames:
				inputPathList_files.append(path+'\\'+fname)
			break

	TotalFileNum = len(inputPathList_files)
	FinishedFileNum = 1
	saved_size_total=0
	
	for inputPath in inputPathList_files:
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
			print('Failed to compress '+inputPath)
		else:
			saved_size_total = saved_size_total+saved_size
			saved_size_str = str(saved_size)+'KB'
			print('Compressed size:'+compressed_size)
			print('Save '+saved_size_str+' !')
			print('')	
			if delorginal.lower() == 'y':
				os.system('del /q "'+inputPath+'"')
			
		FinishedFileNum = FinishedFileNum+1
		print('--------------------------------------------')
		
			
	total_time_end=time.time()
	
	print('\nTotal time cost: ',total_time_end-total_time_start,'s\n')
	print('\nTotal saved space: ',saved_size_total,'KB\n')
	input('\nPress any key to return to the menu')

#============================= Compress_ModeB ===============================
def Compress_ModeB():
	print("================= Compress_ModeB ================")
	print("Type 'return' to return to the previous menu")
	print("Input path must be a folder")
	print("Compressed images will be in the input-path \n")
	inputPathOver = True
	JpgQuality=90

	while True:
		inputPath = input('input-path: ')
		inputPath =inputPath.strip('"').strip('\\')
		if inputPath.lower() == 'return':
			return 1
		elif inputPath == '' or os.path.exists(inputPath) == False:
			print('error,input-path is invalid\n')
		else:
			break
	
	delorginal = input_delorginal()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()
	
	inputPathList_files = []
	for path,useless,fnames in os.walk(inputPath):
		for fname in fnames:
			inputPathList_files.append(path+'\\'+fname)
	
	TotalFileNum = len(inputPathList_files)
	FinishedFileNum = 1
	saved_size_total=0
	for inputPath in inputPathList_files:
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
			print('Failed to compress '+inputPath)
		else:
			saved_size_total = saved_size_total+saved_size
			saved_size_str = str(saved_size)+'KB'
			print('Compressed size:'+compressed_size)
			print('Save '+saved_size_str+' !')
			print('')	
			if delorginal.lower() == 'y':
				os.system('del /q "'+inputPath+'"')
			
		FinishedFileNum = FinishedFileNum+1
		print('--------------------------------------------')
		
			
	total_time_end=time.time()
	
	print('\nTotal time cost: ',total_time_end-total_time_start,'s\n')
	print('\nTotal saved space: ',saved_size_total,'KB\n')
	input('\nPress any key to return to the menu')


#============================= Compress_ModeC ===============================
def Compress_ModeC():
	print("================= Compress_ModeC ================")
	print("Type 'return' to return to the previous menu")
	print("Type 'over' to stop input more path, and input path must be a image")
	print("Compressed images will be in the input-path \n")
	inputPathOver = True
	inputPathList = []
	JpgQuality=90

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			inputPath=inputPath.strip('"').strip('\\')
			
			if inputPath.lower() == 'return':
				return 1
			elif inputPath.lower() == 'over':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == '' or os.path.exists(inputPath) == False:
				print('error,input-path is invalid\n')
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPathList.append(inputPath)
	
	delorginal = input_delorginal()
		
	print('--------------------------------------------')
	
	total_time_start=time.time()

	TotalFileNum = len(inputPathList)
	FinishedFileNum = 1
	saved_size_total=0
	for inputPath in inputPathList:
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
			print('Failed to compress '+inputPath)
		else:
			saved_size_total = saved_size_total+saved_size
			saved_size_str = str(saved_size)+'KB'
			print('Compressed size:'+compressed_size)
			print('Save '+saved_size_str+' !')
			print('')	
			if delorginal.lower() == 'y':
				os.system('del /q "'+inputPath+'"')
			
		FinishedFileNum = FinishedFileNum+1
		print('--------------------------------------------')
		
			
	total_time_end=time.time()
	
	print('\nTotal time cost: ',total_time_end-total_time_start,'s\n')
	print('\nTotal saved space: ',saved_size_total,'KB\n')
	input('\nPress any key to return to the menu')

#=============================Prograss bar==========================
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
	if OldFileNum != 0:
		NewFileNum=0
		time_start = time.time()
		time.sleep(2)
		print('\n')
		while NewFileNum <= OldFileNum and os.path.exists(ScalePath):
			NewFileNum=0
			for files in os.walk(ScalePath):
				for singleFile in files[2]:
					if str(os.path.splitext(singleFile)[1]) in ['.jpg','.png','.jpeg','.tif','.tiff','.bmp','.tga']:
						NewFileNum=NewFileNum+1
			if round_ == 2:
				NewFileNum=NewFileNum-OldFileNum
				
			if NewFileNum==0:
				Percent = 0
				BarStr = ''
				for x in range(0,int(100/3)):
					BarStr = BarStr + '□'
			else:
				Percent = int(100*(NewFileNum/OldFileNum))
				BarStr = ''
				for x in range(0,int(Percent/3)):
					BarStr = BarStr + '■'
				for x in range(0,int(100/3)-int(Percent/3)):
					BarStr = BarStr + '□'
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
					PrograssBar = "\r"+"Round = "+str(round_)+"  Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): ["+BarStr+"]"+str(Percent)+"%  ["+'Time cost: '+timeCost_str+" ]"+"  "+"["+'ETA: '+Seconds2hms(Eta)+" ]"+'   '
				else:
					PrograssBar = "\r"+"Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): ["+BarStr+"]"+str(Percent)+"%  ["+'Time cost: '+timeCost_str+" ]"+"  "+"["+'ETA: '+Seconds2hms(Eta)+" ]"+'   '
				sys.stdout.write(PrograssBar)
				sys.stdout.flush()
					
				
			else:
				if scale == '4':
					PrograssBar = "\r"+"Round = "+str(round_)+"  Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): ["+BarStr+"]"+str(Percent)+"%  ["+'Time cost: '+timeCost_str+" ]"+'          '
				else:
					PrograssBar = "\r"+"Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): ["+BarStr+"]"+str(Percent)+"%  ["+'Time cost: '+timeCost_str+" ]"+'          '
				sys.stdout.write(PrograssBar)
				sys.stdout.flush()
				
			time.sleep(1)
			
#================Clock==================
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
			
#================Multithread==================
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

#=================DelOriginalFiles================
def DelOrgFiles(inputPath):
	Exts=["png","jpg","jpeg","tif","tiff","bmp","tga","gif"]
	for ext in Exts:
		os.system('del /q "'+inputPath+'\\*.'+ext+'"')
		os.system('del /q "'+inputPath+'\\*.'+ext.upper()+'"')
		os.system('del /q "'+inputPath+'\\*.'+ext.capitalize()+'"')
	
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
	os.mkdir(scaledFilePath+'_split')
	try:
	  while True:
	    current = im.tell()
	    im.save(pngDir+'/'+str(current)+'.png')
	    im.seek(current+1)
	except EOFError:
	    pass
	
def assembleGif(scaledFilePath,TIME_GAP,gifQuality):
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
	imageio.mimsave(gif_name, frames, 'GIF', duration = TIME_GAP,subrectangles = gifQuality)
	
	
#====================== Video ==============================
def video2images(inputpath):
	video_dir = os.path.dirname(inputpath)+'\\'
	video_path_filename = os.path.splitext(inputpath)[0]
	video_ext = os.path.splitext(inputpath)[1]
	if video_ext != '.mp4':
		os.system('ffmpeg -i "'+inputpath+'" "'+video_path_filename+'.mp4"')
	frames_dir = video_dir+'frames\\'
	
	cap = cv2.VideoCapture(inputpath)
	frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	frame_figures = len(str(frame_counter))
	
	if os.path.exists(frames_dir) == False:
		os.mkdir(frames_dir)
	
	#os.system('ffmpeg -i "'+inputpath+'" -ss 00:00 -t 00:02 "'+frames_dir+'%0'+str(frame_figures)+'d.png"')
	#os.system('ffmpeg -i "'+inputpath+'" -ss 00:00 -t 00:02 "'+video_dir+'audio.mp3"')

	os.system('ffmpeg -i "'+video_path_filename+'.mp4'+'" "'+frames_dir+'%0'+str(frame_figures)+'d.png"')
	os.system('ffmpeg -i "'+video_path_filename+'.mp4'+'" "'+video_dir+'audio.mp3"')

def images2video(inputpath):
	video_path_filename = os.path.splitext(inputpath)[0]
	video_ext = os.path.splitext(inputpath)[1]
	video_dir = os.path.dirname(inputpath)+'\\'
	frames_scaled_dir = video_dir+'frames\\scaled\\'
	cap = cv2.VideoCapture(inputpath)
	fps = int(round(cap.get(cv2.CAP_PROP_FPS)))
	frame_counter = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
	frame_figures = len(str(frame_counter))
	os.system('ffmpeg -f image2 -framerate '+str(fps)+' -i "'+frames_scaled_dir+'%0'+str(frame_figures)+'d.png" -i "'+video_dir+'audio.mp3" -r '+str(fps)+' -pix_fmt yuv420p "'+video_path_filename+'_waifu2x'+video_ext+'"')

	os.system('del /q "'+video_dir+'audio.mp3"')

	os.system('rd /s/q "'+video_dir+'frames'+'"')
	
#====================== input ============================
def input_scale():
	settings_values = ReadSettings()
	default_value = settings_values['scale']

	while True:
		scale = input('scale(1/2/4, default='+default_value+'): ')
		if scale in ['1','2','4','']:
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
	default_value = settings_values['tileSize']
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
			print('wrong input, pls input again')
		
	if tileSize == '':
		tileSize = default_value
	return tileSize
	
def input_noiseLevel():
	settings_values = ReadSettings()
	default_value = settings_values['noiseLevel']
	while True:
		noiseLevel = input('Noise-level(-1/0/1/2/3, default='+default_value+'): ')
		if noiseLevel in ['-1','0','1','2','3','']:
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
		if delorginal in ['y','n','Y','N','']:
			break
		else:
			print('wrong input, pls input again')
	
	if delorginal == '':
		delorginal = default_value
	return delorginal
	
def input_turnoff():
	while True:
		turnoff = input('turn off computer when finished?(y/n, default=n): ')
		if turnoff in ['y','n','Y','N','']:
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
		if saveAsJPG in ['y','n','Y','N','']:
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
		if Compress in ['y','n','Y','N','']:
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
		highQuality = input('High quality gif?(y/n, default='+default_value+'): ')
		if highQuality in ['y','n','Y','N','']:
			break
		else:
			print('wrong input, pls input again')
	
	if highQuality == '':
		highQuality = default_value
		
	return highQuality
	
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
def checkUpdate(Version_current):
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
			input('press any key to return')
	except BaseException:
		os.system('cls')
		input('Failed to establish connection, pls check your internet, press any key to return....')
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
	'noise3_scale2.0x_model.bin', 'noise3_scale2.0x_model.param', 'scale2.0x_model.bin', 'scale2.0x_model.param']
	
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
		print('Settings')
		print('-----------------------------------------------------------------------------')
		print(' 1: Check for updates at startup. Current value: '+settings_values['CheckUpdate']+'\n')
		print(' 2: Default value of "scale". Current value: '+settings_values['scale']+'\n')
		print(' 3: Default value of "tileSize". Current value: '+settings_values['tileSize']+'\n')
		print(' 4: Default value of "noiseLevel". Current value: '+settings_values['noiseLevel']+'\n')
		print(' 5: Save the result image as .jpg file? Current default value: '+settings_values['saveAsJPG']+'\n')
		print(' 6: Compress the result image?(when saved as .jpg) Current default value: '+settings_values['Compress']+'\n')
		print(' 7: Delete original files when finished? Current default value: '+settings_values['delorginal']+'\n')
		print(' 8: Save high quality gif? Current default value: '+settings_values['highQuality']+'\n')
		print(' 9: Reset error log.\n')
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
				value_ = input('New value: ')
				if value_.isdigit():
					if int(value_) > 0:
						break
				else:
					print('invalid value, pls input again')
					
			settings_values['tileSize']=str(int(value_))
			with open('waifu2x-extension-setting','w+') as f:
				json.dump(settings_values,f)
				
			os.system('cls')
			
		elif mode == "4":
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
			
		elif mode == "5":
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
			
		elif mode == "6":
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
			
		elif mode == "7":
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
			
		elif mode == "8":
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
			
		elif mode == "9":
			os.system('cls')
			
			with open('Error_Log_Waifu2x-Extension.log','w+') as f:
				f.write('')
				
			with open('Error_Log_Waifu2x-Extension.log','a+') as f:
				timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
				f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Error log reseted by user.\n')
			
			input('Error log reseted, press any key to return.')
			
			os.system('cls')
			
		elif mode == "r":
			break
		else:
			os.system('cls')
			os.system('color 0c')
			input('Error : wrong input,pls press any key to return')
			os.system('color 0a')
			os.system('cls')

def ReadSettings():
	current_dir = os.path.dirname(os.path.abspath(__file__))
	settingPath = current_dir+'\\'+'waifu2x-extension-setting'
	if os.path.exists(settingPath) == False:
		default_values = {'CheckUpdate':'y','scale':'2','tileSize':'200',
						'noiseLevel':'2','saveAsJPG':'y',
						'Compress':'n','delorginal':'n','highQuality':'y'}
		with open('waifu2x-extension-setting','w+') as f:
			json.dump(default_values,f)
		return default_values
	else:
		settings_values = {}
		with open('waifu2x-extension-setting','r+') as f:
			settings_values = json.load(f)
		return settings_values

#=================  Init  ================

def init():
	os.system('title = Waifu2x-Extension by Aaron Feng')
	os.system('color 0b')
	os.system('mode con cols=150 lines=35')
	
	sys.stderr = Logger('Error_Log_Waifu2x-Extension.log', sys.stderr)
	with open('Error_Log_Waifu2x-Extension.log','a+') as f:
		timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		f.write('\n--------------------------------\n'+timeStr+'\n--------------------------------\n'+'Start running\n')
		
	settings_values = ReadSettings()
	
	if settings_values['CheckUpdate'] == 'y':
		checkUpdate_start(Version_current)
		
	if VerifyFiles() == 'verified':
		os.system('cls')
		ChooseFormat(Version_current)
	else:
		os.system('cls')
		os.system('color 0c')
		print('-'*40)
		download_latest = input('Some files are missing. Do you wanna download the latest package?(y/n): ')
		if download_latest.lower() == 'y':
			webbrowser.open('https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest')
		os.system('cls')
		input('Press any key to exit.')
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

#============================= Error_Log ====================================

def Error_Log():
	if os.path.exists('Error_Log_Waifu2x-Extension.log') == True:
		print('You can reset error log in the setting menu.')
		print('\033[1;31;40m'+'Close the notepad to continue.'+'\033[0m')
		os.system('notepad Error_Log_Waifu2x-Extension.log')
	else:
		print('Error : error log file is missing.')
		input('Press any key to return.')
		
#======================== Start ========================
init()

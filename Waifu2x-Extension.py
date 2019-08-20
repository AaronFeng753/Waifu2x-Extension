print('Loading.....')

import os
import time
import threading
import sys
import inspect
import ctypes
from PIL import Image
import imageio
import cv2

def ChooseFormat():
	while True:
		print('Waifu2x-Extension v1.11 2019/8/20')
		print('Github: https://github.com/AaronFeng753/Waifu2x-Extension')
		print('---------------------------')
		print('Mode I : Scale image.')
		print('Mode G : Scale gif.')
		print('Mode V : Scale video. (Experimental)')
		print('E : Exit.')
		print('---------------------------')
		mode = input('(i/g/v/e): ')
		mode = mode.lower()
		if mode == "i":
			os.system('cls')
			Image_()
			os.system('cls')
		elif mode == "g":
			os.system('cls')
			Gif_()
			os.system('cls')
		elif mode == "v":
			os.system('cls')
			Video_()
			os.system('cls')
		elif mode == "e":
			os.system('cls')
			return 0
		else:
			os.system('cls')
			input('Error : wrong input,pls press any key to return')
			os.system('cls')

def Image_():
	while True:
		print('Image')
		print('-----------------------------------------------------------------------------')
		print('Mode A: input folders one by one and scaled all images in them.')
		print('Mode B: input one folder and scaled all images in it and it\'s sub-folders.')
		print('Mode C: input images one by one.')
		print('R : return to the main menu')
		print('-----------------------------------------------------------------------------')
		mode = input('(a/b/c/r): ')
		if mode.lower() == "a":
			os.system('cls')
			Image_ModeA()
			os.system('cls')
		elif mode.lower() == "b":
			os.system('cls')
			Image_ModeB()
			os.system('cls')
		elif mode.lower() == "c":
			os.system('cls')
			Image_ModeC()
			os.system('cls')
		elif mode.lower() == "r":
			break
		else:
			os.system('cls')
			input('Error : wrong input,pls press any key to return')
			os.system('cls')
			
def Gif_():
	while True:
		print('GIF')
		print('---------------------------------------------------------------------------')
		print('Mode A: input folders one by one')
		print('Mode B: input one folder and scaled all gif in it and it\'s sub-folders')
		print('Mode C: input gif one by one')
		print('R : return to the main menu')
		print('---------------------------------------------------------------------------')
		mode = input('(a/b/c/r): ')
		if mode.lower() == "a":
			os.system('cls')
			Gif_ModeA()
			os.system('cls')
		elif mode.lower() == "b":
			os.system('cls')
			Gif_ModeB()
			os.system('cls')
		elif mode.lower() == "c":
			os.system('cls')
			Gif_ModeC()
			os.system('cls')
		elif mode.lower() == "r":
			break
		else:
			os.system('cls')
			input('Error : wrong input,pls press any key to return')
			os.system('cls')
			
def Video_():
	while True:
		print('Video (Experimental)')
		print('---------------------------------------------------------------------------')
		print('Mode A: input folders one by one')
		print('Mode B: input one folder and scaled all video in it and it\'s sub-folders')
		print('Mode C: input video one by one')
		print('R : return to the main menu')
		print('---------------------------------------------------------------------------')
		mode = input('(a/b/c/r): ')
		if mode.lower() == "a":
			os.system('cls')
			Video_ModeA()
			os.system('cls')
		elif mode.lower() == "b":
			os.system('cls')
			Video_ModeB()
			os.system('cls')
		elif mode.lower() == "c":
			os.system('cls')
			Video_ModeC()
			os.system('cls')
		elif mode.lower() == "r":
			break
		else:
			os.system('cls')
			input('Error : wrong input,pls press any key to return')
			os.system('cls')
		
#=================Image_MODE A================
def Image_ModeA():
	print("=================Image_MODE A================")
	print("Type 'return' to return to the previous menu")
	print("Type 'over' to stop input more path, and input path must be a folder, not a file")
	print("Scaled images will be in the input-path \n")
	fileTimeCost = {}
	inputPathOver = True
	inputPathList = []
	orginalFileNameAndFullname = {}
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'
	
	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			if inputPath == '':
				print('error,input-path is invalid\n')
			elif inputPath == 'return':
				return 1
			elif inputPath == 'over':
				inputPathOver = False
				inputPathError = False
				break
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPath=inputPath.strip('"')
			inputPathList.append(inputPath)
	
	scale = input('scale(1/2/4, default=2): ')

	if scale == '':
		scale = '2'
	elif scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=2): ')
	
	if noiseLevel == '':
		noiseLevel = '2'
		
	tileSize = input('tile size(>=32, default=200): ')
	
	if tileSize == '':
		tileSize = '200'
		
	saveAsJPG = input('Save as .jpg? (y/n, default=y): ')
	
	if saveAsJPG == '':
		saveAsJPG = 'y'
	
	if saveAsJPG == 'y':
		Compress = input('Compress the .jpg file?(Almost lossless) (y/n, default=n): ')
		if Compress == 'y' or Compress == 'Y':
			JpgQuality=90
		
	turnoff = input('turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
		
	delorginal = input('Delete original files?(y/n, default=n): ')
	
	if delorginal == '':
		delorginal = 'n'
		
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
			
		if saveAsJPG == 'y' or saveAsJPG == 'Y':
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
				if saveAsJPG == 'y' or saveAsJPG == 'Y':
					os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',originalName+"_Waifu2x.jpg"))
				else:
					os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',originalName+"_Waifu2x.png"))
		
		orginalFileNameAndFullname = {}
		
		print('')
		if delorginal == 'y' or delorginal == 'Y':
			DelOrgFiles(inputPath)
		os.system("xcopy /s /i /q /y \""+inputPath+"\\scaled\\*.*\" \""+inputPath+"\"")
		os.system("rd /s/q \""+inputPath+"\\scaled\"")
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')
	
#=================Image_MODE B================
def Image_ModeB():
	print("=================Image_MODE B================")
	print("Type 'return' to return to the previous menu")
	print("Input path must be a folder, not a file")
	print("Scaled images will be in the input-path \n")
	fileTimeCost = {}
	inputPathList = []
	orginalFileNameAndFullname = {}
	inputPathError = True
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathError:
		inputPath = input('input-path: ')
		if inputPath == '':
			print('error,input-path is invalid\n')
		elif inputPath == 'return':
			return 1
		else:
			inputPathError = False
	inputPath=inputPath.strip('"')
	
	scale = input('scale(1/2/4, default=2): ')

	if scale == '':
		scale = '2'
	elif scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=2): ')
	
	if noiseLevel == '':
		noiseLevel = '2'
		
	tileSize = input('tile size(>=32, default=200): ')
	
	if tileSize == '':
		tileSize = '200'
		
	saveAsJPG = input('Save as .jpg? (y/n, default=y): ')
	
	if saveAsJPG == '':
		saveAsJPG = 'y'
	
	if saveAsJPG == 'y':
		Compress = input('Compress the .jpg file?(Almost lossless) (y/n, default=n): ')
		if Compress == 'y' or Compress == 'Y':
			JpgQuality=90
		
	turnoff = input('turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
		
	delorginal = input('Delete original files?(y/n, default=n): ')
	
	if delorginal == '':
		delorginal = 'n'
		
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
		
		if saveAsJPG == 'y' or saveAsJPG == 'Y':
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
				if saveAsJPG == 'y' or saveAsJPG == 'Y':
					os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',originalName+"_Waifu2x.jpg"))
				else:
					os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',originalName+"_Waifu2x.png"))
		orginalFileNameAndFullname = {}	
		
		
		print('')
		if delorginal == 'y' or delorginal == 'Y':
			DelOrgFiles(inputPath)
		os.system("xcopy /s /i /q /y \""+inputPath+"\\scaled\\*.*\" \""+inputPath+"\"")
		os.system("rd /s/q \""+inputPath+"\\scaled\"")
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')
	
#=================Image_MODE C================
def Image_ModeC():
	print("=================Image_MODE C================")
	print("Type 'return' to return to the previous menu")
	print("Type 'over' to stop input more path, and input path must be a file")
	print("Scaled images will be in the input-path \n")
	fileTimeCost = {}
	inputPathOver = True
	inputPathList = []
	JpgQuality=100
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathOver:
		inputPathError = True
		while inputPathError:
			inputPath = input('input-path: ')
			if inputPath == '':
				print('error,input-path is invalid\n')
			elif inputPath == 'return':
				return 1
			elif inputPath == 'over':
				inputPathOver = False
				inputPathError = False
				break
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPath=inputPath.strip('"')
			inputPathList.append(inputPath)
	
	scale = input('Scale(1/2/4, default=2): ')

	if scale == '':
		scale = '2'
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('Noise-level(-1/0/1/2/3, default=2): ')
	
	if noiseLevel == '':
		noiseLevel = '2'
		
	tileSize = input('Tile size(>=32, default=200): ')
	
	if tileSize == '':
		tileSize = '200'
		
	saveAsJPG = input('Save as .jpg? (y/n, default=y): ')
	
	if saveAsJPG == '':
		saveAsJPG = 'y'
		
	if saveAsJPG == 'y':
		Compress = input('Compress the .jpg file?(Almost lossless) (y/n, default=n): ')
		if Compress == 'y' or Compress == 'Y':
			JpgQuality=90
		
	turnoff = input('Turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
	
	
	delorginal = input('Delete original files?(y/n, default=n): ')
	
	if delorginal == '':
		delorginal = 'n'
		
	print('--------------------------------------------')
	
	total_time_start=time.time()

	
	for inputPath in inputPathList:
		scaledFilePath = os.path.splitext(inputPath)[0]
		fileNameAndExt=str(os.path.basename(inputPath))
		
		thread1=ClockThread()
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
		if delorginal == 'y' or delorginal == 'Y':
			os.system('del /q "'+inputPath+'"')
			
		if saveAsJPG == 'y' or saveAsJPG == 'Y':
			print('\n Convert image..... \n')
			imageio.imwrite(scaledFilePath+"_Waifu2x.jpg", imageio.imread(scaledFilePath+"_Waifu2x.png"), 'JPG', quality = JpgQuality)
			os.system('del /q "'+scaledFilePath+"_Waifu2x.png"+'"')
		
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')


#=======================Gif_MODE A=============================
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
			if inputPath == '':
				print('error,input-path is invalid\n')
			elif inputPath == 'return':
				return 1
			elif inputPath == 'over':
				inputPathOver = False
				inputPathError = False
				break
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPath=inputPath.strip('"')
			inputPathList.append(inputPath)
	
	scale = input('scale(1/2/4, default=2): ')

	if scale == '':
		scale = '2'
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=2): ')
	
	if noiseLevel == '':
		noiseLevel = '2'
		
	tileSize = input('tile size(>=32, default=200): ')
	
	if tileSize == '':
		tileSize = '200'
		
	highQuality = input('High quality gif?(y/n, default=y): ')
	
	if highQuality == '':
		highQuality = 'y'
		
	turnoff = input('turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
	
	delorginal = input('Delete original files?(y/n, default=n): ')
	
	if delorginal == '':
		delorginal = 'n'
		
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
		
		
		if highQuality == 'y' or highQuality == 'Y':
			gifQuality = False
		else:
			gifQuality = True
		
		print('Assembling Gif.....')
		assembleGif(scaledFilePath,TIME_GAP,gifQuality)
		print('Gif assembled')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal == 'y' or delorginal == 'Y':
			os.system('del /q "'+inputPath+'"')
		
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')

#=======================Gif_MODE B=============================
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
		if inputPath_ == '':
			print('error,input-path is invalid\n')
		elif inputPath_ == 'return':
			return 1
		else:
			inputPath_=inputPath_.strip('"')
			inputPathError = False
	
	scale = input('scale(1/2/4, default=2): ')

	if scale == '':
		scale = '2'
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=2): ')
	
	if noiseLevel == '':
		noiseLevel = '2'
		
	tileSize = input('tile size(>=32, default=200): ')
	
	if tileSize == '':
		tileSize = '200'
		
	highQuality = input('High quality gif?(y/n, default=y): ')
	
	if highQuality == '':
		highQuality = 'y'
		
	turnoff = input('turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
	
	delorginal = input('Delete original files?(y/n, default=n): ')
	
	if delorginal == '':
		delorginal = 'n'
		
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
		
		
		if highQuality == 'y' or highQuality == 'Y':
			gifQuality = False
		else:
			gifQuality = True
		
		print('Assembling Gif.....')
		assembleGif(scaledFilePath,TIME_GAP,gifQuality)
		print('Gif assembled')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal == 'y' or delorginal == 'Y':
			os.system('del /q "'+inputPath+'"')
		
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')


#=======================Gif_MODE C=============================
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
			if inputPath == '':
				print('error,input-path is invalid\n')
			elif inputPath == 'return':
				return 1
			elif inputPath == 'over':
				inputPathOver = False
				inputPathError = False
				break
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPath=inputPath.strip('"')
			inputPathList.append(inputPath)
	
	scale = input('scale(1/2/4, default=2): ')

	if scale == '':
		scale = '2'
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=2): ')
	
	if noiseLevel == '':
		noiseLevel = '2'
		
	tileSize = input('tile size(>=32, default=200): ')
	
	if tileSize == '':
		tileSize = '200'
		
	highQuality = input('High quality gif?(y/n, default=y): ')
	
	if highQuality == '':
		highQuality = 'y'
		
	turnoff = input('turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
	
	delorginal = input('Delete original files?(y/n, default=n): ')
	
	if delorginal == '':
		delorginal = 'n'
		
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
		
		
		if highQuality == 'y' or highQuality == 'Y':
			gifQuality = False
		else:
			gifQuality = True
		
		print('Assembling Gif.....')
		assembleGif(scaledFilePath,TIME_GAP,gifQuality)
		print('Gif assembled')
		
		os.system("rd /s/q \""+scaledFilePath+'_split"')
		
		if delorginal == 'y' or delorginal == 'Y':
			os.system('del /q "'+inputPath+'"')
		
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')


#================== Video_MODE A =============================
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
			if inputPath == '':
				print('error,input-path is invalid\n')
			elif inputPath == 'over':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == 'return':
				return 1
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPath=inputPath.strip('"')
			inputPathList.append(inputPath)
	
	scale = input('Scale(1/2/4, default=2): ')

	if scale == '':
		scale = '2'
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('Noise-level(-1/0/1/2/3, default=2): ')
	
	if noiseLevel == '':
		noiseLevel = '2'
		
	tileSize = input('Tile size(>=32, default=200): ')
	
	if tileSize == '':
		tileSize = '200'
		
	delorginal = input('Delete original files?(y/n, default=n): ')
	
	if delorginal == '':
		delorginal = 'n'
		
	turnoff = input('Turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
		
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
			
		if delorginal == 'y' or delorginal == 'Y':
			os.system('del /q "'+inputPath+'"')	
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
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
		if inputPath_ == '':
			print('error,input-path is invalid\n')
		if inputPath_ == 'return':
			return 1
		else:
			inputPath_=inputPath_.strip('"')
			inputPathError = False
	
	scale = input('Scale(1/2/4, default=2): ')

	if scale == '':
		scale = '2'
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('Noise-level(-1/0/1/2/3, default=2): ')
	
	if noiseLevel == '':
		noiseLevel = '2'
		
	tileSize = input('Tile size(>=32, default=200): ')
	
	if tileSize == '':
		tileSize = '200'
		
	delorginal = input('Delete original files?(y/n, default=n): ')
	
	if delorginal == '':
		delorginal = 'n'
		
	turnoff = input('Turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
		
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
			
		if delorginal == 'y' or delorginal == 'Y':
			os.system('del /q "'+inputPath+'"')	
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
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
			if inputPath == '':
				print('error,input-path is invalid\n')
			elif inputPath == 'over':
				inputPathOver = False
				inputPathError = False
				break
			elif inputPath == 'return':
				return 1
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPath=inputPath.strip('"')
			inputPathList.append(inputPath)
	
	scale = input('Scale(1/2/4, default=2): ')

	if scale == '':
		scale = '2'
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('Noise-level(-1/0/1/2/3, default=2): ')
	
	if noiseLevel == '':
		noiseLevel = '2'
		
	tileSize = input('Tile size(>=32, default=200): ')
	
	if tileSize == '':
		tileSize = '200'
		
	delorginal = input('Delete original files?(y/n, default=n): ')
	
	if delorginal == '':
		delorginal = 'n'
		
	turnoff = input('Turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
		
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
			
		if delorginal == 'y' or delorginal == 'Y':
			os.system('del /q "'+inputPath+'"')	
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')

#================Prograss bar==================
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
			else:
				Percent = int(100*(NewFileNum/OldFileNum))
				BarStr = ''
				for x in range(0,int(Percent/3)):
					BarStr = BarStr + '>'
			time_now = time.time()
			timeCost_str = str(int(time_now-time_start)) + 's'
			if NewFileNum > 0:
				if NewFileNum > NewFileNum_Old:
					avgTimeCost = int(time_now-time_start)/NewFileNum
					Eta = int(avgTimeCost*(OldFileNum-NewFileNum))
					NewFileNum_Old = NewFileNum
			if Eta != 0:
				if Eta > 1:
					Eta=Eta-1
				if scale == '4':
					PrograssBar = "\r"+"Round = "+str(round_)+"  Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): ["+BarStr+"]"+str(Percent)+"%  ["+'Time cost: '+timeCost_str+"]"+"  "+"["+'ETA: '+str(Eta)+"s]"+'   '
				else:
					PrograssBar = "\r"+"Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): ["+BarStr+"]"+str(Percent)+"%  ["+'Time cost: '+timeCost_str+"]"+"  "+"["+'ETA: '+str(Eta)+"s]"+'   '
				sys.stdout.write(PrograssBar)
				sys.stdout.flush()
					
				
			else:
				if scale == '4':
					PrograssBar = "\r"+"Round = "+str(round_)+"  Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): ["+BarStr+"]"+str(Percent)+"%  ["+'Time cost: '+timeCost_str+"]"+'          '
				else:
					PrograssBar = "\r"+"Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): ["+BarStr+"]"+str(Percent)+"%  ["+'Time cost: '+timeCost_str+"]"+'          '
				sys.stdout.write(PrograssBar)
				sys.stdout.flush()
				
			time.sleep(1)
			
#================Clock==================
class ClockThread (threading.Thread):
    def run(self):
        Clock()

def Clock():
	startTime = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
	image_time_start = time.time()
	time.sleep(2)
	while True:
		image_time_now = time.time()
		timeStr = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
		timeCost = str(int(image_time_now-image_time_start)) + 's'
		clockStr = "\r["+startTime+"]--->["+timeStr+"] = "+timeCost
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

	os.system('ffmpeg -i "'+inputpath+'" "'+frames_dir+'%0'+str(frame_figures)+'d.png"')
	os.system('ffmpeg -i "'+inputpath+'" "'+video_dir+'audio.mp3"')

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
	
#=================Start================
os.system('cls')
ChooseFormat()

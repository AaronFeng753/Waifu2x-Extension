import os
import time
import threading
import random
import sys
import inspect
import ctypes

def ChooseMode():
	while True:
		print('Waifu2x-Batching process extension v0.46')
		print('----------------------------------------------')
		print('Mode A: input folders one by one')
		print('Mode B: input one folder and scaled all images in it and it\'s sub-folders')
		print('Mode C: input images one by one')
		print('Delete space: input one folder and delete all blank spaces in it\'s sub-folders\'name')
		print('----------------------------------------------')
		mode = input('(a/b/c/d) : ')
		if mode.lower() == "a":
			os.system('cls')
			ModeA()
			os.system('cls')
		elif mode.lower() == "b":
			os.system('cls')
			ModeB()
			os.system('cls')
		elif mode.lower() == "c":
			os.system('cls')
			ModeC()
			os.system('cls')
		elif mode.lower() == "d":
			os.system('cls')
			DeleteSpaces()
			os.system('cls')
		else:
			os.system('cls')
			input('Error : wrong input,pls press any key to return')
			os.system('cls')
		
#=================MODE A================
def ModeA():
	print("=================MODE A================")
	print("Type 'over' to stop input more path, and input path must be a folder, not a file")
	print("No blank space in the input-path!!That could cause error!!")
	print("Scaled images will be in the input-path \n")
	fileTimeCost = {}
	inputPathOver = True
	inputPathList = []
	orginalFileNameAndFullname = {}
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
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPath=inputPath.strip('"')
			inputPathList.append(inputPath)
	
	scale = input('scale(1/2, default=2): ')

	if scale == '':
		scale = '2'
	elif scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=0): ')
	
	if noiseLevel == '':
		noiseLevel = '0'
		
	tileSize = input('tile size(>=32, default=400): ')
	
	if tileSize == '':
		tileSize = '400'
		
	turnoff = input('turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
	
	total_time_start=time.time()
	
	for inputPath in inputPathList:
		
		oldfilenumber=FileCount(inputPath)
		scalepath = inputPath+"\\scaled\\"
		thread1=PrograssBarThread(oldfilenumber,scalepath)
		thread1.start()
		
		for files in os.walk(inputPath):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
				
		folder_time_start=time.time()
		os.mkdir(inputPath+"\\scaled\\")
		
		print("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+"\\scaled\\"+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
		os.system("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+"\\scaled\\"+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
		
		folder_time_end=time.time()
		
		if thread1.isAlive()==True:
			stop_thread(thread1)
			
		print('\ntime cost of '+inputPath+':  ',folder_time_end-folder_time_start,'s\n')
		
		for files in os.walk(inputPath+'\\scaled\\'):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				originalName=list(orginalFileNameAndFullname.keys())[list(orginalFileNameAndFullname.values()).index(fileName)]
				os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',originalName+"_Waifu2x.png"))
		orginalFileNameAndFullname = {}	
		os.system("xcopy /s /i /q /y "+inputPath+"\\scaled\\*.* "+inputPath)
		os.system("rd /s/q "+inputPath+"\\scaled")
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')
	
#=================MODE B================
def ModeB():
	print("=================MODE B================")
	print("Input path must be a folder, not a file")
	print("No blank space in the input-path!!That could cause error!!")
	print("Scaled images will be in the input-path \n")
	fileTimeCost = {}
	inputPathList = []
	orginalFileNameAndFullname = {}
	inputPathError = True
	models = 'models-upconv_7_anime_style_art_rgb'

	while inputPathError:
		inputPath = input('input-path: ')
		if inputPath == '':
			print('error,input-path is invalid\n')
		else:
			inputPathError = False
	inputPath=inputPath.strip('"')
	
	scale = input('scale(1/2, default=2): ')

	if scale == '':
		scale = '2'
	elif scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=0): ')
	
	if noiseLevel == '':
		noiseLevel = '0'
		
	tileSize = input('tile size(>=32, default=400): ')
	
	if tileSize == '':
		tileSize = '400'
		
	turnoff = input('turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
	
	total_time_start=time.time()
	
	for dirs in os.walk(inputPath):
		inputPathList.append(str(dirs[0]))
		
	for inputPath in inputPathList:
		
		oldfilenumber=FileCount(inputPath)
		scalepath = inputPath+"\\scaled\\"
		thread1=PrograssBarThread(oldfilenumber,scalepath)
		thread1.start()
		
		for files in os.walk(inputPath):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
				
		folder_time_start=time.time()
		os.mkdir(inputPath+"\\scaled\\")
		
		print("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+"\\scaled\\"+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
		os.system("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+"\\scaled\\"+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
		
		folder_time_end=time.time()
		
		if thread1.isAlive()==True:
			stop_thread(thread1)
		
		print('\ntime cost of '+inputPath+':  ',folder_time_end-folder_time_start,'s\n')
		
		for files in os.walk(inputPath+'\\scaled\\'):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				originalName=list(orginalFileNameAndFullname.keys())[list(orginalFileNameAndFullname.values()).index(fileName)]
				os.rename(os.path.join(inputPath+'\\scaled\\',fileNameAndExt),os.path.join(inputPath+'\\scaled\\',originalName+"_Waifu2x.png"))
		orginalFileNameAndFullname = {}	
		os.system("xcopy /s /i /q /y "+inputPath+"\\scaled\\*.* "+inputPath)
		os.system("rd /s/q "+inputPath+"\\scaled")
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')
	
#=================MODE C================
def ModeC():
	print("=================MODE C================")
	print("Type 'over' to stop input more path, and input path must be a file")
	print("No blank space in the input-path!!That could cause error!!")
	print("Scaled images will be in the input-path \n")
	fileTimeCost = {}
	inputPathOver = True
	inputPathList = []
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
			else:
				inputPathError = False
		if inputPathOver == True:
			inputPath=inputPath.strip('"')
			inputPathList.append(inputPath)
	
	scale = input('scale(1/2, default=2): ')

	if scale == '':
		scale = '2'
	if scale == '1':
		models = 'models-cunet'
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=0): ')
	
	if noiseLevel == '':
		noiseLevel = '0'
		
	tileSize = input('tile size(>=32, default=400): ')
	
	if tileSize == '':
		tileSize = '400'
		
	turnoff = input('turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
	
	total_time_start=time.time()
	
	for inputPath in inputPathList:
		scaledFilePath = os.path.splitext(inputPath)[0]
		fileNameAndExt=str(os.path.basename(inputPath))
		
		thread1=ClockThread()
		thread1.start()
		
		folder_time_start=time.time()
		
		print("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+scaledFilePath+"_Waifu2x.png"+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
		os.system("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+scaledFilePath+"_Waifu2x.png"+" -n "+noiseLevel+ " -s "+scale+" -t "+tileSize+" -m "+models)
		
		folder_time_end=time.time()
		if thread1.isAlive()==True:
			stop_thread(thread1)
		print('\ntime cost of scale'+fileNameAndExt+':  ',folder_time_end-folder_time_start,'s\n')
		
			
	total_time_end=time.time()
	
	print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
	if turnoff=='y' or turnoff=='Y':
		os.system('shutdown -s')
	
	input('\npress any key to exit')
	
	
#=================Delete Spaces================
def DeleteSpaces():
	print("================Delete Spaces===============")
	path = input("path : ")
	path=path.strip('"')
	for dirs,useless,files in os.walk(path):
		os.rename(dirs,dirs.replace(' ', ''))
		dirs=dirs.replace(' ', '')
		for filename in files:
			os.rename(dirs+'\\'+filename,(dirs+'\\'+filename).replace(' ', ''))
	
	input('Success! Press any key to return to the menu')
	
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
    def __init__(self, OldFileNum, ScalePath):
        threading.Thread.__init__(self)
        self.OldFileNum = OldFileNum
        self.ScalePath = ScalePath
    def run(self):
        PrograssBar(self.OldFileNum,self.ScalePath)


def PrograssBar(OldFileNum,ScalePath):
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
			if NewFileNum==0:
				Percent = 0
				BarStr = ''
			else:
				Percent = int(100*(NewFileNum/OldFileNum))
				BarStr = ''
				for x in range(0,int(Percent/2)):
					BarStr = BarStr + '>'
			time_now = time.time()
			timeCost = str(int(time_now-time_start)) + 's'
			PrograssBar = "\r"+"Prograss("+str(NewFileNum)+"/"+str(OldFileNum)+"): ["+BarStr+"]"+str(Percent)+"%  ["+timeCost+"]"
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

	
#=================Start================
ChooseMode()

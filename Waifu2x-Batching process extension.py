import os
import time

def ChooseMode():
	while True:
		print('Waifu2x-Batching process extension v0.3')
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
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=0): ')
	
	if noiseLevel == '':
		noiseLevel = '0'
		
	scale = input('scale(1/2, default=2): ')
	
	if scale == '':
		scale = '2'
		
	tileSize = input('tile size(>=32, default=400): ')
	
	if tileSize == '':
		tileSize = '400'
		
	turnoff = input('turn off computer when finished?(y/n, default=n): ')
	
	if turnoff == '':
		turnoff = 'n'
	
	total_time_start=time.time()
	
	for inputPath in inputPathList:
		
		for files in os.walk(inputPath):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
				
		folder_time_start=time.time()
		os.mkdir(inputPath+"\\scaled\\")
		
		print("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+"\\scaled\\"+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize+" -m models-upconv_7_anime_style_art_rgb")
		os.system("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+"\\scaled\\"+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize+" -m models-upconv_7_anime_style_art_rgb")
		
		folder_time_end=time.time()
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
	while inputPathError:
		inputPath = input('input-path: ')
		if inputPath == '':
			print('error,input-path is invalid\n')
		else:
			inputPathError = False
	inputPath=inputPath.strip('"')
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=0): ')
	
	if noiseLevel == '':
		noiseLevel = '0'
		
	scale = input('scale(1/2, default=2): ')
	
	if scale == '':
		scale = '2'
		
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
		for files in os.walk(inputPath):
			for fileNameAndExt in files[2]:
				fileName=os.path.splitext(fileNameAndExt)[0]
				orginalFileNameAndFullname[fileName]= fileNameAndExt
				
		folder_time_start=time.time()
		os.mkdir(inputPath+"\\scaled\\")
		
		print("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+"\\scaled\\"+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize+" -m models-upconv_7_anime_style_art_rgb")
		os.system("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+"\\scaled\\"+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize+" -m models-upconv_7_anime_style_art_rgb")
		
		folder_time_end=time.time()
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
	
	noiseLevel = input('noise-level(-1/0/1/2/3, default=0): ')
	
	if noiseLevel == '':
		noiseLevel = '0'
		
	scale = input('scale(1/2, default=2): ')
	
	if scale == '':
		scale = '2'
		
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
		folder_time_start=time.time()
		
		print("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+scaledFilePath+"_Waifu2x.png"+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize+" -m models-upconv_7_anime_style_art_rgb")
		os.system("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+scaledFilePath+"_Waifu2x.png"+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize+" -m models-upconv_7_anime_style_art_rgb")
		
		folder_time_end=time.time()
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
	for dirs in os.walk(path):
		os.rename(dirs[0],dirs[0].replace(' ', ''))
	input('Success! Press any key to return to the menu')
	
#=================Start================
ChooseMode()

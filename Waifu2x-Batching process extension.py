import os
import time

print("type 'over' to stop input more path, and input path must be a folder, not a file")
print("No blank space in the input-path!!That could cause error!!")
print("scaled images will be in the input-path \n")
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


total_time_start=time.time()

for inputPath in inputPathList:
	
	for files in os.walk(inputPath):
		for fileNameAndExt in files[2]:
			fileName=os.path.splitext(fileNameAndExt)[0]
			orginalFileNameAndFullname[fileName]= fileNameAndExt
			
	folder_time_start=time.time()
	os.mkdir(inputPath+"\\scaled\\")
	print("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+"\\scaled\\"+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize)
	os.system("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+"\\scaled\\"+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize)
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

input('\npress any key to exit')

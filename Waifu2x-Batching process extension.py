import os
import time

print("type 'over' to stop input more path, and input path must be a folder, not a file\n")

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


total_time_start=time.time()

for inputPath in inputPathList:
	folder_time_start=time.time()
	print("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize)
	os.system("waifu2x-ncnn-vulkan.exe -i "+inputPath+" -o "+inputPath+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize)
	folder_time_end=time.time()
	print('\ntime cost of '+inputPath+':  ',folder_time_end-folder_time_start,'s\n')
		
total_time_end=time.time()

print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')

input('\npress any key to exit')

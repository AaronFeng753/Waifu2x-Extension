import os
import time

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
	for files in os.walk(inputPath):
		for fileNameAndExt in files[2]:
			fileExt=os.path.splitext(fileNameAndExt)[1]
			if fileExt not in [".png",".jpg",".jpeg",".jfif",".tif",".tiff",".bmp",".tga"]:
				print('error, wrong file')
			else:
				fileName=os.path.splitext(fileNameAndExt)[0]
				originalFilenPathAndName = inputPath+'\\'+fileNameAndExt
				scaledFilenPathAndName = inputPath+'\\'+fileName+'_waifu2x'+'.png'
				file_time_start=time.time()
				print("waifu2x-ncnn-vulkan.exe -i "+originalFilenPathAndName+" -o "+scaledFilenPathAndName+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize)
				os.system("waifu2x-ncnn-vulkan.exe -i "+originalFilenPathAndName+" -o "+scaledFilenPathAndName+" -n "+noiseLevel+ " -s " +scale+" -t "+tileSize)
				file_time_end=time.time()
				fileTimeCost[fileNameAndExt]=str(file_time_end-file_time_start)
		
total_time_end=time.time()
print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
for filename,filetime in fileTimeCost.items():
	print(filename+' --- '+filetime+'s')
input('\npress any key to exit')

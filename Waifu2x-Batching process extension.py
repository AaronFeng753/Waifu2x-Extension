import os
import time

noiseLevel = '0'
scale = '2'
fileTimeCost = {}

inputPathError = True
while inputPathError:
	inputPath = input('input-path: ')
	if inputPath == '':
		print('error,input-path is invalid\n')
	else:
		inputPathError = False
inputPath=inputPath.strip('"')
noiseLevel = input('noise-level(-1/0/1/2/3, default=0): ')
scale = input('scale(1/2, default=2): ')


total_time_start=time.time()

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
			os.system("waifu2x-ncnn-vulkan.exe -i "+originalFilenPathAndName+" -o "+scaledFilenPathAndName+" -n "+noiseLevel+ "-s" +scale)
			file_time_end=time.time()
			fileTimeCost[fileNameAndExt]=str(file_time_end-file_time_start)
		
total_time_end=time.time()
print('\ntotal time cost: ',total_time_end-total_time_start,'s\n')
for filename,filetime in fileTimeCost.items():
	print(filename+' --- '+filetime+'s')
input('\npress any key to exit')

# Waifu2x-Extension

# What is Waifu2x-Extension?
Image & GIF & Video Super-Resolution for Anime-style art using Deep Convolutional Neural Networks.

Based on waifu2x-ncnn-vulkan (version 20190712). 

Thanks to waifu2x-ncnn-vulkan, Waifu2x-Extension could use any kind of gpu that support `Vulakn`, even Intel GPU. 

Already been tested on `AMD` RX 550, `NVIDIA` GeForce GTX 1070 and `Intel` UHD 620.

# Features
### New features brought by this extension:
- More friendly way of interacting
- Support 1x/2x/4x/8x magnification
- Batch zoom in still images and GIF dynamic images
- Batch enlarge video files
- Personalization
- Online update
- Save the enlarged image target as .jpg
- Lossless compression of .jpg images after the target is saved
- Optimize enlarged GIF dynamic images to reduce space usage
- Display processing progress and remaining time
- Smart selection of models
- Gif compression & image compression (multi-threading and multiple compression levels)
- Benchmark (to get the tile size value for your computer)
- Multi-threaded mode
- Protect Gif files
- Error catching
- Record error log
- Sleep mode
- Notification sound
- And more

# Samples
### **`Image`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/image

### **`Video`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/video

### **`GIF`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/gif

#### Original Imgae 480x300 (.jpg 93.2 KB):
![Original Imgae](/Samples/image/Original_[480x300].jpg)

#### After 8x magnification and level 3 denoise 3840x2400 (.jpg 525 KB):
![Scaled Imgae](/Samples/image/Waifu2x_8x_[3840x2400].jpg)

#### Original GIF 500 x 372 (493 KB):
![Original GIF](/Samples/gif/2_original.gif)

#### After 2x magnification, level 2 denoise and gif optimize 1000 x 744 (3.91 MB):
![Original GIF](/Samples/gif/2_waifu2x_compressed.gif)

# Screenshot
![mainmenu](/screenshot/mainmenu.png) 
![running](/screenshot/running.png) 

# Download: https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest

# Credits:
waifu2x-ncnn-vulkan:
https://github.com/nihui/waifu2x-ncnn-vulkan

FFmpeg:
https://ffmpeg.org/

Gifsicle:
https://www.lcdf.org/gifsicle/

# Donate

## If this extension helps you, you are welcome to donate to support developers.

![donate](/donate.jpg)

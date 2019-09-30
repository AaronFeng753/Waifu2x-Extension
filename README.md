# Waifu2x-Extension
#### 中文版说明:https://github.com/AaronFeng753/Waifu2x-Extension/blob/master/README-CN.md
#### 本软件已支持简体中文语言
#### 通过修改host加速github访问：https://share.weiyun.com/5u4OPP3
# What is Waifu2x-Extension?
Image & GIF & Video Super-Resolution for Anime-style art using Deep Convolutional Neural Networks.

Based on waifu2x-ncnn-vulkan (version 20190712) and Waifu2x-converter . 

Thanks to waifu2x-ncnn-vulkan, Waifu2x-Extension could use any kind of gpu that support `Vulakn`, even Intel GPU. 

If your gpu doesn't support vulkan, you can use Waifu2x-converter, which is also intergrated into the Waifu2x-Extension.

Already been tested on `AMD` RX 550, `NVIDIA` GeForce GTX 1070 and `Intel` UHD 620.

# Features
### New features brought by this extension:
- More friendly way of interacting and easy to use.
- Achieved with waifu2x-ncnn-vulkan, waifu2x-converter and Anime4K.
- Support 1x/2x/4x/8x/.... magnification
- Batch enlarge still images and GIF dynamic images (Waifu2x-ncnn-vulkan & Waifu2x-converter)
- Batch enlarge video files (Waifu2x-ncnn-vulkan & Waifu2x-converter & Anime 4k)
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
- Compatibility test
- And more

# Samples
### **`Image`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/image

### **`Video`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/video

### **`GIF`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/gif

#### Original Imgae 480x300 (.jpg 93.2 KB):
![Original Imgae](/Samples/image/Original_[480x300].jpg)

#### After 8x magnification, level 3 denoise and compress 3840x2400 (.jpg 525 KB):
![Scaled Imgae](/Samples/image/Waifu2x_8x_[3840x2400].jpg)

#### Original GIF 500 x 372 (493 KB):
![Original GIF](/Samples/gif/2_original.gif)

#### After 2x magnification, level 2 denoise and gif optimize 1000 x 744 (3.91 MB):
![Original GIF](/Samples/gif/2_waifu2x_compressed.gif)

#### Github doesn't support play video online, pls check link below:
### **`Video`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/video

# Screenshot
![mainmenu](/screenshot/mainmenu-en.png) 

# Download: https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest

# How to fix compatibility issue :
#### waifu2x-ncnn-vulkan:
Re-install gpu driver or update it to the latest.
#### waifu2x-converter:
Buy a new conputer.
#### Anime4k:
Install the latest JDK and JRE

# Credits:
waifu2x-ncnn-vulkan:
https://github.com/nihui/waifu2x-ncnn-vulkan

FFmpeg:
https://ffmpeg.org/

Gifsicle:
https://www.lcdf.org/gifsicle/

Anime4K:
https://github.com/bloc97/Anime4K

Waifu2x-converter:
https://github.com/WL-Amigo/waifu2x-converter-cpp

Icon:

Icons made by : Freepik (https://www.flaticon.com/authors/freepik)

From Flaticon : https://www.flaticon.com/

# Donate

## If this extension helps you, you are welcome to donate to support developers.

![donate](/donate.jpg)



### Note: The user agreement of the software is modified based on the MIT protocol, allowing others to make secondary modifications to the software or to use the software-processed images, gifs, and videos for commercial purposes (via the consent of the original author of the image, gif, and video content) However, it is forbidden to use the software for commercial use after the second modification, including but not limited to secondary packaging and sales(for example: sale this software on Taobao or Ebay), integrated in other charging software. After the second modification, the source code must be disclosed. For details, please refer to the built-in user agreement. When you open the software, or modify the software, you agree to the software built-in agreement.

# Waifu2x扩展
#### 通过修改host加速github访问：https://share.weiyun.com/5u4OPP3
# 什么是"Waifu2x扩展" ?
借助深度卷积神经网络进行超分辨率放大动漫风格的艺术作品, 包括图片,gif动态图片以及视频.

基于waifu2x-ncnn-vulkan (version 20190712) 和 Waifu2x-converter.

借助于waifu2x-ncnn-vulkan, Waifu2x-Extension可以借助任何支持`Vulkan`的显卡进行运算, 即便是Intel集成显卡.

如果你的GPU不支持vulkan, 你也可以使用集成在扩展中的Waifu2x-converter.

已经在 `AMD` RX 550, `Intel` UHD 620 和 `NVIDIA` GeForce GTX 1070 上通过测试.

### 注意: 本软件的用户协议基于MIT协议修改, 允许他人对软件进行二次修改或者将软件处理后的 图片,gif,视频 用作商业用途(经 图片,gif,视频 内容原作者同意的前提下).但是, 禁止二次修改本软件后用作商业用途, 包括但不限于二次打包贩卖, 集成在其他收费软件中等. 并且二次修改后必须公开源代码.详细请参阅软件内置的用户协议.当您打开本软件, 或者对软件进行修改时即代表您同意软件内置之协议.

# 功能与特性
### 扩展带来的新功能有:

- 更友好的交互方式
- 支持 1x/2x/4x/8x 放大
- 批量放大静态图片与GIF动态图片 (Waifu2x-ncnn-vulkan & Waifu2x-converter)
- 批量放大视频文件 (Waifu2x-ncnn-vulkan & Waifu2x-converter & Anime 4k)
- 个性化设置
- 在线更新
- 将放大后的图片目标另存为.jpg
- 对目标另存为后的.jpg图片进行无损压缩
- 优化放大后的GIF动态图片, 减少空间占用
- 显示处理进度以及剩余时间
- 智能选择models
- Gif 压缩 & 图片压缩(支持多线程以及多个压缩等级)
- 基准测试(用于获得适用于您电脑的tile size值)
- 多线程模式
- 保护Gif文件
- 错误捕捉
- 记录错误日志
- 睡眠模式
- 提示音
- 兼容性测试
- 以及更多

# 示例
### **`图片`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/image

### **`视频`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/video

### **`GIF动态图`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/gif

#### 原图 480x300 (.jpg 93.2 KB):
![Original Imgae](/Samples/image/Original_[480x300].jpg)

#### 8倍放大以及3级降噪后 3840x2400 (.jpg 525 KB):
![Scaled Imgae](/Samples/image/Waifu2x_8x_[3840x2400].jpg)

#### 原GIF 500 x 372 (493 KB):
![Original GIF](/Samples/gif/2_original.gif)

#### 经过2倍放大, 2级降噪以及gif优化处理后 1000 x 744 (3.91 MB):
![Original GIF](/Samples/gif/2_waifu2x_compressed.gif)

#### Github 不支持在线播放视频,请查看下方链接:
### **`Video`** : https://github.com/AaronFeng753/Waifu2x-Extension/tree/master/Samples/video

# 截图
![mainmenu](/screenshot/mainmenu-cn.png) 
![running](/screenshot/running.png) 

# 下载: https://github.com/AaronFeng753/Waifu2x-Extension/releases/latest

# 如何修复兼容性问题 :
#### waifu2x-ncnn-vulkan:
重装或者升级显卡驱动.
#### waifu2x-converter:
买台新电脑.
#### Anime4k:
安装最新版的JDK和JRE.

# Wafu2x扩展的诞生离不开以下开源项目:
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

图标:

图标作者 : Freepik (https://www.flaticon.com/authors/freepik)

来自 Flaticon : https://www.flaticon.com/


# 捐赠

## 如果这个扩展程序帮助了您, 欢迎您捐赠支持开发者. 

![donate](/donate.jpg)

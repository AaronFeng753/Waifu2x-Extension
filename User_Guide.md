# Waifu2x-Extension User Guide
### Main Menu
----
![mainmenu Imgae](/User_Guide_Pics/mainmenu.png)

In the main menu and other interfaces, you can interacting with software by entering options and pressing the `Enter` key.

The following is the explanation of some main menu interface options:

- 4.Tile size: This value will affacts GPU memory usage.Larger tile size means waifu2x will use more GPU memory and run faster.Smaller tile size means waifu2x will use less GPU memory and run slower.The "Benchmark" in the main menu can help you to determine the best value of "tile size".

- 5.GPU ID: This determines which GPU is used in Waifu2x-ncnn-vulkan mode. The default is to automatically select the GPU. You can also manually adjust which GPU is used for calculations by changing the GPU ID.

- 6.Save as .jpg?(Scale & Denoise): This determines whether to save the picture as a .jpg file after processing the picture. If set to 'n', it will be saved as .png. Saving as .jpg will cause a slight loss of picture quality, but will save a lot of space .

- 7.Optimize .gif?(Scale & Denoise): This decides whether to optimize the GIF after processing it, the image quality will be slightly lost after optimization, but it will save a lot of space.
----

### [Scale & Denoise Image & GIF] & [Scale & Denoise Video.] & [Compress image & gif]
----

![process Imgae](/User_Guide_Pics/process.png)

You can directly type the path of the files and folders you want to work on, or you can drag it directly into the program window, and the program will automatically fill the path.

After entering a path, you need to press the Enter key to confirm the entry, and then you can continue to enter the next path until you have entered the path of all the files you want to process. At this point you can enter 'o' and then Press Enter to inform the software that you have entered all the paths you want to process.

Of course, you can also type 'r' and press Enter to return to the main menu.

After completing the input path, you can set various parameters, and finally the software will process all the pictures(video) in the input path according to the parameters you set.

----

### Image Style
----

There are two image style : `2D Anime` and `3D Real-life`, you can choose the appropriate image style based on the type of image you want to process.

For example, if you want to process the image (anime) as shown below, you can set the image style to `2D Anime`.

2D Anime image:

![2d_anime](/User_Guide_Pics/2d_anime.jpg)

However, when you want to process two kinds of images as shown below, we recommend that you switch the image style to `3D Real-life`.

3D image:

![3D_image](/User_Guide_Pics/3D_image.jpg)

Real-life image:

![Real-life](/User_Guide_Pics/Real-life.jpg)

It should be noted that only `waifu2x-ncnn-vulkan` mode supports switching the image style to `3D Real-life`, and other modes only support the default `2D Anime`.

#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'PIL module'
__author__ = 'nyc'


# PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用。
#
# 由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。
#
# 安装Pillow
#
# 如果安装了Anaconda，Pillow就已经可用了。否则，需要在命令行下通过pip安装：
#
# $ pip install pillow
# 如果遇到Permission denied安装失败，请加上sudo重试。

# 操作图像
#
# 来看看最常见的图像缩放操作，只需三四行代码：
from PIL import Image
# 打开图像文件，路径为当前路径
im=Image.open("1.jpg");
# 获得图像尺寸:
w,h=im.size
print('image size: %s %s'%(w,h))
# image size: 1080 1920
# 缩放到50%:
im.thumbnail((w//2,h//2));
print('resize image size:%s %s'%(w//2,h//2))
# resize image size:540 960
# 把缩放后的图像用jpeg格式保存:
im.save("thumbnail.png","png")


# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
#
# 比如，模糊效果也只需几行代码：

from PIL import Image,ImageFilter
im=Image.open("1.jpg");
# 应用模糊滤镜:
im2=im.filter(ImageFilter.BLUR);
im2.save("blur.jpg","jpeg");

# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：
from PIL import Image,ImageFilter,ImageFont,ImageDraw
import random

# 随机字母:
def rndChar():
    return chr(random.randint(65,90))

# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60:
width = 60 * 4
height = 60
image=Image.new('RGB',(width,height),(255,255,255))
# 创建Font对象:
font=ImageFont.truetype('Arial.ttf',36)
# 创建Draw对象:
draw=ImageDraw.Draw(image);
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x,y),fill=rndColor())
# 输出文字:
for t in range(4):
    draw.text((60*t+10,10),rndChar(),font=font,fill=rndColor2())
# 模糊:
image=image.filter(ImageFilter.BLUR)
image.save("code.jpg","jpeg")

# 如果运行的时候报错：
#
# IOError: cannot open resource
# 这是因为PIL无法定位到字体文件的位置，可以根据操作系统提供绝对路径，比如：
#
# '/Library/Fonts/Arial.ttf'
# 要详细了解PIL的强大功能，请请参考Pillow官方文档：
#
# https://pillow.readthedocs.org/
#
# 小结
#
# PIL提供了操作图像的强大功能，可以通过简单的代码完成复杂的图像处理。



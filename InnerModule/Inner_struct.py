#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'struct module'
__author__ = 'nyc'
# 概要:
# struct.pack 转换为字节
# unpack把bytes变成相应的数据类型

# 准确地讲，Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。
# 而在C语言中，我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
#
# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：
#
# >>> n = 10240099
# >>> b1 = (n & 0xff000000) >> 24
# >>> b2 = (n & 0xff0000) >> 16
# >>> b3 = (n & 0xff00) >> 8
# >>> b4 = n & 0xff
# >>> bs = bytes([b1, b2, b3, b4])
# >>> bs
# b'\x00\x9c@c'
# 非常麻烦。如果换成浮点数就无能为力了。
#
# 好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换

# struct的pack函数把任意数据类型变成bytes：
import struct
c=struct.pack('>I',10240099);
print(c);# b'\x00\x9c@c'
# pack的第一个参数是处理指令，'>I'的意思是：
#
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
#
# 后面的参数个数要和处理指令一致。


# unpack把bytes变成相应的数据类型：
h=struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(h)
# (4042322160, 32896)
# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
#
# 所以，尽管Python不适合编写底层操作字节流的代码，但在对性能要求不高的地方，利用struct就方便多了。
#
# struct模块定义的数据类型可以参考Python官方文档：
#
# https://docs.python.org/3/library/struct.html#format-characters


# Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。
import base64
with open('F:/1.bmp','rb') as f:
    print(f.read(30));
s=b'BM\xb6[\x15\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x00`\x03\x00\x00\x1c\x02\x00\x00\x01\x00\x18\x00'
# BMP格式采用小端方式存储数据，文件头的结构按顺序如下：
#
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。

# 所以，组合起来用unpack读取：

l=struct.unpack('<ccIIIIIIHH', s)
print(l)
(b'B', b'M', 1399734, 0, 54, 40, 864, 540, 1, 24)
# 结果显示，b'B'、b'M'说明是Windows位图，位图大小为864x540，颜色数为24。

# 请编写一个bmpinfo.py，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。

# -*- coding: utf-8 -*-
import base64, struct
bmp_data = base64.b64decode('Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')
def bmp_info(data):
    s=struct.unpack('<ccIIIIIIHH',data[:30])
    if (s[0] + s[1]) in [b'BM', b'BA']:
        return {
            'width': s[6],
            'height': s[7],
            'color': s[9]
        }
    else:
        return False
# 测试
bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

s='哈哈哈哈三四十';
print(s[:4])
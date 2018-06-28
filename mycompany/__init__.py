#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

# __init__.py为入口文件

'a test module'
__author__ = 'nyc'

# 在导入的模块中加入__all__=['a','b'] 即为允许导入的变量
__all__=['']

# 批量引入模块，只需在__init__.py文件中引用，那么其他引用此包的模块都引用了这些模块
import sys
import io


#避免循环引用模块   p1引用p2  p2引用p1 造成错误

# 导入模块，会执行模块中的所有代码




#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'文档测试 module'
__author__ = 'nyc'

# 此模块报错了，还没解决：
# Traceback (most recent call last):
#   File "D:\python\PyCharm 2017.2.3\helpers\pycharm\docrunner.py", line 83, in <module>
#     class DocTestRunner(doctest.DocTestRunner):
# AttributeError: module 'pycharm_doctest' has no attribute 'DocTestRunner'

# 这些代码与其他说明可以写在注释中，然后，由一些工具来自动生成文档。既然这些代码本身就可以粘贴出来直接运行，那么，可不可以自动执行写在注释中的这些代码呢？
#
# 答案是肯定的。
#
# 当我们编写注释时，如果写上这样的注释：
# def abs(n):
#     '''
#     Function to get absolute value of number.
#
#     Example:
#
#     >>> abs(1)
#     1
#     >>> abs(-1)
#     1
#     >>> abs(0)
#     0
#     '''
#     return n if n >= 0 else (-n)
# 无疑更明确地告诉函数的调用者该函数的期望输入和输出。
#
# 并且，Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。
#
# doctest严格按照Python交互式命令行的输入和输出来判断测试结果是否正确。只有测试异常的时候，可以用...表示中间一大段烦人的输出


# 让我们用doctest来测试上次编写的Dict类：
class Dict(dict):
    '''
    Simple dict but also support access as x.y style

    >>>d1=Dict()
    >>>d1['x']=100
    >>>d1.x
    100
    >>>d1.y=200
    >>>d1['y']
    200
    >>>d2=Dict(a=1,b=2,c='3')
    >>>d2.c
    '3'
    >>>d2['empty']
    Traceback (most recent call last ):
    ...
    KeyError:'empty'
    >>>d2.empty
    Traceback (most recent call last):
    ...
    AttributeError:'Dict' object has no attrbute 'empty'
    '''

    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'调试 module'
__author__ = 'nyc'
# 概要：
# 断言
# logging
# pdf

# 程序能一次写完并正常运行的概率很小，基本不超过1%。总会有各种各样的bug需要修正。
# 有的bug很简单，看看错误信息就知道，有的bug很复杂，我们需要知道出错时，哪些变量的值是正确的，哪些变量的值是错误的，
# 因此，需要一整套调试程序的手段来修复bug。
#
# 第一种方法简单直接粗暴有效，就是用print()把可能有问题的变量打印出来看看：
# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，运行结果也会包含很多垃圾信息。所以，我们又有第二种方法。

#　断言
# 凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：
def foo(s):
    n=int(s);
    assert  n!=0,'n is zero '
    return 10/n;
def main():
    foo('0');
# main();
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
#
# 如果断言失败，assert语句本身就会抛出AssertionError：
#
# Traceback (most recent call last):
#   File "F:/mygit/python/Error/debug.py", line 25, in <module>
#     main();
#   File "F:/mygit/python/Error/debug.py", line 24, in main
#     foo('0');
#   File "F:/mygit/python/Error/debug.py", line 21, in foo
#     assert  n!=0,'n is zero '
# AssertionError: n is zero


# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：
# 这个功能不知道咋用
# 关闭后，你可以把所有的assert语句当成pass来看。

# logging
#
# 把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
import  logging
# s='0';
# n=int(s);
# logging.info('n= %d'%n);
# print(10/n);

# Traceback (most recent call last):
#   File "F:/mygit/python/Error/debug.py", line 51, in <module>
#     print(10/n);
# ZeroDivisionError: division by zero
# # logging.info()就可以输出一段文本。运行，发现除了ZeroDivisionError，没有任何信息。怎么回事？
#
# 别急，在import logging之后添加一行配置再试试：

import logging
logging.basicConfig(level=logging.INFO);

# s='0';
# n=int(s);
# logging.info('n=%d'%n);
#print(10/n);

# INFO:root:n=0    这行是通过配置出来的
# Traceback (most recent call last):
#   File "F:/mygit/python/Error/debug.py", line 67, in <module>
#     print(10/n);
# ZeroDivisionError: division by zero

# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
#
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件


# pdb
#
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

# s = '0'
# n = int(s)
# print(10 / n)
# debug 可以单步调试
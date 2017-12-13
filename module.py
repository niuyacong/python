# user:nyc
# time:2017-12-13
# 模块(以下为标准注释)

#!/usr/bin/env python3  (这个注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行)
# -*- coding: utf-8 -*-  （表示.py文件本身使用标准UTF-8编码）

'a test module'   # 一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
__author__ = 'nyc'  # 使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；

# 使用模块
# 以内建的sys模块为例，编写一个hello的模块：
import  sys;


# sys模块有一个argv变量，用list存储了命令行的所有参数。argv至少有一个元素，因为第一个参数永远是该.py文件的名称，例如：
#
# 运行python3
# hello.py获得的sys.argv就是['hello.py']；
#
# 运行python3
# hello.py
# Michael获得的sys.argv就是['hello.py', 'Michael]。
def test():
    args=sys.argv;
    print(args); # ['F:/mygit/python/module.py']
    if len(args)==1:
        print('hello world');
    elif len(args)==2:
        print('hello %s'% args[1])
    else:
        print('too many arguments')

# print(__name__)# __main__
if __name__=='__main__':
    test()# hello world
# Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
#测试详见module1.py  import module.py 之后，页面并没有打印hello world
# 需要module1 调用module.test()



# 作用域
#
# 在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。在Python中，是通过_前缀来实现的。
#
# 正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
#
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
#
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；
#
# 之所以我们说，private函数和变量“不应该”被直接引用，而不是“不能”被直接引用，是因为Python并没有一种方法可以完全限制访问private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
# private函数作用：
def _private_1(name):
    return 'Hello , %s'%name;
def _private_2(name):
    return 'Hi , %s'%name;
def greeting(name):
    if len(name)>3:
        return _private_1(name);
    else:
        return _private_2(name);
# 我们在模块里公开greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用greeting()函数不用关心内部的private函数细节，
#
# 这也是一种非常有用的代码封装和抽象的方法，即：
#
# 外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。



























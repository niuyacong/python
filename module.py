# user:nyc
# time:2017-12-13
# 模块(以下为标准注释)
# 使用模块，安装第三方模块

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



# 导入第三方模块
#  file -- setting -- project: python --project interpreter --添加（+）

# 安装常用模块
#
# 在使用Python时，我们经常需要用到很多第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。用pip一个一个安装费时费力，还需要考虑兼容性。我们推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。
#
# 可以从Anaconda官网下载GUI安装包，安装包有500~600M，所以需要耐心等待下载。网速慢的同学请移步国内镜像。下载后直接安装，Anaconda会把系统Path中的python指向自己自带的Python，并且，Anaconda安装的第三方模块会安装在Anaconda自己的路径下，不影响系统已安装的Python目录。
#
# 安装好Anaconda后，重新打开命令行窗口，输入python，可以看到Anaconda的信息：



# 模块搜索路径
#
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：
# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
# 如果我们要添加自己的搜索目录，有两种方法：
#
# 一是直接修改sys.path，添加要搜索的目录：
# >>> import sys
#>>> sys.path.append('/Users/michael/my_py_scripts')
# 这种方法是在运行时修改，运行结束后失效。
# 第二种方法是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。




























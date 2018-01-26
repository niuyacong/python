#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'a test module'
__author__ = 'nyc'

class Hello(object):
    def Hello(self,name='world'):
        print('Hello,%s'% name);

# 使用type()创建出类nyc,而无需定义class nyc...
def fn(self,name='haha'):
    print('nyc:%s'%name);
NYC=type('NYC',(object,),dict(nyc=fn));# 创建NYC class

n=NYC();
print(type(NYC)); # <class 'type'>
print(type(n));   # <class '__main__.NYC'>
# 通过type()定义的类，可以在自己的模块使用
# 要创建一个class对象，type()函数依次传入3个参数：
#
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
#
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，
# 也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，
# 要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。

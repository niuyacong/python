#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'面向对象高级编程'
__author__ = 'nyc'

# 简要说明：
# __slots__
# @property
# 多重继承
# 定制类


# __slots__
# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性
class Student(object):
    pass
# 给实例绑定一个属性
s=Student();
s.name='nyc.test';
print(s.name);      # nyc.test
# 给实例绑定一个方法
def set_age(self,age):
    self.age=age;

from types import MethodType
s.set_age=MethodType(set_age,s);# 给实例绑定一个方法
s.set_age(25);              #调用实例方法
print(s.age);           #25
# 给一个实例绑定的方法，对另一个实例是不起作用的
# 为了给所以实例绑定方法，可以给class 绑定方法
def set_score(self,score):
    self.score=score;
Student.set_score=set_score;    # 给类绑定方法
s.set_score(100);               # 实例调用方法
print(s.score);                 # 100

# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
# __slots__
class Student(object):
    __slots__ = ('name','age'); # # 用tuple定义允许绑定的属性名称
a=Student();
a.age=10;
# a.score=10; # AttributeError: 'Student' object has no attribute 'score'
# score 不是Student类绑定的属性，使用会报错
# __slots__仅对当前类的实例起作用，对继承的子类不起作用
class Child(Student):
    pass
c=Child();
c.score=10;
print(c.score);         #10
# 除非在子类中也定义__slots__,子类实例允许定义的属性就是子类的__slots__加父类的__slots__
class Childs(Student):
    __slots__ = 'score';
d=Childs();
d.score=100;
print(d.score);         # 100
d.age=50;
print(d.age);           # 父类的__slots__也可以
# d.sex='女';   既不是父类的__slots__ 也不是子类的__slots__ 抛出异常AttributeError: 'Childs' object has no attribute 'sex'
#
#
#
#
#
#
# 使用@property
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
s=Student();
s.age=100;
# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
class Student():
    __slots__ = ('name','age');
    def set_age(self,value):
        if not isinstance(value,int):
            raise  ValueError("age must be integer");
        if value<0 or value>100:
            raise ValueError("age must between 0~100");
        self.age=value;
    def get_age(self):
        return self.age;
# 类的实例设置属性
s=Student();
#s.set_age(110); ValueError: age must between 0~100
s.set_age(80);
print(s.get_age());         # 80
s.age=112;
print(s.age);#　112
# 以上的方法，是通过特定的方法限制类Student，age的取值方法，直接对类的属性操作时，没有效果
# so
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
# 对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class  Student(object):
    @property
    def score(self):
        return  self._score;
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError("score must be int");
        if value<0 or value>100:
            raise ValueError("score must between 0~100");
        self._score=value;
# @property的实现比较复杂，我们先考察如何使用。
# 把一个getter方法变成属性，只需要加上@property就可以了，
# 此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
s=Student();
# s.score=110;# ValueError: score must between 0~100
s.score =4;
print(s.score); # 4

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
#
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):
    @property
    def birth(self):
        return  self._birth;
    @birth.setter
    def birth(self,value):
        self._birth=value;
    @property
    def age(self):
        return 2018-self._birth;
s=Student();
s.birth=2012;
print(s.birth);# 2012
print(s.age); # 6
# s.age=10; # AttributeError: can't set attribute
# age是只读的
#
#
#
#
#
#
#多重继承
# 回忆一下Animal类层次的设计，假设我们要实现以下4种动物：
#
# Dog - 狗狗；
# Bat - 蝙蝠；
# Parrot - 鹦鹉；
# Ostrich - 鸵鸟
# 按照哺乳动物和鸟类归类：
# 动物--哺乳类--（dog 和 bat）
# 动物--鸟类--（Parrot、Ostrich）
# 如果按照哺乳动物和鸟类，能飞和不能飞归类，那就得设计更多的层次，累的层次就更复杂了
# 如果要再增加“宠物类”和“非宠物类”，这么搞下去，类的数量会呈指数增长，很明显这样设计是不行的。
#
# 正确的做法是采用多重继承。首先，主要的类层次仍按照哺乳类和鸟类设计：
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
# 各种动物
class Dog(Mammal):
    pass
class Bat(Mammal):
    pass
class Parrot(Bird):
    pass
class Ostrich(Bird):
    pass

# 现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print("running...");
class Flyable(object):
    def fly(self):
        print("Flying...");
# 对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal,Runnable):
    pass
# 对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
class Bat(Mammal,Flyable):
    pass
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。

# MixIn

# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，你还可以定义出肉食动物CarnivorousMixIn和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：

# MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

#Python自带的很多库也使用了MixIn。举个例子，Python自带了TCPServer和UDPServer这两类网络服务，而要同时服务多个用户就必须使用多进程或多线程模型，这两种模型由ForkingMixIn和ThreadingMixIn提供。通过组合，我们就可以创造出合适的服务来。

# example:
# 比如，编写一个多进程模式的TCP服务，定义如下
#分叉(fork)，Windows系统不支持
# from socketserver import TCPServer,ForkingMixIn
# class MyTCPServer(TCPServer,ForkingMixIn):
#      pass
# 编写一个多线程模式的UDP服务，定义如下：
from socketserver import UDPServer,ThreadingMixIn
class MyUDPServer(UDPServer, ThreadingMixIn):
    pass
#
#
#
#
#
#
#定制类
# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
#
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
#
# __str__
class Student(object):
    def __init__(self,value):
        self.name=value;
print(Student('nyc'));      # <__main__.Student object at 0x00000000021EB438>
# 打印出一堆<__main__.Student object at 0x109afb190>，不好看。
#
# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：
class Student(object):
    def __init__(self,value):
        self.name=value;
    def __str__(self):
        return 'Student object (name %s )'%self.name
print(Student('nyc'));          # Student object (name nyc )
s=Student('aaa');
# 但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
#
# >>> s = Student('Michael')
# >>> s
# <__main__.Student object at 0x109afb310>
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
#
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
class Student(object):
    def __init__(self,value):
        self.name=value;
    def __str__(self):
        return 'Student object (name %s )'%self.name

    __repr__ = __str__













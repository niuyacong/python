#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'Face To Object'
__author__ = 'nyc'
""" 
类的基本作用：封装代码
类就是一个模板，可以产生多个不同对象
类（行为、特征）

实例化类的时候，会执行__init__构造函数，不能返回字符串

局部变量不会覆盖全局变量

构造函数：
1、初始化对象的属性
"""
# 面向对象编程
# 类和实例(类、封装)
# 访问限制（私有变量）
# 继承和多态
# 获取对象信息
# 实例属性和类属性

# 类和实例
#
# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
# 比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
# 定义类是通过class关键字
class Student(object):
    pass;
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
# 表示该类是从哪个类继承下来的，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
#
# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
bart=Student();
print(bart);        # <__main__.Student object at 0x0000000001E9C1D0>
# 变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类。
#
# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
bart.name='bart simpson';
print(bart.name)    # bart simpson
#
#
#由于类可以起到模板的作用，因此，可以在创建实例的时候，
# 把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
#
class Student1():

    def __init__(self,name,score):# 构造函数
        self.name=name;
        self.score=score;
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，
# 就可以把各种属性绑定到self，因为self就指向创建的实例本身。
#
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，
# 但self不需要传，Python解释器自己会把实例变量传进去：

bar=Student1('test',12);
print(bar.name)
# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，
# 并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，
# 所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

#
# 封装
#
# 类的方法：
class Student(object):
    def __init__(self,name,score):
        self.name=name;
        self.score=score;
    def print_n(self):
        print('%s score is %s'%(self.name,self.score));

bar =Student('nyc',100);
bar.print_n();  #nyc score is 100
# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。
# 要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
#
# 封装的好处
# 从外部看Student类，就只需要知道，创建实例需要给出name和score，
# 而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
# 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
class Student(object):
    def __init__(self,name,score):
        self.name=name;
        self.score=score;
    def print_n(self):
        print('%s score is %s'%(self.name,self.score));
    def get_grade(self):
        if self.score>90:
            print('A');
        elif self.score>60:
            print('C')
        else:
            print('D');
bar =Student('nyc',100);
bar.print_n();  #nyc score is 100
bar.get_grade();# A

# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
#
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
#
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
#
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：

# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
class Student():
    def __init__(self,name,score):
        self.__name=name;
        self.__score=score;
    def print_score(self):
        print('%s : %s'%(self.__name,self.__score));

bar = Student('nyc',100);
# bar.name;# AttributeError: 'Student' object has no attribute 'name'
bar.print_score();# nyc : 100
# 如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
class Student():
    def __init__(self,name,score):
        self.__name=name;
        self.__score=score;
    def print_score(self):
        print('%s : %s'%(self.__name,self.__score));
    def get_name(self):
        return self.__name;
    def set_name(self,names):
        self.__name=names;
bar = Student('nyc',100);
print(bar.get_name());# nyc
bar.set_name('yc');
print(bar.get_name());# yc

# 原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
# example:
class Student():
    def __init__(self,name,score):
        self.__name=name;
        self.__score=score;
    def print_score(self):
        print('%s : %s'%(self.__name,self.__score));
    def get_name(self):
        return self.__name;
    def set_name(self,names):
        if len(names)<3 or len(names)>4:
            print('name is error')
        else:
            self.__name = names;

bar = Student('nyc',100);
print(bar.get_name());# nyc
bar.set_name('yc'); # name is error
print(bar.get_name());# nyc

# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
#
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
print(bar._Student__name);# nyc
# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
# 错误写法：
bar = Student('nyc',100);
bar.get_name();# nyc
bar.__name='text';
print(bar.__name);# text
print(bar.get_name())# nyc
# 并没有如期打印出text,而是返回初始化的nyc
# 外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！
# 内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量






# 继承和多态
# 编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal(object):
    def run(self):
        print('Animal is running...');
# 需要编写Dog和Cat类时，就可以直接从Animal类继承：
class Dog(Animal):
    pass;
class Cat(Animal):
    pass
# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
# 继承有什么好处？
# 最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：
dog=Dog();
dog.run();# Animal is running...
# 也可以对子类增加一些方法，比如Dog类：
class Dog(Animal):
    def run(self):
        print('Dog is running...');
    def eat(self):
        print('Eating meet...');
dog=Dog();
dog.run();# Dog is running...
dog.eat();# Eating meet...
# 继承的第二个好处需要我们对代码做一点改进。你看到了，无论是Dog还是Cat，它们run()的时候，显示的都是Animal is running...，符合逻辑的做法是分别显示Dog is running...和Cat is running...，因此，对Dog和Cat类改进如下：
class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(Animal):

    def run(self):
        print('Cat is running...')
# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，
# 在代码运行的时候，总是会调用子类的run()。这样，我们就获得了继承的另一个好处：多态。
#
# 要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。
# 我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：
a=list();
b=Dog();
c=Animal();
# 判断一个变量是否是某个类型可以用isinstance()判断：
print(isinstance(a,list))# True
print(isinstance(b,Dog))# True
print(isinstance(c,Animal));# True
print(isinstance(b,Animal)); # True  b不仅仅是Dog,还是Animal
# 如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：
print(isinstance(c,Dog))# False
# Dog可以看成Animal，但Animal不可以看成Dog。
#
# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：
def run_twice(Animal):
    Animal.run();
    Animal.run();
# 传入Animal的实例
run_twice(Animal())
# Animal is running...
# Animal is running...
# 传入Dog的实例：
run_twice(Dog())
# Dog is running...
# Dog is running...
# 新增一个Animal的子类，不必对run_twice()做任何修改，
# 实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
#
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
#
# 对扩展开放：允许新增Animal子类；
#
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
#
# 继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object
#
#
#
#
#
# 静态语言 vs 动态语言
#
# 对于静态语言（例如Java）来说，如果需要传入Animal类型，则传入的对象必须是Animal类型或者它的子类，否则，将无法调用run()方法。
#
# 对于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了：
class Timer(object):
    def run(self):
        print('time is lose');
run_twice(Timer())
# time is lose
# time is lose
# Timer也可以调用run_twice方法，但是不必继承于Animal,Timer有run方法，像Animal就可以了,这就是动态语言的特点
#
# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。
# 但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，
# 你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。
#
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
#
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。
#
#
#
#
#
#
# 获取对象信息
# 拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 判断对象类型，使用type()函数：
print(type(123))    #<class 'int'>
print(type('123'))  #<class 'str'>
print(type(1.12))   #<class 'float'>
print(type([1,2,4]))# <class 'list'>
# 如果一个变量指向函数或者类，也可以用type()判断
print(type(run_twice)); # <class 'function'> type 里面只放名字，不加调用的括号（）
b=Dog();
c=Animal()
print(type(b)); # <class '__main__.Dog'>
print(type(c)); # <class '__main__.Animal'>
print(type(abs)) # abs:绝对值函数，<class 'builtin_function_or_method'>
# 在if语句中判断，就需要比较两个变量的type类型是否相同：
print(type(123)==type(234)); # True
print(type('123')==type(123)) # False
print(type('123')==str) # True
#
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types;
def fn():
    pass;
print(type(fn)==types.FunctionType);# True
print(type(abs)==types.BuiltinFunctionType);# True
print(type(lambda x:x)==types.LambdaType);# True
print(type((x for x in range(1,10)))==types.GeneratorType)# True
#
# 使用isinstance()
#
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 如果继承关系是：object -> Animal -> Dog
print('isinstance');
a=Animal();
b=Dog();
print(isinstance(b,Dog));# True
print(isinstance(b,Animal));# True
# 能用type()判断的基本类型也可以用isinstance()判断：
print(isinstance('a',str))# True
print(isinstance(b'a',bytes));# True
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print('1');
print(isinstance([1,2,3,4],(list,tuple))) #True
print(isinstance((1,2,3,4),(list,tuple)))# True　
# !!! 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。
#
# 使用dir()
#
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))
#　['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(dir(Animal));
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'run']
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(len('ABC'));      # 3
print('ABC'.__len__()); # 3
#我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyDog():
    def __len__(self):
        return 100;
dog=MyDog();
print(len(dog));# 100
# 剩下的都是普通属性或方法，比如lower()返回小写的字符串：
print('ABC'.lower()); # abc
# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class Myobject():
    def __init__(self):
        self.x=9;
    def power(self):
        return self.x*self.x;
obj=Myobject();
print(hasattr(obj,'x')); #　True
print(obj.x);# 9
setattr(obj,'y',10);
print(hasattr(obj,'y'));#True
print(getattr(obj,'y')) # 10
print(getattr(obj,'z',-1));#　如果不存在的属性会报错，可以附加默认值，直接返回默认值
# 也可以获得对象的方法：
print(hasattr(obj,'power')) # True
print(getattr(obj,'power')) # <bound method Myobject.power of <__main__.Myobject object at 0x0000000002853278>>
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
fn # fn指向obj.power
# <bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
fn() # 调用fn()与调用obj.power()是一样的   81
#
#
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。
# 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
# sum = obj.x + obj.y
# 就不要写：
# sum = getattr(obj, 'x') + getattr(obj, 'y')
# 一个正确的用法的例子如下：
def ReadImage(fp):
    if hasattr(fp,'read'):
        return readData(fp);
    return  None;
def readData():
    pass;
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，如果不存在，则无法读取。
# hasattr()就派上了用场。

# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，
# 也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。
#
#
#
#
#
#
# 实例属性和类属性
# 由于Python是动态语言，根据类创建的实例可以任意绑定属性。
#
# 给实例绑定属性的方法是通过实例变量，或者通过self变量：
class Student(object):
    def __init__(self,name):
        self.name=name;
s=Student('Bob');
s.score=10;
# 但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：
class Student(object):
    name="Student";
s=Student();
# 当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到
print(s.name); # Student
print(Student.name) # Student
s.name='test';
print(s.name);  # test
print(Student.name)# Student












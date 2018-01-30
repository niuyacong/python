#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'单元测试 module'
__author__ = 'nyc'

# 比如对函数abs()，我们可以编写出以下几个测试用例：
#
# 输入正数，比如1、1.2、0.99，期待返回值与输入相同；
#
# 输入负数，比如-1、-1.2、-0.99，期待返回值与输入相反；
#
# 输入0，期待返回0；
#
# 输入非数值类型，比如None、[]、{}，期待抛出TypeError。
#
# 把上面的测试用例放到一个测试模块里，就是一个完整的单元测试。
#
# 我们来编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样：
d=dict(a=1,b=2);
print(d['a']); # 1
# 编写mydict
class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw);
    def __getattr__(self, item):
        try:
            return self[item];
        except KeyError:
            raise  AttributeError(r"'Dict' object has no attribute '%s'"%item);
    def __setattr__(self, key, value):
        self[key]=value;
# 为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py(详见relation/unittest/mydict_test.py)


# 练习
#
# 对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'

# 单元测试详见relation/unittest/Student_test.py

# 改过之后的Student类;
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score>100:
            raise  ValueError;
        if self.score >= 80:
            return 'A'
        if self.score >= 60:
            return 'B'
        if self.score<0:
            raise  ValueError
        return 'C'

#
# 小结
#
# 单元测试可以有效地测试某个程序模块的行为，是未来重构代码的信心保证。
#
# 单元测试的测试用例要覆盖常用的输入组合、边界条件和异常。
#
# 单元测试代码要非常简单，如果测试代码太复杂，那么测试代码本身就可能有bug。
#
# 单元测试通过了并不意味着程序就没有bug了，但是不通过程序肯定有bug。

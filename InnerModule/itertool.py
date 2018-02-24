#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'迭代工具 module'
__author__ = 'nyc'
# 概要：
# count()
# cycle()
# repeat()
# takewhile()
# chain()
# groupby()


# Python的内建模块itertools提供了非常有用的用于操作迭代对象的函数。
#
# 首先，我们看看itertools提供的几个“无限”迭代器：


import itertools
natuals=itertools.count(1)
# for i in natuals:
#     print(i)
# 1
# 2
# 3
# 4
# ...



# 因为count()会创建一个无限的迭代器，所以上述代码会打印出自然数序列，根本停不下来，只能按Ctrl+C退出。


# cycle()会把传入的一个序列无限重复下去：
import itertools
ac=itertools.cycle('ABC');
# for n in ac:
#     print(n)
# A
# B
# C
# A
# ...

# 同样停不下来


# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数：
import itertools
ns=itertools.repeat('A',3);
for n in ns:
    print(n);
# A
# A
# A
#
# 无限序列只有在for迭代时才会无限地迭代下去，如果只是创建了一个迭代对象，它不会事先把无限个元素生成出来，
# 事实上也不可能在内存中创建无限多个元素。
#
# 无限序列虽然可以无限迭代下去，但是通常我们会通过takewhile()等函数根据条件判断来截取出一个有限的序列：
natuals=itertools.count(1);
ns=itertools.takewhile(lambda x:x<10 ,natuals);
print(list(ns))
[1, 2, 3, 4, 5, 6, 7, 8, 9]

# itertools提供的几个迭代器操作函数更加有用：
# chain()
#
# chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for c in itertools.chain('ABC','EFG'):
    print(c);
# A
# B
# C
# E
# F
# G
g=itertools.count(1)
a=itertools.takewhile(lambda x:x<10,g);

# a = itertools.count(1)
# b = itertools.takewhile(lambda x: x % 3 == 0, a)
# takewhile:只要有一个满足条件的值，便舍弃后面的值，b的结果为1
b=itertools.cycle('ab')
c=itertools.takewhile(lambda x:x!='b',b)
for c in itertools.chain(a,c):
    print(c);
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# a


# groupby()
#
# groupby()把迭代器中相邻的重复元素挑出来放在一起：

for key,group in itertools.groupby('AAABBBCCAAA'):
    print(key,list(group))
# A ['A', 'A', 'A']
# B ['B', 'B', 'B']
# C ['C', 'C']
# A ['A', 'A', 'A']

# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
# 如果我们要忽略大小写分组，就可以让元素'A'和'a'都返回相同的key：
for key,group in itertools.groupby('AaaBBbcCAAa',lambda c:c.upper()):
    print(key,list(group))
# A ['A', 'a', 'a']
# B ['B', 'B', 'b']
# C ['c', 'C']
# A ['A', 'A', 'a']

# 练习
#
# 计算圆周率可以根据公式：
#
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：
# -*- coding: utf-8 -*-
import itertools
def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    a=itertools.count(1,2)
    b=itertools.takewhile(lambda x:x<=2*N-1,a)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    q=[4,-4]
    c=itertools.cycle(q);
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    d=0;
    for n in b:
        wt = next(c);
        d = d + wt / n
    # step 4: 求和:
    return d
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')


import itertools
def pis(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    a=itertools.count(1,2)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    c=itertools.cycle([4,-4]);
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...

    # step 4: 求和:
    return sum(next(c)/next(a) for i in range(N))
# 测试:
print(pis(10))
print(pis(100))
print(pis(1000))
print(pis(10000))
assert 3.04 < pis(10) < 3.05
assert 3.13 < pis(100) < 3.14
assert 3.140 < pis(1000) < 3.141
assert 3.1414 < pis(10000) < 3.1415
print('ok')
# 结果同上

# 高级特性

# 切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3]);# ['Michael', 'Sarah', 'Tracy'] 从索引0取到索引3，不包括索引3，最后一个元素索引是-1
print(L[:3]);# ['Michael', 'Sarah', 'Tracy'] 不写起始索引，默认是0
print(L[-2]);# 取出索引为-2的元素 Bob
print(L[-2:-1]);# ['Bob']
print(L[-3:-1]);# ['Tracy', 'Bob']
print(L[:]);# 原样复制['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串

# 迭代
# 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
# 迭代是通过for ... in来完成的
# dic的迭代
# 键
d={'a':1,'b':2,'c':3};
for key in d:
    print(key);
# a
# b
# c
# 值
for val in d.values():
    print(val);
# 键、值
for key,val in d.items():
    print(key,val);
# 判断迭代对象
# 方法是通过collections模块的Iterable类型判断
from collections import Iterable
print(isinstance('acd',Iterable));# true
print([1,2,3],Iterable);# true
print(123,Iterable);# false

# java中list有下标，python中enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
lists=[1,2,3];
for i,val in enumerate(lists):
    print(i,val);
    print(lists[i]);

#　列表生成式
print(list(range(1,11)));# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 1到10 输出每个数的平方
a=[];
for i in list(range(1,11)):
    a.append(i*i);
print(a); # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 使用列表生成式 i*i 放在前面表示要输出的结果  循环放后面 有条件放到循环后面 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
[i*i for i in range(1,11)]
print([i*i for i in range(1,11)]);
print([i*i for i in range(1,11) if i%2==0]) # [4, 16, 36, 64, 100]
d = {'x': 'A', 'y': 'B', 'z': 'C' }
[k+'='+v for k,v in d.items()]
print([k+'='+v for k,v in d.items()])# ['x=A', 'y=B', 'z=C']
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for  s in L]); # ['hello', 'world', 'ibm', 'apple']

# python 内置对象 isinstance函数可以判断一个变量是不是字符串：
y=123;
isinstance(y,str);
print(isinstance(y,str)); #　False




# 生成器:这种一边循环一边计算的机制，称为生成器
# generator(),list[]
g=(x * x for x in range(10));
print(g);# <generator object <genexpr> at 0x0000000001E0FFC0>
# next()函数获得generator的下一个返回值
print(next(g));# 0
print(next(g));# 1
print(next(g));# 4

# 每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

# 上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象

# 前面输出三个next(g)，for循环的g从9开始到81结束
for n in g:
    print(n);

# examplr:著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# def fib(max):
#     n,a,b=0,0,1;
#     while n<max:
#         print(b);
#         a,b=b,a+b;
#         n=n+1;
#     return 'done';
# fib(5);
# 这个函数和生成器十分类似，将print改为yield 就变成了生成器
# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
    n,a,b=0,0,1;
    while n<max:
        yield b;
        a,b=b,a+b;
        n=n+1;
    return 'done';

#print(fib(5));# <generator object fib at 0x0000000001DEFDB0>
f=fib(5);
print(next(f));# 1  next(f)是将1取出来了，不加print 不会显示

def odd():
    print("step 1");
    yield 1;
    print("step 2");
    yield 2;
    print("step 3");
    yield 3;
# 生成一个generator对象，然后调用
# 调用方法一：
# o=odd();
# next(o); 输出 step 1

for n in odd():
    print(n);
#pass;step 1  step 2   step 3
#print(n);
# step 1
# 1
# step 2
# 2
# step 3
# 3

# 由此可知，yield 会终止一次操作，但是不会自动输出yield 的值，需要添加print()用来输出结果

# 用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
g=fib(5);
while True:
    try:
        x=next(g);
        print(x);
    except StopIteration as e:
        print(e.value);
        break;
# 1
# 1
# 2
# 3
# 5
# done

print(range(5));
# 杨辉三角
def trans(max):
    i=0;
    asd=[];
    newasd=[];
    if(max<2):
        print("no!")
    else:
        for j in range(max):
            i=0;
            while i<=j:
                if i == 0:
                    asd=[];
                    asd.append(1);
                elif j == i:
                    asd.append(1);
                else:
                    asd.append(newasd[i - 1] + newasd[i]);
                i=i+1;
            yield (asd);
            newasd=asd;
trans(6);
n = 0
results = []
for t in trans(10):
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')





# 迭代器：可以被next()函数调用并不断返回下一个值的对象成为迭代器Iterator

# 可用于for循环的数据类型：
# 1、集合数据类型：dict、list、tuple、set、str
# 2、generator，包括生成器和带yield的generator的function
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable
# 可以使用isinstance()判断是否是Ierable对象
from collections import Iterable
print(isinstance([],Iterable));# true
# 生成器不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIterable错误表示无法继续返回下一个值了
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数：
from collections import Iterator
print(isinstance(iter('abc'),Iterator));# True

print(isinstance('abc',Iterator));# False

#
# 你可能会问，为什么list、dict、str等数据类型不是Iterator？
#
# 这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
#
# Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。

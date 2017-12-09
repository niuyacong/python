# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# 简要：
# 高阶函数：1、map/reduce 2、filter 3、sorted
# 返回函数


# map函数
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
def f(x):
    return  x*x;

r=map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]);
print(r);# <map object at 0x00000000021EC0F0>
# map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(r));# [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# reduce函数
# 必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场

from functools import reduce
def fn(x,y):
    return  x*10+y;
print(reduce(fn,[1,3,5,7,9]));# 13579

# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数
def fn(x,y):
    return x*10+y;

def char2num(s):
    return {'0':0,'1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];

print(char2num('1'));# 1

r=reduce(fn,map(char2num,'13579'));
print(r);# 13579
#整理成一个str2int的函数就是
def str2int(s):
    def fn(x,y):
        return x*10+y;
    def char2num(s):
        return  {'0':0,'1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];
    return reduce(fn,map(char2num,s));
print(str2int('13578'));# 13578

# 还可以用lambda函数进一步简化成：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s];
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print(str2int('135'));# 135

# example:
#1、利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

q=[];
def xunhuan(name):
    i=0;

    while i<len(name):
        if(i==0):
           s = name[i].upper();
        else:
            s+= name[i].lower();
        i=i+1;
    return s;
r=(['adam', 'LISA', 'barT']);
print(list(map(xunhuan,r))); # ['Adam', 'Lisa', 'Bart']

# 2、利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# 10的n次方：10**n
def text(maps):
    f = 1;
    point = 0;
    nums=list(map(zhuan,maps));
    def str2float(x, y):
        nonlocal f;
        nonlocal point;
        if (f < 0):
            point = point + 1;
        if y > 0:
            if f > 0:
                x = x * 10 + y;
                return x;
            else:
                flag = 10 ** point;
                x = x + y / flag;
                return x;
        elif y < 0:
            f = -1;
            return x;
    return reduce(str2float,nums);

def zhuan(s):
    return {'0':0,'1':1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':-1}[s];


s=(text('123.456'));
print('str2float(\'123.456\') =',text('123.456'))
if abs(text('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
# 下面见第一版失败案例

# 解法2（优化了point部分，即小数点部分，每次乘10）
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float1(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums)

print(str2float1('0'))
print(str2float1('123.456'))
print(str2float1('123.45600'))


# 失败案例
f = 1;
point = 0;
def str2float(x, y):
    global f;
    global point;
    if (f < 0):
        point = point + 1;
    if y > 0:
        if f > 0:
            x = x * 10 + y;
            return x;
        else:
            flag = 10 ** point;
            x = x + y / flag;
            return x;
    elif y < 0:
        f = -1;
        return x;
    return x;
print(reduce(str2float,map(zhuan,'123.456')))
print(reduce(str2float,map(zhuan,'123.456')))
# 两次输出结果不一致
# 错误原因：
# f、point 是全局变量，下一次输出会使用上一次输出保留的f、point值，导致结果不正确
# 使用上述正确方法，使用内部方法，请注意global和nonlocal用法



# filter:filter()函数用于过滤序列
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

# 在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
    return  n%2==1;
print(list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15])))# [1, 5, 9, 15]

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip();
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])));# ['A', 'B', 'C']

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。


# 用filter求素数
#
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
#
# 首先，列出从2开始的所有自然数，构造一个序列：
#
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
#
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
#
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
#
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
#
# 不断筛下去，就可以得到所有的素数。
#
# 用Python来实现这个算法，可以先构造一个从3开始的奇数序列：
def _old_iter():
    n=1;
    while True:
        n=n+2;
        yield n;
# 筛选函数：
def _not_divisible(n):
        return lambda x:x%n>0;
# 定义生成器，不断返回下一个素数
def primes():
    yield 2;
    it=_old_iter();
    while True:
        n=next(it);
        yield n;
        it = filter(_not_divisible(n),it);
for n in primes():
    if n<1000:
        print(n);
    else:
        break
# 注意到Iterator是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。

# Test:
#回数是指从左向右读和从右向左读都是一样的数，例如12321，909。请利用filter()筛选出回数：
def is_palindrome(n):
    r = str(n);
    it=[];
    i = 0;
    f = 0;
    if len(r)==1:
        return n;
    else:
        if len(r) % 2 == 0:
            while i < (len(r) / 2):
                if (r[i] != r[len(r) - i - 1]):
                    f = f + 1;
                i = i + 1;
            if f == 0:
                # it.append(n);# 为yield时，全部输出的原因
                return n;
        else:
            while i < ((len(r) - 1) / 2):
                if (r[i] != r[len(r) - i-1]):
                    f = f + 1;
                i=i+1;
            if f == 0:
                return n;
    # return it;

# 返回是两种方案：
# 1、使用数组[],把符合条件的项append到it[]中，最后输出it
# 2、把符合条件的项直接return,return n.filter本身返回的也是生成器，惰性序列，用list(),显示成数组
# 3、每次把符合条件的yield n；这样是不可以的，自己的理解：yield 返回的是生成器，需要用next()函数，或者是用for..in..的方式循环出每一项的值，而filter作用于每一项时，
# 都需要难道返回值，所以走不通。

print(list(filter(is_palindrome, range(10, 20))));
# 测试:
output = filter(is_palindrome, range(1, 200))
print(output);
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')








# sorted:排序算法
# 1、Python内置的sorted()函数就可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]));# [-21, -12, 5, 9, 36]
# 2、sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21],key=abs));# [5, 9, -12, -21, 36]
#3、字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']));# ['Credit', 'Zoo', 'about', 'bob']
# 4、字符串不区分大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower));# ['about', 'bob', 'Credit', 'Zoo']
# 5、要进行反向排序，可以不改动key函数，可以传入第三个参数
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.lower,reverse=True));# ['Zoo', 'Credit', 'bob', 'about']
# example:用一组tuple表示学生名字和成绩,用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
   x,y=t;
   return x;
L2 = sorted(L, key=by_name)
print(L2)# [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
# 按分数排序
def by_score(t):
    x, y = t;
    return y;
L2 = sorted(L, key=by_score,reverse=True)
print(L2) # [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]

# 官方解法：
from operator import itemgetter
students = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=itemgetter(0)))# [('Adam', 92), ('Bart', 66), ('Bob', 75), ('Lisa', 88)]
print(sorted(students, key=lambda t: t[1]))# [('Bart', 66), ('Bob', 75), ('Lisa', 88), ('Adam', 92)]
print(sorted(students, key=itemgetter(1), reverse=True))# [('Adam', 92), ('Lisa', 88), ('Bob', 75), ('Bart', 66)]




# 返回函数：


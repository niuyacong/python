# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

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

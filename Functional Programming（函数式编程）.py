# 函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！
# 简要：
# 高阶函数：1、map/reduce 2、filter 3、sorted
# 返回函数
# 匿名函数
# 装饰器
# 偏函数


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




# 返回函数：函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 实现一个可变参数的求和
def calc_sum(*args):
    ax=0;
    for n in args:
        ax=ax+n;
    return ax;
# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
def lazy_sum(*args):
    def sum():
        ax=0;
        for n in args:
            ax=ax+n;
        return ax;
    return sum;

f=lazy_sum(1,2,3,4);
print(f);# <function lazy_sum.<locals>.sum at 0x00000000022FBA60>返回的是求和函数
print(f());# 调用求和函数 10

# 函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1=lazy_sum(1,2,3,4);
f2=lazy_sum(1,2,3,4);
print(f1==f2); # False 即使传入相同参数，返回值也是不一样的

# 闭包：
def count():
    fs=[];
    for i in range(1,4):
        def f():
            return i*i;
        fs.append(f);
    return fs;
f1,f2,f3=count();
print(f1())# 9
print(f2())# 9
print(f3())# 9
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记一点：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j*j;
        return g;
    fs=[];
    for i in range(1,4):
        fs.append(f(i));
    return fs;
f1,f2,f3=count();
print(f1());# 1
print(f2());# 4
print(f3());# 9
# example:利用闭包返回一个计数器函数，每次调用它返回递增整数：
s = 3 #设置全局变量
def createCounter():
    def counter():
        global s #引用全局变量
        s = s+1
        return s
    return counter
counterA = createCounter()
print(counterA()) #每次调用子函数，都是会保留上次s的值进行计算的
print(counterA())

def createCounter():
    s = [0]
    def counter():
        s[0] = s[0]+1
        return s[0]
    return counter

counterA = createCounter()
print(counterA())



# 匿名函数
# 在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])));# [1, 4, 9, 16, 25, 36, 49, 64, 81]
# 匿名函数lambda x: x * x实际上就是
def f(x):
    return  x*x;
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
f= lambda x:x*x;
print(f(5));# 55
# 同样，也可以把匿名函数作为返回值返回
def build(x,y):
    return  lambda:x*x+y*y;
b=build(1,2);# 返回的是一个函数，需要调用一下显示值
print(b());# 5

# example :请用匿名函数改造下面的代码：
def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 20)))

print(L);# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# 改造：
S=list(filter(lambda x:x%2==1, range(1, 20)))
print(S);# [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2015-2-3');
f=now;
f();# 2015-2-3
# 函数对象有一个__name__属性，可以拿到函数的名字
print(now.__name__)# now
print(f.__name__)# now
# 现在，假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'% func.__name__);
        return func(*args,**kw);
    return wrapper;
# 上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print('2013-2-3');
now();
# call now():
# 2013-2-3
# 把@log放到now()函数的定义处，相当于执行了语句：now = log(now)

#　如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log(text):
    def decorator(func):
        def wrapper(*args,**kw):
            print('%s %s():'%(text,func.__name__));
            return func(*args,**kw);
        return wrapper;
    return decorator;

@log('execute')
def now():
    print('2015-3-25')

now();
# execute now():
# 2015-3-25
# 3层嵌套的效果是这样的：log('execute')(now())

# 剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，
# 但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
print(now.__name__);# wrapper

# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
#
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的

import functools
def log(func):
    # @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2013-2-3');
now();
print(now.__name__)

# 带参数的decorator
import functools;
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            print('%s %s ():'% (text,func.__name__));
            return func(*args,**kw);
        return wrapper;
    return decorator;
@log('execcute')
def now():
    print('2045-22-33');
now();
print(now.__name__);
# execcute now ():
# 2045-22-33
# now

# 设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import  time,functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kw):
        startime=time.time()
        print('%s start time: %s' % (func.__name__,startime))
        func(*args,**kw);
        endtime=time.time()
        print('%s end time :%s' % (func.__name__,endtime))
        print('%s execute time:%s'% (func.__name__,str(endtime-startime)))
        return func(*args,**kw);
    return wrapper;
@log
def fast(x, y):
    time.sleep(0.0012)
    return x + y;
print(fast(1,22));
# 测试
@log
def fast(x, y):
    time.sleep(0.0012)
    return x + y;

@log
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;

f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试成功')





# 偏函数：
# 通过设定参数的默认值，可以降低函数调用的难度。而偏函数也可以做到这一点
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print(int('12345'));# 12345
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print(int('12345',base=8));# 转换为八进制 5349
print(int('12345',16));# 转换为十六进制 74565
# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x,base=2):
    return  int(x,base);
print(int2('1000000'));# 64
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
import functools;
int2=functools.partial(int,base=2);
print(int2('1010101'))#　85.
# functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
#
# 注意到上面的新的int2函数，仅仅是把base参数重新设定默认值为2，但也可以在函数调用时传入其他值：
print(int2('1000000',base=10));# 1000000
# 创建偏函数时，实际上可以接收函数对象、*args和**kw这3个参数，当传入：
# int2 = functools.partial(int, base=2)
# 实际上固定了int()函数的关键字参数base，也就是：
# int2('10010')
# 相当于： kw={'base':2};  int('100000',**kw);
# 当传入：
# max2 = functools.partial(max, 10)
# 实际上会把10作为*args的一部分自动加到左边，也就是：
# max2(5, 6, 7)相当于：args = (10, 5, 6, 7) max(*args)
# 当函数的参数个数太多，需要简化时，
# 使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。




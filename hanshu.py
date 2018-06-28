#　python 官网函数文档  http://docs.python.org/3/library/functions.html

# 内置函数的命令，在命令行help(函数名称)  help(round)

""" 
函数功能：
1、功能性
2、隐藏细节
3、避免编写重复的代码

"""

# 绝对值的函数abs
print(abs(-5)); # 5
# max() 求最大值函数
print(max(1,5,10,-2));# 10


#　数据类型转换
print(int(3)); # 3
print(int(1.3)); #　１
print(float(1));# 1.0
print(float(2.22)); # 2.22
print(str(1)); # 1
print(str('ddf')); # ddf
print(bool('')); # False
print(bool(0)); # False
print(bool(1)); # True　

# 定义函数
""" 
1、参数列表可以没有
2、没有return 默认返回 return None
"""
def my_abs(x):
    if x>0:
        return x;
    else:
        return  -x;

print(my_abs(-2)); # 2

# 定义一个什么事也不做的空函数，可以用pass语句
def nop():
    pass

# pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
# 例子：
age=0;
if age>19:
    pass

#　数据类型检查可以用内置函数isinstance()实现
def test(x):
    if not isinstance(x,(int,float)):
        raise  TypeError("bad type");
    if(x>0):
        return  x;
    else:
        return -x;
#print(test('卡卡卡'));#　TypeError: bad type
print(test(-5)); # 5
# 返回多个值，使用函数时import导入函数
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6);
print(x,y); # 151.96152422706632 70.0

# 函数可以同时返回多个值，但其实就是一个tuple。
a= move(100, 100, 60, math.pi / 6);
print(a);# (151.96152422706632, 70.0) 用x,y接受时，就赋值给xy了

""" 
参数：
1、必选参数
2、关键字参数（形参  形式参数  add(x=2,y=3))
3、默认参数 def a(x=1,y)
"""




# 默认参数
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
def power(x,n=2):
    s=1;
    while n>0:
        n=n-1
        s=s*x
    return s;

print(power(2)); # 4
print(power(2,3)); # 8

# 默认参数必须指向不变对象
def add_end(L=[]):
    L.append('END')
    return L
print(add_end()); # ['END']  第一次调用的结果和预期结果一致
print(add_end()); # ['END', 'END'] 第二次结果和预期不一致  原因：第一次调用，可变L已被赋值为['END']  所以默认参数应指向不变对象
# 变更如下
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end()); # ['END']
print(add_end()); # ['END']


# 可变参数
#　由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传进来
def calc(numbers):
    sum=0;
    for n in numbers:
        sum=sum+n*n;
    return sum;
# 调用的时候，需要先组装出一个list或tuple：
#print(calc([1, 2, 3]));
#print(calc((1, 3, 5, 7)))
# print(calc());这样会报错，必须传入一个参数
# 把参数变为可变参数
def c(*numbers): #　接收到的是一个tuple
    b=0;
    for s in numbers:
       b=b+s*s;
    return b;
print(c(1, 3, 5, 7));# 调用时直接传可变的参数即可
print(c()); # 0

# 如果已经有一个list或者tuple，要调用一个可变参数怎么办？
nums = [1, 2, 3]
print(c(nums[0], nums[1], nums[2]))#　14






# 关键字函数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
    print('name',name,'age',age,'other',kw);

person('Michael', 30) #　name Michael age 30 other {}
person('niu',14,city='sjz',test='123')# name niu age 14 other {'city': 'sjz', 'test': '123'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra) # name Jack age 24 other {'city': 'Beijing', 'job': 'Engineer'} 直接传入extra 需要加上** 告知是可变参数

# 命名关键字参数
def person(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass #　pass是占位符，if没有语句块  不会报错
    print('name',name,'age',age,'other',kw);
# 要限制关键字参数的名字，就可以用命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)
    # 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
# 调用
person('Jack', 24, city='Beijing', job='Engineer') #　Jack 24 Beijing Engineer
#　person('Jack', 24, city='Beijing', job='Engineer',test='test')　会报错　　没有test这个参数

#　如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)
person('Jack', 24, city='Beijing', job='Engineer')# Jack 24 () Beijing Engineer
# person('Jack', 24)# 这是不可以的  需要传值
# 命名参数必须传入参数名
# 命名关键字参数可以有缺省值
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job);
person('aa',34,job='ces'); # aa 34 Beijing ces

# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*Python解释器将无法识别位置参数和命名关键字参数：

# 可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw);

f1(1, 2)
f2(1, 2, d=99, ext=None)


# 递归函数
def act(n):
    if n==1:
        return  1;
    return n*act(n-1);
print(act(5)); # 120
# print(act(1000)); #　RecursionError: maximum recursion depth exceeded in comparison
# 原因：函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

#　解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
def act(n):
    return  act_f(n,1);
def act_f(n,p):
    if n==1:
        return  p;
    return act_f(n-1,n*p);
print(act(5)); # 120
#　print(act(1000)); 栈溢出
#　使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。

#　针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。

#　Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

# 利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
     print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)


move(2, 'A', 'B', 'C')
# move(2,acb)  a----c   muve 2 bac
#  a--b a---c
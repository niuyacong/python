# 第一个程序n
print('hello 你好');

#在文件夹下建__init__.py文件，那该文件夹变成一个包,导入此模块时，默认执行__init__.py，详见mycompany包
#import 只能导出模块
#from 。。 import.. 可导入模块和变量  from ... import * 导入所有变量和函数  在导入的模块中加入__all__=['a','b'] 即为允许导入的变量

# start
#变量：字母数字下划线  首字母不能使数字  区别大小写
a=100;
if a>0:
    print(a);
else:
    print(-a);
# id(变量)#得到变量的十进制地址
# hex(id(变量))#得到变量的十六进制内存地址
# e:10
print(1.2e-5 * 10);

# 转义字符 \
# r''表示''内部的字符串默认不转义,但是这样就不管用了 ex:print(r' I'm a "smart" girl ');
# \n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\  \r回车
# 有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容

print(" I'm a \"smart\"girl");
print(r' I am a "smart" girl ');
print("我是\t谁");
print('''line1
line2
line3''');


#切片
a[0:4:2]#最后一个参数是步长，每隔2个取一次

# 布尔值Ture False 区分大小写
# and
print(True and False);
# or
print(2>3 or 3>4);
# not
print(not True);
print(not 2>3);

#很多类型都可以和boolean进行转换
print(int(True)) #1
print(int(False))#0

print(bool(1))#True
print(bool(0))#False

#复数  数字+j
36j

# 空值，用 NULL表示，不能用0表示

# 常量，通常用全部大写的变量名表示。例如：PI = 3.14159265359

# 除法
# /
print(10/3);# 3.3333333333333335
# 即使是两个整数恰好整除，结果也是浮点数
print(9/3);# 3.0

# 地板除：两个整数相除结果仍然是整数
print(10//3);# 3

#二进制、十进制、八进制、十六进制
#二进制 0b开头  八进制0o开头  十六进制 0x开头
0b10 # 2
0o10 #8
0x10 #16
#转换成二进制
bin(0x10)
#转换成十进制
int(0b10)
#转换成十六进制hex()
#转换成八进制oct()


# 字符串
# 1、对于单个字符的编码，ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print(ord('A')); # 65
print(chr(66)); # B
# 2、知道字符的整数编码，还可以用十六进制这么写
print('\u4e2d\u6587'); # 中文
# 3、Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，
# 就需要把str变为以字节为单位的bytes
# 要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
print( b'ABC');
print( '中文'.encode('utf-8'));
# 4、含有中文的str无法用ASCII编码，因为中文编码的范围超过了ASCII编码的范围，Python会报错。
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示

# 5、网络或磁盘上读取了字节流，将字节流转换为str
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')); # 中文
# 6、计算str包含多少个字符，可以用len()函数
print( len('ABC')); # 3
print(len('中文')); # 2
# 换成bytes，len()函数就计算字节数
print(len(b'ABC')); # 3
print(len(b'\xe4\xb8\xad\xe6\x96\x87')); # 6
print( len('中文'.encode('utf-8'))); # 6
# 由上可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
# str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换

# 格式化字符串
# %s表示用字符串替换，%d表示用整数替换,%f 浮点数，%x十六进制整数，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好
# 。如果只有一个%?，括号可以省略
print( 'Hello, %s' % 'world');
print('hi ,%s ,you have $%d'%('niu',100));

#字符串运算
'hello'+' world' #hello world
'hello'*3 #'hellohellohello'
'hello'[1]#e
'hello'[-1]#o
'hello'[0:4]#'hell'
'hello'[0:-1]#'hell'
'hello'[0:20]#'hello'
'hello'[2:]#'llo'
'hello'[:-1]#'hell'

# list
#支持切片操作[n:m]、[n]、+
print([1]+[2,3])#[1,2,3]
newlist=['Michael', 'Bob', 'Tracy'];
print(len(newlist));# 数组newlist的长度
print(newlist[0]);# Michael
print(newlist[-1]);# Tracy 索引为-1，取的是最后一个值 -2 -3 -4 以此类推
print(newlist[0:2])#['Michael', 'Bob']得到的结果还是list   
newlist.append("hello");# 追加元素到末尾
print(newlist); # ['Michael', 'Bob', 'Tracy', 'hello']
newlist.insert(1,"aaa"); # 插入元素到索引为1的位置
print(newlist); # ['Michael', 'aaa', 'Bob', 'Tracy', 'hello']
newlist.pop(); # 删除末尾元素
print(newlist); # ['Michael', 'aaa', 'Bob', 'Tracy']
newlist.pop(1); # 删除索引为1的元素
print(newlist); # ['Michael', 'Bob', 'Tracy']
newlist[1]="Sarah"; # 将索引为1的位置替换为Sarah
print(newlist); # ['Michael', 'Sarah', 'Tracy']
# list元素类型可不同，可组成多维数组
L = ['Apple', 123, True];
s = ['python', 'java', ['asp', 'php'], 'scheme']
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s[2][0]);# 取到asp
a=[];
print(len(a)); # 0


# tuple 有序列表  一旦初始化就不能修改（长度等均不可修改），列表中元素指向一个list ,元素还是指向list是不可变得，但是list中的元素可变
#支持切片操作、+、*
print((1,2)+(3,4))#(1,2,3,4)
print((1,2)*2)#(1,2,1,2)
classmates = ('Michael', 'Bob', 'Tracy');
print(classmates); # ('Michael', 'Bob', 'Tracy')
print(classmates[0]); # Michael
t = ();# 一个空的tuple元素
print(t); # ()
r=(1,); # 定义一个元素的tuple，必须加上逗号，以区分数学中的小括号
print(r); # (1,)
t = ('a', 'b', ['A', 'B']);
print(t); # ('a', 'b', ['A', 'B'])
t[2][0] = 'X';
t[2][1] = 'Y';
print(t); # ('a', 'b', ['X', 'Y']) tuple不变指的是指向不变


# 条件判断:执行缩进代码块
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')# your age is 3 teenager
# elif是else if的缩写
# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else
age=10;
if age>2:
    print("小");
elif age>20:
    print("中");
else:
    print("大");
# 只要x是非零数值、非空字符串、非空list等，就判断为True，否则为False
x=True;
if x:
    print("true");
# 获取用户输入的值 input()获取的值是str类型，可以用int()转换为int类型
#code=input("birth:");
#print(code);
#if int(code)>2:
#   print("success");




# 循环
# for...in.. 执行缩进代码块
name=["a","b","c"];
for a in name:
    print(a);
    print(1);
# a
# b
# c
# 1至10求和
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum) # 55
# rang()函数  rang(5) 0 到小于5之间的整数
print(range(5)); # range(0, 5)
# 用list函数转换为数组
print(list(range(5))); # [0, 1, 2, 3, 4]
# 1到100求和
sum = 0
for x in range(101):
    sum = sum + x
print(sum) # 5050

for x in range(100):#range(0,10,2) 2:步长 输出0 2 4 6 8 range(10,0,-2) 输出8 6 4 2 0
    pass
else:#for 循环正常执行完，会执行else  循环中有break,不会执行else
    pass
# while 条件满足  就会一直执行
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# break中断循环
n = 1
while n <= 100:
    print(n)
    n = n + 1
print('END')# 循环1到100  输出end
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END') # 输出1到10  输出end

# continue语句，跳过当前的这次循环，直接开始下一次循环。
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n);
    
while n<10:
    pass
else:
    pass
# dict 和 set
# dict即dictionary
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85};
print(d["Bob"]); # 75
# 写入
d['Adam'] = 67;
d['Jack'] = 90;
print(d);  # {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adam': 67, 'Jack': 90}
# print(d["test"]); # 不存在键test 会报错 ，可先用in判断键是否存在  如下
print('test' in d); # False 判断dict中是否存在键test
# 还可以通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Thomas')); # 不存在，返回None
print(d.get('Thomas',-1)); # 不存在 返回指定value-1
# 删除key
print(d); # {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adam': 67, 'Jack': 90}
d.pop("Bob");
print(d); # {'Michael': 95, 'Tracy': 85, 'Adam': 67, 'Jack': 90}
# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。

# dict的key必须是不可变对象
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。
# 这个通过key计算位置的算法称为哈希算法（Hash）。

# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# 创建一个set，需要提供一个list作为输入集合：
s=set([1,2,3]);
print(s); # {1, 2, 3}
# 重复元素在set中自动被过滤：
s=set([1,1,2,3]);
print(s); # {1, 2, 3}
# 方法add(key)可以添加元素到set,重复添加没有效果
print(s); # {1, 2, 3}
s.add("4");
print(s); # {1, 2, 3, '4'}
# 方法remove(key)可以从set中移除元素
print(s);# {1, 2, 3, '4'}
s.remove("4");
print(s); #{1, 2, 3}
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1=set([1,2,3,4]);
s2=set([0,1,2,5]);
s3=set([1,2])
print(s1&s2); #{1, 2}
print(s1|s2);#{0, 1, 2, 3, 4, 5}
print(s1-s3)#{1,2}
#定义空集合
set()

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，
# 所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
s=[1,2,3];
s1="e";
# q=set([1,s]);TypeError: unhashable type: 'list'
q=set([1,s1]);
print(q); # {1, 'e'}

# 不可变对象和可变对象
# 不可变对象 str
a="abc";
b=a.replace("a","A");
print(a+" and "+b);# abc and Abc 变量a 的值没有变，产生的新值Abc赋给了变量b
# 可变对象
c=[1,3,2];
c.sort();
print(c);# [1, 2, 3] 变量c的值发生了变化
# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。

#tuple:有序列表
a=(1,2,3);
s=set([1,a]);
print(s); # {1, (1, 2, 3)}
b=(1,2,[3.4])
#　s=set(b);
# print(s); # TypeError: unhashable type: 'list'

# from hanshu import my_abs

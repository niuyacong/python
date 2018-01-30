#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'错误处理 module'
__author__ = 'nyc'
# 概要：
# try
# 调用栈



# 在程序运行的过程中，如果发生了错误，可以事先约定返回一个错误代码，这样，就可以知道是否有错，以及出错的原因。
# 在操作系统提供的调用中，返回错误码非常常见。比如打开文件的函数open()，成功时返回文件描述符（就是一个整数），出错时返回-1。
#
# 用错误码来表示是否出错十分不便，因为函数本身应该返回的正常结果和错误码混在一起，造成调用者必须用大量的代码来判断是否出错：
# 一旦出错，还要一级一级上报，直到某个函数可以处理该错误（比如，给用户输出一个错误信息）。
#
# 所以高级语言通常都内置了一套try...except...finally...的错误处理机制，Python也不例外。
#
#try
try:
    print('try...');
    r=10/0;
    print('result:',r);
except ZeroDivisionError as e:
    print('except:',e);
finally:
    print('finally...');
print('END');
# 输出：
# try...
# except: division by zero
# finally...
# END
# 从输出可以看到，当错误发生时，后续语句print('result:', r)不会被执行，
# except由于捕获到ZeroDivisionError，因此被执行。最后，finally语句被执行。然后，程序继续按照流程往下走。

# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，
# 即except语句块，执行完except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。

try:
    print('try...');
    r=10/2;
    print('result:',r);
except ZeroDivisionError as e:
    print('except:',e);
finally:
    print('END');
# try...
# result: 5.0
# END

# 由于没有错误发生，所以except语句块不会被执行，但是finally如果有，则一定会被执行（可以没有finally语句）。

# 错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误：
try:
    print('try...');
    r=10/int('a');
    print('result:',r);
except ValueError as a:
    print('valueerror:',a);
except ZeroDivisionError as e:
    print('ZeroDivisionError',e);
finally:
    print('finally...');
print('END');

# try...
# valueerror: invalid literal for int() with base 10: 'a'
# finally...
# END

# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')
# try...
# result: 5.0
# no error!
# finally...
# END

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：
def foo():
    r = 10 / int('a')
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
# ValueError
# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。
#
# Python所有的错误都是从BaseException类派生的


# 使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用，比如函数main()调用foo()，
# foo()调用bar()，结果bar()出错了，这时，只要main()捕获到了，就可以处理：
def foo(s):
    return 10/int(s);
def bar(s):
    return foo(s)*2;
def main():
    try:
        bar('a');
    except Exception as e:
        print('Error:',e);
    finally:
        print('finally..');
main();
# Error: invalid literal for int() with base 10: 'a'
# finally..

# 也就是说，不需要在每个可能出错的地方去捕获错误，只要在合适的层次去捕获错误就可以了。
# 这样一来，就大大减少了写try...except...finally的麻烦。
#
#
# 调用栈
# 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。来看看err.py：
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    bar('0')

# main()
# 输出错误：
# Traceback (most recent call last):
#   File "F:/mygit/python/Error/dealerror.py", line 141, in <module>
#     main()
#   File "F:/mygit/python/Error/dealerror.py", line 139, in main
#     bar('0')
#   File "F:/mygit/python/Error/dealerror.py", line 136, in bar
#     return foo(s) * 2
#   File "F:/mygit/python/Error/dealerror.py", line 133, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# 出错并不可怕，可怕的是不知道哪里出错了。解读错误信息是定位错误的关键。我们从上往下可以看到整个错误的调用函数链：
# 出错的时候，一定要分析错误的调用栈信息，才能定位错误的位置。

# 记录错误

# 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。
# 既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。
#
# Python内置的logging模块可以非常容易地记录错误信息：

import logging;
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0');
    except Exception as e:
        logging.exception(e);

main();
print('END');
# ERROR:root:division by zero
# Traceback (most recent call last):
#   File "F:/mygit/python/Error/dealerror.py", line 172, in main
#     bar('0');
#   File "F:/mygit/python/Error/dealerror.py", line 168, in bar
#     return foo(s) * 2
#   File "F:/mygit/python/Error/dealerror.py", line 165, in foo
#     return 10 / int(s)
# ZeroDivisionError: division by zero
# END

# 同样是出错，但程序打印完错误信息后会继续执行，并正常退出
# 稍后试试
# 通过配置，logging还可以把错误记录到日志文件里，方便事后排查。


# 抛出错误
# 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。
# Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

# 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：
class FooError(ValueError):
    pass
def foo(s):
    n=int(s);
    if n==0:
        raise FooError('invaild error %s'% n);
    return 20/n;
#foo('0');

# Traceback (most recent call last):
#   File "F:/mygit/python/Error/dealerror.py", line 206, in <module>
#     foo('0');
#   File "F:/mygit/python/Error/dealerror.py", line 204, in foo
#     raise FooError('invaild error %s'% n);
# __main__.FooError: invaild error 0

# 只有在必要的时候才定义我们自己的错误类型。
# 如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。





# 最后，我们来看另一种错误处理的方式：
def foo(s):
    n=int(s);
    if n==0:
        raise  ValueError('invalidvalue error: %s'%n);
    return 10/n;
def bar ():
    try:
        foo('0');
    except ValueError as e:
        print('InvailValueError');
        raise

# bar() # InvailValueError 并把foo中ValueError原样输出，导致程序中断
#
# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
#
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，
# 所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，
# 如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
#
# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：

# try:
#     10/0;
# except ZeroDivisionError:
#     raise  ValueError('INPUT ERROR');

# During handling of the above exception, another exception occurred:
#
# Traceback (most recent call last):
#   File "F:/mygit/python/Error/dealerror.py", line 248, in <module>
#     raise  ValueError('INPUT ERROR');
# ValueError: INPUT ERROR
# 只要是合理的转换逻辑就可以，但是，决不应该把一个IOError转换成毫不相干的ValueError。


from functools import reduce

def str2num(s):
    return float(s)

def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)

def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)

main()

print(1)
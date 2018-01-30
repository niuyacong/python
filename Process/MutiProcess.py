#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'多进程 module'
__author__ = 'nyc'
#概要：
# 1、Process在windows下不可使用
# 2、multiprocessing支持windows
# 3、进程池
# 4、子进程
# 5、进程间通信

####
#以下内容在windows下不可实现
# 要让Python程序实现多进程（multiprocessing），我们先了解操作系统的相关知识。
#
# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
#
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()就可以拿到父进程的ID。
#
# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程：
#
# import os
#
# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# 运行结果如下：
#
# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.
# 由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！
#
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求
#
###



#　multiprocessing

# 如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？
#
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
#
# multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run Child process %s (%s)..'%(name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s .' % os.getpid());
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start();
    p.join();
    print('Child process end.')
# Parent process 17584 .
# Child process will start.
# Run Child process test (9224)..
# Child process end.
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
#
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。


# Pool
#
# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
from multiprocessing import Pool
import os,time,random

def long_time_task(name):
    print('Run task %s (%s)..' % (name,os.getpid()))
    start=time.time()
    time.sleep(random.random()*3)
    end=time.time()
    print('Task %s runs %0.2f seconds .' %(name,(end-start)))

if __name__=='__main__':
    print('Parent process %s .'%os.getpid())
    p=Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('Waitting for all subprocess done..');
    p.close();
    p.join();
    print('All subprocess done.')
# Parent process 18036 .
# Waitting for all subprocess done..
# Run task 0 (17356)..
# Run task 1 (13080)..
# Run task 2 (8612)..
# Run task 3 (13896)..
# Task 3 runs 0.56 seconds .
# Run task 4 (13896)..
# Task 4 runs 0.49 seconds .
# Task 2 runs 1.85 seconds .
# Task 0 runs 2.25 seconds .
# Task 1 runs 2.98 seconds .
# All subprocess done.


# 代码解读：
#
# 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
#
# 请注意输出的结果，task 0，1，2，3是立刻执行的，而task 4要等待前面某个task完成后才执行，这是因为Pool的默认大小在我的电脑上是4，因此，最多同时执行4个进程。这是Pool有意设计的限制，并不是操作系统的限制。如果改成：
#
# p = Pool(5)
# 就可以同时跑5个进程。
#
# 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到上面的等待效果

# ## ???问题？
# 如果在这段代码前面加上print('pool..') 那么在进程池执行当中会多次执行这个print

# 子进程
#
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。
#
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
#
# 下面的例子演示了如何在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
import subprocess
print('$ nslookup www.python.org')
r=subprocess.call(['nslookup','www.python.org'])# nslookup是用来解析域名的,子进程用来输出解析的域名
print('Exit code:', r)

# $ nslookup www.python.org
# ��Ȩ��Ӧ��:
# ������:  Cache4-zone1-sjz
# Address:  222.222.222.222
#
# ����:    python.map.fastly.net
# Addresses:  2a04:4e42:36::223
# 	  151.101.228.223
# Aliases:  www.python.org
#
# Exit code: 0


# 如果子进程还需要输入，则可以通过communicate()方法输入：
import subprocess
print('$ nslookup')
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stderr=subprocess.PIPE)
# output,err=p.communicate(b'set q=mx\nbaidu.com\nexit\n')
p.communicate(b'set q=mx\npython.org\nexit\n')#　此方法没有返回数 ， 所以要输出上面的output err 都是NoneType
# 上面的代码相当于在命令行执行命令nslookup，然后手动输入：
# set q=mx
# python.org
# exit
print('Exit code：',p.returncode);
# $ nslookup
# Ĭ�Ϸ�����:  SJZ-CA6-ZONE2
# Address:  222.222.222.222
#
# > > ������:  SJZ-CA6-ZONE2
# Address:  222.222.222.222
#
# python.org	MX preference = 50, mail exchanger = mail.python.org
# > Exit code： 0

# 进程间通信
# Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
# Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
#
# 我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
from multiprocessing import Process,Queue
import os,time,random

# 写数据进程执行的代码
def write(q):
    print('Process to write :%s '% os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue ...'%value);
        q.put(value);
        time.sleep(random.random());
# 读数据进程执行的代码:
def read(q):
    print('Process to read : %s ' % os.getpid())
    while True:
        value=q.get(True);
        print('Get %s from queue...'% value)

if __name__=="__main__":
# 父进程创建Queue，并传给各个子进程：
    q= Queue();
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
# 启动子进程pw，写入:
    pw.start()
# 启动子进程pr，读取:
    pr.start()
# 等待pw结束:
    pw.join()
# pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

# Process to write :15500
# Put A to queue ...
# Process to read : 15324
# Get A from queue...
# Put B to queue ...
# Get B from queue...
# Put C to queue ...
# Get C from queue...


# 在Unix/Linux下，multiprocessing模块封装了fork()调用，使我们不需要关注fork()的细节。由于Windows没有fork调用，因此，multiprocessing需要“模拟”出fork的效果，父进程所有Python对象都必须通过pickle序列化再传到子进程去，所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
#
# 小结
#
# 在Unix/Linux下，可以使用fork()调用实现多进程。
#
# 要实现跨平台的多进程，可以使用multiprocessing模块。
#
# 进程间通信是通过Queue、Pipes等实现的。

#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'psutil module'
__author__ = 'nyc'
# 获取cpu信息
# 获取内存信息
# 获取磁盘信息
# 获取网络信息
# 获取进程信息

# 用Python来编写脚本简化日常的运维工作是Python的一个重要用途。在Linux下，有许多系统命令可以让我们时刻监控系统运行的状态，如ps，top，free等等。要获取这些系统信息，Python可以通过subprocess模块调用并获取结果。但这样做显得很麻烦，尤其是要写很多解析代码。
#
# 在Python中获取系统信息的另一个好办法是使用psutil这个第三方模块。顾名思义，psutil = process and system utilities，它不仅可以通过一两行代码实现系统监控，还可以跨平台使用，支持Linux／UNIX／OSX／Windows等，是系统管理员和运维小伙伴不可或缺的必备模块。
#
# 安装psutil
#
# 如果安装了Anaconda，psutil就已经可用了。否则，需要在命令行下通过pip安装：
#
# $ pip install psutil
# 如果遇到Permission denied安装失败，请加上sudo重试。


# 获取CPU信息
#
# 我们先来获取CPU的信息：
import  psutil
print(psutil.cpu_count());# CPU逻辑数量
# 4
print(psutil.cpu_count(logical=False)) # CPU物理核心
# 4
# 2说明是双核超线程, 4则是4核非超线程


# 统计CPU的用户／系统／空闲时间：
print(psutil.cpu_times());
# scputimes(user=34502.3828125, system=28281.75, idle=1378656.125, interrupt=292.2054672241211, dpc=270.5525302886963)

# 再实现类似top命令的CPU使用率，每秒刷新一次，累计10次：
for x in range(10):
    print(psutil.cpu_percent(interval=1,percpu=True))
[21.8, 26.2, 26.1, 28.1]
[9.4, 7.9, 4.8, 6.2]
[3.1, 10.8, 6.2, 13.8]
[13.8, 11.0, 6.2, 7.7]
[7.7, 6.2, 6.2, 4.8]
[9.4, 13.8, 13.8, 21.9]
[6.2, 3.1, 1.6, 10.8]
[7.9, 4.8, 4.6, 14.3]
[7.7, 7.7, 3.1, 7.9]
[7.9, 12.5, 3.1, 6.2]



# 获取内存信息
#
# 使用psutil获取物理内存和交换内存信息，分别使用：
print(psutil.virtual_memory());
# svmem(total=8543531008, available=2075205632, percent=75.7, used=6468325376, free=2075205632)
print(psutil.swap_memory());
# sswap(total=17085140992, used=9453932544, free=7631208448, percent=55.3, sin=0, sout=0)
# 返回的是字节为单位的整数，可以看到，总内存大小是8543531008 = 8 GB，6468325376 ，使用了75.7%。
#
# 而交换区大小是1073741824 = 1 .7GB。


# 获取磁盘信息
#
# 可以通过psutil获取磁盘分区、磁盘使用率和磁盘IO信息：
print(psutil.disk_partitions())# 磁盘分区信息
# [sdiskpart(device='C:\\', mountpoint='C:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='D:\\', mountpoint='D:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='E:\\', mountpoint='E:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='F:\\', mountpoint='F:\\', fstype='NTFS', opts='rw,fixed'), sdiskpart(device='G:\\', mountpoint='G:\\', fstype='', opts='cdrom')]
print(psutil.disk_usage("/"))# 磁盘使用情况
# sdiskusage(total=293584883712, used=34864001024, free=258720882688, percent=11.9)
print(psutil.disk_io_counters())# 磁盘IO
# sdiskio(read_count=1993847, write_count=2335317, read_bytes=45581486592, write_bytes=43696318976, read_time=401691, write_time=9024)
# 可以看到，磁盘'/'的总容量是293584883712 = 293 GB，使用了11.9%。文件格式是NTFS，opts中包含rw表示可读写，journaled表示支持日志。



# 获取网络信息
#
# psutil可以获取网络接口和网络连接信息：
print(psutil.net_io_counters())# 获取网络读写字节／包的个数

# snetio(bytes_sent=225305293, bytes_recv=1548070560, packets_sent=1594778, packets_recv=1829425, errin=0, errout=0, dropin=0, dropout=0)

print(psutil.net_if_addrs())# 获取网络接口信息

# {'本地连接 2': [snic(family=<AddressFamily.AF_LINK: -1>, address='00-FF-0A-51-E4-29', netmask=None, broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET: 2>, address='169.254.96.228', netmask='255.255.0.0', broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET6: 23>, address='fe80::d962:833f:36f0:60e4', netmask=None, broadcast=None, ptp=None)], '本地连接': [snic(family=<AddressFamily.AF_LINK: -1>, address='74-27-EA-CE-7E-80', netmask=None, broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET: 2>, address='192.168.190.245', netmask='255.255.255.0', broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET6: 23>, address='fe80::941b:d0e5:a5af:4fd5', netmask=None, broadcast=None, ptp=None)], 'VMware Network Adapter VMnet1': [snic(family=<AddressFamily.AF_LINK: -1>, address='00-50-56-C0-00-01', netmask=None, broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET: 2>, address='192.168.243.1', netmask='255.255.255.0', broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET6: 23>, address='fe80::1c82:6c05:da2b:ed4c', netmask=None, broadcast=None, ptp=None)], 'VMware Network Adapter VMnet8': [snic(family=<AddressFamily.AF_LINK: -1>, address='00-50-56-C0-00-08', netmask=None, broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET: 2>, address='192.168.75.1', netmask='255.255.255.0', broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET6: 23>, address='fe80::7193:fe78:f8d0:3941', netmask=None, broadcast=None, ptp=None)], 'isatap.{0A51E429-1AEF-4FF4-B4D9-DDD990C3B0D8}': [snic(family=<AddressFamily.AF_LINK: -1>, address='00-00-00-00-00-00-00-E0', netmask=None, broadcast=None, ptp=None)], 'Teredo Tunneling Pseudo-Interface': [snic(family=<AddressFamily.AF_LINK: -1>, address='00-00-00-00-00-00-00-E0', netmask=None, broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET6: 23>, address='fe80::100:7f:fffe', netmask=None, broadcast=None, ptp=None)], 'isatap.{D81B0613-8898-4638-BD9C-B1DE46D134B7}': [snic(family=<AddressFamily.AF_LINK: -1>, address='00-00-00-00-00-00-00-E0', netmask=None, broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET6: 23>, address='fe80::5efe:192.168.190.245', netmask=None, broadcast=None, ptp=None)], 'isatap.localdomain': [snic(family=<AddressFamily.AF_LINK: -1>, address='00-00-00-00-00-00-00-E0', netmask=None, broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET6: 23>, address='fe80::5efe:192.168.75.1', netmask=None, broadcast=None, ptp=None)], 'isatap.{2D9E57B2-59C8-4C52-A2D4-25162569B827}': [snic(family=<AddressFamily.AF_LINK: -1>, address='00-00-00-00-00-00-00-E0', netmask=None, broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET6: 23>, address='fe80::5efe:192.168.243.1', netmask=None, broadcast=None, ptp=None)], 'Loopback Pseudo-Interface 1': [snic(family=<AddressFamily.AF_INET: 2>, address='127.0.0.1', netmask='255.0.0.0', broadcast=None, ptp=None), snic(family=<AddressFamily.AF_INET6: 23>, address='::1', netmask=None, broadcast=None, ptp=None)]}

print(psutil.net_if_stats())# 获取网络接口状态

# {'本地连接': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1000, mtu=1500), '本地连接 2': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=10, mtu=1500), 'VMware Network Adapter VMnet1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500), 'VMware Network Adapter VMnet8': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=100, mtu=1500), 'Loopback Pseudo-Interface 1': snicstats(isup=True, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=1073, mtu=1500), 'isatap.{0A51E429-1AEF-4FF4-B4D9-DDD990C3B0D8}': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1280), 'Teredo Tunneling Pseudo-Interface': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1472), 'isatap.{D81B0613-8898-4638-BD9C-B1DE46D134B7}': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1280), 'isatap.localdomain': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1280), 'isatap.{2D9E57B2-59C8-4C52-A2D4-25162569B827}': snicstats(isup=False, duplex=<NicDuplex.NIC_DUPLEX_FULL: 2>, speed=0, mtu=1280)}


# 要获取当前网络连接信息，使用net_connections()：
print(psutil.net_connections());
# [sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=85), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=139), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=1434), raddr=(), status='NONE', pid=2984), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49173), raddr=(), status='LISTEN', pid=588), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=80), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=135), raddr=(), status='LISTEN', pid=872), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=123), raddr=(), status='NONE', pid=364), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49190), raddr=addr(ip='127.0.0.1', port=49191), status='ESTABLISHED', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=9974), raddr=(), status='LISTEN', pid=9768), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49153), raddr=(), status='LISTEN', pid=1004), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=4300), raddr=(), status='LISTEN', pid=3336), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=4530), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=51213), raddr=addr(ip='101.199.97.177', port=80), status='ESTABLISHED', pid=4980), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5353), raddr=(), status='NONE', pid=5272), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49161), raddr=addr(ip='127.0.0.1', port=49160), status='ESTABLISHED', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=2105), raddr=(), status='LISTEN', pid=2092), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=9974), raddr=addr(ip='127.0.0.1', port=53509), status='ESTABLISHED', pid=9768), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=59527), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=85), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=445), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=56883), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=2012), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.75.1', port=137), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=50205), raddr=addr(ip='223.252.199.69', port=6003), status='ESTABLISHED', pid=4564), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49157), raddr=(), status='LISTEN', pid=2092), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=5939), raddr=(), status='LISTEN', pid=2428), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=58612), raddr=addr(ip='127.0.0.1', port=58611), status='ESTABLISHED', pid=13368), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=52803), raddr=addr(ip='159.8.209.221', port=5938), status='ESTABLISHED', pid=2428), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49194), raddr=(), status='LISTEN', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5353), raddr=(), status='NONE', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49159), raddr=addr(ip='127.0.0.1', port=49158), status='ESTABLISHED', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=53458), raddr=addr(ip='203.208.43.76', port=443), status='ESTABLISHED', pid=5272), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=83), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=9973), raddr=(), status='LISTEN', pid=9768), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=1801), raddr=(), status='LISTEN', pid=2092), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=5355), raddr=(), status='NONE', pid=1292), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49188), raddr=addr(ip='127.0.0.1', port=49187), status='ESTABLISHED', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=83), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49158), raddr=addr(ip='127.0.0.1', port=49159), status='ESTABLISHED', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5353), raddr=(), status='NONE', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=2012), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=81), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=58610), raddr=addr(ip='127.0.0.1', port=58609), status='ESTABLISHED', pid=13368), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5355), raddr=(), status='NONE', pid=1292), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=50411), raddr=(), status='NONE', pid=2640), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=78), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=57755), raddr=(), status='LISTEN', pid=1452), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=135), raddr=(), status='LISTEN', pid=872), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.75.1', port=139), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=1434), raddr=(), status='LISTEN', pid=2196), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=58611), raddr=addr(ip='127.0.0.1', port=58612), status='ESTABLISHED', pid=13368), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=57242), raddr=(), status='NONE', pid=5272), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=54533), raddr=addr(ip='192.168.190.4', port=9100), status='SYN_SENT', pid=1452), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=2107), raddr=(), status='LISTEN', pid=2092), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=4530), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=5353), raddr=(), status='NONE', pid=5272), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=1026), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=58609), raddr=addr(ip='127.0.0.1', port=58610), status='ESTABLISHED', pid=13368), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=2383), raddr=(), status='LISTEN', pid=2264), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=2105), raddr=(), status='LISTEN', pid=2092), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=51077), raddr=addr(ip='123.151.14.56', port=80), status='CLOSE_WAIT', pid=3336), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49176), raddr=(), status='LISTEN', pid=4116), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='169.254.57.65', port=5353), raddr=(), status='NONE', pid=2428), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=62268), raddr=addr(ip='61.151.217.106', port=80), status='CLOSE_WAIT', pid=3336), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=55436), raddr=addr(ip='120.92.91.106', port=80), status='CLOSE_WAIT', pid=7444), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.243.1', port=138), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=1433), raddr=(), status='LISTEN', pid=2196), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49156), raddr=(), status='LISTEN', pid=424), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=63342), raddr=(), status='LISTEN', pid=13368), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=4301), raddr=(), status='LISTEN', pid=3336), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49160), raddr=addr(ip='127.0.0.1', port=49161), status='ESTABLISHED', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=52709), raddr=addr(ip='123.151.152.54', port=80), status='CLOSE_WAIT', pid=3336), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=80), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=81), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=53490), raddr=addr(ip='116.207.160.54', port=80), status='CLOSE_WAIT', pid=7444), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=445), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=2383), raddr=(), status='LISTEN', pid=2264), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=9974), raddr=(), status='LISTEN', pid=9768), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=902), raddr=(), status='LISTEN', pid=3420), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49191), raddr=addr(ip='127.0.0.1', port=49190), status='ESTABLISHED', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=8080), raddr=(), status='LISTEN', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=63369), raddr=(), status='NONE', pid=2428), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=6942), raddr=(), status='LISTEN', pid=13368), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=61604), raddr=addr(ip='101.227.162.139', port=8080), status='ESTABLISHED', pid=6476), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49187), raddr=addr(ip='127.0.0.1', port=49188), status='ESTABLISHED', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=500), raddr=(), status='NONE', pid=424), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49265), raddr=addr(ip='127.0.0.1', port=5939), status='ESTABLISHED', pid=5520), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=2103), raddr=(), status='LISTEN', pid=2092), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=88), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=56883), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=123), raddr=(), status='NONE', pid=364), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49176), raddr=(), status='LISTEN', pid=4116), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.190.245', port=5353), raddr=(), status='NONE', pid=2428), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=55739), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=78), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=88), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=33848), raddr=(), status='NONE', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=54703), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.190.245', port=138), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=59527), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.243.1', port=5353), raddr=(), status='NONE', pid=2428), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49153), raddr=(), status='LISTEN', pid=1004), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=33848), raddr=(), status='NONE', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=8001), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=51269), raddr=addr(ip='101.199.97.163', port=80), status='ESTABLISHED', pid=7632), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=3600), raddr=(), status='NONE', pid=4980), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=1026), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=55437), raddr=addr(ip='120.92.91.106', port=80), status='CLOSE_WAIT', pid=7444), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.243.1', port=139), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=4500), raddr=(), status='NONE', pid=424), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=57835), raddr=(), status='NONE', pid=3336), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=50027), raddr=addr(ip='127.0.0.1', port=9974), status='ESTABLISHED', pid=10064), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=55739), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=8001), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=912), raddr=(), status='LISTEN', pid=3420), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49152), raddr=(), status='LISTEN', pid=492), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=58921), raddr=(), status='NONE', pid=4980), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=55435), raddr=addr(ip='120.92.91.106', port=80), status='CLOSE_WAIT', pid=7444), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=500), raddr=(), status='NONE', pid=424), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=1433), raddr=(), status='LISTEN', pid=2196), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=9974), raddr=addr(ip='127.0.0.1', port=50027), status='ESTABLISHED', pid=9768), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=56065), raddr=addr(ip='14.17.41.210', port=80), status='CLOSE_WAIT', pid=3336), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=49485), raddr=addr(ip='192.168.190.1', port=80), status='ESTABLISHED', pid=4980), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49194), raddr=(), status='LISTEN', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=3306), raddr=(), status='LISTEN', pid=2296), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=5939), raddr=addr(ip='127.0.0.1', port=49265), status='ESTABLISHED', pid=2428), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49154), raddr=(), status='LISTEN', pid=596), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49273), raddr=addr(ip='127.0.0.1', port=49274), status='ESTABLISHED', pid=5520), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='fe80::7193:fe78:f8d0:3941', port=5353), raddr=(), status='NONE', pid=2428), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=4009), raddr=(), status='NONE', pid=3336), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.243.1', port=137), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=65211), raddr=addr(ip='180.163.238.135', port=80), status='ESTABLISHED', pid=4980), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49173), raddr=(), status='LISTEN', pid=588), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=54534), raddr=addr(ip='127.0.0.1', port=9229), status='SYN_SENT', pid=10064), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.75.1', port=138), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49156), raddr=(), status='LISTEN', pid=424), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=63370), raddr=(), status='NONE', pid=2428), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=3306), raddr=(), status='LISTEN', pid=2296), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=54535), raddr=addr(ip='127.0.0.1', port=9229), status='SYN_SENT', pid=10064), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=86), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=9975), raddr=(), status='LISTEN', pid=9768), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=49152), raddr=(), status='LISTEN', pid=492), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=62626), raddr=(), status='NONE', pid=7632), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=51527), raddr=addr(ip='121.42.33.20', port=8306), status='CLOSE_WAIT', pid=8968), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=49274), raddr=addr(ip='127.0.0.1', port=49273), status='ESTABLISHED', pid=5520), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=86), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=1801), raddr=(), status='LISTEN', pid=2092), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49157), raddr=(), status='LISTEN', pid=2092), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=8080), raddr=(), status='LISTEN', pid=1672), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=1434), raddr=(), status='NONE', pid=2984), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=49154), raddr=(), status='LISTEN', pid=596), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='192.168.190.245', port=137), raddr=(), status='NONE', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=2, laddr=addr(ip='::', port=4500), raddr=(), status='NONE', pid=424), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=2107), raddr=(), status='LISTEN', pid=2092), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=53509), raddr=addr(ip='127.0.0.1', port=9974), status='ESTABLISHED', pid=10064), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=2, laddr=addr(ip='0.0.0.0', port=57836), raddr=(), status='NONE', pid=3336), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::1', port=1434), raddr=(), status='LISTEN', pid=2196), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=54703), raddr=(), status='LISTEN', pid=4), sconn(fd=-1, family=<AddressFamily.AF_INET6: 23>, type=1, laddr=addr(ip='::', port=57755), raddr=(), status='LISTEN', pid=1452), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='192.168.190.245', port=54197), raddr=addr(ip='180.163.251.43', port=80), status='CLOSE_WAIT', pid=7632), sconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='0.0.0.0', port=2103), raddr=(), status='LISTEN', pid=2092)]

# 你可能会得到一个AccessDenied错误，原因是psutil获取信息也是要走系统接口，而获取网络连接信息需要root权限，这种情况下，可以退出Python交互环境，用sudo重新启动：
#
# $ sudo python3
# Password: ******
# Python 3.6.3 ... on darwin
# Type "help", ... for more information.
# >>> import psutil
# >>> psutil.net_connections()



# 获取进程信息
#
# 通过psutil可以获取到所有进程的详细信息：
print(psutil.pids());# 所有进程ID
[0, 4, 348, 416, 484, 492, 540, 588, 596, 604, 696, 872, 952, 1004, 128, 364, 424, 1268, 1292, 1452, 1552, 1708, 1732, 1760, 1824, 1896, 1192, 1468, 1672, 1920, 2092, 2196, 2264, 2296, 2400, 2640, 2700, 2984, 3024, 2012, 2428, 3140, 3180, 3228, 3256, 3420, 3652, 3688, 4072, 4116, 4160, 4168, 4700, 3524, 4688, 4780, 4980, 4864, 3412, 1140, 2948, 2660, 5224, 5520, 6556, 6564, 3508, 5272, 6332, 6608, 6032, 7632, 6340, 2444, 7460, 5952, 6044, 6732, 3168, 8472, 8480, 8340, 8968, 5236, 7276, 6060, 7688, 5492, 6168, 1744, 7800, 5048, 4564, 10164, 7408, 10252, 4836, 10068, 5744, 11968, 5284, 12616, 6896, 9480, 14460, 12008, 10372, 10064, 6580, 16340, 9768, 14856, 15524, 16136, 13368, 13900, 14252, 7444, 3336, 14696, 6476, 10808, 10796, 6908, 9220, 396]

p=psutil.Process(14720)#  获取指定进程ID=3776，其实就是当前Python交互环境
print(p)
# psutil.Process(pid=13368, name='pycharm64.exe')
print(p.name());# 进程名称
# pycharm64.exe
print(p.exe())# 进程exe路径
# D:\python\PyCharm 2017.2.3\bin\pycharm64.exe
print(p.cwd())# 进程工作目录
# C:\Windows\system32
print(p.cmdline());# 进程启动的命令行
# ['D:\\python\\PyCharm 2017.2.3\\bin\\pycharm64.exe']
print(p.ppid())# 父进程ID
# 4780
print(p.parent())# 父进程
# psutil.Process(pid=4780, name='explorer.exe')
print(p.children())# 子进程列表
# [<psutil.Process(pid=13900, name='fsnotifier64.exe') at 35710288>, <psutil.Process(pid=16172, name='python.exe') at 39402856>]
print(p.status())# 进程状态
# running
print(p.username())# 进程用户名
# J-PC\Administrator
print(p.create_time())# 进程创建时间
# 1519710008.0

# print(p.terminal())# 进程终端
# AttributeError: 'Process' object has no attribute 'terminal'

print(p.cpu_times())# 进程使用的CPU时间
# pcputimes(user=150.5565651, system=6.4896416, children_user=0.0, children_system=0.0)

print(p.memory_info())# 进程使用的内存
# pmem(rss=739237888, vms=789250048, num_page_faults=491166, peak_wset=739278848, wset=739237888, peak_paged_pool=388368, paged_pool=356592, peak_nonpaged_pool=85448, nonpaged_pool=57816, pagefile=789250048, peak_pagefile=790175744, private=789250048)

print(p.open_files())# 进程打开的文件
# [popenfile(path='D:\\python\\PyCharm 2017.2.3\\lib\\jdom.jar', fd=-1)....]

print(p.connections())# 进程相关网络连接
# [pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=58662), raddr=addr(ip='127.0.0.1', port=58663), status='ESTABLISHED'), pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=58661), raddr=addr(ip='127.0.0.1', port=58660), status='ESTABLISHED'), pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=63342), raddr=(), status='LISTEN'), pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=58663), raddr=addr(ip='127.0.0.1', port=58662), status='ESTABLISHED'), pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=58660), raddr=addr(ip='127.0.0.1', port=58661), status='ESTABLISHED'), pconn(fd=-1, family=<AddressFamily.AF_INET: 2>, type=1, laddr=addr(ip='127.0.0.1', port=6942), raddr=(), status='LISTEN')]

print(p.num_threads())# 进程的线程数量
#45

print(p.threads())# 所有线程信息
# [pthread(id=9300, user_time=0.7644048999999999, system_time=0.18720119999999998), ......]

print(p.environ()) # 进程环境变量
# {'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming',...}

# p.terminate() # 结束进程,自己把自己结束了


# 和获取网络连接类似，获取一个root用户的进程需要root权限，启动Python交互环境或者.py文件时，需要sudo权限。
#
# psutil还提供了一个test()函数，可以模拟出ps命令的效果：
#
# $ sudo python3
# Password: ******
# Python 3.6.3 ... on darwin
# Type "help", ... for more information.
# >>> import psutil
# >>> psutil.test()

psutil.test()
# USER         PID %MEM     VSZ     RSS TTY           START    TIME  COMMAND
# SYSTEM         0    ?       ?      24 ?             Feb23   02:55  System Idle Process
# SYSTEM         4    ?     128      52 ?             Feb23   23:50  System
#              128  0.1    6044    8320 ?             Feb23   00:01  svchost.exe
#              348    ?     572     132 ?             Feb23   00:00  smss.exe
#              364  0.3   11716   24020 ?             Feb23   00:19  svchost.exe
#              416    ?    2896    3508 ?             Feb23   00:13  csrss.exe
#              424  0.6   47096   49492 ?             Feb23   11:46  svchost.exe
#              484  0.7   15824   62204 ?             Feb23   03:05  csrss.exe
#              492    ?    1700     256 ?             Feb23   00:01  wininit.exe
#              540    ?    3524    3012 ?             Feb23   00:03  winlogon.exe
#              588  0.1    7284    7556 ?             Feb23   02:03  services.exe
#              596  0.1    6696    9648 ?             Feb23   02:48  lsass.exe
#              604    ?    4000    3592 ?             Feb23   00:58  lsm.exe
#              696  0.1    5604    7048 ?             Feb23   01:08  svchost.exe
#              872  0.1    6740    6760 ?             Feb23   00:12  svchost.exe
#              952    ?    1768    1228 ?             Feb23   00:00  atiesrxx.exe
#             1004  0.2   27992   16884 ?             Feb23   02:19  svchost.exe
# Administra  1140  0.2   32092   16848 ?             Feb23   01:19  TSVNCache.exe
#             1192    ?   19188    1788 ?             Feb23   00:00  jenkins.exe
#             1268  0.1   44388    6340 ?             Feb23   00:12  ZhuDongFangYu.exe
#             1292  0.1   15532   12400 ?             Feb23   01:40  svchost.exe
#             1452  0.1   10796   10648 ?             Feb23   02:40  spoolsv.exe
#             1468    ?   74276    1964 ?             Feb23   00:06  MsDtsSrvr.exe
#             1552  0.1   11772    8872 ?             Feb23   00:58  svchost.exe
#             1672  1.0  157688   83828 ?             Feb23   00:43  java.exe
#             1708    ?    4836    1556 ?             Feb23   00:00  svchost.exe
#             1732  0.1    9100   10376 ?             Feb23   00:05  svchost.exe


# 小结
#
# psutil使得Python程序获取系统信息变得易如反掌。
#
# psutil还可以获取用户信息、Windows服务等很多有用的系统信息，具体请参考psutil的官网：https://github.com/giampaolo/psutil


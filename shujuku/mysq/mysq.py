#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'mysql module'
__author__ = 'nyc'

# MySQL是Web世界中使用最广泛的数据库服务器。SQLite的特点是轻量级、可嵌入，但不能承受高并发访问，适合桌面和移动应用。而MySQL是为服务器端设计的数据库，能承受高并发访问，同时占用的内存也远远大于SQLite。
#
# 此外，MySQL内部有多种数据库引擎，最常用的引擎是支持数据库事务的InnoDB。
#
# 安装MySQL
#
# 可以直接从MySQL官方网站下载最新的Community Server 5.6.x版本。MySQL是跨平台的，选择对应的平台下载安装文件，安装即可。
#
# 安装时，MySQL会提示输入root用户的口令，请务必记清楚。如果怕记不住，就把口令设置为password。
#
# 在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。
#
# 在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在/etc/my.cnf或者/etc/mysql/my.cnf：
# mysql> show variables like '%char%';
# 看到utf8字样就表示编码设置正确。

# 注：如果MySQL的版本≥5.5.3，可以把编码设置为utf8mb4，utf8mb4和utf8完全兼容，但它支持最新的Unicode标准，可以显示emoji字符。
# 安装MySQL驱动
#
# 由于MySQL服务器以独立的进程运行，并通过网络对外服务，所以，需要支持Python的MySQL驱动来连接到MySQL服务器。MySQL官方提供了mysql-connector-python驱动，但是安装的时候需要给pip命令加上参数--allow-external：
#
# $ pip install mysql-connector-python --allow-external mysql-connector-python
# 如果上面的命令安装失败，可以试试另一个驱动：
#
# $ pip install mysql-connector


# 连接到MySQL服务器的test数据库：
# 导入MySQL驱动:
import  mysql.connector
# 注意把password设为你的root口令:
conn=mysql.connector.connect(user='root',password='111111',database='test')
cursor=conn.cursor();
# 创建user表:

# cursor.execute('create table user(id VARCHAR (20) PRIMARY KEY ,name VARCHAR (200)) ');

# 插入一行记录，注意MySQL的占位符是%s:
cursor.execute('insert into user(id,name) values(%s,%s)',['1','niu'])
print(cursor.rowcount)
# 提交事务:
conn.commit()
cursor.close()

cursor=conn.cursor()
cursor.execute('select * from user where id =%s',('1',));
value=cursor.fetchall()
print(value)
cursor.close()
conn.close()

# 由于Python的DB-API定义都是通用的，所以，操作MySQL的数据库代码和SQLite类似。
#
# 小结
#
# 执行INSERT等操作后要调用commit()提交事务；
#
# MySQL的SQL占位符是%s。



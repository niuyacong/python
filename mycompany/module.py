#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'a test module'
__author__ = 'nyc'

# 通过包来组织模块，避免冲突。方法是选择一个顶层包名，比如mycompany
#
# 引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。现在，module.py模块的名字就变成了mycompany.module
# 测试可以在主目录下的module1.py中测试
#
def companyTest():
    print('mycompany包下的模块');
companyTest() # mycompany包下的模块
# 规范：
# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，
# 否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，
# 因为__init__.py本身就是一个模块，而它的模块名就是mycompany。

# 创建自己的模块时，要注意：
#
# 模块名要遵循Python变量命名规范，不要使用中文、特殊字符；
# 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块。

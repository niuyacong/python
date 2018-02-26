#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'HTMLParser module'
__author__ = 'nyc'


# 如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。
#
# 假设第一步已经完成了，第二步应该如何解析HTML呢？
#
# HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。
#
# 好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：

from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('<%s>'%tag);
    def handle_endtag(self, tag):
        print('</%s>'%tag);
    def handle_startendtag(self, tag, attrs):
        print('<%s/>'%tag);
    def handle_data(self, data):
        print(data);
    def handle_comment(self, data):
        print('<!--',data,'-->');
    def handle_entityref(self, name):
        print('&%s;'%name);
    def handle_charref(self, name):
        print('&#%s;'%name)
parser = MyHTMLParser()
parser.feed('''<html>
<head></head>
<body>
<!-- test html parser -->
    <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
</body></html>''')

# < html >
#
# < head >
# < / head >
#
# < body >
#
# < !--  test
# html
# parser -->
#
# < p >
# Some
# < a >
# html
# < / a >
# HTML tutorial...
# < br >
# END
# < / p >
#
# < / body >
# < / html >

# feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。
#
# 特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。



# 小结
#
# 利用HTMLParser，可以把网页中的文本、图像等解析出来。
from html.parser import HTMLParser
from urllib import  request
import re

class MyHtmlParser(HTMLParser):

    da = ''
    flag = 0
    res = []

    #开始标签
    def handle_starttag(self, tag, attrs):
        if tag =='ul':
            print(attrs[0])
            for att in attrs:
                if 'list-recent-events menu' in att[1]:
                    self.flag = 1
        if tag == 'time'and self.flag == 1:
            self.da = 'time'

        if tag == 'span'and self.flag == 1:
            self.da = 'address'

        if tag == 'a'and self.flag == 1:
            self.da = 'title'


    def handle_endtag(self, tag):
       if tag == 'ul'and self.flag == 1:
          self.flag=0

    def handle_data(self, data):
        if self.flag ==1 and self.da != '':
            if self.da =='title':
                self.res.append({'title': data, 'time': '', 'address': ''})
            else:
                self.res[len(self.res)-1][self.da] = data
            self.da = ''

Parser = MyHtmlParser()

with request.urlopen('https://www.python.org/events/python-events/')as f:
    data = f.read().decode('utf-8')

Parser.feed(data)
for item in Parser.res:
    print('---------------------')
    for k,v in item.items():
        print('%s: %s'%(k,v))
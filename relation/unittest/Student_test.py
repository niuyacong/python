#!/usr/bin/env python3 
# -*- coding: utf-8 -*-  

'a test module'
__author__ = 'nyc'

import unittest

from Error.unittest import  Student

# class TestStudent(unittest.TestCase):
#     def test_init(self):
#         n=Student('nyc',100);
#         self.assertEqual(n.name,'nyc');
#         self.assertEqual(n.score,100)
#         self.assertTrue(isinstance(n,Student));
#
#     def test_attr(self):
#         a=Student('NYC',100);
#         self.assertEqual(a.get_grade(),'A');
#         b=Student('B',70);
#         self.assertEqual(b.get_grade(),'B');
#         c=Student('c',50);
#         self.assertEqual(c.get_grade(),'C');

# 测试例子：
# 不同之处：
# 测试get_score()用的两端临界值
# 学生分数是0到100之间，所以Student类中超过100，或者小于0的应该抛出异常
class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()
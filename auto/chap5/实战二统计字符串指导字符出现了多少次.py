# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

s='HelloPython,HelloJava,hellophp'
h=input("请输入要统计的字符：")
count=s.lower().count(h)
print('{0}在{1}中一共出现了{2}次'.format(h,s,count))
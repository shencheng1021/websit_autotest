# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

s='hellowlord'

print('{0:*^20}'.format(s))#字符串显示宽度20，居中对其，空白的部分用*补齐

print('{0:*<20}'.format(s))#字符串显示宽度20，左对其，空白的部分用*补齐

print('{0:*>20}'.format(s))#字符串显示宽度20，右对其，空白的部分用*补齐

print(s.center(20,'*'))   #center方法居中对齐

#千位分隔符用逗号表示，只试用于数字
print('{0:,}'.format(546764562454674))
print('{0:,}'.format(5467645654674.454))

#使用.数字f来控制保留几位小数
print('{0:.1f}'.format(3.1453214))

#使用.数字来控制字符串的最大长度
print('{0:.5}'.format(s))
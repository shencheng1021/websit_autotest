# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import re

ret=r'\d\.\d+'

s='3.454ewqdadgd gdfg dgdf dghsdf hgh 5.321'

match=re.match(ret,s,re.I)
print(match)
print('匹配结果得开始位置：' , match.start())
print('匹配结果得结束位置：' ,match.end())
print('匹配结果值：' ,match.group())
print('匹配结果得区间：' ,match.span())
print('匹配的字符串：' ,match.string)







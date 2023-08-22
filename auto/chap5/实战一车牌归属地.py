# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import re

list=['京A197776','津B3H876','晋A87B8','沪A765888','川S1932D5']

pattern=r'[A-Z]{1}'

for item in list:
    search=re.split(pattern,item)
    print(item+' '+'归属地：'+search[0])
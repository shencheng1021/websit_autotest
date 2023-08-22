# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import re

pattern='[a-z]?#\d{2,4}'
s='asffwe#1242455#145766sad$#dasd.#23213ff'
a='xxx'
sub=re.sub(pattern,a,s,flags=0)
print(sub)

split=re.split(pattern,s,flags=0)
print(split)



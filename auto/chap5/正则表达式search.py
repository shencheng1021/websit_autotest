# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import re

pattern='\d+\.[a-z]{3}'
s='啊沙发沙发dasd13.124.fsdfdg234fsdf113@#$55.qwefdf54622'
search=re.search(pattern,s,flags=0)
print(search.group())
print(search.start())



# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

import re

pattern=r'[a-z]{4}\.\d{2,4}'
s='qwerr@wrrr.344sdfffgdvc.12354445.daff'
findall=re.findall(pattern,s,flags=0)
print(findall)

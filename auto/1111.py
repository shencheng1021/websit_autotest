# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

count=0

for i in range(1,100):
    if i % 2==0:
        count -=1
    else:
        count +=1
print(count)
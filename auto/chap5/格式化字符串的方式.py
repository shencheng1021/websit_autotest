# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

name = '张三'
age =25
score=98.5

#1、使用占位符进行格式化
print('姓名:%s,年龄：%d,成绩：%0.1f'%(name,age,score))

#2、f-string方式进行格式化

print(f'姓名：{name},年龄：{age},成绩：{score}')

#3、使用.format方式格式化格式
print('姓名：{0},年龄：{1},成绩{2}'.format(name,age,score))


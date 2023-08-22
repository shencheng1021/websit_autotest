# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

#判断是否未阿拉伯数字
print('04521450'.isdigit()) #TRUE

#判断是否为数字（阿拉伯数字、中文数字、罗马数字）
print('1一Ⅰ'.isnumeric())#TRUE

#判断字符串中都是字母(英文、中文)
print('weqeeee张三'.isalpha()) #TRUE
print('weqeeee张三123'.isalpha()) #flase
print('weqeeee张三一'.isalpha()) #TRUE

#判断字符串中都是中文+字母+数字(1,一、Ⅰ、壹)
print('helloword你好123'.isalnum())#TRUE
print('helloword你好123一二三ⅠⅣ壹贰'.isalnum())#TRUE


#判断字符串中是否都是小写字母
print('HelloWord'.islower()) #FLASE
print('helloword'.islower())#TRUE
print('hello你好'.islower())#TRUE

#所以字符都是大写吗？
print('Helloword'.isupper())#FLASE
print('HELLOWORD'.isupper())#TRUE
print('HELLOWORD你好'.isupper())#TRUE

#判断首字母是否大写
print('Helloword'.istitle())#TRUE
print('helloword'.istitle())#FLASE
print('HelloWord'.istitle())#FLASE
print('Hello word'.istitle())#FLASE
print('Hello Word'.istitle())#TRUE
print('HElloword'.istitle())#FLASE

#判断是否都是空白字符
print('\t'.isspace())#TRUE
print('  '.isspace())#TRUE
print('\n'.isspace())#TRUE



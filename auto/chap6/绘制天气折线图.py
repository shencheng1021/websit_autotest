# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

from matplotlib import pyplot

# pyplot.plot([1,2,3,4,5],[1,7,5,3,8])
# print(pyplot.show())
import pandas
t=pandas.read_excel('七月天气预报.xlsx')
#用于中文处理
pyplot.rcParams['font.sans-serif']=['SimHei']

x=t['日期']
y=t['温度']
pyplot.figure(figsize=(12,6),facecolor='b')  #画布设置
pyplot.xlabel("七月份温度统计表")
pyplot.ylabel("温度/℃")
pyplot.yticks(range(17,37))
pyplot.plot(x,y,color='r',linestyle='--')
pyplot.show()
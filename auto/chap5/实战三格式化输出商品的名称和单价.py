# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""

list=[['编号','名称','品牌','单价'],['01','电风扇','美的','500'],['02','洗衣机','TCL','1000'],['03','微波炉','老板','400']]

for item in list:
    print('{0:<10}{1:<10}{2:<10}{3}'.format(item[0],item[1],item[2],item[3]))


print('---------------------格式化后得输出结果-------------------')
i=1
for item in list:
    if i == 1:
        print('{0:<10}{1:<10}{2:<10}{3}'.format(item[0], item[1], item[2], item[3]))
    else:
        print('{0:<10}{1:<10}{2:<10}￥{3:.2f}'.format('0000'+item[0],item[1],item[2],int(item[3])))
    i+=1

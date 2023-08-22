# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""


list=[['G1569','北京南-天津南','18:05','18:39','00:34'],['G1567','北京南-天津南','18:15','18:49','00:34']
    ,['G8917','北京南-天津西','18:20','19:19','00:59'],['G203','北京南-天津南','18:35','19:09','00:34']]


for item in list:
    print(item)

while True:
    flag=False
    carid=input("请输入要购买的车次:")
    for item in list:
        if item[0]==carid:
            platform=item[1]
            starttime=item[2]
            username = input("请输入乘车人，如果是多个乘车人请使用逗号分隔：")
            print("您已购买了" + carid + "次列车，" + platform + '  ' + starttime + ' 开，请' + username + '尽快换取纸质车票。【铁路客服】')
            flag=True
            break

    if flag==False:
        print("输出的车次不存在请重新输入！")
        continue

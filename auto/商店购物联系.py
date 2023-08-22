# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
# d={'a':20,'b':50,'c':60}
# d2=d
# print(d2['b'])
# d['b']=100
# print(d2['b'])
#
# print(d['b']+d2['b'])
#
# list=[100,200]
# list.append(['200',300])
# print(len(list))

# list=[88,89,90,98,0,99]
# list2=[]
# #print(list2.append(list[0]))
#
# for i in range(0,len(list)):
#     if list[i] > 0:
#         list2.append(1900+list[i])
#     else:
#         list2.append(2000+list[i])
#
#
# print(list)
# print(list2)

# lst =[1,3,4,7,8]
# lst.reverse()
# print(lst.reverse())
# print(lst)

list=[]
for i in range(5):
    print("请输入商品名称和商品编号进行入库，每次只能输入一个商品：")
    t=input()
    list.append(t)


cart=[]
while True:
    print("请输出想要购买的商品编号：")
    num=input()
    flag=False
    if num=='q':
        print('关闭购物商店,您购物车中的商品为：')
        print(cart)
        break
    else:
        for item in list:
            if num==item[:4]:
                cart.append(item)
                flag=True
                break
    if flag==False and num!='q':
        print('你输出的商品编号不存在')











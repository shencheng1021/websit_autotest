# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
from web_test_tytest.common.excel_util import ExcelUtil


def demo01():

    list11=ExcelUtil().excel_read('login_data')
    for i in range(0,len(list11)):
        if list11[i][0] == 1:
            print(1)
        elif list11[i][0] == 2 or list11[i][0]==3 or list11[i][0]==4:
            print(2)
        elif list11[i][0] == 5:
            print(3)
        else:
            print(4)

if __name__ == '__main__':
    demo01()

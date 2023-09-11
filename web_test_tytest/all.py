# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: PyCharm
@description: test
@time: 2022/4/13 9:34
"""
import os

import allure
import pytest

if __name__ == '__main__':
    pytest.main(["-vs", "./test_case","--alluredir","./temp","--clean-alluredir"])
    os.system("allure generate ./temp -o ./report --clean")
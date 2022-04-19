# -*- coding: utf-8 -*-

"""
@author: shencheng
@software: 砼联数科官网
@description: 创建测试报告
@time: 2022/4/13 14:34
"""


import unittest

from HTMLTestRunner.HTMLTestRunner import HTMLTestRunner

title="砼联数科官网自动化测试"
description="砼联数科官网自动化测试，并自动生成报告"
suite=unittest.defaultTestLoader.discover("../test_case","test_login.py")
report_file=open("../report/reports.html","wb")
runner=HTMLTestRunner(stream=report_file, title=title, description=description)
runner.run(suite)

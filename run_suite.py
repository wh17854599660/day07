"""
测试套件：
    按照需求组合被执行的测试函数

自动化测试执行顺序：
        增--> 改--> 查--> 删
补充说明：
    关于测试套件的组织，接口业务测试中，需要保证测试套件中接口的执行顺序：
    合法实现：suite.addTest(类名（’函数名‘）)逐一添加
    非法实现：suite.addTest(unittest.makSuite(类名))虽然
"""
# 1，导包

import unittest

from app import PRO_PATH
from case.Test_IHRM_Emp import Test_Emp
from case.Test_IHRM_Login import Test_Login

# 2，实例化测试套件，组织被执行测试函数
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(Test_Login('test_login_success'))  # 组织登录测试函数
suite.addTest(Test_Emp('test_add'))  # 组织员工增测试函数
suite.addTest(Test_Emp('test_update'))  #组织员工修改测试函数
suite.addTest(Test_Emp('test_get'))  #组织员工查看测试函数
suite.addTest(Test_Emp('test_delete'))  #组织员工删除测试函数


# runner = unittest.TextTestRunner()
# runner.run(suite)
# 3，执行套件，生成测试报告
with open(PRO_PATH + '/report/report.html','wb') as f:
    runner = HTMLTestRunner(f,title='测试报告')
    #执行测试报告
    runner.run(suite)




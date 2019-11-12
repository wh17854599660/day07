"""
测试员工模块的增删改查实现
"""

# 1.导包
import logging

import requests
import unittest

import app
from api.EmpAPI import EmpCRUP

# 2。创建测试类
from case.Test_IHRM_Login import Test_Login


class Test_Emp(unittest.TestCase):
    # 3，初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCRUP()

    # 4，资源卸载
    def tearDown(self) -> None:
        self.session.close()

    # 5，测试函数1：增
    # 直接执行该测试函数失败原因：
    # 1，先执行登录操作  2，再提交银行卡
    # 解决：1，使用测试套件组织接口的执行顺序
    #     2，如何提交银行卡，如何关联
    #      核心步骤1：token的提取
    #       核心步骤2：token的提交
    def test_add(self):
        logging.info('员工新增信息')
        # 1,请求业务
        response = self.emp_obj.add(self.session, username='横华东数格式的环境少法', mobile='13900001210')
        # 2，断言业务
        print('员工新增响应结果：', response.json())
        id = response.json().get('data').get('id')
        app.USER_ID = id
        print('新增员工的ID：', id)
        self.assertEqual(True,response.json().get('success'))
        self.assertEqual(10000,response.json().get('code'))
        self.assertIn('操作成功',response.json().get('message'))

    # 6，测试函数3：改
    def test_update(self):
        logging.warning('员工修改信息')
        # 请求业务
        response = self.emp_obj.update(self.session, app.USER_ID, '哈歌美飒绝对方')
        # 断言业务
        print('修改后员工的ID：', response.json())
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    # 7，测试函数4：查
    def test_get(self):
        logging.info('员工查询信息')
        # 请求业务
        response = self.emp_obj.get(self.session, app.USER_ID)
        # 断言业务
        print('查询员工：', response.json())
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    # 8，测试函数2：删
    def test_delete(self):
        logging.info('员工删除信息')
        # 请求业务
        response = self.emp_obj.delete(self.session, app.BASE_URL)
        # 断言业务
        print("删除员工：", response.json())

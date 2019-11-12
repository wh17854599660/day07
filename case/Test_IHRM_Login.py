"""
封装unitest相关实现
"""
# 1，导包
import json
import unittest
import requests

import app
from api.LoginAPI import Login
from app import PRO_PATH

# 参数化1：导包
from parameterized import parameterized


# 参数化2：解析
def read_json_file():
    # 1.创建空列表
    data_list = []
    # 2.解析文件流，将数据
    with open(PRO_PATH + '/data/login_data.json', encoding='utf-8') as f:
        for v in json.load(f).values():
            data_list.append((v.get('mobile'),
                              v.get('password'),
                              v.get('success'),
                              v.get('code'),
                              v.get('message')))
            # print(v)
    # 返回列表
    return data_list


# 2，创建测试类（unittest.TestCase）
class Test_Login(unittest.TestCase):

    # 3.初始化函数
    def setUp(self) -> None:
        # 初始化session
        self.session = requests.session()
        # 测试api对象
        self.login_obj = Login()

    # 4.资源释放
    def tearDown(self) -> None:
        self.session.close()  # 销毁session

    # 5.核心：测试函数-登录
    # 5-1.参数化
    @parameterized.expand(read_json_file())  # 调用
    def test_login(self, mobile, password, success, code, message):
        print('_' * 95)
        print("参数化读取数据：", mobile, password, success, message)

        # 5-2.请求业务
        response = self.login_obj.login(self.session, mobile, password)  # 传参
        print("登录响应结果：", response.json())
        # 5-3.断言业务
        self.assertEqual(success, response.json().get('success'))
        self.assertEqual(code, response.json().get('code'))
        self.assertIn(message, response.json().get('message'))

    # 编写登录成功的测试函数
    def test_login_success(self):
        # 1.直接通过提交正向数据发送
        response = self.login_obj.login(self.session, '13800000002', '123456')

        # 2，断言业务  53c2bad2-e933-48c1-8e96-f8f0473944fa
        print('登录成功的结果：', response.json())
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))
        #提取token
        token = response.json().get('data')
        print('登录后响应token:',token)
        #预期允许其他文件调用该token，可以
        app.TOKEN = token
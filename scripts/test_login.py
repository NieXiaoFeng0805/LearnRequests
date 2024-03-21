# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/21 10:55
# software: PyCharm
"""
文件说明：

"""
import unittest

import config
from api.login_api import Login
import logging
from parameterized import parameterized
from utils import read_json_data


# class TestLogin_ByManualTest(unittest.TestCase):
#     def setUp(self) -> None:
#         '''
#         实例化封装的接口
#         :return:
#         '''
#         self.login_api = Login()
#
#     def test01_login_success(self):
#         # 发送登录请求并接收结果
#         response = self.login_api.login("15321919666", "123456")
#         # 使用logging 输出结果
#         logging.info(f"登录结果为：{response.json()}")
#         logging.info(f"显示cookies：{response.cookies}")
#         self.assertEquals(200, response.status_code)  # 断言响应状态码
#         self.assertEquals("响应成功", response.json().get("message"))
#
#     def test02_password_error(self):
#         # 发送登录请求并接收结果
#         response = self.login_api.login("15321919666", "12456")
#         # 使用logging 输出结果
#         logging.info(f"登录结果为：{response.json()}")
#         self.assertEquals(200, response.status_code)  # 断言响应状态码
#         self.assertEquals("用户名密码错误", response.json().get("message"))
#
#     def test03_phone_null(self):
#         '''
#         电话号码为空
#         :return:
#         '''
#         # 发送登录请求并接收结果
#         response = self.login_api.login("", "123456")
#         # 使用logging 输出结果
#         logging.info(f"登录结果为：{response.json()}")
#         self.assertEquals(200, response.status_code)  # 断言响应状态码
#         self.assertEquals("用户名密码错误", response.json().get("message"))
#
#     def test04_password_null(self):
#         '''
#         密码为空
#         :return:
#         '''
#         # 发送登录请求并接收结果
#         response = self.login_api.login("15321919666", "")
#         # 使用logging 输出结果
#         logging.info(f"登录结果为：{response.json()}")
#         self.assertEquals(200, response.status_code)  # 断言响应状态码
#         self.assertEquals("用户名密码错误", response.json().get("message"))

class TestLogin_ByAutoTest(unittest.TestCase):
    def setUp(self) -> None:
        self.login_api = Login()

    @parameterized.expand(read_json_data(config.BASE_PATH + "/data/login.json"))
    def test_login(self, case_name, phone, password, response_code, message):
        response = self.login_api.login(phone=phone, password=password)
        logging.info(f"{case_name}的结果为: {response.json()}")
        # logging.info(f"登录的cookie为:{response.json()}")
        self.assertEquals(response_code, response.status_code)
        self.assertEquals(message, response.json().get("message"))

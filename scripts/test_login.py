# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/21 10:55
# software: PyCharm
"""
文件说明：

"""
import unittest
from api.login_api import Login
import logging


class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        '''
        实例化封装的接口
        :return:
        '''
        self.login_api = Login()

    def test01_login_success(self):
        # 发送登录请求并接收结果
        response = self.login_api.login("15321919666", "13456")
        # 使用logging 输出结果
        logging.info("登录结果为：", response.json())

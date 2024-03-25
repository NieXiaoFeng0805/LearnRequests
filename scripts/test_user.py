import unittest

import config
from api.user_api import UserAPI
import logging
from jsonpath import jsonpath
from utils import get_login_token


class TestUser(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        get_login_token("15321919666", "123456")

    def setUp(self) -> None:
        self.user_api = UserAPI()

    def test_01_user_manager(self):
        # 查询用户列表
        request_body = {"currentPage": 1, "pageSize": 10}
        response = self.user_api.query_all_user(headers=config.BASE_HEADERS, request_body=request_body)
        logging.info(f"查询用户列表的结果为：{response.json()}")
        # 搜索用户
        request_body = {
            "currentPage": 1,
            "pageSize": 10,
            "username": '15588886123',
            "startCreateTime": "",
            "endCreateTime": ""
        }
        response = self.user_api.search_user(headers=config.BASE_HEADERS, request_body=request_body)
        logging.info(f"搜索指定用户结果为：{response}")
        # 查询用户权限
        response = self.user_api.query_user_Auth(config.BASE_HEADERS)
        logging.info(f"查询到的用户权限为：{response.json()}")

        # 冻结/解冻用户
        response = self.user_api.frOrUnfr_user(headers=config.BASE_HEADERS)
        logging.info(f"冻结id为 100030011 的用户，结果为{response}")

        response = self.user_api.frOrUnfr_user(headers=config.BASE_HEADERS)
        logging.info(f"解冻id为 100030011 的用户，结果为{response}")
        # 修改用户权限
        response = self.user_api.modify_user_root(headers=config.BASE_HEADERS)
        logging.info(f"修改用户权限, 结果为：{response}")

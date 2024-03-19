# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/19 20:23
# software: PyCharm
"""
文件说明：

"""
import requests
import config


class Login:
    def __init__(self):
        self.edu_url = config.BASE_LaGouEDU_URL + "/ssm_web/user/login"
        self.shop_url = config.BASE_LaGouShop_URL

    def login(self, phone, password):
        return requests.post(url=self.edu_url,
                             params={"phone": phone, "password": password})

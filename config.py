# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/19 19:48
# software: PyCharm
"""
文件说明：配置公有属性
"""

import os.path

BASE_LaGouEDU_URL = "http://192.168.80.106:8080"
BASE_LaGouShop_URL = "http://192.168.85.139"
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
BASE_HEADERS = {
    "Content-Type": "application/json",
    # "Authorization": "f631edee-35bc-4cd8-b580-39d8e9a9dbb9",
    # "Cookie": "E214ADBD8096D8126CAE6E87F1655165",
    "Authorization": "",
    "Cookie": ""
}

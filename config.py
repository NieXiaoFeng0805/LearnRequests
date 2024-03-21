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
    "Authorization": ""
}

# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/19 19:48
# software: PyCharm
"""
文件说明：

"""
import json
import logging
from logging import handlers
import os


def init_logging():
    '''
    # 初始化日志配置文件
    1. 获取日志器
    2. 设置日志等级
    3. 获取处理器
    4. 设置日志的格式
    5. 将日志的格式添加到处理器
    6. 将处理器添加到日志
    :return:
    '''
    # 实例化日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 获取日志处理器
    # 控制台处理器
    sh = logging.StreamHandler()
    # 文件处理器 os.path.dirname(os.path.abspath(__file__)) 是获取当前utils.py的父级目录
    fh = logging.handlers.TimedRotatingFileHandler(os.path.dirname(os.path.abspath(__file__)) + "/logs/lagou.log",
                                                   when='h',
                                                   interval=24,
                                                   backupCount=3,
                                                   encoding="utf-8")
    # 设置日志格式
    fmt = "%(asctime)s [%(levelname)s] [%(funcName)s %(lineno)d] %(message)s"
    formatter = logging.Formatter(fmt)
    # 将格式添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)
    # 返回日志器
    return logger


def read_json_data(file_name):
    with open(file_name, mode='r', encoding="utf-8") as f:
        json_data = json.load(f)
        result_list = []
        for case_data in json_data:  # type:dict
            result_list.append(tuple(case_data.values()))  # 转换成元组数据是 parameterized 所需的

        return result_list

# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/19 19:48
# software: PyCharm
"""
文件说明：

"""

import unittest
import time
import config
from lib import HTMLTestRunner_PY3
from scripts.test_login import TestLogin_ByAutoTest
from scripts.test_course import TestCourse
from utils import GenerateResult
import threadpool

# # 创建测试套件
# suite = unittest.TestSuite()
# # 将测试用例添加到测试套件中
# suite.addTest(unittest.makeSuite(TestLogin_ByAutoTest))
# suite.addTest(unittest.makeSuite(TestCourse))

# 使用HTMLTestRunner运行测试用例,生成测试报告——单线程
# with open("./reports/HTMLPY3_report{}.html".format(time.strftime('%Y%m%d%H%M%S')), 'wb') as f:
#     # 实例化runner
#     runner = HTMLTestRunner_PY3.HTMLTestRunner(f)
#     # 使用runner 运行测试套件,得到测试结果
#     result = runner.run(suite)
#     # 使用runner生成测试报告
#     runner.generateReport(suite, result)
#


# 多线程测试结果并打印测试报告
gr = GenerateResult()
# 自动获取TestCase
cases = unittest.defaultTestLoader.discover(config.BASE_PATH + '/scripts', 'test*.py')
pool = threadpool.ThreadPool(10)
req_list = threadpool.makeRequests(gr.run_case, cases)
for req in req_list:
    print('req:', req)
    pool.putRequest(req)
pool.wait()  # 等待线程全部完成
result = gr.combine_result()  # 整合多线程运行的结果
gr.runner.generateReport(cases, result)

import unittest

import config
from api.course_api import CourseAPI
import logging
from jsonpath import jsonpath
from utils import get_login_token


class TestCourse(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        get_login_token("15321919666", "123456")

    def setUp(self) -> None:
        self.course_api = CourseAPI()

    def test_01_course_manager(self):
        # 查询所有课程
        response = self.course_api.query_all_course(config.BASE_HEADERS)
        logging.info(f"查询的所有结果为：{response.json()}")
        # 使用json断言判断
        # 断言 id = 15 的courseName 是否 为 大数据云计算
        result = jsonpath(response.json(), "$.content[?(@.id==15)].courseName")
        # logging.info(f"断言 id = 15 的courseName 是否 为 大数据云计算:{result}")
        self.assertEquals("大数据云计算", result[0])
        # 添加课程
        request_body = {"brief": "测试接口自动化测试", "courseDescriptionMarkDown": "", "courseImgUrl": "",
                        "courseListImg": "",
                        "courseName": "测试添加课程", "discounts": "1", "discountsTag": "泰坦", "id": "",
                        "previewFirstField": "这是一个测试用视频", "previewSecondField": "这是一个测试用视频",
                        "price": "1", "sales": "1", "sortNum": "", "status": "", "teacherName": "泰坦",
                        "position": "讲师", "description": "讲师简介", "teacherDTO": {}, "activityCourse": False,
                        "activityCourseDTO": {}}
        response = self.course_api.add_course(config.BASE_HEADERS, request_body)
        logging.info(f"添加课程的结果为：{response.json()}")

        # 修改课程
        request_body = {"brief": "lllllll", "courseDescriptionMarkDown": "", "courseImgUrl": "",
                        "courseListImg": "",
                        "courseName": "测试添加课程", "discounts": "1", "discountsTag": "泰坦", "id": "27",
                        "previewFirstField": "这是一个测试用视频", "previewSecondField": "这是一个测试用视频",
                        "price": "1", "sales": "1", "sortNum": "", "status": "", "teacherName": "泰坦",
                        "position": "讲师", "description": "讲师简介", "teacherDTO": {}, "activityCourse": False,
                        "activityCourseDTO": {}}
        response = self.course_api.modify_course(config.BASE_HEADERS, request_body)
        logging.info(f"修改课程的结果为：{response.json()}")

        # 更新课程
        response = self.course_api.update_course_status(config.BASE_HEADERS, status=1, id=33)
        logging.info(f"更新课程的结果：{response.json()}")

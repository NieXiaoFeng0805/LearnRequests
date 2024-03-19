# author: Feng
# contact: 1245272985@qq.com
# datetime:2024/3/19 20:31
# software: PyCharm
"""
文件说明：

"""
import requests
import config


class CourseAPI:
    def __init__(self):
        self.URL_query_course = config.BASE_LaGouEDU_URL + "/ssm_web/course/findAllCourse"
        self.URL_add_course = config.BASE_LaGouEDU_URL + "/ssm_web/course/saveOrUpdateCourse"
        self.URL_modify_course = config.BASE_LaGouEDU_URL + "/ssm_web/course/saveOrUpdateCourse"
        self.URL_updata_course_status = config.BASE_LaGouEDU_URL + "/ssm_web/course/updateCourseStatus"

    # 接口封装

    # 查询所有课程
    def query_all_course(self, headers):
        return requests.post(url=self.URL_query_course, json={}, headers=headers)

    # 新增课程
    def add_course(self, headers, request_body):
        return requests.post(url=self.URL_add_course, json=request_body, headers=headers)

    # 修改课程
    def modify_course(self, headers, request_body):
        return requests.post(url=self.URL_modify_course, json=request_body, headers=headers)

    # 更新课程状态
    def update_course_status(self, headers, status, id):
        return requests.get(url=self.URL_updata_course_status, headers=headers, params={"status": status, "id": id})

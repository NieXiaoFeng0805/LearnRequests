import requests
import config


class UserAPI:
    def __init__(self):
        self.URL_query_userList = config.BASE_LaGouEDU_URL + "/ssm_web/user/findAllUserByPage"
        self.URL_search_user = config.BASE_LaGouEDU_URL + "/ssm_web/user/findAllUserByPage"
        self.URL_query_userAuth = config.BASE_LaGouEDU_URL + "/ssm_web/user/getUserPermissions"
        self.URL_user_login = config.BASE_LaGouEDU_URL + "/ssm_web/user/login"
        self.URL_frOrUnfr_user = config.BASE_LaGouEDU_URL + "/ssm_web/user/updateUserStatus?id=100030011&status=DISABLE"
        self.URL_modify_userAuth = config.BASE_LaGouEDU_URL + "/ssm_web/user/userContextRole"

    def query_all_user(self, headers, request_body):
        '''
        查询所有用户（查询用户列表）
        :param request_body:
        :param headers:
        :return:
        '''
        return requests.post(url=self.URL_query_userList, headers=headers, json=request_body)

    def search_user(self, headers, request_body):
        '''
        搜索用户
        :param headers:
        :param request_body:
        :return:
        '''
        return requests.post(url=self.URL_search_user, headers=headers, json=request_body)

    def query_user_Auth(self, headers):
        '''
        查询用户权限
        :param headers:
        :return:
        '''
        return requests.get(url=self.URL_query_userAuth, headers=headers)

    def user_login(self, phone, password):
        '''
        用户登录
        :param password:
        :param phone:
        :return:
        '''
        return requests.post(url=self.URL_user_login, params={"phone": phone, "password": password})

    def frOrUnfr_user(self, headers):
        '''
        冻结/解冻用户
        :param headers:
        :param id:
        :param status:
        :return:
        '''
        return requests.post(url=self.URL_frOrUnfr_user, headers=headers)

    def modify_user_root(self, headers):
        '''
        修改用户权限
        :param headers:
        :return:
        '''
        return requests.post(url=self.URL_modify_userAuth, headers=headers)

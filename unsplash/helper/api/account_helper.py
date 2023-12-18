import requests
from core.api.request_helper import BaseAPI
from core.env_info.env_info import EnvironmentInfo
class AccountHelper():
    account_api_category = '/Account/v1/'
    generate_token_endpoint = account_api_category + 'GenerateToken'
    global_token = None

    @classmethod
    def generate_token(cls, account):
        data = {"userName": account.username, "password": account.password}
        return BaseAPI(url= EnvironmentInfo.api_url + cls.generate_token_endpoint, data=data).post()
    
    @classmethod
    def get_token(cls, account, re_generate=False):
        if cls.global_token == None or re_generate:
            cls.global_token = cls.generate_token(account).json()["token"]
        return cls.global_token



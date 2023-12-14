from core.utilities.file_utils import get_full_path
import json
class Account():
    def __init__(self, username, password, user_id):
        self.username = username
        self.password = password
        self.user_id  = user_id
    
    @classmethod
    def get_list_account_from_json(cls, json_file_path, account_type):
        result = []
        with open(get_full_path(json_file_path)) as f:
            data = json.load(f)
            list_json_account = data[account_type]
            for json_account in list_json_account:
                result.append(Account(**json_account))
            
        return result


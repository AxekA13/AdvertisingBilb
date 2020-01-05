from Models.AdminModel import AdminModel
from enum import Enum


class ManageUsersContr:
    def __init__(self):
        self.model = AdminModel()

    def add_user(self, name):
        import re
        if re.search(r'[^a-zA-Z]', name) or name == '':
            return AddUserResult.ERROR_MESSAGE
        elif name in [i.name for i in self.model.users]:
            return AddUserResult.NAME_EXIST
        else:
            self.model.create_user(name)
            return AddUserResult.OK

    def user_remove_list(self):
        return [i.name for i in self.model.users]

    def delete_user(self, select_user):
        if select_user == '':
            return 0
        else:
            self.model.delete_user(select_user)
            return 1


class AddUserResult(Enum):
    OK = 1
    ERROR_MESSAGE = 2
    NAME_EXIST = 3

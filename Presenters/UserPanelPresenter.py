from Models.AdminModel import AdminModel


class UserPanelContr:
    user_box_list = {}

    def __init__(self):
        self.model = AdminModel()

    def user_list(self):
        return [i.name for i in self.model.users]

    def select_user(self, select_user):
        if select_user == '':
            return 0
        else:
            for i in self.model.users:
                if i.name == select_user:
                    return i

    def add_user_box(self, select_user):
        if select_user in UserPanelContr.user_box_list.keys():
            return False
        else:
            UserPanelContr.user_box_list[select_user] = ''
            return True

    def delete_frame(self, user_name):
        if user_name in UserPanelContr.user_box_list.keys():
            UserPanelContr.user_box_list[user_name].destroy()

    def get_devices(self):
        devices_list = []
        for dev in self.model.devices:
            if dev.group is True:
                print(dev.devices)
                for dev2 in dev.devices:
                    dev2.server = dev.server
                    devices_list.append(dev2)
            else:
                devices_list.append(dev)
        return devices_list
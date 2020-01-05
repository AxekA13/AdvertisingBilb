from Models.UserModel import UserModel
from Models import DeviceModel
from Models import AdvertisingModel
from Models import DeviceGroup


class AdminModel:
    users = []
    devices = []

    def create_user(self, name):
        name = UserModel(name)
        AdminModel.users.append(name)

    def delete_user(self, name):
        for i in AdminModel.users:
            if i.name == name:
                for j in i.devices:
                    for k in AdminModel.devices:
                        if j == k:
                            k.status = 'Awaiting appointment'
                AdminModel.users.remove(i)
                del i

    def create_device(self, name, memory):
        name = DeviceModel.DeviceModel(name, memory)
        AdminModel.devices.append(name)

    def delete_device(self, name):
        for i in AdminModel.devices:
            if i.name == name:
                AdminModel.devices.remove(i)
                del i
        for i in AdminModel.users:
            for dev in i.devices:
                if dev.name == name:
                    AdvertisingModel.AdvertisingModel.numbers -= len(dev.advertising)
                    i.devices.remove(dev)
                    del dev

    def set_device_user(self, device, user):
        for us in AdminModel.users:
            if us.name == user:
                for dev in AdminModel.devices:
                    if dev.name == device:
                        us.devices.append(dev)
                        dev.status = 'Active'

    def create_group_device(self, selected_devices, name, memory):
        devices = []
        for elem in selected_devices:
            for dev in AdminModel.devices:
                if dev.name == elem:
                    dev.server = None
                    devices.append(dev)
                    AdminModel.devices.remove(dev)
        group = DeviceGroup.DeviceGroup(devices, 'Group' + name, memory)
        AdminModel.devices.append(group)

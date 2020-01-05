from Models.AdminModel import AdminModel
from enum import Enum
import tkinter as tk
import os
import shutil


class ManageDeviceContr:
    def __init__(self):
        self.model = AdminModel()

    def add_device(self, name, memory):
        import re
        if re.search(r'[^a-zA-Z]', name) or name == '':
            return AddDeviceResult.ERROR_MESSAGE
        elif name in [i.name for i in self.model.devices]:
            return AddDeviceResult.NAME_EXIST
        else:
            if re.search(r'[^\d]', memory):
                return AddDeviceResult.ERROR_MESSAGE
            if memory == '':
                self.model.create_device(name, 32)
            elif int(memory) >= 256 or int(memory) <= 0:
                return AddDeviceResult.ERROR_MESSAGE
            else:
                self.model.create_device(name, int(memory))
            return AddDeviceResult.OK

    def device_remove_list(self):
        return [i.name for i in self.model.devices]

    def available_device(self):
        available_devices = []
        for device in self.model.devices:
            if device.status == 'Awaiting appointment':
                available_devices.append(device.name)
        return available_devices

    def delete_device(self, select_device):
        if select_device == '':
            return 0
        else:
            for dev in self.model.devices:
                if dev.name == select_device:
                    file_path = dev.server.directory
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path)
            self.model.delete_device(select_device)
            return 1

    def set_device_to_user(self, select_device, select_user):
        if select_device == '' or select_user == '':
            return 0
        else:
            self.model.set_device_user(select_device, select_user)
            return 1

    def get_no_group_list(self):
        no_group_devices = []
        for elem in self.model.devices:
            if elem.group == False and elem.status != 'Active':
                no_group_devices.append(elem.name)
        return no_group_devices

    def set_devices_to_group(self, list_select_devices):
        if len(list_select_devices) == 0:
            return False
        else:
            list_devices = []
            for i in range(len(list_select_devices)):
                if list_select_devices[i].get() == 1:
                    list_devices.append(i)
            if len(list_devices) == 0 or len(list_devices) == 1:
                return False
            return list_devices

    def input_name(self, devices, name, memory):
        import re
        if re.search(r'[^a-zA-Z]', name) or name == '':
            return AddDeviceResult.ERROR_MESSAGE
        elif name in [i.name for i in self.model.devices]:
            return AddDeviceResult.NAME_EXIST
        else:
            if re.search(r'[^\d]', memory):
                return AddDeviceResult.ERROR_MESSAGE
            if memory == '':
                self.model.create_group_device(devices, name, 32)
            elif int(memory) >= 256:
                return AddDeviceResult.ERROR_MESSAGE
            else:
                self.model.create_group_device(devices, name, memory)
                folder = r'C:\Users\nasty\PycharmProjects\Bilbords\Server'
                for dev in devices:
                    file_path = os.path.join(folder, dev)
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path)
        return AddDeviceResult.OK


class AddDeviceResult(Enum):
    OK = 1
    ERROR_MESSAGE = 2
    NAME_EXIST = 3
    NOT_USER = 4


class SetDeviceResult(Enum):
    OK = 1
    DEVICE_EXIST = 2
    ERROR = 3

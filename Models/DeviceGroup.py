from Models.DeviceModel import DeviceModel


class DeviceGroup(DeviceModel):
    def __init__(self, list_devices, name, memory):
        super().__init__(name, memory)
        self.devices = list_devices
        self.group = True

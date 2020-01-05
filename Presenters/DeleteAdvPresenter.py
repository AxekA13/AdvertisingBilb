class DeleteAdvController:
    def __init__(self, user):
        self.user = user

    def get_device_list(self):
        devices = []
        for dev in self.user.devices:
            devices.append(dev.name)
        return devices

    def get_advertising(self, device):
        if device == '':
            return 0
        for dev in self.user.devices:
            if dev.name == device:
                return [adv.name for adv in dev.advertising]

    def delete_advertising(self, device, select_advertising):
        if select_advertising == '':
            return 0
        else:
            self.user.delete_advertising(device, select_advertising)
            return 1

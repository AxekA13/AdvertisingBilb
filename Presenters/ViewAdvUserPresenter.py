class ViewAdvUserController:
    def __init__(self, user):
        self.user = user

    def get_advertising_list(self, device):
        advertising = []
        for dev in self.user.devices:
            if dev.name == device:
                for data in dev.server.data:
                    advertising.append(data)
            else:
                if dev.group == True:
                    for dev2 in dev.devices:
                        if dev2.name == device:
                            for data in dev2.server.data:
                                advertising.append(data)

        return advertising

    def get_device_list(self):
        devices = []
        for dev in self.user.devices:
            if dev.group is True:
                print(dev.devices)
                for dev2 in dev.devices:
                    dev2.server = dev.server
                    devices.append(dev2)
            else:
                devices.append(dev)
        return devices

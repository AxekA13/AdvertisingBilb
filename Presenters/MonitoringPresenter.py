from Models.AdminModel import AdminModel


class MonitoringContr:
    def __init__(self):
        self.model = AdminModel()

    def device_list(self):
        devices = []
        if len(self.model.devices) == 0:
            return devices, 0
        else:
            for name in [(item.uid, item.name, item.status, [adv.name for adv in item.advertising], item.server.memory,
                          item.server.size) for
                         item in self.model.devices]:
                devices.append(name)

        return devices, 1

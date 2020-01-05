class StatusController:
    def device_list(self, user):
        devices = []
        if len(user.devices) == 0:
            return devices, 0
        else:
            for name in [(item.uid, item.name, item.status, [adv.name for adv in item.advertising], item.server.memory,
                          item.server.size) for
                         item in user.devices]:
                devices.append(name)

        return devices, 1

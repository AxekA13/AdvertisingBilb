

class SelectFormController:
    def __init__(self, user):
        self.user = user

    def get_list_devices(self):
        return [i.name for i in self.user.devices]

    def get_list_advertising(self, device):
        advert = []
        for dev in self.user.devices:
            if dev.name == device:
                for adv in dev.advertising:
                    if adv.timetable is None:
                        advert.append(adv.name)
        return advert

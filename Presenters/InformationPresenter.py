from Models.AdminModel import AdminModel
from Models.AdvertisingModel import AdvertisingModel

class InformationContr:
    def __init__(self):
        self.model = AdminModel

    def give_list_of_numbers(self):
        return len(self.model.users), len(self.model.devices), AdvertisingModel.numbers

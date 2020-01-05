import datetime
import re


class InputScheduleController:
    rest_of_hour = {}

    def __init__(self, user):
        self.user = user

    def check_schedule_to_adv(self, device, advertising, interval, start):
        now = datetime.datetime.now()
        if (interval == '' or re.search(r'[^\d]', interval)) and (start == '' or not re.fullmatch(
                r'^(([0,1][0-9])|(2[0-3])):[0][0]', start)):
            return 0
        elif int(now.hour) > int(start.split(':')[0]):
            return 1
        for dev in self.user.devices:
            if dev.name == device:
                for adv in dev.advertising:
                    if adv.name == advertising:
                        if int(3600 / int(adv.timescale)) < int(interval):
                            return 2
                        else:
                            if start not in list(InputScheduleController.rest_of_hour.keys()):
                                InputScheduleController.rest_of_hour[start] = 3600 - int(adv.timescale) * int(interval)
                                self.user.set_schedule_to_advertising(device, advertising, int(interval), start)
                                return 3, InputScheduleController.rest_of_hour[start]
                            else:
                                if InputScheduleController.rest_of_hour[start] - int(adv.timescale) * int(
                                        interval) <= 0:
                                    return 4, InputScheduleController.rest_of_hour[start]
                                else:
                                    InputScheduleController.rest_of_hour[start] = InputScheduleController.rest_of_hour[
                                                                                      start] - int(adv.timescale) * int(
                                        interval)
                                    self.user.set_schedule_to_advertising(device, advertising, int(interval), start)
                                    return 3, InputScheduleController.rest_of_hour[start]

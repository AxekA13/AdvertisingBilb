import random
import os
from Models.ServerModel import Server
from Models.AdvertisingModel import AdvertisingModel
import datetime
import time


class DeviceModel:
    def __init__(self, name, memory):
        self.name = name
        self.status = 'Awaiting appointment'
        self.advertising = []
        self.uid = random.randrange(1000, 10001, 1)
        self.group = False
        self.server = Server(name, memory)
        self.default_video = r'C:\Users\nasty\PycharmProjects\Bilbords\30-ти секундный ролик.mp4'

    def get_schedule_timer(self):
        queue = []
        temp = []
        counter = 0
        balance = 3600
        wait_time = 0.5
        current_time = 0
        now = datetime.datetime.now()
        if len(self.advertising) == 0:
            current_time = 120
            wait_time = int(current_time / 30)
            for i in range(wait_time):
                queue.append(self.default_video)
            return queue
        else:
            for adv in self.advertising:
                if adv.timetable is not None:
                    temp.append(adv)
            sorted_advertising = sorted(temp, key=AdvertisingModel.get_timetable)
            if len(sorted_advertising) == 0:
                current_time = 120
                wait_time = int(current_time / 30)
                for i in range(wait_time):
                    queue.append(self.default_video)
                return queue
            else:
                """
                if str(now.hour) < sorted_advertising[0].timetable.start_time:
                    hours = int(sorted_advertising[0].timetable.start_time.split(':')[0]) - int(now.hour)
                    minutes = hours * 60 - int(now.minute)
                    interval_to_show = int(minutes * 60 / 30)
                    for i in range(interval_to_show):
                        queue.append(self.default_video)
                """
                for elem in sorted_advertising:
                    queue.append(self.server.directory + '\\' + elem.name)
                return queue

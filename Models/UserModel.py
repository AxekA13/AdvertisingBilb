import random
import shutil
import os
from Models import AdvertisingModel
from Models import TimetableModel
from moviepy.editor import VideoFileClip
import logging
import json
from tkinter import filedialog


class UserModel:

    def __init__(self, name):
        self.name = name
        self.uid = random.randrange(1000, 10001, 1)
        self.devices = []

    def add_advertising(self, file_name, device):
        for dev in self.devices:
            if dev.name == device:
                name_adv = os.path.basename(file_name)
                file_size = os.stat(file_name).st_size / 1073741824.0
                clip = VideoFileClip(file_name)
                clip.close()
                timescale = clip.duration
                advertising = AdvertisingModel.AdvertisingModel(name_adv, file_size, timescale)
                dev.advertising.append(advertising)
                dev.server.data.append(dev.server.directory + '\\' + name_adv)
                shutil.copy(file_name, dev.server.directory)
                logging.info('User ' + self.name + ' add advertising ' + name_adv + ' on device ' + device)

    def delete_advertising(self, device, advertising):
        for dev in self.devices:
            if dev.name == device:
                for adv in dev.advertising:
                    if adv.name == advertising:
                        dev.advertising.remove(adv)
                        del adv
                        for data in dev.server.data:
                            if advertising in data:
                                folder = dev.server.directory
                                file_path = os.path.join(folder, advertising)
                                os.remove(file_path)
                                dev.server.data.remove(data)
                                AdvertisingModel.AdvertisingModel.numbers -= 1
                                logging.info(
                                    'User ' + self.name + ' delete advertising ' + advertising + ' on device ' + device)

    def set_schedule_to_advertising(self, device, advertising, interval, start):
        for dev in self.devices:
            if dev.name == device:
                for adv in dev.advertising:
                    if adv.name == advertising:
                        adv.timetable = TimetableModel.Timetable(int(interval), str(start))
                        logging.info(
                            'User ' + self.name + ' set schedule ' + str(
                                adv.timetable.uid) + ' on advertising ' + advertising + ' in device ' + device)
                        print(adv.timetable.start_time)
                        print(adv.timetable.interval)

    def export_schedule(self, device, advertising):
        for dev in self.devices:
            if dev.name == device:
                for adv in dev.advertising:
                    if adv.name == advertising:
                        schedule_dict = {}
                        schedule_dict['interval'] = adv.timetable.interval
                        schedule_dict['start'] = adv.timetable.start_time
                        f = filedialog.asksaveasfile(mode='w', defaultextension=".json",
                                                     filetypes=(('JSON Files', '.json'),))
                        json.dump(schedule_dict, f)
                        logging.info(
                            'User ' + self.name + ' export schedule ' + str(
                                adv.timetable.uid) + ' from advertising ' + advertising + ' on device ' + device + ' in file ' + f.name)

from Presenters.InputSchedulePresenter import InputScheduleController
from tkinter import filedialog as fd
import json
import logging


class ImportScheduleController(InputScheduleController):
    def __init__(self, user):
        super().__init__(user)

    def select_file(self, device, advertising):
        file_name = fd.askopenfilename(filetypes=(('JSON Files', '*.json'),), title='Select file')
        with open(file_name, 'r', encoding='utf-8') as fh:  # открываем файл на чтение
            data = json.load(fh)
        data_list = list(data.keys())
        data_list.sort()
        if len(data_list) != 2:
            return 4
        elif data_list != ['interval', 'start']:
            return 5
        else:
            print(data['start'])
            print(data['interval'])
            interval = str(data['interval'])
            start = str(data['start'])
            logging.info(
                'User ' + self.user.name + ' import schedule ' + file_name + ' on advertising ' + advertising + ' in device ' + device)
            result = self.check_schedule_to_adv(device, advertising, interval, start)
            return result

    def check_export_schedule(self, device, advertising):
        for dev in self.user.devices:
            if dev.name == device:
                for adv in dev.advertising:
                    if adv.name == advertising:
                        if adv.timetable == None:
                            return 0
                        else:
                            self.user.export_schedule(device, advertising)

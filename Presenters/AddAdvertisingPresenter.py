import shutil
from tkinter import filedialog as fd
import os


class AddAdvContr:
    def __init__(self, user):
        self.user = user

    def select_video(self, device):

        file_name = fd.askopenfilename(filetypes=(('MP4 Files', '*.mp4'),), title='Select file')
        file_size = os.stat(file_name).st_size
        file_size = file_size / 1073741824.0
        base = os.path.basename(file_name)
        for dev in self.user.devices:
            if dev.name == device:
                if dev.server.memory + file_size <= dev.server.size:
                    if base in [adv.name for adv in dev.advertising]:
                        return 0
                    else:
                        self.user.add_advertising(file_name, device)
                        dev.server.memory += file_size
                else:
                    return 2
        return 1

    def get_device_list(self):
        devices = []
        for dev in self.user.devices:
            devices.append(dev.name)
        return devices

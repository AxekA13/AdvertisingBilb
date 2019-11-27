import tkinter as tk
from tkinter import ttk
from BasicWindow import Window


class ManageDevicesView(Window):
    def __init__(self):
        super().__init__()
        self.init_manage_devices()

    def init_manage_devices(self):
        self.configure(bg='white')
        self.set_window('Manage Devices')

        add_device_button = ttk.Button(self, text='Add device')
        add_device_button.place(x=6, y=100, width=130, height=50)
        delete_device_button = ttk.Button(self, text='Delete device')
        delete_device_button.place(x=175, y=100, width=140, height=50)
        combine_devices_button = ttk.Button(self, text='Combine device')
        combine_devices_button.place(x=360, y=100, width=130, height=50)
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=195, y=200, width=100, height=30)

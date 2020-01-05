import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters import ManageDevicePresenter
from tkinter import messagebox
from View.InterNameGroup import InterNameView


class GroupDeviceView(Window):
    def __init__(self):
        super().__init__()
        self.show_group_device()

    def show_group_device(self):
        x = 230
        y = 50
        self.set_window('Group Device')
        self.configure(bg='white')
        self.focus_force()
        text = tk.Label(self, text='Please, select the devices', bg='white')
        text.place(x=190, y=20)
        self.device_list = ManageDevicePresenter.ManageDeviceContr().get_no_group_list()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=205, y=250, width=100, height=30)
        selected_devices = []
        for machine in range(len(self.device_list)):
            text = self.device_list[machine]
            self.device_list[machine] = tk.IntVar()
            selected_devices.append(self.device_list[machine])
            tk.Checkbutton(self, text=text, variable=self.device_list[machine], bg='white').place(x=x, y=y)
            y += 30
        combine_button = ttk.Button(self, text='Combine', command=lambda: self.group_devices(selected_devices))
        combine_button.place(x=205, y=210, width=100, height=30)

    def group_devices(self, selected_devices):
        result = ManageDevicePresenter.ManageDeviceContr().set_devices_to_group(selected_devices)
        if result is False:
            messagebox.showerror('ERROR', 'Select devices')
        else:
            selected = []
            device_list_copy = ManageDevicePresenter.ManageDeviceContr().get_no_group_list()
            for i in result:
                selected.append(device_list_copy[i])
            self.destroy()
            self.show_input_name(selected)

    def show_input_name(self, devices):
        InterNameView(devices)

from tkinter import ttk
from tkinter import messagebox
from View.BasicWindow import Window
from View.AddDevice import AddDeviceView
from View.DeleteDevice import DeleteDeviceView
from View.SetDeviceUser import SetDeviceUserView
from View.GroupDevice import GroupDeviceView


class ManageDevicesView(Window):
    def __init__(self):
        super().__init__()
        self.init_manage_devices()

    def init_manage_devices(self):
        self.configure(bg='white')
        self.set_window('Manage Devices')

        add_device_button = ttk.Button(self, text='Add device', command=self.open_add_device_view)
        add_device_button.place(x=6, y=80, width=130, height=50)
        delete_device_button = ttk.Button(self, text='Delete device', command=self.open_delete_device_view)
        delete_device_button.place(x=175, y=80, width=140, height=50)
        combine_devices_button = ttk.Button(self, text='Combine device', command=self.open_group_device_view)
        combine_devices_button.place(x=360, y=80, width=130, height=50)
        set_device_user_button = ttk.Button(self, text='Set device to user', command=self.open_set_device_user_view)
        set_device_user_button.place(x=175, y=160, width=140, height=50)
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=200, y=240, width=100, height=30)

    def open_add_device_view(self):
        AddDeviceView()
        self.destroy()

    def open_delete_device_view(self):
        DeleteDeviceView()
        self.destroy()

    def open_set_device_user_view(self):
        SetDeviceUserView()
        self.destroy()

    def open_group_device_view(self):
        GroupDeviceView()
        self.destroy()

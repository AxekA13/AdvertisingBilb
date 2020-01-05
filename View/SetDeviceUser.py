import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters import ManageDevicePresenter
from Presenters.ManageDevicePresenter import SetDeviceResult
from Presenters import ManageUsersPresenter
from tkinter import messagebox


class SetDeviceUserView(Window):
    def __init__(self):
        super().__init__()
        self.show_set_device_user()

    def show_set_device_user(self):
        self.set_window('Set device to user')
        self.configure(bg='white')
        self.focus_force()
        text = tk.Label(self, text='Select the device', bg='white', padx=150, pady=60)
        text.pack()
        text_user = tk.Label(self, text='Select the user', bg='white')
        text_user.pack()
        username = tk.StringVar()
        device_name = tk.StringVar()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=270, y=230, width=100, height=30)
        select_device = ttk.Combobox(self, width=20, textvariable=username, state='readonly')
        select_device['values'] = ManageDevicePresenter.ManageDeviceContr().available_device()
        select_device.place(x=180, y=100)
        select_user = ttk.Combobox(self, width=20, textvariable=device_name, state='readonly')
        select_user['values'] = ManageUsersPresenter.ManageUsersContr().user_remove_list()
        select_user.place(x=180, y=180)
        accept_button = ttk.Button(self, text='Set', command=lambda: self.set_device_user(select_device, select_user))
        accept_button.place(x=140, y=230, width=100, height=30)

    def set_device_user(self, select_device, select_user):
        result = ManageDevicePresenter.ManageDeviceContr().set_device_to_user(select_device.get(), select_user.get())
        if result == 0:
            messagebox.showerror('ERROR', 'Cannot set device')
        else:
            self.destroy()
            messagebox.showinfo('Successful', 'The device was successfully installed')

import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters import DeleteAdvPresenter
from View import DeleteAdvertising
from tkinter import messagebox


class DeviceDeleteAdvertisingView(Window):
    def __init__(self, user):
        super().__init__()
        self.show_select_dev(user)

    def show_select_dev(self, user):
        self.set_window('Select device')
        self.configure(bg='white')
        self.focus_force()
        text = tk.Label(self, text='Please, select the device', bg='white', padx=150, pady=60)
        text.pack()
        advertising_name = tk.StringVar()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=201, y=230, width=100, height=30)
        select_adv = ttk.Button(self, text='Select', command=lambda: self.show_delete_adv(user))
        select_adv.place(x=201, y=180, width=100, height=30)
        self.select_device = ttk.Combobox(self, width=20, textvariable=advertising_name, state='readonly')
        self.select_device['values'] = DeleteAdvPresenter.DeleteAdvController(user).get_device_list()
        self.select_device.place(x=180, y=110)

    def show_delete_adv(self, user):
        DeleteAdvertising.DeleteAdvertisingView(user, self.select_device.get())

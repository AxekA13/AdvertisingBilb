import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters import SetSchedulePresenter
from View.SelectAdvertising import SelectAdvView
from tkinter import messagebox


class SelectDevAdvView(Window):
    def __init__(self, user):
        super().__init__()
        self.show_select_form(user)

    def show_select_form(self, user):
        self.set_window('Select device')
        self.configure(bg='white')
        self.focus_force()
        text = tk.Label(self, text='Please, select the device', bg='white', padx=150, pady=60)
        text.pack()
        username = tk.StringVar()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=201, y=230, width=100, height=30)
        select_device = ttk.Combobox(self, width=20, textvariable=username, state='readonly')
        select_device['values'] = SetSchedulePresenter.SelectFormController(user).get_list_devices()
        select_device.place(x=180, y=100)
        select_device_button = ttk.Button(self, text='Select device',
                                          command=lambda: self.check_select_device(user, select_device.get()))
        select_device_button.place(x=201, y=180, width=100, height=30)

    def check_select_device(self, user, device):
        if device == '':
            messagebox.showerror('ERROR', 'Select device')
        else:
            self.destroy()
            SelectAdvView(user, device)

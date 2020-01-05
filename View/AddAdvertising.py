import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters import AddAdvertisingPresenter
from tkinter import messagebox
import shutil
from tkinter import filedialog as fd


class AddAdvertisingView(Window):
    def __init__(self, user):
        super().__init__()
        self.show_add_adv(user)

    def show_add_adv(self, user):
        self.set_window('Add Advertising')
        self.configure(bg='white')
        self.focus_force()
        text = tk.Label(self, text='Please, select the device', bg='white', padx=150, pady=60)
        text.pack()
        username = tk.StringVar()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=201, y=230, width=100, height=30)
        select_adv = ttk.Button(self, text='Select Ad',
                                command=lambda: self.add_adv(user))
        select_adv.place(x=201, y=180, width=100, height=30)
        self.select_device = ttk.Combobox(self, width=20, textvariable=username, state='readonly')
        self.select_device['values'] = AddAdvertisingPresenter.AddAdvContr(user).get_device_list()
        self.select_device.place(x=180, y=110)

    def add_adv(self, user):
        result = AddAdvertisingPresenter.AddAdvContr(user).select_video(
            self.select_device.get())
        if result == 0:
            messagebox.showerror('ERROR', 'Cannot add this file')
        elif result == 2:
            messagebox.showerror('ERROR', 'File size too large')
        else:
            messagebox.showinfo('Complete', 'Advertising added successful')

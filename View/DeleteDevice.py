import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters import ManageDevicePresenter
from tkinter import messagebox


class DeleteDeviceView(Window):
    def __init__(self):
        super().__init__()
        self.show_delete_device()

    def show_delete_device(self):
        self.set_window('Delete Device')
        self.configure(bg='white')
        self.focus_force()
        text = tk.Label(self, text='Please, select the device', bg='white', padx=150, pady=60)
        text.pack()
        username = tk.StringVar()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=201, y=230, width=100, height=30)
        delete_button = ttk.Button(self, text='Delete', command=lambda: self.delete_device(username))
        delete_button.place(x=201, y=150, width=100, height=30)
        select_device = ttk.Combobox(self, width=20, textvariable=username, state='readonly')
        select_device['values'] = ManageDevicePresenter.ManageDeviceContr().device_remove_list()
        select_device.place(x=180, y=110)

    def delete_device(self, select_device):
        result = ManageDevicePresenter.ManageDeviceContr().delete_device(select_device.get())
        if result == 0:
            messagebox.showerror('ERROR', 'Cannot delete user' + select_device.get())
        else:
            self.show_delete_device()
            self.destroy()
            messagebox.showinfo('Complete', 'User ' + select_device.get() + ' was successfully deleted')
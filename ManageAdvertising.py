import tkinter as tk
from tkinter import ttk
from BasicWindow import Window


class ManageAdvertisingView(Window):
    def __init__(self):
        super().__init__()
        self.init_manage()

    def init_manage(self):
        self.configure(bg='white')
        self.set_window('ManageAdvertising')
        add_advertising_button = ttk.Button(self, text='Add Advertising')
        add_advertising_button.place(x=6, y=70, width=130, height=50)
        delete_advertising_button = ttk.Button(self, text='Delete Advertising')
        delete_advertising_button.place(x=175, y=70, width=140, height=50)
        view_ad_statistics_button = ttk.Button(self, text='View Add Statistics')
        view_ad_statistics_button.place(x=360, y=70, width=130, height=50)
        set_schedule_button = ttk.Button(self, text='Set Schedule')
        set_schedule_button.place(x=175, y=150, width=140, height=50)
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=195, y=250, width=100, height=30)

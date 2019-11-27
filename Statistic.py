from BasicWindow import Window
from tkinter import ttk
import tkinter as tk


class StatisticView(Window):
    def __init__(self):
        super().__init__()
        self.init_view_of_numbers()

    def init_view_of_numbers(self):
        width = 35
        height = 5
        bg = 'white'
        brd = 3
        rel = 'groove'
        self.configure(bg='white')
        self.set_window('Info about numbers')
        numbers_of_users = tk.Label(self, text='Numbers of users', width=width, height=height, bg=bg,
                                    borderwidth=brd, relief=rel)
        numbers_of_users.grid(row=1, column=0)
        numbers_of_devices = tk.Label(self, text='Numbers of devices', width=width, height=height, bg=bg,
                                      borderwidth=brd, relief=rel)
        numbers_of_devices.grid(row=2, column=0)
        number_of_advertising = tk.Label(self, text='Numbers of ads', width=width, height=height, bg=bg,
                                         borderwidth=brd, relief=rel)
        number_of_advertising.grid(row=3, column=0)
        numbers_users = tk.Label(self, text='3', width=width, height=height, bg=bg,
                                 borderwidth=brd, relief=rel)
        numbers_users.grid(row=1, column=1)
        numbers_devices = tk.Label(self, text='1', width=width, height=height, bg=bg,
                                   borderwidth=brd, relief=rel)
        numbers_devices.grid(row=2, column=1)
        number_adv = tk.Label(self, text='2', width=width, height=height, bg=bg,
                              borderwidth=brd, relief=rel)
        number_adv.grid(row=3, column=1)
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=210, y=260, width=100, height=30)

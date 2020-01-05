from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from View.BasicWindow import Window
from Presenters.ManageDevicePresenter import ManageDeviceContr, AddDeviceResult


class InterNameView(Window):
    def __init__(self, devices):
        super().__init__()
        self.devices = devices
        self.input_name()

    def input_name(self):
        name = tk.StringVar()
        memory = tk.StringVar()
        self.set_window('Input Name')
        self.configure(bg='white')
        text = tk.Label(self, text='Please, enter name', bg='white', padx=150, pady=60)
        text.pack()
        text2 = tk.Label(self, text='Memory,max = 256 GB', bg='white')
        text2.pack(ipadx=150, ipady=1)
        input_memory = ttk.Entry(self, textvariable=memory)
        input_memory.place(x=190, y=170)
        input_text = ttk.Entry(self, textvariable=name)
        input_text.place(x=190, y=100)
        input_text.focus_force()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=204, y=230, width=100, height=30)
        clear_button = ttk.Button(self, text='Clear',
                                  command=lambda: (input_text.delete(0, 'end'), input_memory.delete(0, 'end')))
        clear_button.place(x=260, y=200, width=90, height=25)
        add_button = ttk.Button(self, text='Ok',
                                command=lambda: self.set_name(self.devices, input_text, input_memory))
        add_button.place(x=160, y=200, width=90, height=25)

    def set_name(self, devices, name, memory):
        result = ManageDeviceContr().input_name(devices, name.get(), memory.get())
        name.delete(0, 'end')
        memory.delete(0, 'end')
        name.focus()
        if result == AddDeviceResult.OK:
            messagebox.showinfo('Complete', 'Group add successful')
        if result == AddDeviceResult.ERROR_MESSAGE:
            messagebox.showerror('ERROR', 'Invalid message format\n\n Name must be string')
        if result == AddDeviceResult.NAME_EXIST:
            messagebox.showerror('ERROR', 'Name ' + name.get() + ' already exist')

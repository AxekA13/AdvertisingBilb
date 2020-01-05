from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from View.BasicWindow import Window
from Presenters.ManageDevicePresenter import ManageDeviceContr, AddDeviceResult


class AddDeviceView(Window):
    def __init__(self):
        super().__init__()
        self.input_name()

    def input_name(self):
        name = tk.StringVar()
        memory = tk.IntVar()
        self.set_window('Input Name')
        self.configure(bg='white')
        text = tk.Label(self, text='Please, enter device name and memory', bg='white', padx=150, pady=60)
        text.pack()
        text2 = tk.Label(self, text='Memory,max = 256 GB', bg='white')
        text2.pack(ipadx=150, ipady=1)
        input_text = ttk.Entry(self, textvariable=name)
        input_text.place(x=190, y=100)
        input_text.focus_force()
        input_memory = ttk.Entry(self, textvariable=memory)
        input_memory.place(x=190, y=170)
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=204, y=260, width=100, height=30)
        clear_button = ttk.Button(self, text='Clear', command=lambda: input_text.delete(0, 'end'))
        clear_button.place(x=260, y=220, width=90, height=25)
        add_button = ttk.Button(self, text='Add',
                                command=lambda: self.add_device(input_text, input_memory))
        add_button.place(x=160, y=220, width=90, height=25)

    def add_device(self, username_input, memory):
        result = ManageDeviceContr().add_device(username_input.get(), memory.get())
        username_input.delete(0, 'end')
        memory.delete(0, 'end')
        username_input.focus()
        if result == AddDeviceResult.OK:
            messagebox.showinfo('Complete', 'Device add successful')
        if result == AddDeviceResult.ERROR_MESSAGE:
            messagebox.showerror('ERROR', 'Invalid message format\n\n Name must be string')
        if result == AddDeviceResult.NAME_EXIST:
            messagebox.showerror('ERROR', 'Device ' + username_input.get() + ' already exist')

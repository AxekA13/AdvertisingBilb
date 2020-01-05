from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from View.BasicWindow import Window
from Presenters.ManageUsersPresenter import ManageUsersContr, AddUserResult


class AddUserView(Window):
    def __init__(self):
        super().__init__()
        self.input_name()

    def input_name(self):
        name = tk.StringVar()
        self.set_window('Input Name')
        self.configure(bg='white')
        text = tk.Label(self, text='Please, enter user name', bg='white', padx=150, pady=60)
        text.pack()
        input_text = ttk.Entry(self, textvariable=name)
        input_text.place(x=190, y=100)
        input_text.focus_force()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=204, y=230, width=100, height=30)
        clear_button = ttk.Button(self, text='Clear', command=lambda: input_text.delete(0, 'end'))
        clear_button.place(x=260, y=150, width=90, height=25)
        add_button = ttk.Button(self, text='Add',
                                command=lambda: self.add_user(input_text))
        add_button.place(x=160, y=150, width=90, height=25)

    def add_user(self, username_input):
        result = ManageUsersContr().add_user(username_input.get())
        username_input.delete(0, 'end')
        username_input.focus()
        if result == AddUserResult.OK:
            messagebox.showinfo('Complete', 'User add successful')
        if result == AddUserResult.ERROR_MESSAGE:
            messagebox.showerror('ERROR', 'Invalid message format\n\n Name must be string')
        if result == AddUserResult.NAME_EXIST:
            messagebox.showerror('ERROR', 'Username ' + username_input.get() + ' already exist')


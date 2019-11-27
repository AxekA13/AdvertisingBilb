import tkinter as tk
from tkinter import ttk
from BasicWindow import Window


class ManageUsersView(Window):
    def __init__(self):
        super().__init__()
        self.init_manage_users()

    def init_manage_users(self):
        self.configure(bg='white')
        self.set_window('Manage Users')
        add_user_button = ttk.Button(self, text='Add user')
        add_user_button.place(x=6, y=100, width=130, height=50)
        delete_user_button = ttk.Button(self, text='Delete user')
        delete_user_button.place(x=175, y=100, width=140, height=50)
        show_action_button = ttk.Button(self, text='Show user action')
        show_action_button.place(x=360, y=100, width=130, height=50)
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=195, y=200, width=100, height=30)

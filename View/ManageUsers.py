from tkinter import ttk
from View.BasicWindow import Window
from View.AddUser import AddUserView
from View.DeleteUser import DeleteUserView
from View.UserAction import UserActionView


class ManageUsersView(Window):
    def __init__(self):
        super().__init__()
        self.init_manage_users()

    def init_manage_users(self):
        self.configure(bg='white')
        self.set_window('Manage Users')
        add_user_button = ttk.Button(self, text='Add user', command=self.open_add_user_view)
        add_user_button.place(x=6, y=100, width=130, height=50)
        delete_user_button = ttk.Button(self, text='Delete user', command=self.open_delete_user_view)
        delete_user_button.place(x=175, y=100, width=140, height=50)
        show_action_button = ttk.Button(self, text='Show user action', command=lambda: UserActionView())
        show_action_button.place(x=360, y=100, width=130, height=50)
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=195, y=200, width=100, height=30)

    def open_add_user_view(self):
        AddUserView()
        self.destroy()

    def open_delete_user_view(self):
        DeleteUserView()
        self.destroy()

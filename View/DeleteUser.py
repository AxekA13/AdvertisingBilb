import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters import ManageUsersPresenter, UserPanelPresenter
from tkinter import messagebox


class DeleteUserView(Window):
    def __init__(self):
        super().__init__()
        self.show_delete_user()

    def show_delete_user(self):
        self.set_window('Delete User')
        self.configure(bg='white')
        self.focus_force()
        text = tk.Label(self, text='Please, select the user', bg='white', padx=150, pady=60)
        text.pack()
        username = tk.StringVar()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=201, y=230, width=100, height=30)
        delete_button = ttk.Button(self, text='Delete', command=lambda: self.delete_user(username))
        delete_button.place(x=201, y=150, width=100, height=30)
        select_user = ttk.Combobox(self, width=20, textvariable=username, state='readonly')
        select_user['values'] = ManageUsersPresenter.ManageUsersContr().user_remove_list()
        select_user.place(x=180, y=110)

    def delete_user(self, select_user):
        result = ManageUsersPresenter.ManageUsersContr().delete_user(select_user.get())
        if result == 0:
            messagebox.showerror('ERROR', 'Cannot delete user' + select_user.get())
        else:
            UserPanelPresenter.UserPanelContr().delete_frame(select_user.get())
            self.show_delete_user()
            self.destroy()
            messagebox.showinfo('Complete', 'User ' + select_user.get() + ' was successfully deleted')

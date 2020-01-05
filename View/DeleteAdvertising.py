import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from tkinter import messagebox
from Presenters.DeleteAdvPresenter import DeleteAdvController


class DeleteAdvertisingView(Window):
    def __init__(self, user, device):
        super().__init__()
        self.device = device
        self.controller = DeleteAdvController(user)
        self.show_delete_advertising()

    def show_delete_advertising(self):
        self.set_window('Delete Advertising')
        self.configure(bg='white')
        self.focus_force()
        text = tk.Label(self, text='Please, select the advertising', bg='white', padx=150, pady=60)
        text.pack()
        username = tk.StringVar()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=201, y=230, width=100, height=30)
        delete_button = ttk.Button(self, text='Delete', command=lambda: self.delete_advertising(self.select_advertising))
        delete_button.place(x=201, y=150, width=100, height=30)
        self.select_advertising = ttk.Combobox(self, width=20, textvariable=username, state='readonly')
        self.select_advertising['values'] = self.controller.get_advertising(self.device)
        self.select_advertising.place(x=180, y=110)

    def delete_advertising(self, select_advertising):
        result = self.controller.delete_advertising(self.device, select_advertising.get())
        if result == 0:
            messagebox.showerror('ERROR', 'Cannot delete advertising')
        else:
            self.show_delete_advertising()
            self.destroy()
            messagebox.showinfo('Complete', 'Advertising ' + 'was successfully deleted')


import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters import SetSchedulePresenter
from Presenters import ImportSchedulePresenter
from tkinter import messagebox


class SelectAdvImportView(Window):
    def __init__(self, user, device):
        super().__init__()
        self.show_select_form(user, device)

    def show_select_form(self, user, device):
        self.set_window('Select advertising')
        self.configure(bg='white')
        self.focus_force()
        text = tk.Label(self, text='Please, select the advertising', bg='white', padx=150, pady=60)
        text.pack()
        username = tk.StringVar()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=201, y=230, width=100, height=30)

        select_adv = ttk.Combobox(self, width=20, textvariable=username, state='readonly')
        select_adv['values'] = SetSchedulePresenter.SelectFormController(user).get_list_advertising(device)
        select_adv.place(x=180, y=100)
        select_adv_button = ttk.Button(self, text='Select advertising',
                                       command=lambda: self.check_select_advertising(user, device, select_adv.get()))
        select_adv_button.place(x=201, y=180, width=100, height=30)

    def check_select_advertising(self, user, device, advertising):
        if advertising == '':
            messagebox.showerror('ERROR', 'Select advertising')
        else:
            self.destroy()
            result = ImportSchedulePresenter.ImportScheduleController(user).select_file(device, advertising)
            if result == 4:
                messagebox.showerror('ERROR', 'Invalid format.Example {"interval": 6,"start": "15:30"}')
            elif result == 5:
                messagebox.showerror('ERROR', 'Use this format JSON file {"interval": value,"start": "5:30"}')
            elif result == 3:
                messagebox.showinfo('Complete', 'Import schedule was successful')
            else:
                messagebox.showerror('ERROR', 'Invalid format')

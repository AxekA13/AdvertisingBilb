import tkinter as tk
from tkinter import ttk
from View import AdminInformation, ManageDevices, ManageUsers, DeviceStatus, ManageAdvertising, ViewAdvertising
from Presenters import UserPanelPresenter, ViewAdvUserPresenter
from tkinter import messagebox
import os
import shutil
import logging
from View.UserAction import TextHandler


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        # Управление вкладками
        s = ttk.Style()
        s.configure('TNotebook.Tab', padding=[20, 5])
        s.configure('W.TButton', font=('arial', 'bold'))
        self.tab_control = ttk.Notebook(root)
        self.tab_user = tk.Frame(self.tab_control, bg='white')
        tab_admin = tk.Frame(self.tab_control, bg='white')
        self.tab_control.add(self.tab_user, text='Users')
        self.tab_control.add(tab_admin, text='Admin')
        self.tab_control.pack(expand=1, fill='both')
        self.tab_control.bind('<<NotebookTabChanged>>', personalData)

        # Окно Юзера
        text = tk.Label(self.tab_user, text='Please, select the user', bg='white', padx=150, pady=60)
        text.pack()
        username = tk.StringVar()
        close_button = ttk.Button(self.tab_user, text='Close', command=root.destroy)
        close_button.place(x=201, y=230, width=100, height=30)
        self.select_user_list = ttk.Combobox(self.tab_user, width=20, textvariable=username, state='normal')
        self.select_user_list['values'] = UserPanelPresenter.UserPanelContr().user_list()
        self.select_user_list.place(x=180, y=110)
        select_button = ttk.Button(self.tab_user, text='Select',
                                   command=lambda: self.select_user(self.select_user_list))
        select_button.place(x=201, y=150, width=100, height=30)

        # Окно Админа
        manage_devices_button = ttk.Button(tab_admin, text='Manage Devices',
                                           command=lambda: ManageDevices.ManageDevicesView())
        manage_devices_button.place(x=6, y=50, width=130, height=50)
        manage_users_button = ttk.Button(tab_admin, text='Manage Users', command=lambda: ManageUsers.ManageUsersView())
        manage_users_button.place(x=175, y=50, width=140, height=50)
        information_system_button = ttk.Button(tab_admin, text='Information',
                                               command=lambda: AdminInformation.ConfigureSystemView())
        information_system_button.place(x=360, y=50, width=130, height=50)
        view_adv_button = ttk.Button(tab_admin, text='View Advertising',command=self.show_admin_view_advertising)
        view_adv_button.place(x=175, y=130, width=140, height=50)
        close_button = ttk.Button(tab_admin, text='Close', command=root.destroy)
        close_button.place(x=195, y=210, width=100, height=30)

    def select_user(self, select_user):
        result = UserPanelPresenter.UserPanelContr().select_user(select_user.get())
        if result == 0:
            messagebox.showerror('ERROR', 'Select User' + select_user.get())
        else:
            self.update_user_box(result)
            self.select_user_list.delete(0, tk.END)

    def update_user_list(self):
        self.select_user_list['values'] = UserPanelPresenter.UserPanelContr().user_list()

    def update_user_box(self, user):
        result = UserPanelPresenter.UserPanelContr().add_user_box(user.name)
        if result is False:
            messagebox.showerror('ERROR', 'Window ' + user.name + ' is already created')
        else:
            tab_user = tk.Frame(self.tab_control, bg='white')
            UserPanelPresenter.UserPanelContr.user_box_list[user.name] = tab_user
            self.tab_control.add(tab_user, text=user.name)
            manage_advertising_button = ttk.Button(tab_user, text='Manage Advertising',
                                                   command=lambda: ManageAdvertising.ManageAdvertisingView(user))
            manage_advertising_button.place(x=6, y=90, width=130, height=50)
            view_status_button = ttk.Button(tab_user, text='View status of all devices',
                                            command=lambda: DeviceStatus.DeviceStatusView(user))
            view_status_button.place(x=175, y=90, width=140, height=50)
            view_advertising_button = ttk.Button(tab_user, text='View Advertising',
                                                 command=lambda: self.show_view_advertising(user))
            view_advertising_button.place(x=360, y=90, width=130, height=50)
            close_button = ttk.Button(tab_user, text='Close', command=root.destroy)
            close_button.place(x=195, y=200, width=100, height=30)
            self.tab_control.pack(expand=1, fill='both')

    def show_view_advertising(self, user):
        logging.info('User ' + user.name + ' view advertising ')
        devices = ViewAdvUserPresenter.ViewAdvUserController(user).get_device_list()
        if len(devices) == 0:
            messagebox.showerror('ERROR', 'there are no devices')
        else:
            for dev in devices:
                ViewAdvertising.ViewAdvertising(dev)

    def show_admin_view_advertising(self):
        logging.info('Admin view advertising ')
        devices = UserPanelPresenter.UserPanelContr().get_devices()
        if len(devices) == 0:
            messagebox.showerror('ERROR', 'there are no devices')
        else:
            for dev in devices:
                ViewAdvertising.ViewAdvertising(dev)


def personalData(event):
    if event.widget.index("current") == 0:
        app.update_user_list()


if __name__ == '__main__':
    root = tk.Tk()
    app = Main(root)
    app.pack()
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.title('Control System')
    root.geometry('500x300')
    root.wm_geometry('+%d+%d' % (x, y))
    root.resizable(False, False)
    # Create textLogger
    text_handler = TextHandler()

    # Logging configuration
    logging.basicConfig(filename=r'C:\Users\nasty\PycharmProjects\Bilbords\user_action.log',
                        level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Add the handler to logger
    logger = logging.getLogger()
    logger.addHandler(text_handler)

    root.mainloop()
    try:
        app.winfo_exists()
    except:
        folder = r'C:\Users\nasty\PycharmProjects\Bilbords\Server'
        for file in os.listdir(folder):
            file_path = os.path.join(folder, file)
            if os.path.isdir(file_path):
                shutil.rmtree(file_path)

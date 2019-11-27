import tkinter as tk
from tkinter import ttk
import ManageAdvertising
import DeviceStatus
import ManageDevices
import ManageUsers
import AdminInformation
from tkinter import messagebox


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()

    def init_main(self):
        # Управление вкладками
        s = ttk.Style()
        s.configure('TNotebook.Tab', padding=[20, 5])
        s.configure('W.TButton', font=('arial', 'bold'))
        tab_control = ttk.Notebook(root)
        tab_user = tk.Frame(tab_control, bg='white')
        tab_admin = tk.Frame(tab_control, bg='white')
        tab_control.add(tab_user, text='User')
        tab_control.add(tab_admin, text='Admin')
        tab_control.pack(expand=1, fill='both')

        # Окно Юзера
        manage_advertising_button = ttk.Button(tab_user, text='Manage Advertising',
                                               command=lambda: ManageAdvertising.ManageAdvertisingView())
        manage_advertising_button.place(x=6, y=90, width=130, height=50)
        view_status_button = ttk.Button(tab_user, text='View status of all devices',
                                        command=lambda: DeviceStatus.DeviceStatusView())
        view_status_button.place(x=175, y=90, width=140, height=50)
        view_advertising_button = ttk.Button(tab_user, text='View Advertising')
        view_advertising_button.place(x=360, y=90, width=130, height=50)
        close_button = ttk.Button(tab_user, text='Close', command=root.destroy)
        close_button.place(x=195, y=200, width=100, height=30)

        # Окно Админа
        manage_devices_button = ttk.Button(tab_admin, text='Manage Devices',
                                           command=lambda: ManageDevices.ManageDevicesView())
        manage_devices_button.place(x=6, y=50, width=130, height=50)
        manage_users_button = ttk.Button(tab_admin, text='Manage Users', command=lambda: ManageUsers.ManageUsersView())
        manage_users_button.place(x=175, y=50, width=140, height=50)
        information_system_button = ttk.Button(tab_admin, text='Information',
                                               command=lambda: AdminInformation.ConfigureSystemView())
        information_system_button.place(x=360, y=50, width=130, height=50)
        view_adv_button = ttk.Button(tab_admin, text='View Advertising')
        view_adv_button.place(x=175, y=130, width=140, height=50)
        close_button = ttk.Button(tab_admin, text='Close', command=root.destroy)
        close_button.place(x=195, y=210, width=100, height=30)


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

    root.mainloop()

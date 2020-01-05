from tkinter import ttk
from View.BasicWindow import Window
from View import AddAdvertising, DeviceDeleteAdvertising, SetSchedule

class ManageAdvertisingView(Window):
    def __init__(self, user):
        super().__init__()
        self.init_manage(user)

    def init_manage(self, user):
        self.configure(bg='white')
        self.set_window('ManageAdvertising')
        self.focus_force()
        add_advertising_button = ttk.Button(self, text='Add Advertising',
                                            command=lambda: self.show_add_advert(user))
        add_advertising_button.place(x=6, y=70, width=130, height=50)
        delete_advertising_button = ttk.Button(self, text='Delete Advertising',
                                               command=lambda: DeviceDeleteAdvertising.DeviceDeleteAdvertisingView(
                                                   user))
        delete_advertising_button.place(x=175, y=70, width=140, height=50)
        view_ad_statistics_button = ttk.Button(self, text='View Add Statistics')
        view_ad_statistics_button.place(x=360, y=70, width=130, height=50)
        set_schedule_button = ttk.Button(self, text='Set Schedule', command=lambda: SetSchedule.SetScheduleView(user))
        set_schedule_button.place(x=175, y=150, width=140, height=50)
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=195, y=250, width=100, height=30)

    def show_add_advert(self, user):
        self.destroy()
        AddAdvertising.AddAdvertisingView(user)

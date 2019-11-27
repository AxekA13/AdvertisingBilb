from tkinter import ttk
from BasicWindow import Window
import Statistic
import Monitoring


class ConfigureSystemView(Window):
    def __init__(self):
        super().__init__()
        self.init_config_system()

    def init_config_system(self):
        self.configure(bg='white')
        self.set_window('Information')
        monitoring_devices_button = ttk.Button(self, text='Monitoring devices', command=self.view_monitoring_devices)
        monitoring_devices_button.place(x=70, y=100, width=130, height=50)
        all_numbers_button = ttk.Button(self, text='View the numbers', command=self.view_statistics)
        all_numbers_button.place(x=300, y=100, width=130, height=50)
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=200, y=200, width=100, height=30)

    def view_statistics(self):
        Statistic.StatisticView().focus_force()
        self.destroy()

    def view_monitoring_devices(self):
        Monitoring.DeviceMonitoringView()
        self.destroy()

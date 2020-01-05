import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters.MonitoringPresenter import MonitoringContr


class DeviceMonitoringView(Window):
    def __init__(self):
        super().__init__()
        self.devices = self.list_device()
        self.init_status()

    def init_status(self):
        self.set_window('Monitoring')
        tree = ttk.Treeview(self, column=('ID', 'Name', 'Status', 'Advertising', 'Current size', 'Server size'),
                            height=15,
                            show='headings',
                            selectmode='browse')
        vsb = ttk.Scrollbar(self, orient='vertical', command=tree.yview)
        vsb.place(x=30 + 200 + 2, y=95, height=200 + 20)
        vsb.pack(side='right', fill='y')
        vsb2 = ttk.Scrollbar(self, orient='horizontal', command=tree.xview)
        vsb2.place(x=30 + 200 + 2, y=300, width=300 + 20)
        vsb2.pack(side='bottom', fill='x')
        tree.column('ID', width=120, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('Name', width=120, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('Status', width=120, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('Advertising', width=120, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('Current size', width=120, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('Server size', width=120, anchor=tk.CENTER, stretch=tk.NO)
        tree.heading('ID', text='ID')
        tree.heading('Name', text='Name')
        tree.heading('Status', text='Status')
        tree.heading('Advertising', text='Advertising')
        tree.heading('Current size', text='Current size')
        tree.heading('Server size', text='Server size')
        tree.configure(yscrollcommand=vsb.set)
        self.print_devices(tree)

        tree.pack()
        tree.focus_force()

    def list_device(self):
        result, code = MonitoringContr().device_list()
        if code == 0:
            return ()
        else:
            return result

    def print_devices(self, table):
        for item in self.devices:
            table.insert('', 'end', values=item)

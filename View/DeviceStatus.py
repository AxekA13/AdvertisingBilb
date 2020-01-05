import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters.DeviceStatusUserPresenter import StatusController


class DeviceStatusView(Window):
    def __init__(self, user):
        super().__init__()
        self.devices = self.list_device(user)
        self.init_status()

    def init_status(self):
        self.set_window('Device Status')
        self.tree = ttk.Treeview(self, column=('ID', 'Name', 'Status', 'Advertising', 'Current size', 'Server size'), height=15, show='headings',
                                 selectmode='browse')
        vsb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        vsb.place(x=30 + 200 + 2, y=95, height=200 + 20)
        vsb.pack(side='right', fill='y')
        vsb2 = ttk.Scrollbar(self, orient='horizontal', command=self.tree.xview)
        vsb2.place(x=30 + 200 + 2, y=300, width=300 + 20)
        vsb2.pack(side='bottom', fill='x')
        self.tree.column('ID', width=120, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.column('Name', width=120, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.column('Status', width=120, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.column('Advertising', width=120, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.column('Current size', width=120, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.column('Server size', width=120, anchor=tk.CENTER, stretch=tk.NO)
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Status', text='Status')
        self.tree.heading('Advertising', text='Advertising')
        self.tree.heading('Current size', text='Current size')
        self.tree.heading('Server size', text='Server size')
        self.tree.configure(yscrollcommand=vsb.set)
        self.print_devices(self.tree)

        self.tree.pack()
        self.focus_force()

    def list_device(self, user):
        result, code = StatusController().device_list(user)
        if code == 0:
            return ()
        else:
            return result

    def print_devices(self, table):
        for item in self.devices:
            table.insert('', 'end', values=item)

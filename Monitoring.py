import tkinter as tk
from tkinter import ttk
from BasicWindow import Window


class DeviceMonitoringView(Window):
    def __init__(self):
        super().__init__()
        self.init_status()

    def init_status(self):
        self.set_window('Monitoring')
        tree = ttk.Treeview(self, column=('ID', 'Name', 'Status', 'Advertising'), height=15, show='headings',
                            selectmode='browse')
        vsb = ttk.Scrollbar(self, orient='vertical', command=tree.yview)
        vsb.place(x=30 + 200 + 2, y=95, height=200 + 20)
        vsb.pack(side='right', fill='y')
        tree.column('ID', width=120, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('Name', width=120, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('Status', width=120, anchor=tk.CENTER, stretch=tk.NO)
        tree.column('Advertising', width=120, anchor=tk.CENTER, stretch=tk.NO)
        tree.heading('ID', text='ID')
        tree.heading('Name', text='Name')
        tree.heading('Status', text='Status')
        tree.heading('Advertising', text='Advertising')
        tree.configure(yscrollcommand=vsb.set)

        tree.pack()

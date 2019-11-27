import tkinter as tk
from tkinter import ttk
from BasicWindow import Window


class DeviceStatusView(Window):
    def __init__(self):
        super().__init__()
        self.init_status()

    def init_status(self):
        self.set_window('Device Status')
        self.tree = ttk.Treeview(self, column=('ID', 'Name', 'Status'), height=15, show='headings', selectmode='browse')
        vsb = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        vsb.place(x=30 + 200 + 2, y=95, height=200 + 20)
        vsb.pack(side='right', fill='y')
        self.tree.column('ID', width=155, anchor=tk.CENTER)
        self.tree.column('Name', width=160, anchor=tk.CENTER)
        self.tree.column('Status', width=165, anchor=tk.CENTER)
        self.tree.heading('ID', text='ID')
        self.tree.heading('Name', text='Name')
        self.tree.heading('Status', text='Status')
        self.tree.configure(yscrollcommand=vsb.set)

        self.tree.pack()

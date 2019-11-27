import tkinter as tk
from tkinter import ttk


class Window(tk.Toplevel):
    def set_window(self, title):
        self.configure(bg='white')
        x = (self.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.winfo_screenheight() - self.winfo_reqheight()) / 2
        self.title(title)
        self.geometry('500x300')
        self.wm_geometry('+%d+%d' % (x, y))
        self.resizable(False, False)
        self.grab_set()
        self.focus()

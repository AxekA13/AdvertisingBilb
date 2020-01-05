import time
import threading
import logging
import tkinter as tk  # Python 3.x
import tkinter.scrolledtext as ScrolledText
from View.BasicWindow import Window
from Presenters.UserActionPresenter import UserActionContr


class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06

    def __init__(self):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to

    def emit(self, record):
        msg = self.format(record)


class UserActionView(Window):

    # This class defines the graphical user interface

    def __init__(self):
        super().__init__()
        self.build_gui()

    def build_gui(self):
        # Build GUI
        self.configure(bg='white')
        self.set_window('User Action')
        self.grid()
        self.grid_columnconfigure(0, weight=1, uniform='a')
        self.grid_columnconfigure(1, weight=1, uniform='a')
        self.grid_columnconfigure(2, weight=1, uniform='a')
        self.grid_columnconfigure(3, weight=1, uniform='a')

        # Add text widget to display logging info
        scrollbar = tk.Scrollbar(self)
        st = ScrolledText.ScrolledText(self, state='disabled', xscrollcommand=scrollbar.set)
        st.configure(font='TkFixedFont')
        st.grid(column=0, row=1, sticky='w', columnspan=4)

        result = UserActionContr().get_log()
        for item in result:
            st.insert(tk.END, item + '\n')

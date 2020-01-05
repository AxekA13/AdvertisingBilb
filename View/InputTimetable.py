import tkinter as tk
from tkinter import ttk
from View.BasicWindow import Window
from Presenters import InputSchedulePresenter
from tkinter import messagebox


class InputTimetableView(Window):
    def __init__(self, user, device, advertising):
        super().__init__()
        self.show_input_timetable(user, device, advertising)

    def show_input_timetable(self, user, device, advertising):
        self.set_window('Input schedule')
        self.configure(bg='white')
        self.focus_force()
        interval = tk.StringVar()
        start_time = tk.StringVar()
        text_interval = tk.Label(self, text='Enter interval (number of times per hour)', bg='white')
        text_interval.place(x=10, y=60)
        input_interval = ttk.Entry(self, textvariable=interval)
        input_interval.place(x=60, y=100)
        input_interval.focus_force()
        text_start = tk.Label(self, text='Enter start time (example 19:00)', bg='white')
        text_start.place(x=280, y=60)
        input_start = ttk.Entry(self, textvariable=start_time)
        input_start.place(x=300, y=100)
        input_start.focus_force()
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=204, y=250, width=100, height=30)
        set_button = ttk.Button(self, text='Set',
                                command=lambda: self.check_input(user, device, advertising, input_interval,
                                                                 input_start))
        set_button.place(x=204, y=180, width=100, height=30)

    def check_input(self, user, device, advertising, interval, start):
        result, balance = InputSchedulePresenter.InputScheduleController(user).check_schedule_to_adv(device,
                                                                                                     advertising,
                                                                                                     interval.get(),
                                                                                                     start.get())
        if result == 0:
            messagebox.showerror('ERROR', 'Invalid format. The time should start with a full hour (ex. 19:00)')
        elif result == 1:
            messagebox.showerror('ERROR', 'Enter an hour longer than the current one')
        elif result == 2:
            messagebox.showerror('ERROR',
                                 'Incorrect number of times per hour, because there are already other ads in the current hour')
        elif result == 4:
            messagebox.showerror('ERROR', 'Reduce the number of times per hour, balance = ' + str(balance))
        else:
            messagebox.showinfo('Successful', 'The schedule is successfully installed, balance = ' + str(balance))
            self.destroy()

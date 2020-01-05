from tkinter import ttk
from View.BasicWindow import Window
from View.ImportSchedule import ImportScheduleView
from View.SelectFormSchedule import SelectDevAdvView
from View.SelectDeviceScheduleExport import SelectDevScheduleView


class SetScheduleView(Window):
    def __init__(self, user):
        super().__init__()
        self.show_set_schedule_view(user)

    def show_set_schedule_view(self, user):
        self.set_window('Set Schedule')
        self.configure(bg='white')
        self.focus_force()
        set_schedule_button = ttk.Button(self, text='Make Schedule',
                                         command=lambda: SelectDevAdvView(user))
        set_schedule_button.place(x=6, y=80, width=130, height=50)
        import_schedule_button = ttk.Button(self, text='Import Schedule', command=lambda: ImportScheduleView(user))
        import_schedule_button.place(x=175, y=80, width=140, height=50)
        export_schedule_button = ttk.Button(self, text='Export Schedule', command=lambda: SelectDevScheduleView(user))
        export_schedule_button.place(x=360, y=80, width=130, height=50)
        close_button = ttk.Button(self, text='Close', command=self.destroy)
        close_button.place(x=195, y=200, width=100, height=30)

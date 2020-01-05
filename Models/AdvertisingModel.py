import os


class AdvertisingModel:
    numbers = 0

    def __init__(self, name, size, timescale):
        self.name = name
        self.size = size
        self.timetable = None
        self.status = 'Waiting'
        self.timescale = timescale
        AdvertisingModel.numbers += 1

    def get_timetable(self):
        return self.timetable.start_time

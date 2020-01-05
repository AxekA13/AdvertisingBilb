import random


class Timetable:
    def __init__(self, interval, start_time):
        self.interval = interval  # amount of show per hour
        self.amount_of_shows = 0
        self.amount_of_shows_minutes = 0
        self.uid = self.uid = random.randrange(1000, 10001, 1)
        self.start_time = start_time

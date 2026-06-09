import datetime
import time

class Event:
    def __init__(self):
        self.id: int
        self.calendar_date: CalendarDate
        self.title: str
        self.description: str
        self.time = time.time()

class CalendarDate:
    def __init__(self, day: int, month: int, year: int, is_holiday = False):
        self.calendar_date = datetime.datetime(
            year,
            month,
            day,
            tzinfo=datetime.timezone(-datetime.timedelta(hours=4), "Chile Standard Time") 
            # TODO: update this so it automatically changes for daylight savings,
            # it's possible, I remember I read it in the documentation but I don't remember how to do it T-T
        )
        self.weekday_name = self.calendar_date.strftime("%A")
        self.is_holiday = is_holiday
        self.note = ""

    def set_note(self, new_note: str = ""):
        if len(new_note) > 255:
            raise ValueError
        self.note = new_note
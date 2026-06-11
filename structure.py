from zoneinfo import ZoneInfo
import datetime
from typing import Optional

class CalendarDate:
    def __init__(self, day: int, month: int, year: int, is_holiday = False):
        self.calendar_date = datetime.datetime(
            year,
            month,
            day,
            tzinfo=ZoneInfo("Chile/Continental")
        )
        self.weekday_name = self.calendar_date.strftime("%A")
        self.is_holiday = is_holiday
        self.note = ""

    def set_note(self, new_note: str = ""):
        if len(new_note) > 255:
            raise ValueError
        self.note = new_note

class Event:
    def __init__(self, calendar_date: CalendarDate, title: str, description: Optional[str] = None, time: Optional[datetime.time] = None):
        self.id: int
        self.calendar_date: CalendarDate
        self.title: str
        self.description: str
        self.time: datetime.time
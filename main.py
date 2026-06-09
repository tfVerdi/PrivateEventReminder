import database as db
import structure 
import time

if __name__ == "__main__":
    DB = db.Database()
    DB.add_calendar_date(structure.CalendarDate(10, 6, 2026))
    DB.add_event("test_Dia del completo", "Dia del completo, vamos Chile!!!", 24, 5, 2026)
    DB.add_event("test_Grandma's accidental falling through the stairs", "No Mr. Insurance man, she did not plan to fall from the beginning and we did not conspire with her to achieve that.", 12, 6, 2026, time.time())
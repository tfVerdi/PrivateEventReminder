import database as db
import structure 

if __name__ == "__main__":
    DB = db.Database()
    test_date = structure.CalendarDate(10, 6, 2026)
    DB.add_calendar_date(test_date)
    DB.add_event(structure.Event(test_date, "test_Dia del completo", "Dia del completo, vamos Chile!!!"))
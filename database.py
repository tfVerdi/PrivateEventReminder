from dotenv import load_dotenv
from structure import CalendarDate, Event
import os
import mysql.connector

class Database:
    def __init__(self):
        load_dotenv()

        self.MYSQL_NAME = os.getenv("MYSQL_NAME")
        self.MYSQL_PASS = os.getenv("MYSQL_PASS")
        self.HOST = os.getenv("HOST")
        self.DATABASE = os.getenv("DATABASE")
    
    def create_tables(self):
        with mysql.connector.connect(user=self.MYSQL_NAME, password=self.MYSQL_PASS, host=self.HOST, database=self.DATABASE) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"USE {self.DATABASE};")
                cursor.execute("""CREATE TABLE IF NOT EXISTS calendar_date (
                CalendarDate  DATE          NOT NULL,
                WeekdayName   VARCHAR(10)   NOT NULL,
                IsHoliday     BOOLEAN       DEFAULT FALSE,
                Note          VARCHAR(255),
                PRIMARY KEY (CalendarDate)
                );
                
                CREATE TABLE IF NOT EXISTS event (
                ID_Event      INT           NOT NULL AUTO_INCREMENT,
                CalendarDate  DATE          NOT NULL,
                Title         VARCHAR(255)  NOT NULL,
                Description   VARCHAR(1000),
                EventTime     TIME,
                PRIMARY KEY (ID_Event),
                FOREIGN KEY (CalendarDate) REFERENCES calendar_date(CalendarDate)
                );""")
                connection.commit()
    
    def add_calendar_date(self, calendar_date: CalendarDate):
        with mysql.connector.connect(user=self.MYSQL_NAME, password=self.MYSQL_PASS, host=self.HOST, database=self.DATABASE) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"USE {self.DATABASE};")
                cursor.execute(f"""INSERT INTO calendar_date (CalendarDate, WeekdayName, IsHoliday, Note) VALUES (\
                    '{calendar_date.calendar_date.year}-{calendar_date.calendar_date.month}-{calendar_date.calendar_date.day}', \
                    '{calendar_date.weekday_name}', \
                    {calendar_date.is_holiday}, \
                    {("'" + calendar_date.note + "'") if calendar_date.note else "NULL"}\
                    );""")
                connection.commit()
    
    def add_event(self, event: Event, double_check_day: bool = True):
        calendar_date = event.calendar_date.calendar_date
        with mysql.connector.connect(user=self.MYSQL_NAME, password=self.MYSQL_PASS, host=self.HOST, database=self.DATABASE) as connection:
            with connection.cursor() as cursor:
                cursor.execute(f"USE {self.DATABASE};")
                if double_check_day:
                    cursor.execute(f"SELECT * FROM calendar_date WHERE CalendarDate = '{calendar_date.year}-{calendar_date.month}-{calendar_date.day}';")
                    result = [i for i in cursor] # type: ignore
                    if len(result) == 0:
                        self.add_calendar_date(CalendarDate(day=calendar_date.day, month=calendar_date.month, year=calendar_date.year))
                if event.time == None:
                    cursor.execute(f"""INSERT INTO events (CalendarDate, Title, Description) VALUES (\
                        '{calendar_date.year}-{calendar_date.month}-{calendar_date.day}', '{event.title}', '{event.description}'
                        );""")
                else:
                    cursor.execute(f"""INSERT INTO events (CalendarDate, Title, Description, EventTime) VALUES (\
                        '{calendar_date.year}-{calendar_date.month}-{calendar_date.day}', '{event.title}', '{event.description}',\
                        '{event.time.hour}:{event.time.hour}:{event.time.second}'\
                        );""")
                connection.commit()


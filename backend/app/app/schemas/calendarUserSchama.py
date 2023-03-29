from pydantic import BaseModel

class CalendarInDB(BaseModel):
    pass

class CalendarCreateDTO(CalendarInDB):
    pass

class CalendarUpdateDTO(CalendarInDB):
    pass

class CalendarDeleteDTO(CalendarInDB):
    pass

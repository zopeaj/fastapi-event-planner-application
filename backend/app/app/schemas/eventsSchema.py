from pydantic import BaseModel

class EventsInDB(BaseModel):
    pass

class EventsCreateDTO(EventsInDB):
    pass

class EventsUpdateDTO(EventsInDB):
    pass

class EventsDeleteDTO(BaseModel):
    pass

    class Config:
        orm_mode = True

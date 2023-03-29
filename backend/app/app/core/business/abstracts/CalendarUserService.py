import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.crud.repository.CalendarUserRepository import CalendarUserRepository
from app.models.calendarUser import CalendarUser

class CalendarUserService:
    def __init__(self, calendarUserRepository):
        self.calendarUserRepository = calendarUserRepository

    def save(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass

    def getById(self):
        pass

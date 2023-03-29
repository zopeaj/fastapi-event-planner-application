import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.db.get_db import get_db
from sqlalchemy.orm import Session
from app.models.events import Event
from fastapi import Depends

class EventsRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def saveEvent(self):
        pass

    def deleteEvent(self):
        pass

    def updateEvent(self):
        pass

    def getEventById(self):
        pass

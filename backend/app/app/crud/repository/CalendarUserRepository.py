import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.models.calendarUser import CalendarUser
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.get_db import get_db

class CalendarUserRepository:
    def __init__(self):
        self.db: Session = Depends(get_db)

    def findByEmail(email):
        pass



import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from uuid import uuid4
from sqlalchemy import Column, Integer, String, Boolean, Sequence, relationship
from app.db.base import Base



class Event(Base):
    id = Column(Integer, primary_key=True, default=uuid4)
    summary = Column(String, nullable=False)
    description = Column(String, nullable=False)
    when = Column(String)
    calendaruser = relationship("CalendarUser", back_populates="roles")
    attendee = relationship("CalendarUser", back_populates="roles")

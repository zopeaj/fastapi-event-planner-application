import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.db.base import Base
from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship

class CalendarUser(Base):
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    password = Column(String)
    roles = relationship("Role", back_populates="calendaruser", uselist=True)

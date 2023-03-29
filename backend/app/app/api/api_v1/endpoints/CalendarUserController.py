import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import APIRouter, Response, status
from app.core.business.abstracts.CalendarUserService import CalendarUserService
from app.models.calendarUser import CalendarUser

calendaruserroutes = APIRouter()

@calendaruserroutes.post("/")
def create_calendar_user():
    pass

@calendaruserroutes.get("/")
def get_calendar_user():
    pass

@calendaruserroutes.put("/")
def update_calendar_user():
    pass

@calendaruserroutes.delete("/")
def delete_calendar_user():
    pass


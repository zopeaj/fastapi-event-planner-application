import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import APIRouter
from app.api.api_v1.endpoints.CalendarUserController import calendaruserroutes
from app.api.api_v1.endpoints.EventsController import eventroutes

api_router = APIRouter()
api_router.include_router(calendaruserroutes, prefix="", tags=[""])
api_router.include_router(eventroutes, prefix="", tags=[""])


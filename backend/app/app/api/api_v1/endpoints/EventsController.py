import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from fastapi import APIRouter, Response, status
from app.core.business.abstracts.EventsService import EventService
from app.models.events import Event

eventroutes = APIRouter()

@eventroutes.post("/")
def create_event_for_user():
    pass

@eventroutes.update("/")
def update_event_for_user():
    pass

@eventroutes.get("/")
def get_event_for_user():
    pass


@eventroutes.delete("/")
def delete_event_for_user():
    pass



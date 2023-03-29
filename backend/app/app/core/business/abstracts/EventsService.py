import os
import sys
from dotenv import load_dotenv
load_dotenv()

path = os.environ["FILE_PATH"]
sys.path.append(path)

from app.crud.repository.EventsRepository import EventRepository
from app.models.events import Event

class EventsService:
    def __init__(self, eventsRepository):
        self.eventsRepository = eventsRepository

    def save(self):
        pass

    def update(self):
        pass

    def get(self):
        pass

    def delete(self):
        pass

import pytest
from .events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New registry")
def test_insert_event():
    event = {
        "uuid": "UUID2",
        "title": "TITLE",
        "slug": "SLUG2",
        "maximum_attendees": 10,
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

@pytest.mark.skip(reason="Get by id")
def test_get_event_by_id():
    event_id = "UUID"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)

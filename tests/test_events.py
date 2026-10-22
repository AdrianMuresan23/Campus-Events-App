
from app import app


def test_get_events_returns_200():
    response = app.test_client().get("/api/events")
    assert response.status_code == 200


def test_get_events_returns_list():
    response = app.test_client().get("/api/events")
    assert isinstance(response.get_json(), list)


def test_get_events_contains_events():
    response = app.test_client().get("/api/events")
    events = response.get_json()

    assert len(events) >= 1

    for event in events:
        assert "id" in event
        assert "title" in event
        assert "date" in event

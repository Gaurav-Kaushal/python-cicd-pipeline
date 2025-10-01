import json
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to the Task Manager API!" in response.data

def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert type(data) == list
    assert len(data) >= 2

def test_add_task():
    client = app.test_client()
    response = client.post("/tasks", json={"title": "New Task"})
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data["title"] == "New Task"

def test_delete_task():
    client = app.test_client()
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "Task deleted" in data["message"]

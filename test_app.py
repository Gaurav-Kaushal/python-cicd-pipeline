import pytest
from app import app, tasks

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Welcome to the Task Manager API!" in res.data

def test_get_tasks(client):
    res = client.get("/tasks")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data, list)
    assert len(data) >= 2  # initial 2 tasks

def test_add_task(client):
    res = client.post("/tasks", json={"title": "New Task"})
    assert res.status_code == 201
    data = res.get_json()
    assert data["title"] == "New Task"
    assert data["done"] is False

def test_add_task_missing_title(client):
    res = client.post("/tasks", json={})
    assert res.status_code == 400
    data = res.get_json()
    assert "error" in data

def test_update_task(client):
    res = client.put("/tasks/1")
    assert res.status_code == 200
    data = res.get_json()
    assert data["done"] is True

def test_update_task_not_found(client):
    res = client.put("/tasks/999")
    assert res.status_code == 404
    data = res.get_json()
    assert "error" in data

def test_delete_task(client):
    res = client.delete("/tasks/2")
    assert res.status_code == 200
    data = res.get_json()
    assert "Task deleted" in data["message"]

    res2 = client.get("/tasks")
    data2 = res2.get_json()
    assert all(task["id"] != 2 for task in data2)

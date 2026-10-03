from fastapi.testclient import TestClient

from app.main import _todos, app

client = TestClient(app)


def setup_function():
    """Reinicia el almacenamiento en memoria antes de cada test."""
    _todos.clear()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_create_and_list_todo():
    response = client.post("/todos", json={"title": "Aprender FastAPI"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Aprender FastAPI"
    assert data["completed"] is False

    response = client.get("/todos")
    assert response.status_code == 200
    assert len(response.json()) == 1


def test_get_todo():
    created = client.post("/todos", json={"title": "Tarea de prueba"}).json()
    response = client.get(f"/todos/{created['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == "Tarea de prueba"


def test_update_todo():
    created = client.post("/todos", json={"title": "Tarea original"}).json()
    response = client.put(f"/todos/{created['id']}", json={"completed": True})
    assert response.status_code == 200
    assert response.json()["completed"] is True


def test_delete_todo():
    created = client.post("/todos", json={"title": "Tarea a borrar"}).json()
    response = client.delete(f"/todos/{created['id']}")
    assert response.status_code == 204

    response = client.get(f"/todos/{created['id']}")
    assert response.status_code == 404


def test_get_nonexistent_todo():
    response = client.get("/todos/999")
    assert response.status_code == 404

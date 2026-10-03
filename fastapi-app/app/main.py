"""
API de tareas (To-Do) — proyecto de ejemplo en FastAPI para el taller de CI/CD.

Equivalente conceptual de 04-app (Node/Express), pero en Python, para comparar
cómo se ve el mismo tipo de proyecto en otro stack.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Taller CI/CD — API de tareas",
    description="Ejemplo en FastAPI para comparar con la app de Node del taller",
    version="1.0.0",
)


class Todo(BaseModel):
    id: int
    title: str
    completed: bool = False


class TodoCreate(BaseModel):
    title: str


class TodoUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None


# Almacenamiento en memoria (se reinicia cada vez que arranca el proceso).
# Intencionalmente simple: el objetivo es el pipeline de CI/CD, no la persistencia.
_todos: dict[int, Todo] = {}
_next_id: int = 1


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/")
def root() -> dict:
    return {"message": "Bienvenido a la API de tareas del taller de CI/CD"}


@app.get("/todos", response_model=list[Todo])
def list_todos() -> list[Todo]:
    return list(_todos.values())


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(payload: TodoCreate) -> Todo:
    global _next_id
    todo = Todo(id=_next_id, title=payload.title)
    _todos[_next_id] = todo
    _next_id += 1
    return todo


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int) -> Todo:
    todo = _todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    return todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, payload: TodoUpdate) -> Todo:
    todo = _todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    if payload.title is not None:
        todo.title = payload.title
    if payload.completed is not None:
        todo.completed = payload.completed
    _todos[todo_id] = todo
    return todo


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int) -> None:
    if todo_id not in _todos:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")
    del _todos[todo_id]

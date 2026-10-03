# FastAPI — API de tareas (To-Do)

Proyecto adicional del taller, en **Python/FastAPI**, para comparar contra la app de Node (`04-app/`). No es parte de la secuencia numerada (`00` a `07`) del taller: es material extra para mostrar cómo cambian (o no cambian) los mismos conceptos de CI/CD al cambiar de stack.

## ¿Por qué este proyecto y no el mismo de Node en Python?

Elegimos una API de tareas (CRUD en memoria) en vez de replicar exactamente la app de Node, para que el grupo vea algo ligeramente distinto: múltiples rutas, un modelo de datos con Pydantic, y una API REST más "completa" (`GET`, `POST`, `PUT`, `DELETE`). El objetivo sigue siendo el mismo: comparar el **pipeline**, no competir en complejidad de la app.

## Comparación rápida: Node (`04-app/`) vs FastAPI (`fastapi-app/`)

| | Node (`04-app/`) | FastAPI (`fastapi-app/`) |
|---|---|---|
| Framework | Express | FastAPI |
| Gestor de paquetes | npm | pip |
| Archivo de dependencias | `package.json` | `requirements.txt` / `requirements-dev.txt` |
| Validación de datos | Manual | Automática, con Pydantic |
| Lint | ESLint | Ruff |
| Tests | `node --test` | `pytest` |
| Servidor | Node nativo | Uvicorn (servidor ASGI) |
| Dockerfile | 1 stage | 5 stages (`base`, `dev-deps`, `dev`, `builder`, `prod-deps`, `prod`) |
| Docs de la API | — | Automáticas en `/docs` (Swagger UI) |

## Correr localmente (sin Docker)

```bash
cd fastapi-app
python -m venv .venv
source .venv/bin/activate   # En Windows: .venv\Scripts\activate
pip install -r requirements.txt -r requirements-dev.txt

uvicorn app.main:app --reload
```

Visita `http://localhost:8000/docs` para la documentación interactiva (esto no existe en el proyecto de Node, es una ventaja propia de FastAPI).

## Lint y tests

```bash
ruff check .
pytest
```

## Docker — las 5 stages

El `Dockerfile` tiene un patrón más elaborado que el de `04-app/`, pensado para mostrar cómo se ve un multi-stage build real:

| Stage | Para qué sirve |
|---|---|
| `base` | Imagen base compartida por el resto de las stages |
| `dev-deps` | Instala **todas** las dependencias (producción + desarrollo/tests) |
| `dev` | Entorno de desarrollo local, con `--reload` activado |
| `builder` | Genera los *wheels* (paquetes ya compilados) de las dependencias de producción |
| `prod-deps` | Instala **solo** las dependencias de producción, desde los wheels |
| `prod` | Imagen final, mínima, sin herramientas de build, usuario no root — **esta es la que se publica y se despliega** |

Construir la imagen de desarrollo:
```bash
docker build --target dev -t taller-fastapi:dev .
docker run -p 8000:8000 -v $(pwd):/app taller-fastapi:dev
```

Construir la imagen de producción (la que usa el CI/CD):
```bash
docker build --target prod -t taller-fastapi:prod .
docker run -p 8000:8000 taller-fastapi:prod
```

(`docker build .` sin `--target` construye `prod` por defecto, al ser la última stage del archivo.)

## Endpoints

| Método | Ruta | Descripción |
|---|---|---|
| `GET` | `/health` | Healthcheck |
| `GET` | `/` | Mensaje de bienvenida |
| `GET` | `/todos` | Lista todas las tareas |
| `POST` | `/todos` | Crea una tarea (`{"title": "..."}`) |
| `GET` | `/todos/{id}` | Obtiene una tarea |
| `PUT` | `/todos/{id}` | Actualiza una tarea (`title` y/o `completed`) |
| `DELETE` | `/todos/{id}` | Elimina una tarea |

## CI/CD

Este proyecto tiene sus propios workflows, separados de los de `04-app/`, aunque viven en el mismo `.github/workflows/` (GitHub solo reconoce ese único directorio en la raíz del repo):

- **`ci-fastapi.yml`** — lint (Ruff) + tests (pytest)
- **`docker-publish-fastapi.yml`** — build de la stage `prod`, caché, Trivy, publicación en GHCR (con un tag distinto: `...-fastapi`) y disparo del deploy en Render
- **`healthcheck-fastapi.yml`** — verificación post-deploy, con reintentos

Los tres usan un filtro `paths: fastapi-app/**`, así que **solo se disparan si tocas algo dentro de esta carpeta** — tocar `04-app/` no los activa, y viceversa.

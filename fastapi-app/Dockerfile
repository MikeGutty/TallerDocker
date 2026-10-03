# syntax=docker/dockerfile:1
#
# Dockerfile multi-stage para la API de tareas (FastAPI).
# A diferencia del Dockerfile simple de 04-app (Node), aquí mostramos el
# patrón completo de 5 stages que se usa en proyectos reales:
#
#   base ──┬─→ dev-deps ─→ dev           (entorno de desarrollo local)
#          └─→ builder ─→ prod-deps ─→ prod   (imagen final de producción)
#
# `docker build` sin --target construye la ÚLTIMA stage (prod) por defecto.
# Para desarrollo local: docker build --target dev -t taller-fastapi:dev .

# ---------------------------------------------------------------------------
# base: todo lo que comparten el resto de las stages
# ---------------------------------------------------------------------------
FROM python:3.14-slim AS base
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1


# ---------------------------------------------------------------------------
# dev-deps: instala TODAS las dependencias (producción + desarrollo/tests)
# ---------------------------------------------------------------------------
FROM base AS dev-deps
COPY requirements.txt requirements-dev.txt ./
RUN pip install -r requirements.txt -r requirements-dev.txt


# ---------------------------------------------------------------------------
# dev: entorno de desarrollo local, con hot-reload y el código montado
# ---------------------------------------------------------------------------
FROM dev-deps AS dev
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]


# ---------------------------------------------------------------------------
# builder: genera los wheels (paquetes ya compilados) de las dependencias
# de producción, para no necesitar herramientas de build en la imagen final
# ---------------------------------------------------------------------------
FROM base AS builder
COPY requirements.txt ./
RUN pip wheel --wheel-dir /wheels -r requirements.txt


# ---------------------------------------------------------------------------
# prod-deps: instala SOLO las dependencias de producción (sin pytest, ruff,
# ni nada de desarrollo), usando los wheels ya construidos
# ---------------------------------------------------------------------------
FROM base AS prod-deps
COPY --from=builder /wheels /wheels
COPY requirements.txt ./
RUN pip install --no-index --find-links=/wheels -r requirements.txt


# ---------------------------------------------------------------------------
# prod: imagen final. Parte de python:3.13-slim limpia (no de "base", para
# no arrastrar capas intermedias), usuario no root, y solo el código + las
# dependencias de producción ya instaladas. Esta es la imagen que se publica
# en GHCR y se despliega en Render.
# ---------------------------------------------------------------------------
FROM python:3.14-slim AS prod
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN useradd --create-home --shell /bin/bash appuser

COPY --from=prod-deps /usr/local/lib/python3.14/site-packages /usr/local/lib/python3.14/site-packages
COPY --from=prod-deps /usr/local/bin /usr/local/bin
COPY app ./app

USER appuser

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Paso 2 — Docker

**Tag de referencia:** `paso-2-docker`

## Objetivo

Construir y correr la imagen Docker de la app del taller, y levantarla junto a un segundo servicio con Docker Compose.

## Qué hacer

(Pendiente de completar con el detalle de la práctica guiada — ver `03-docker/ejemplos/`)

## Cómo verifico que funcionó

- `docker build -t taller-app .` termina sin errores
- `curl http://localhost:3000/health` responde `{"status":"ok"}`
- `docker compose up -d` levanta los dos servicios (`app` y `cache`) sin errores
- `docker compose ps` muestra ambos contenedores como `running`

## Reto avanzado

Ver sección "Reto avanzado" en [`03-docker/README.md`](../03-docker/README.md)

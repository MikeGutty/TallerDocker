# Ejemplos — Docker

## Ejemplo 1 — Correr una imagen ya existente

```bash
docker run hello-world
docker run -p 8080:80 nginx
```

Abre `http://localhost:8080` en el navegador.

## Ejemplo 2 — Dockerfile de nuestra app

Este es el Dockerfile que usaremos para la app del taller (carpeta [`04-app/`](../../04-app/) en la raíz del repo):

```dockerfile
FROM node:22-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
```

Construir y correr:

```bash
docker build -t taller-app .
docker run -p 3000:3000 taller-app
```

Verifica en `http://localhost:3000/health`.

## Ejemplo 3 — Docker Compose (app + Redis)

Hasta ahora corrimos un solo contenedor. Este ejemplo levanta **dos servicios a la vez**: nuestra app y una caché en Redis, comunicándose entre sí.

Archivo `docker-compose.yml` (colócalo junto al `Dockerfile`, en `04-app/`):

```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - REDIS_URL=redis://cache:6379
    depends_on:
      - cache

  cache:
    image: redis:7-alpine
    ports:
      - "6379:6379"
```

Puntos clave para explicar en vivo:

- **`services`**: cada bloque es un contenedor. Aquí hay dos: `app` y `cache`.
- **`build: .`** vs **`image: redis:7-alpine`**: `app` se construye desde nuestro Dockerfile; `cache` usa una imagen ya publicada en Docker Hub, no hace falta escribirle un Dockerfile.
- **`depends_on`**: le dice a Compose que levante `cache` antes que `app`.
- **Red interna automática**: dentro de Compose, `app` puede llamar a `cache` por su *nombre de servicio* (`redis://cache:6379`), sin necesidad de IPs ni `localhost`. Esto es lo que Compose resuelve que `docker run` no resuelve solo.

Levantar y verificar:

```bash
docker compose up -d
docker compose ps
docker compose logs -f app
docker compose down
```

> Nota: para que este ejemplo use Redis de verdad, la app necesitaría código adicional que se conecte a `REDIS_URL` (no viene incluido en el starter, que es intencionalmente mínimo). El objetivo aquí es que el participante entienda la mecánica de Compose, no implementar caché real.

## Reto avanzado — Multi-stage build

```dockerfile
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .

FROM node:22-alpine
WORKDIR /app
COPY --from=builder /app ./
USER node
EXPOSE 3000
CMD ["npm", "start"]
```

Compara el tamaño de ambas imágenes con `docker images`.

## Reto avanzado — Volumen en Compose

Agrega persistencia a Redis para que los datos sobrevivan un `docker compose down`:

```yaml
services:
  cache:
    image: redis:7-alpine
    volumes:
      - redis-data:/data

volumes:
  redis-data:
```

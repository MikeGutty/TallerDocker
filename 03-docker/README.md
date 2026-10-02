# 03 — Docker

Fundamentos de Docker, con foco en lo que luego automatizamos en CI/CD.

## Objetivos

- Entender la diferencia entre imagen y contenedor
- Correr un contenedor desde una imagen ya existente
- Escribir el Dockerfile de nuestra app y construir la imagen
- Entender el concepto de capas y el `.dockerignore` (esto conecta directo con la optimización de caché que veremos en CI)
- Usar Docker Compose para levantar nuestra app junto a un segundo servicio (ej. una caché en Redis) con un solo comando

## Comandos clave — Docker

```bash
docker run hello-world
docker run -p 8080:80 nginx
docker build -t mi-app .
docker run -p 3000:3000 mi-app
docker ps
docker logs <container-id>
docker images
```

## Comandos clave — Docker Compose

```bash
docker compose up
docker compose up -d
docker compose down
docker compose logs -f
docker compose ps
```

## ¿Por qué Docker Compose, si nuestra app es un solo contenedor?

Hasta ahora, cada `docker run` levanta **un** contenedor. Pero en proyectos reales casi siempre hay más de un servicio corriendo a la vez (la app + una base de datos, una caché, etc.). Compose resuelve dos problemas:

1. **Evita comandos largos repetidos.** En vez de recordar `docker run -p 3000:3000 -e REDIS_URL=... --network ... mi-app`, defines todo una vez en un archivo `docker-compose.yml` y corres `docker compose up`.
2. **Orquesta varios contenedores juntos**, con su propia red interna, para que se puedan comunicar entre sí por nombre de servicio.

## Práctica

Ver la carpeta [`ejemplos/`](./ejemplos/) para los ejemplos progresivos, incluyendo el ejemplo de Compose con dos servicios.

## Reto avanzado (para quienes ya tienen experiencia)

- Convertir el Dockerfile a multi-stage build
- Configurar un usuario no root
- Agregar un `HEALTHCHECK` al Dockerfile
- Comparar el tamaño final de la imagen antes y después de optimizar
- Agregar un volumen a Compose para persistir datos entre reinicios

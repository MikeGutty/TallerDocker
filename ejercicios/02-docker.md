# Ejercicios — Docker

Puedes usar la app del taller (`04-app/` o `fastapi-app/`) para varios de estos, o crear algo mínimo propio.

---

## 1. Tu primer Dockerfile desde cero 🟢

**Enunciado:** Sin mirar los Dockerfiles del taller, escribe uno propio para una app simple (puede ser un `index.html` servido con nginx, o un script de una sola línea). Constrúyelo y córrelo.

**Pista:** `FROM nginx:alpine` + `COPY` tu archivo a `/usr/share/nginx/html/` es la forma más corta de lograrlo.

**Cómo verifico que funcionó:** `docker run -p 8080:80 tu-imagen` y ver tu contenido en `http://localhost:8080`.

---

## 2. Variables de entorno en un contenedor 🟢

**Enunciado:** Modifica temporalmente la app del taller (`04-app/src/index.js`) para que lea una variable de entorno (ej. `SALUDO`) y la incluya en la respuesta de `GET /`. Pasa esa variable al correr el contenedor.

**Pista:** `docker run -e SALUDO="Hola taller" ...`

**Cómo verifico que funcionó:** Cambias el valor de `SALUDO` entre una corrida y otra, sin reconstruir la imagen, y la respuesta cambia.

---

## 3. Persistir datos con un volumen 🟡

**Enunciado:** Corre un contenedor de `redis` (o `postgres`) con un volumen montado. Escribe un dato, detén y elimina el contenedor, y vuelve a levantarlo con el mismo volumen. Confirma que el dato sigue ahí.

**Pista:** `docker run -v mi-volumen:/data redis:7-alpine`

**Cómo verifico que funcionó:** El dato sobrevive aunque el contenedor se haya eliminado por completo (`docker rm`).

---

## 4. Reducir el tamaño de una imagen 🟡

**Enunciado:** Construye la imagen de `04-app/` tal como está, y anota su tamaño (`docker images`). Luego aplica el reto de multi-stage build que está en `02-docker/README.md`, y compara el tamaño antes/después.

**Cómo verifico que funcionó:** Tienes dos números de tamaño distintos, y puedes explicar de dónde salió la diferencia (pista: ¿qué se queda afuera de la imagen final?).

---

## 5. Inspeccionar un contenedor por dentro 🟢

**Enunciado:** Con cualquier contenedor corriendo, entra a su terminal interna, navega el sistema de archivos, y encuentra dónde quedó copiado tu código.

**Pista:** `docker exec -it <nombre-o-id> sh` (o `bash`, si la imagen lo tiene).

**Cómo verifico que funcionó:** Puedes listar los archivos de tu app desde dentro del contenedor, en la ruta que definiste con `WORKDIR`.

---

## 6. Docker Compose con tus propios dos servicios 🟡

**Enunciado:** Sin copiar el `docker-compose.yml` de `03-docker/ejemplos/`, escribe uno propio desde cero que levante dos servicios cualquiera (pueden ser dos imágenes públicas simples, como `nginx` y `redis`, sin que se comuniquen entre sí todavía).

**Cómo verifico que funcionó:** `docker compose up -d` levanta ambos, y `docker compose ps` los muestra como `running`.

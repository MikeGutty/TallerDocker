# Cheat Sheet — Docker

## Imágenes

```bash
docker build -t <nombre> .          # construir imagen desde el Dockerfile actual
docker images                        # listar imágenes locales
docker rmi <imagen>                  # eliminar una imagen
```

## Contenedores

```bash
docker run <imagen>                      # correr un contenedor
docker run -p 3000:3000 <imagen>         # mapear puertos (host:contenedor)
docker run -d <imagen>                   # correr en segundo plano (detached)
docker ps                                # contenedores corriendo
docker ps -a                             # todos los contenedores (incluso detenidos)
docker stop <id>                         # detener un contenedor
docker rm <id>                           # eliminar un contenedor
docker logs <id>                         # ver logs de un contenedor
docker exec -it <id> sh                  # entrar a la terminal del contenedor
```

## Docker Compose

```bash
docker compose up
docker compose up -d
docker compose down
docker compose logs -f
```

## Limpieza

```bash
docker system prune          # elimina recursos no usados (cuidado)
docker image prune           # elimina imágenes huérfanas
```

## Conceptos clave para el taller

- **Imagen**: plantilla inmutable. **Contenedor**: instancia corriendo de una imagen.
- **Capas**: cada instrucción del Dockerfile crea una capa; Docker las cachea. Ordena el Dockerfile de lo que cambia menos a lo que cambia más.
- **`.dockerignore`**: evita copiar archivos innecesarios (como `node_modules`) a la imagen.

<p align="center">
  <a href="http://nestjs.com/" target="blank"><img src="https://nestjs.com/img/logo-small.svg" width="200" alt="Nest Logo" /></a>
</p>


# Teslo API

1. Clonar proyecto
2. ```yarn install```
3. Clonar el archivo ```.env.template``` y renombrarlo a ```.env```
4. Cambiar las variables de entorno
5. Levantar la base de datos
```
docker-compose up -d
```

6. Levantar: ```yarn start:dev```

7. Ejecutar SEED 
```
http://localhost:3000/api/seed
```



# Production notes:

Ejecutar este comando
```
docker compose -f docker-compose.prod.yml build
```

Para subir la imagen a docker hub
```
docker buildx build --platform linux/amd64,linux/arm64 -t mike777king/teslo-shop:1.1.0 --push .
```

Para subir la imagen a digital ocean
```
docker buildx build --platform linux/amd64,linux/arm64 -t registry.digitalocean.com/teslo-registry/teslo-shop:1.1.0 --push .
```
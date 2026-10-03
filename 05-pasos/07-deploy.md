# Paso 7 — Deploy a Render (desde la imagen de GHCR)

**Tag de referencia:** `completed`

## Objetivo

Que Render despliegue **la misma imagen que publicamos en GHCR** (la que ya pasó por caché y el escaneo de Trivy), en vez de reconstruir el código desde cero. Esto conecta de verdad los tres workflows en una sola cadena: CI → GHCR → Deploy → Verificación.

## Por qué cambiamos el enfoque

En una primera versión de este paso, configuramos Render para construir su propia imagen directamente desde el Dockerfile, de forma independiente a `docker-publish.yml`. Funcionaba, pero significaba que la imagen escaneada por Trivy y la que corría en producción eran, literalmente, dos builds distintos. Ahora Render va a **desplegar la imagen que ya existe en GHCR**, que es como se hace en un pipeline de CD real: *build once, deploy everywhere*.

## Los dos secretos de este paso (no son lo mismo)

Este paso usa **dos secretos distintos, en dos workflows distintos, para dos cosas distintas**. Es la parte que más confunde si no se aclara de entrada, así que antes de tocar nada:

| Secreto | ¿Dónde se usa? | ¿Para qué sirve? |
|---|---|---|
| **`RENDER_DEPLOY_HOOK_URL`** | `docker-publish.yml` | Avisarle a Render "hay una imagen nueva, vuelve a desplegar" |
| **`RENDER_URL`** | `healthcheck.yml` | Preguntarle a la app ya desplegada "¿sigues viva?" (`GET /health`) |

Uno **dispara** el deploy, el otro **verifica** que el deploy funcionó. Son pasos consecutivos pero independientes, por eso son dos secretos separados en vez de uno solo.

## Qué hacer

### 1. Reconfigurar (o crear) el servicio en Render

Si ya tenías el servicio creado con el método anterior (build desde Dockerfile), estos pasos lo reconfiguran; si es la primera vez, créalo con esta configuración desde el inicio.

1. En Render, entra a tu servicio → **Settings**
2. Busca la opción para cambiar la fuente del deploy a **"Existing Image"** (imagen existente en un registro)
3. **Image URL:** `ghcr.io/<tu-usuario-en-minúsculas>/<tu-repo-en-minúsculas>:latest`
   - Revisa el paso "Normalizar nombre de la imagen" en [`docker-publish.yml`](../.github/workflows/docker-publish.yml) si tienes dudas del nombre exacto
   - Como el paquete ya es público (lo hiciste en el paso 5), Render no necesita credenciales para descargarlo
4. **Instance Type:** Free
5. Guarda. Render va a hacer un primer deploy jalando la imagen `:latest` actual.

### 2. Configurar el healthcheck en Render

1. En **Settings → Health Check Path**, configura `/health`
2. Esto le permite a Render saber si la app realmente está lista, no solo si el contenedor arrancó

### 3. Crear el Deploy Hook (secreto `RENDER_DEPLOY_HOOK_URL`, usado en `docker-publish.yml`)

Este es el paso nuevo y clave: un Deploy Hook es una URL secreta que, al recibir un `POST`, le dice a Render "vuelve a desplegar ahora mismo" (jalando de nuevo la imagen `:latest`).

1. En Render: **Settings → Deploy Hook** → copia la URL que te da (algo como `https://api.render.com/deploy/srv-xxxx?key=yyyy`)
2. En GitHub: `Settings → Secrets and variables → Actions → New repository secret`
3. Nombre: `RENDER_DEPLOY_HOOK_URL`, valor: la URL que copiaste
4. Revisa el nuevo paso **"Disparar el deploy en Render"**, al final de [`docker-publish.yml`](../.github/workflows/docker-publish.yml): llama a ese hook automáticamente después de publicar cada imagen nueva

### 4. Conectar el workflow de verificación automática (secreto `RENDER_URL`, usado en `healthcheck.yml`)

1. Copia la URL pública de tu servicio en Render (la de arriba de la página, no el Deploy Hook)
2. En GitHub, crea el secreto `RENDER_URL` con esa URL (sin `/health` al final)
3. Revisa cómo quedó [`healthcheck.yml`](../.github/workflows/healthcheck.yml): ahora tiene un trigger `workflow_run` que lo dispara automáticamente **cuando `Docker Publish` termina con éxito**, además de poder correrlo manualmente o por horario
4. Como el deploy en Render no es instantáneo, el workflow **reintenta hasta 10 veces, esperando 15 segundos entre cada intento**, en vez de fallar al primer chequeo

### 5. Probar el ciclo completo

Haz un push cualquiera (ej. un comentario en el código) y observa la secuencia en la pestaña Actions:

```
Push a main
   → ci.yml corre (lint + tests)
   → docker-publish.yml corre (build + GHCR + Trivy + dispara Render)
       → Render empieza a desplegar la imagen nueva
   → healthcheck.yml se dispara solo al terminar docker-publish.yml
       → reintenta hasta que Render termine y el servicio responda 200
```

## Sobre el "cold start" del free tier

El plan gratuito de Render "duerme" el servicio tras 15 minutos sin tráfico. La primera petición después de eso puede tardar 30-50 segundos en responder mientras el servicio despierta. Por eso el healthcheck reintenta en vez de fallar al primer golpe: el mismo mecanismo cubre tanto el "cold start" como el tiempo normal de un deploy.

## Cómo verifico que funcionó

- Al hacer push, ves los tres workflows corriendo en secuencia (los dos primeros en paralelo, el tercero disparado por el segundo)
- El log de "Disparar el deploy en Render" confirma que llamó al Deploy Hook
- `healthcheck.yml` eventualmente reporta código 200, aunque haya tardado varios reintentos
- Puedes explicar la diferencia entre "Render construye su propia imagen" (como lo hicimos primero) vs. "Render despliega la imagen que ya publicamos en GHCR" (como quedó ahora)

## Cierre del taller

Con esto el pipeline queda realmente conectado de punta a punta: **código → lint/tests (CI) → build + caché + escaneo de seguridad → publicación en GHCR → deploy automático de esa misma imagen → verificación con reintentos**. Es un buen momento para repasar el diagrama del paso 0 (`01-conceptos-previos/03-que-es-un-pipeline.md`) y que el grupo note que ya construyó, en vivo, exactamente eso, sin atajos.

## Reto avanzado

Ver guía de deploy con Fly.io en [`../07-challenges/`](../07-challenges/)

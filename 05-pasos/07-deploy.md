# Paso 7 — Deploy a Render

**Tag de referencia:** `completed`

## Objetivo

Desplegar la app a producción conectando Render directo a GitHub, y agregar una verificación automática de que el servicio sigue respondiendo (`healthcheck`).

## Por qué este paso es distinto a los anteriores

A diferencia de CI y de la publicación en GHCR, el deploy a Render **no se configura con un workflow de GitHub Actions**. Render se conecta directamente al repositorio y hace su propio deploy automático en cada push. Es justo lo que lo hace más simple que Fly.io (ver [`07-challenges/`](../07-challenges/) si quieres la versión con más control manual).

Esta parte se recomienda hacer como **demo guiada por el instructor**, ya que requiere crear una cuenta y esperar el primer deploy (puede tardar varios minutos).

## Qué hacer

### 1. Crear el servicio en Render

1. Crea una cuenta en [render.com](https://render.com) (no pide tarjeta de crédito)
2. **New → Web Service**
3. Conecta tu cuenta de GitHub y selecciona el repositorio del taller
4. Configuración clave:
   - **Root Directory:** `04-app` (el Dockerfile está ahí, no en la raíz del repo)
   - **Environment:** Docker (Render detecta el Dockerfile automáticamente)
   - **Instance Type:** Free
5. Click en **Create Web Service**. El primer deploy puede tardar varios minutos.

### 2. Configurar el healthcheck en Render

1. En la configuración del servicio, busca **Health Check Path**
2. Configúralo como `/health` (el mismo endpoint que probamos desde el módulo de Docker)
3. Esto le permite a Render saber si tu app está realmente lista, no solo si el contenedor arrancó

### 3. Verificar el deploy

1. Cuando termine, Render te da una URL pública (algo como `https://taller-app-xxxx.onrender.com`)
2. Visita `<tu-url>/health` y confirma que responde `{"status":"ok"}`

### 4. Conectar el workflow de verificación automática

1. Copia tu URL de Render (sin el `/health` al final)
2. En GitHub: `Settings → Secrets and variables → Actions → New repository secret`
3. Nombre: `RENDER_URL`, valor: tu URL (ej. `https://taller-app-xxxx.onrender.com`)
4. Ve a la pestaña **Actions**, busca el workflow **"Healthcheck Producción"** y corrélo manualmente (`Run workflow`)
5. Revisa el log: debería confirmar que el servicio responde con código 200

El workflow [`.github/workflows/healthcheck.yml`](../.github/workflows/healthcheck.yml) también corre solo cada hora (`cron`), simulando un monitoreo básico de producción.

## Sobre el "cold start" del free tier

El plan gratuito de Render "duerme" el servicio tras 15 minutos sin tráfico. La primera petición después de eso puede tardar 30-50 segundos en responder mientras el servicio despierta. **Es un buen momento para preguntar al grupo:** ¿por qué el healthcheck debería tolerar esto en un entorno real? (Respuesta: timeouts generosos, y quizás un servicio "ping" externo si de verdad no se quiere dejar dormir.)

## Cómo verifico que funcionó

- La URL pública de Render responde en `/health` con `{"status":"ok"}`
- El workflow "Healthcheck Producción" corre manualmente y termina en verde
- Puedes explicar por qué el deploy no usa un workflow de Actions, a diferencia de CI y GHCR

## Cierre del taller

Con esto se completa el pipeline: **código → lint/tests (CI) → imagen Docker publicada (GHCR) → caché y escaneo de seguridad → deploy → verificación automática**. Es un buen momento para repasar el diagrama del paso 0 (`01-conceptos-previos/03-que-es-un-pipeline.md`) y que el grupo note que ya construyó, en vivo, exactamente eso.

## Reto avanzado

Ver guía de deploy con Fly.io en [`../07-challenges/`](../07-challenges/)

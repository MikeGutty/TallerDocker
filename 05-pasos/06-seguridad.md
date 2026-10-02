# Paso 6 — Caché y seguridad con Trivy

**Tag de referencia:** `paso-6-seguridad`

## Objetivo

Acelerar las construcciones repetidas de la imagen con caché, y detectar vulnerabilidades conocidas sin romper el pipeline (todavía).

## Qué hacer

1. Revisa los cambios en [`.github/workflows/docker-publish.yml`](../.github/workflows/docker-publish.yml):
   - **`docker/setup-buildx-action@v3`**: necesario para poder usar el tipo de caché `gha` (GitHub Actions cache)
   - **`cache-from: type=gha`** y **`cache-to: type=gha,mode=max`**: le dicen a Docker que reutilice las capas ya construidas en ejecuciones anteriores, guardadas en la caché de Actions (esto conecta directo con el concepto de capas que vimos en el módulo de Docker)
   - **Trivy**: un escáner de vulnerabilidades que revisa la imagen ya publicada, buscando CVEs conocidos en el sistema operativo base y las dependencias

2. **Haz dos pushes seguidos** (puede ser un cambio mínimo, como un comentario) y compara el tiempo del paso "Construir y publicar la imagen" entre el primero y el segundo. El segundo debería ser notablemente más rápido gracias a la caché.

3. Revisa el reporte de Trivy en los logs del workflow (pestaña Actions → el job → el paso "Escanear vulnerabilidades con Trivy"). Vas a ver una tabla con las vulnerabilidades encontradas, agrupadas por severidad.

4. **Nota importante sobre `exit-code: "0"`:** así está configurado a propósito. Esto significa que **Trivy solo reporta, no bloquea el pipeline**, incluso si encuentra vulnerabilidades críticas. Es la forma correcta de introducir un scanner por primera vez: primero ves qué aparece en un proyecto real, después decides qué tan estricto ser.

## Cómo verifico que funcionó

- El segundo build (con caché) es visiblemente más rápido que el primero
- El reporte de Trivy aparece en los logs, con una tabla de vulnerabilidades por severidad
- El workflow sigue en verde aunque Trivy encuentre vulnerabilidades (por el `exit-code: "0"`)

## Reto avanzado

- **Subir el reporte a la pestaña Security de GitHub:** cambiar `format: table` por `format: sarif`, guardar la salida en un archivo, y subirlo con `github/codeql-action/upload-sarif@v3`. Esto hace que las vulnerabilidades aparezcan en `Security → Code scanning alerts`, no solo en los logs.
- **Endurecer Trivy:** una vez que el equipo ya conoce el reporte base, cambiar `exit-code: "0"` por `exit-code: "1"` (y `severity: "CRITICAL"` para no ser demasiado estricto de entrada), para que el pipeline sí falle ante vulnerabilidades críticas nuevas.

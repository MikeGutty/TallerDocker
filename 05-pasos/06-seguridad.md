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

5. **Fijáte cómo está referenciada la propia action de Trivy:** no dice `@v0.35.0` ni `@0.28.0`, dice `@57a97c7e...` (un hash de commit). Esto no es casualidad, ver la sección de abajo.

## Caso real: por qué esta action va pineada a un commit, no a una tag

En marzo de 2026, `aquasecurity/trivy-action` (la action que estamos usando en este mismo paso) sufrió un **ataque real a la cadena de suministro** ([CVE-2026-33634](https://cve.circl.lu/cve/CVE-2026-33634)). Un atacante obtuvo credenciales comprometidas y reescribió (`force-push`) **76 de las 77 tags** del repositorio para que apuntaran a código malicioso que robaba credenciales de quién sea que corriera el workflow. Tags como `@v0.34.0` o `@0.28.0`, que muchísimos repositorios tenían referenciadas, de repente apuntaban a otra cosa sin que nadie tocara su propio workflow.

**La lección central:** una tag como `@v4` o `@0.28.0` no es una versión fija, es un **puntero** que quien administra el repositorio puede mover cuando quiera (o un atacante, si compromete sus credenciales). Un **commit SHA** (`@57a97c7e...`) sí es inmutable: apunta siempre al mismo código exacto, pase lo que pase con las tags después.

Por eso este workflow usa:
```yaml
uses: aquasecurity/trivy-action@57a97c7e7821a5776cebc9bb87c984fa69cba8f1
```
en vez de `@v0.35.0`. Ese commit es el que Aqua Security confirmó como la versión seguridad conocida tras el incidente.

**Pregunta para el grupo:** miren las demás actions de este mismo workflow (`actions/checkout@v4`, `docker/build-push-action@v6`, etc.). ¿Están todas pineadas a un commit? (Respuesta: no, y ese es justo el riesgo. Esto es intencional para el taller, para que el grupo note la diferencia y entienda el trade-off entre comodidad y seguridad.)

## Cómo verifico que funcionó

- El segundo build (con caché) es visiblemente más rápido que el primero
- El reporte de Trivy aparece en los logs, con una tabla de vulnerabilidades por severidad
- El workflow sigue en verde aunque Trivy encuentre vulnerabilidades (por el `exit-code: "0"`)

## Reto avanzado

- **Subir el reporte a la pestaña Security de GitHub:** cambiar `format: table` por `format: sarif`, guardar la salida en un archivo, y subirlo con `github/codeql-action/upload-sarif@v3`. Esto hace que las vulnerabilidades aparezcan en `Security → Code scanning alerts`, no solo en los logs.
- **Endurecer Trivy:** una vez que el equipo ya conoce el reporte base, cambiar `exit-code: "0"` por `exit-code: "1"` (y `severity: "CRITICAL"` para no ser demasiado estricto de entrada), para que el pipeline sí falle ante vulnerabilidades críticas nuevas.
- **Pinear el resto de las actions del workflow a su commit SHA** (no solo Trivy), y explicar por qué esto es una práctica recomendada para cualquier action de terceros en un entorno de producción real.

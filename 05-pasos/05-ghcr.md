# Paso 5 — CD a GitHub Container Registry (GHCR)

**Tag de referencia:** `paso-5-ghcr`

## Objetivo

Que cada push a `main` construya la imagen Docker de la app y la publique automáticamente en GHCR.

## Qué hacer

1. Revisa el nuevo workflow en [`.github/workflows/docker-publish.yml`](../.github/workflows/docker-publish.yml). Es un **workflow separado** del `ci.yml`, no un paso más dentro de él, para mantener responsabilidades claras: uno verifica el código, el otro lo publica.
2. Fíjate en los `permissions` del workflow: necesita `packages: write` además de `contents: read`. Sin este permiso explícito, el `GITHUB_TOKEN` no puede publicar en GHCR, y este es el error #1 más común al configurar esto por primera vez.
3. Analiza el paso **"Normalizar nombre de la imagen"**: GHCR exige que el nombre de la imagen esté completamente en minúsculas. Si tu usuario u organización de GitHub tiene mayúsculas (ej. `MiUsuario`), usar `github.repository` directamente rompe el build. Este paso lo convierte a minúsculas con `tr` antes de usarlo.
4. Haz push a `main` y ve a la pestaña **Actions**: deberías ver el workflow `Docker Publish` corriendo.
5. Cuando termine, ve a la página principal de tu repositorio en GitHub y busca la sección **"Packages"** (columna derecha). Ahí debería aparecer tu imagen `taller-app`.
6. **Importante:** por defecto, el paquete se publica como **privado**. Entra a la configuración del paquete (`Package settings`) y cambia su visibilidad a pública si quieres poder hacer `docker pull` sin autenticarte (útil para la demo del taller).
7. Prueba descargar tu propia imagen:
   ```bash
   docker pull ghcr.io/<tu-usuario-en-minúsculas>/taller-app:latest
   docker run -p 3000:3000 ghcr.io/<tu-usuario-en-minúsculas>/taller-app:latest
   ```

## Cómo verifico que funcionó

- El workflow `Docker Publish` termina en verde
- La imagen aparece en la pestaña **Packages** del repositorio
- Puedes hacer `docker pull` de la imagen publicada y correrla

## Errores comunes (y cómo detectarlos)

| Síntoma | Causa probable |
|---|---|
| `denied: permission_denied` al publicar | Falta `permissions: packages: write` en el workflow |
| El build falla al construir el nombre de la imagen | El usuario/organización tiene mayúsculas y no se normalizó |
| `docker pull` pide autenticación | El paquete sigue siendo privado; cambia su visibilidad en Package settings |

## Reto avanzado

Agregar tags semánticos automáticos con [`docker/metadata-action`](https://github.com/docker/metadata-action), para que además de `latest` y el hash del commit, se generen tags como `v1.2.3` cuando se publique un release.

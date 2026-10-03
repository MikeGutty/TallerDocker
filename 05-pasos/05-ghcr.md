# Paso 5 — CD a GitHub Container Registry (GHCR)

**Tag de referencia:** `paso-5-ghcr`

## Objetivo

Que cada push a `main` construya la imagen Docker de la app y la publique automáticamente en GHCR.

## Qué hacer

1. Revisa el nuevo workflow en [`.github/workflows/docker-publish.yml`](../.github/workflows/docker-publish.yml). Es un **workflow separado** del `ci.yml`, no un paso más dentro de él, para mantener responsabilidades claras: uno verifica el código, el otro lo publica.
2. Fíjate en los `permissions` del workflow: necesita `packages: write` además de `contents: read`. Sin este permiso explícito, el `GITHUB_TOKEN` no puede publicar en GHCR, y este es el error #1 más común al configurar esto por primera vez.
3. Analiza el paso **"Normalizar nombre de la imagen"**: GHCR exige que el nombre de la imagen esté completamente en minúsculas. Si tu usuario u organización de GitHub tiene mayúsculas (ej. `MiUsuario`), usar `github.repository` directamente rompe el build. Este paso lo convierte a minúsculas con `tr` antes de usarlo.
4. Analiza el paso **"Leer la versión de la app"**: en vez de etiquetar la imagen con el hash del commit (poco legible, ej. `a3f9c21`), leemos el campo `"version"` de [`04-app/package.json`](../04-app/package.json) con `jq` y la usamos como tag. Así la imagen se publica como `:latest` **y** `:1.0.0`, siguiendo versionado semántico normal de software.
5. Haz push a `main` y ve a la pestaña **Actions**: deberías ver el workflow `Docker Publish` corriendo.
6. Cuando termine, ve a la página principal de tu repositorio en GitHub y busca la sección **"Packages"** (columna derecha). Ahí debería aparecer tu imagen, con dos tags: `latest` y `1.0.0`.
7. **Importante:** por defecto, el paquete se publica como **privado**. Entra a la configuración del paquete (`Package settings`) y cambia su visibilidad a pública si quieres poder hacer `docker pull` sin autenticarte (útil para la demo del taller).
8. Prueba descargar tu propia imagen:
   ```bash
   docker pull ghcr.io/<tu-usuario-en-minúsculas>/<tu-repo-en-minúsculas>:1.0.0
   docker run -p 3000:3000 ghcr.io/<tu-usuario-en-minúsculas>/<tu-repo-en-minúsculas>:1.0.0
   ```

## Cómo se sube de versión (para la próxima vez que publiques)

Como el tag ahora viene de `package.json`, para publicar una nueva versión **no alcanza con hacer push**: primero tienes que subir el número de versión ahí. La forma estándar es con npm, desde `04-app/`:

```bash
npm version patch   # 1.0.0 -> 1.0.1 (arreglo pequeño)
npm version minor    # 1.0.0 -> 1.1.0 (nueva funcionalidad)
npm version major    # 1.0.0 -> 2.0.0 (cambio que rompe compatibilidad)
```

Esto actualiza `package.json` y crea un commit + tag de Git automáticamente. Al hacer `git push`, el workflow lee la nueva versión y publica la imagen con ese tag.

**Importante:** si haces push sin cambiar la versión, el workflow va a intentar publicar el mismo tag otra vez (ej. `1.0.0` de nuevo), sobrescribiéndolo. GHCR lo permite, pero no es buena práctica: cada versión publicada debería ser única e inmutable.

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

Usar [`docker/metadata-action`](https://github.com/docker/metadata-action) para generar tags automáticamente a partir de eventos de Git (branches, pull requests, tags de Git con prefijo `v`), en vez de leer manualmente el `package.json` con `jq`. Es el enfoque que usan muchos proyectos reales cuando el versionado se maneja con GitHub Releases en vez de con el versionado de npm.

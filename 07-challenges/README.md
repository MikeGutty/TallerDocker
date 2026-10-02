# Retos avanzados

Esta carpeta es para quienes ya tienen experiencia con Git, Docker o CI/CD y quieren ir más allá del contenido base de cada paso. Son opcionales: si terminas antes que el resto, intenta uno de estos.

## Git y GitHub
- Rebase interactivo para limpiar historial
- Branch protection rules en tu propio repo
- Convenciones de nombres de rama (`feat/`, `fix/`, `chore/`)

## Docker
- Multi-stage build
- Usuario no root
- `HEALTHCHECK` en el Dockerfile
- Comparar tamaño de imagen antes/después de optimizar

## CI
- Matrix de versiones de Node (22.x y 24.x)
- Cachear `node_modules` entre runs

## CD y seguridad
- Tags semánticos automáticos con `docker/metadata-action`
- Subir reporte de Trivy en SARIF a la pestaña Security
- Environments con aprobación manual

## Deploy — Reto: Fly.io

A diferencia de Render, Fly.io requiere tarjeta de crédito y se maneja principalmente por CLI. Es un buen ejercicio para quienes quieren más control sobre la infraestructura.

Pasos generales:

```bash
# Instalar la CLI
curl -L https://fly.io/install.sh | sh

# Autenticarse
fly auth login

# Inicializar la app (genera fly.toml)
fly launch

# Desplegar
fly deploy
```

Diferencias clave frente a Render:
- `fly.toml` define la configuración (puertos, regiones, recursos)
- Permite desplegar en múltiples regiones
- No tiene "cold start" por inactividad, a cambio de no ser gratuito

## Automatizaciones extra
- Notificación a Slack o Discord cuando el pipeline falla o se despliega con éxito

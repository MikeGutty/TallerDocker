# Checklist de Requisitos — Taller CI/CD con GitHub Actions y Docker

Antes del taller, por favor verifica que tengas instalado y funcionando lo siguiente. Si algo falla, tienes tiempo de resolverlo con anticipación (o usar la alternativa de GitHub Codespaces, ver más abajo).

## 1. Cuenta y herramientas base

| Herramienta | Versión mínima | Cómo verificar |
|---|---|---|
| Cuenta de GitHub | — | Iniciar sesión en [github.com](https://github.com) |
| Git | 2.43 o superior (no anterior a 2.30) | `git --version` |
| VS Code | Última versión disponible | Abrir la aplicación |

## 2. Docker

| Herramienta | Versión mínima | Cómo verificar |
|---|---|---|
| Docker Desktop (Windows/Mac) | 4.70 o superior | `docker --version` |
| Docker Engine (Linux nativo) | 27.x o superior | `docker --version` |
| Docker Compose | v2 (integrado, comando `docker compose`) | `docker compose version` |

**Verificación funcional (obligatoria):**

```bash
docker run hello-world
```

Si este comando corre sin errores, Docker está listo.

## 3. Lenguaje de la app de ejemplo: Node.js

| Herramienta | Versión mínima | Cómo verificar |
|---|---|---|
| Node.js | 22.x o 24.x (LTS) | `node --version` |
| npm | 10.x o superior (viene con Node) | `npm --version` |

## 4. Opcionales (recomendado para participantes avanzados)

| Herramienta | Versión mínima | Cómo verificar |
|---|---|---|
| GitHub CLI (`gh`) | 2.60 o superior | `gh --version` |
| act (correr Actions localmente) | 0.2.x | `act --version` |

## 5. Alternativa sin instalar nada: GitHub Codespaces

Si tienes problemas instalando Docker Desktop (común en equipos corporativos o con virtualización deshabilitada), puedes seguir el taller completo desde el navegador, sin instalar nada, usando **GitHub Codespaces**.

**Verificación:**
1. Entra a cualquier repositorio en GitHub.
2. Haz clic en **Code → Codespaces → Create codespace on main**.
3. Si se abre un entorno de VS Code en el navegador, ya estás listo.

## Resumen rápido (para copiar y pegar)

```
□ Cuenta de GitHub creada
□ Git instalado (git --version)
□ VS Code instalado
□ Docker Desktop instalado y corriendo (docker run hello-world)
□ Node.js 22.x o 24.x instalado
□ (Opcional) GitHub CLI instalado
□ (Opcional) act instalado
□ (Alternativa) Acceso a GitHub Codespaces verificado
```

---

*Si tienes dudas o algo no funciona, escríbenos antes del taller para resolverlo con tiempo.*

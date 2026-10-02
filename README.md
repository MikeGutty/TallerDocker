# Taller de CI/CD con GitHub Actions y Docker

Bienvenido/a al taller. Este repositorio contiene todo el material: presentaciones, guías de instalación, ejemplos y los pasos prácticos que seguiremos en las dos sesiones.

No necesitas experiencia previa en Docker o CI/CD. Si ya tienes experiencia, cada paso incluye un **reto avanzado** para que sigas aprendiendo a tu ritmo.

## Antes de empezar

1. Revisa el checklist de instalación: [`requisitos-taller-cicd.md`](./requisitos-taller-cicd.md)
2. Usa el botón **"Use this template"** de GitHub para crear tu propia copia de este repositorio (no hagas fork).
3. Clónalo en tu máquina, o ábrelo directo en **GitHub Codespaces** si prefieres no instalar nada localmente.

## Estructura del repositorio

Las carpetas están numeradas en el orden en que se usan durante el taller:

```
taller-cicd/
├── README.md                     # este archivo
├── requisitos-taller-cicd.md     # checklist de instalación previa
├── 00-presentaciones/             # slides de cada bloque
├── 01-conceptos-previos/          # terminal, YAML y el concepto de pipeline
├── 02-git-github/                 # fundamentos de Git y GitHub
├── 03-docker/                     # fundamentos de Docker
├── 04-app/                        # app de ejemplo en Node.js
├── 05-pasos/                      # guía de cada paso del taller
├── 06-docs/                       # guías de referencia y cheat sheets
├── 07-challenges/                 # retos para quienes ya tienen experiencia
└── .github/workflows/             # workflows de CI/CD (crecen paso a paso)
```

> Nota: la carpeta `.github/` va sin numerar y exactamente con ese nombre, es un requisito técnico de GitHub para que detecte los workflows de Actions.

## Agenda del taller (4 horas, en dos sesiones de 2 horas)

### Sesión 1 — Conceptos previos, Fundamentos y CI

| Horario | Tema | Carpeta / guía |
|---|---|---|
| 0:00 – 0:15 | Bienvenida, setup, terminal, YAML y qué es un pipeline | [`05-pasos/00-conceptos-previos.md`](./05-pasos/00-conceptos-previos.md) |
| 0:15 – 0:50 | Git y GitHub | [`02-git-github/`](./02-git-github/) |
| 0:50 – 1:35 | Docker | [`03-docker/`](./03-docker/) |
| 1:35 – 2:00 | Cierre y preguntas | — |

### Sesión 2 — CI/CD con GitHub Actions

| Horario | Tema | Carpeta / guía |
|---|---|---|
| 0:00 – 0:50 | CI: primer workflow, lint, tests, variables y secretos | [`05-pasos/03-ci.md`](./05-pasos/03-ci.md), [`05-pasos/04-secretos.md`](./05-pasos/04-secretos.md) |
| 0:50 – 1:30 | CD: build y push a GitHub Container Registry (GHCR) | [`05-pasos/05-ghcr.md`](./05-pasos/05-ghcr.md) |
| 1:30 – 1:50 | Caché y seguridad con Trivy | [`05-pasos/06-seguridad.md`](./05-pasos/06-seguridad.md) |
| 1:50 – 2:00 | Deploy a Render y cierre | [`05-pasos/07-deploy.md`](./05-pasos/07-deploy.md) |

## Cómo avanzar o retomar el taller

Cada paso tiene un tag de Git. Si te atrasas o quieres repasar, puedes saltar directo al punto de partida de cualquier paso:

```bash
git checkout paso-3-ci
```

| Paso | Tema | Tag |
|---|---|---|
| 0 | Conceptos previos (terminal, YAML, pipeline) | `paso-0-conceptos` |
| 1 | Git y GitHub | `paso-1-git` |
| 2 | Docker | `paso-2-docker` |
| 3 | Primer CI (lint y tests) | `paso-3-ci` |
| 4 | Variables, secretos, `GITHUB_TOKEN` | `paso-4-secretos` |
| 5 | CD a GHCR | `paso-5-ghcr` |
| 6 | Caché y Trivy | `paso-6-seguridad` |
| 7 | Deploy a Render | `completed` |

## La app de ejemplo

Usamos una única API mínima en **Node.js** a lo largo de todo el taller (carpeta [`04-app/`](./04-app/)), con un endpoint `GET /health` y un par de tests. La idea es que no aprendas una app nueva en cada módulo: solo le vamos sumando capas (Docker, CI, CD).

## Plataforma de deploy: Render

Para el paso final de despliegue usamos **[Render](https://render.com)**, porque:
- No requiere tarjeta de crédito para el tier gratuito
- El deploy se conecta directo a GitHub y es muy simple de configurar
- Soporta Docker nativamente

Si ya tienes experiencia y quieres un reto extra, en [`07-challenges/`](./07-challenges/) encontrarás una guía para hacer lo mismo con **Fly.io**, una plataforma más orientada a infraestructura y control manual (CLI, `fly.toml`, despliegue multi-región).

## Fuera de alcance (a propósito)

Este taller tiene un alcance deliberadamente acotado para caber en 4 horas con principiantes. Los siguientes temas **no se cubren**, pero vale la pena que sepas que existen para cuando quieras seguir aprendiendo por tu cuenta:

| Tema | Por qué queda fuera | Para seguir después |
|---|---|---|
| **Kubernetes y orquestación** | Es un salto conceptual grande (clusters, pods, manifests) que requiere entender Docker a fondo primero; no cabe en una introducción de 4 horas | Una vez cómodo con Docker y Compose, el siguiente paso natural es un curso dedicado a Kubernetes (o Docker Swarm, más simple, como puente) |
| **Testing avanzado** (mocks, cobertura, tests de integración) | Los tests que usamos son intencionalmente simples, solo para que el pipeline de CI tenga algo real que ejecutar | Profundizar en el framework de testing de tu lenguaje (ej. Jest para Node) una vez que el flujo de CI/CD ya te resulte familiar |

## ¿Te atascaste con Docker?

Si tienes problemas instalando Docker Desktop (común en equipos corporativos o con virtualización deshabilitada), puedes seguir el taller completo desde el navegador con **GitHub Codespaces**, sin instalar nada. Ver instrucciones en [`requisitos-taller-cicd.md`](./requisitos-taller-cicd.md).

## Para quienes ya tienen experiencia

Revisa la carpeta [`07-challenges/`](./07-challenges/) en cada paso. Incluye, entre otros:
- Multi-stage builds y usuario no root en Docker
- Matrix builds en CI
- Environments con aprobación manual
- Deploy con Fly.io
- Branch protection y alertas a Slack/Discord

Si terminas antes que el resto, siéntete libre de ayudar a otros participantes en tu mesa. 🙌

---

¿Dudas antes o durante el taller? Abre un *issue* en este repositorio o pregunta directamente al instructor.

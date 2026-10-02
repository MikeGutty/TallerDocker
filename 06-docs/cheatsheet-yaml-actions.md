# Cheat Sheet — YAML y GitHub Actions

## Estructura básica de un workflow

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: "22"
      - run: npm install
      - run: npm test
```

## Triggers (`on`) comunes

```yaml
on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:      # permite correrlo manualmente desde la UI
  schedule:
    - cron: "0 6 * * *"   # cron en UTC
```

## Variables y secretos

```yaml
env:
  NODE_ENV: production

steps:
  - run: echo "Usando token"
    env:
      TOKEN: ${{ secrets.MI_SECRETO }}
```

## Permisos (necesario para publicar en GHCR)

```yaml
permissions:
  contents: read
  packages: write
```

## Errores comunes de indentación

- YAML usa espacios, no tabs
- La indentación es significativa: dos elementos al mismo nivel deben tener exactamente la misma cantidad de espacios
- `steps` es una lista: cada paso empieza con `- `

## Tip

Usa la extensión "GitHub Actions" de VS Code para autocompletado y validación en tiempo real.

# 02 — Git y GitHub

Fundamentos de Git y GitHub que vamos a necesitar durante el resto del taller. No es un curso completo de Git: es justo lo necesario para que el flujo de CI/CD tenga sentido.

## Objetivos

- Entender la diferencia entre Git (herramienta local) y GitHub (plataforma remota)
- Clonar un repositorio, hacer cambios, confirmarlos y subirlos
- Crear una rama, abrir un Pull Request y entender por qué esto dispara los workflows de Actions
- Resolver un conflicto de merge sencillo, guiado

## Comandos clave

```bash
git clone <url>
git status
git add .
git commit -m "mensaje descriptivo"
git push origin <rama>
git pull
git checkout -b nueva-rama
```

## Práctica

Ver la carpeta [`practica/`](./practica/) para los ejercicios guiados sobre el repositorio real del taller.

## Reto avanzado (para quienes ya tienen experiencia)

- Hacer un `rebase` interactivo para limpiar el historial de commits
- Usar convenciones de nombres de rama (`feat/`, `fix/`, `chore/`)
- Configurar una regla de branch protection en tu propio repo

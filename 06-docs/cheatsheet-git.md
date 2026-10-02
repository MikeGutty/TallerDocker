# Cheat Sheet — Git

## Flujo básico

```bash
git clone <url>
git status
git add .
git add <archivo>
git commit -m "mensaje descriptivo"
git push origin <rama>
git pull
```

## Ramas

```bash
git branch                  # listar ramas locales
git checkout -b <nombre>    # crear y cambiar a una rama nueva
git checkout <rama>         # cambiar de rama
git merge <rama>            # fusionar una rama en la actual
```

## Deshacer cosas

```bash
git restore <archivo>       # descartar cambios no confirmados
git reset HEAD~1            # deshacer el último commit (mantiene cambios)
git revert <hash>           # crear un commit que revierte otro
```

## Tags (usados en este taller para navegar entre pasos)

```bash
git tag                     # listar tags
git checkout <tag>          # moverse a un tag específico
```

## Avanzado

```bash
git rebase -i HEAD~3        # reordenar/combinar los últimos 3 commits
git log --oneline --graph   # ver historial de forma visual
```

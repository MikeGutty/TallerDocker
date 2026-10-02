# Práctica — Git y GitHub

Ejercicios guiados. Sigue el orden; cada uno se apoya en el anterior.

## Ejercicio 1 — Tu primer cambio

1. Crea una rama nueva: `git checkout -b mi-primer-cambio`
2. Edita el archivo `app/README.md` y agrega tu nombre a la lista de participantes
3. Confirma el cambio: `git add .` y `git commit -m "agrego mi nombre"`
4. Sube la rama: `git push origin mi-primer-cambio`
5. Ve a GitHub y abre un Pull Request

## Ejercicio 2 — Leer la pestaña Actions

1. Entra a la pestaña **Actions** de tu repositorio en GitHub
2. Aunque todavía no hay workflows, familiarízate con la interfaz: vas a volver aquí en cada paso siguiente

## Ejercicio 3 — Conflicto de merge (guiado por el instructor)

El instructor indicará cómo generar un conflicto sencillo y cómo resolverlo paso a paso.

## Reto avanzado

- Repite el ejercicio 1 pero usando `git rebase` en vez de merge
- Crea una rama siguiendo la convención `feat/<tu-nombre>-cambio`

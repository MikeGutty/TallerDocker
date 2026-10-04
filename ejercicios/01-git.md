# Ejercicios — Git y GitHub

Usa cualquier repositorio de práctica (puede ser una copia de este mismo, o uno nuevo vacío). No hace falta que sea el repo del taller.

---

## 1. Flujo básico completo 🟢

**Enunciado:** Crea un repositorio nuevo (local o en GitHub), agrega un archivo `notas.md` con cualquier contenido, confírmalo con un mensaje descriptivo, y súbelo.

**Cómo verifico que funcionó:** `git log --oneline` muestra tu commit, y si lo subiste a GitHub, el archivo aparece ahí.

---

## 2. Rama + Pull Request 🟢

**Enunciado:** Crea una rama nueva, agrega una línea a `notas.md`, sube la rama, y abre un Pull Request hacia `main`. No lo fusiones todavía.

**Pista:** `git checkout -b` crea y cambia de rama en un solo paso.

**Cómo verifico que funcionó:** El Pull Request aparece en GitHub, mostrando exactamente la línea que agregaste (y nada más).

---

## 3. Resolver un conflicto de merge 🟡

**Enunciado:** Provócate un conflicto a propósito: desde `main`, edita la línea 1 de `notas.md` y confirma el cambio. Luego cambia a la rama del ejercicio 2 y edita esa misma línea 1 con un texto distinto. Intenta fusionar una rama en la otra y resuelve el conflicto manualmente.

**Pista:** Git marca las zonas en conflicto con `<<<<<<<`, `=======` y `>>>>>>>` directamente en el archivo.

**Cómo verifico que funcionó:** Después de resolver el conflicto y confirmar el merge, `notas.md` tiene el contenido final que tú decidiste, sin los marcadores de conflicto.

---

## 4. Deshacer un commit sin perder el trabajo 🟡

**Enunciado:** Haz un commit con un error intencional (por ejemplo, un typo en el mensaje o en el contenido). Corrígelo de dos formas distintas: primero con `git revert`, y en otro commit, con `git reset`. Investiga la diferencia entre ambos.

**Pista:** `git revert` crea un commit nuevo que deshace el anterior; `git reset` mueve el puntero de la rama hacia atrás.

**Cómo verifico que funcionó:** Puedes explicar, con tus propias palabras, cuándo usarías uno y cuándo el otro (pista: ¿cuál es más seguro si ya subiste el commit a un repo compartido?).

---

## 5. Guardar cambios a medias con `git stash` 🟡

**Enunciado:** Empieza a editar un archivo sin terminar el cambio. Sin confirmar nada, guarda ese trabajo a medias con `git stash`, cambia de rama, y luego vuelve a traer tu cambio pendiente.

**Pista:** `git stash list` te muestra qué tienes guardado; `git stash pop` lo trae de vuelta.

**Cómo verifico que funcionó:** Pudiste cambiar de rama con cambios sin confirmar "en el aire", sin perderlos y sin tener que confirmarlos a medio terminar.

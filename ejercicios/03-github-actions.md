# Ejercicios — GitHub Actions

Haz estos cambios en una rama propia (no directo en `main`), y ábrelos como Pull Request para ver el workflow correr antes de fusionar.

---

## 1. Agregar un paso informativo 🟢

**Enunciado:** Agrega un paso nuevo a `ci.yml` que imprima la fecha y hora en que corrió el workflow.

**Pista:** `run: date` es todo lo que necesitas.

**Cómo verifico que funcionó:** El log de ese paso, en la pestaña Actions, muestra la fecha real de la ejecución.

---

## 2. Workflow desde cero: "Hola mundo" 🟢

**Enunciado:** Crea un archivo **nuevo** (no toques `ci.yml`) llamado `.github/workflows/hola.yml`, que se dispare solo manualmente (`workflow_dispatch`) y que imprima un saludo.

**Pista:** Revisa `01-conceptos-previos/02-yaml.md` si te trabas con la indentación.

**Cómo verifico que funcionó:** Lo encuentras y lo corres manualmente desde la pestaña Actions → "Run workflow".

---

## 3. Ejecutar un paso solo bajo una condición 🟡

**Enunciado:** Agrega un paso a tu workflow `hola.yml` que solo se ejecute si estás en la rama `main` (y no en otra). Pruébalo en una rama distinta primero, y confirma que ese paso se salta.

**Pista:** Se usa la palabra clave `if:` junto con `github.ref`.

**Cómo verifico que funcionó:** En una rama que no sea `main`, el paso aparece marcado como "Skipped" en el log, no como ejecutado ni como fallido.

---

## 4. Matrix build 🟡

**Enunciado:** Modifica (en una rama, sin fusionar) el `ci.yml` de `04-app/` para que los tests corran en **dos versiones de Node a la vez** (por ejemplo, 22 y 24), usando `strategy.matrix`.

**Pista:** Está la fórmula exacta en el reto avanzado de `05-pasos/03-ci.md`.

**Cómo verifico que funcionó:** En la pestaña Actions, ves **dos** jobs corriendo en paralelo para el mismo workflow, uno por cada versión.

---

## 5. Usar la salida de un paso en el siguiente 🟡

**Enunciado:** Crea un workflow con dos pasos: el primero genera un valor (por ejemplo, un número aleatorio o la fecha), y el segundo lo usa e imprime un mensaje con ese valor incluido.

**Pista:** Necesitas `id:` en el primer paso, y `echo "nombre=valor" >> "$GITHUB_OUTPUT"` para exponerlo. Revisa cómo lo hace el paso "Normalizar nombre de la imagen" en `docker-publish.yml` como referencia.

**Cómo verifico que funcionó:** El log del segundo paso muestra el valor exacto que generó el primero, sin que lo hayas escrito a mano.

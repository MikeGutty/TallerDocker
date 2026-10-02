# YAML — el lenguaje de GitHub Actions

Todo workflow de GitHub Actions se escribe en YAML. No es un lenguaje de programación, es un formato para describir datos de forma legible, parecido a una lista o una tabla escrita a mano.

## Las dos estructuras que vas a ver todo el taller

**Pares clave-valor** (como un diccionario):

```yaml
name: CI
on: push
```

**Listas** (cada elemento empieza con `- `):

```yaml
steps:
  - uses: actions/checkout@v4
  - run: npm install
```

**Anidado** (listas dentro de claves, claves dentro de listas):

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
```

## La regla de oro: la indentación ES la estructura

A diferencia de un lenguaje con llaves `{}`, en YAML **los espacios definen qué pertenece a qué**. Dos elementos al mismo nivel deben tener exactamente la misma cantidad de espacios.

```yaml
# Correcto
jobs:
  build:
    runs-on: ubuntu-latest

# Incorrecto (indentación inconsistente)
jobs:
  build:
      runs-on: ubuntu-latest
```

## Reglas rápidas

- Usa **espacios, nunca tabs** (la mayoría de editores lo hacen automático)
- Dos elementos "hermanos" (al mismo nivel) van con la misma indentación
- `:` separa clave y valor; `- ` indica un elemento de lista
- Los comentarios empiezan con `#`

## Ejercicio mental (sin computadora)

Mira el `ci.yml` del taller (en `.github/workflows/ci.yml`) y responde:
- ¿Cuántos espacios de indentación tiene cada `step`?
- ¿Qué pasaría si uno de los `steps` tuviera un espacio de más o de menos?

## Tip para el taller

Usa la extensión **"YAML"** o **"GitHub Actions"** de VS Code: subraya en rojo los errores de indentación antes de que falle en GitHub.

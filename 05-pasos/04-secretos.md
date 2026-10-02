# Paso 4 — Variables, secretos y GITHUB_TOKEN

**Tag de referencia:** `paso-4-secretos`

## Objetivo

Entender las tres formas de pasar información a un workflow, de menos a más sensible:

1. **Variable de entorno simple** (`env`) — no es secreta, puede aparecer en los logs
2. **Secreto del repositorio** (`secrets.MI_SECRETO`) — se enmascara automáticamente en los logs
3. **`GITHUB_TOKEN`** — un token temporal que GitHub genera solo, sin que tengas que crear nada

## Qué hacer

1. Revisa los tres pasos nuevos agregados al final de [`.github/workflows/ci.yml`](../.github/workflows/ci.yml): "Variable de entorno simple", "Usar un secreto del repositorio" y "Usar el GITHUB_TOKEN automático".

2. **Crea tu primer secreto de repositorio:**
   - En GitHub: `Settings → Secrets and variables → Actions → New repository secret`
   - Nombre: `MI_SECRETO`
   - Valor: cualquier texto, por ejemplo `hola-mundo-123`
   - Guarda y haz push de nuevo (o vuelve a correr el workflow manualmente desde la pestaña Actions)

3. **Compara los logs antes y después:**
   - Antes de crear el secreto, el paso "Usar un secreto del repositorio" muestra el mensaje de que no está configurado
   - Después de crearlo, el log dice que el secreto existe, pero el valor real **nunca aparece**, ni si intentas imprimirlo con `echo $MI_SECRETO`. GitHub lo detecta y lo reemplaza por `***` automáticamente.

4. **Observa el paso del `GITHUB_TOKEN`:** no tuviste que crear nada para que funcione. GitHub genera este token automáticamente en cada ejecución, con permisos limitados al propio repositorio, y expira al terminar el workflow. Por eso el bloque `permissions: contents: read` al inicio del archivo es importante: limita lo que ese token puede hacer. En el paso 5 vamos a ampliar esos permisos para poder publicar en GHCR.

## Cómo verifico que funcionó

- El workflow sigue en verde después de agregar los tres pasos nuevos
- Si alguien intenta imprimir `$MI_SECRETO` directamente, el log muestra `***` en vez del valor real
- Puedes explicar con tus palabras la diferencia entre los tres tipos (env simple, secreto, `GITHUB_TOKEN`)

## Reto avanzado

- Configurar un **Environment** (`Settings → Environments`) con aprobación manual, y mover el secreto ahí en vez de a nivel de repositorio, para que un humano tenga que aprobar antes de que el workflow continúe
- Investigar por qué nunca se deben poner secretos directamente en el código del workflow, ni siquiera "temporalmente" para probar

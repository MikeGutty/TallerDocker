# ¿Qué es un pipeline de CI/CD? (sin código, solo el concepto)

Antes de ver la sintaxis de GitHub Actions, es importante entender **por qué existe** esto. Este bloque es 100% conceptual, no hay comandos todavía.

## El problema que resuelve

Imagina que trabajas en un equipo sin automatización:

1. Alguien escribe código y lo sube
2. Para saber si "funciona", alguien tiene que bajarlo, instalarlo y probarlo a mano
3. Si quieren publicarlo, alguien construye la imagen Docker a mano y la sube a mano
4. Si quieren desplegarlo, alguien se conecta al servidor y lo actualiza a mano

Cada uno de estos pasos manuales es una oportunidad para el error humano, y no escala: si 5 personas suben código el mismo día, alguien tiene que hacer esto 5 veces.

## Qué es un pipeline

Un **pipeline** es una secuencia de pasos automatizados que se ejecutan cada vez que pasa un evento determinado (por ejemplo, cada `push` a la rama principal). Reemplaza el trabajo manual de arriba por algo que corre solo.

```
Código subido → Instalar → Probar → Construir imagen → Publicar → Desplegar
```

## CI vs CD (la diferencia que mucha gente confunde)

| | Qué es | Pregunta que responde |
|---|---|---|
| **CI** (Integración Continua) | Automatizar la verificación: instalar, lint, tests | "¿Mi cambio rompió algo?" |
| **CD** (Entrega/Despliegue Continuo) | Automatizar la entrega: construir, publicar, desplegar | "¿Mi cambio ya está en producción?" |

En este taller, **CI** es lo que vamos a construir primero (paso 3: lint + tests), y **CD** es lo que viene después (pasos 5-7: GHCR, caché/seguridad, deploy).

## Por qué esto importa antes de ver el YAML

Cuando en el paso 3 veas un archivo `ci.yml` con `on: push`, `jobs`, y `steps`, ya vas a saber **qué problema está resolviendo cada parte**, en vez de memorizar sintaxis sin contexto.

## Pregunta para reflexionar (antes de seguir)

Si tu equipo no tuviera ningún pipeline automatizado, ¿en qué paso del proceso manual descrito arriba crees que sería más fácil que alguien cometiera un error?

# Terminal — lo mínimo para sobrevivir el taller

No necesitas ser experto en la línea de comandos. Necesitas poder hacer cuatro cosas: saber dónde estás, moverte, ver qué hay, y ejecutar un comando sin miedo a "romper algo".

## ¿Qué es una terminal?

Es una forma de hablarle a la computadora escribiendo comandos en vez de hacer clic. No es más peligrosa que el Finder o el Explorador de archivos, solo que no hay botones.

## Comandos esenciales

```bash
pwd              # ¿en qué carpeta estoy? (print working directory)
ls                # ¿qué hay en esta carpeta? (en Windows con Git Bash también funciona)
cd nombre-carpeta # entrar a una carpeta
cd ..             # subir un nivel
cd ~              # ir a la carpeta "home" del usuario
```

## Práctica rápida (2 minutos)

1. Abre tu terminal (en VS Code: `Ctrl/Cmd + ñ` o el menú Terminal → New Terminal)
2. Ejecuta `pwd` y observa dónde estás
3. Ejecuta `ls` y observa qué hay ahí
4. Navega a la carpeta de este repositorio con `cd`
5. Verifica que llegaste bien con `pwd` otra vez

## Errores comunes

- **"command not found"**: el programa no está instalado, o no está en el PATH. No es que "rompiste" algo.
- **Mayúsculas y minúsculas importan** en Mac/Linux, no tanto en Windows.
- **Los espacios en nombres de carpeta** complican todo. Si puedes, evita espacios en nombres de archivo/carpeta durante el taller.

## Nota para Windows

Si usas Windows, recomendamos usar **Git Bash** (se instala junto con Git) o la terminal integrada de VS Code, para que los comandos de este taller funcionen igual que en Mac/Linux.

# Mi Voz

Comunicador con símbolos y voz en español, pensado para personas con autismo u otras dificultades para hablar. Funciona sin internet. No envía datos a ningún lado: los tableros y las fotos se guardan solo en el celular.

Este proyecto compila el APK de Android automáticamente en GitHub. No hace falta instalar nada en tu computadora.

## Archivos del proyecto

Son todos archivos sueltos en la raíz del repositorio, salvo el flujo de compilación:

- `index.html` (la app completa, con las tipografías incluidas)
- `make_icons.py` (crea el ícono)
- `package.json`
- `capacitor.config.json`
- `.gitignore`
- `README.md`
- `.github/workflows/build-apk.yml` (el flujo que compila el APK)

## Cómo conseguir el APK

1. **Creá un repositorio** en github.com (botón "New"). Puede ser privado.
2. **Subí los archivos sueltos** con "Add file" y después "Upload files": `index.html`, `make_icons.py`, `package.json`, `capacitor.config.json`, `.gitignore` y `README.md`. Después "Commit changes".
3. **Creá el flujo de compilación.** Es una carpeta oculta y por eso no conviene subirla: usá "Add file" y después "Create new file". En el nombre escribí `.github/workflows/build-apk.yml` (las barras crean las carpetas) y pegá adentro el contenido del archivo `build-apk.yml`. Después "Commit changes".
4. **Esperá la compilación.** Entrá a la pestaña **Actions**. Si GitHub pide habilitar los flujos de trabajo, aceptá. Tarda entre 5 y 10 minutos. Cuando aparece una tilde verde, terminó.
5. **Descargá el APK.** En la página principal del repositorio, a la derecha, entrá a **Releases** y abrí "Mi Voz (APK)". Tocá `MiVoz.apk` para bajarlo. También lo encontrás en Actions, dentro de la ejecución, en la sección Artifacts.
6. **Instalalo en el celular.** Abrí el archivo descargado y, si Android lo pide, permití instalar apps desde ese origen. Es una versión de prueba firmada con clave de desarrollo, ideal para uso personal. No sirve para subirla a Google Play.

## Para cambiar algo

Editá `index.html` en GitHub (ícono del lápiz) y hacé commit. El APK se vuelve a compilar solo y se actualiza en Releases.

Para volver a ejecutar la compilación sin cambiar nada: pestaña Actions, "Compilar APK", botón "Run workflow".

## Si la compilación falla

Abrí la ejecución con la cruz roja en Actions, tocá el paso marcado en rojo y copiá las últimas líneas del error.

## Qué incluye

- Tableros listos en español rioplatense, con color por tipo de palabra.
- Frase armada con símbolos y botón para decirla en voz alta con la voz de Android.
- Edición de tableros y símbolos, con fotos propias.
- Ajustes de tamaño de símbolos, velocidad y tono de la voz.
- Funciona sin conexión.

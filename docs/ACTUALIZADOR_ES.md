# Actualizador de Ampere en español

Traducción local del instalador personalizado v0.5.14, 2026-11-14. Se tradujeron 85 constantes visibles (10 clases): título, botones, progreso, selección opcional, cancelación y mensajes principales de error. Las excepciones técnicas de Java o bibliotecas pueden conservar su diagnóstico original. No se cambian URLs, hashes, argumentos ni procedimientos de descarga.

Herramienta reproducible: `python herramientas/traducir_actualizador.py`; genera un JAR revisable en `datos/actualizador`. Con `--instalar` sincroniza la instancia activa de PrismLauncher y únicamente la entrada packwiz-installer.jar del ZIP de instalación. Copia original conservada en `datos/actualizador/packwiz-installer-original.jar`. El bootstrap personalizado ya viene con skipUpdate=true; no fue necesario modificarlo para conservar la personalización.

Validación: 210 clases del instalador cargadas con Java 17 y -Xverify:all; CRC ZIP correcto y JAR de distribución idéntico al instalado. No se ejecutó una descarga real del pack durante la prueba ni se abrió Minecraft. Revisión visual en la próxima ejecución del actualizador pendiente. Cambios locales, sin publicación.

Para traducciones del juego puede usarse un resource pack o un mod de recursos con assets/<namespace>/lang/es_es.json, es_mx.json y las demás variantes disponibles. Minecraft selecciona el archivo del idioma activo; no es necesario descargar o desactivar el mod al cambiar de idioma. Deben cubrirse las claves faltantes por mod y preservar placeholders. Los textos hardcodeados necesitan adaptación en código; un archivo lang no puede reemplazarlos automáticamente.

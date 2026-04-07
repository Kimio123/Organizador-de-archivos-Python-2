# Organizador-de-archivos-Python-2
Organizador de Archivos Inteligente (Python)
Este es un script de automatización desarrollado en Python diseñado para limpiar el caos de carpetas saturadas (como la carpeta de Descargas). A diferencia de un organizador básico, este script utiliza lógica avanzada para clasificar archivos no solo por tipo, sino también por fecha y orden alfabético.

Características Principales
Clasificación por Categorías: Separa automáticamente Documentos, Imágenes, Videos, Audios, Instaladores, Comprimidos y Scripts.

Organización Cronológica: Las Imágenes y Videos se agrupan automáticamente en subcarpetas por Año y Mes (ej: 2024-03), ideal para mantener recuerdos ordenados.

Orden Alfabético (A-Z): Los Documentos, Audios e Instaladores se organizan en subcarpetas de la A a la Z según su nombre inicial.

Gestión de Errores: El script omite archivos que están en uso o que no tienen permisos, evitando que el programa se detenga bruscamente.

Ligero y Rápido: No requiere librerías externas pesadas; utiliza el núcleo estándar de Python.

Tecnologías Utilizadas
Lenguaje: Python 3.x

Librerías: os, shutil, pathlib, datetime.

Cómo utilizarlo
Clona el repositorio o descarga el archivo organizador.py.

Ejecuta el script desde tu terminal:

Bash
python organizador.py
Ingresa la ruta de la carpeta que deseas organizar cuando el script lo solicite (ej: C:\Usuarios\TuUsuario\Downloads).

¡Listo! Verás en tiempo real cómo tus archivos se mueven a sus nuevas carpetas.

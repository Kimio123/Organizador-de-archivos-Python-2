import os
import shutil
import datetime

def obtener_subcarpeta_alfabetica(nombre_archivo):
    """Devuelve la primera letra del archivo en mayúscula, o '#' si es un símbolo/número."""
    primera_letra = nombre_archivo[0].upper()
    return primera_letra if primera_letra.isalpha() else "#"

def obtener_subcarpeta_fecha(ruta_archivo):
    """Devuelve el año y mes de modificación del archivo (ej. '2023-10')."""
    timestamp = os.path.getmtime(ruta_archivo)
    fecha = datetime.datetime.fromtimestamp(timestamp)
    return fecha.strftime('%Y-%m')

def organizar_archivos(ruta_directorio):
    """
    Organiza los archivos de un directorio en subcarpetas según su extensión,
    y luego en subcarpetas por fecha o alfabéticamente según la categoría.
    """
    if not os.path.exists(ruta_directorio):
        print(f"Error: La ruta '{ruta_directorio}' no existe.")
        return

    categorias = {
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'Imagenes': ['.jpg', '.jpeg', '.png', '.gif', '.svg'],
        'Videos': ['.mp4', '.avi', '.mkv'],
        'Audio': ['.mp3', '.wav'],
        'Comprimidos': ['.zip', '.rar', '.tar', '.gz'],
        'Instaladores': ['.exe', '.msi'],
        'Scripts': ['.py', '.js', '.html']
    }

    archivos_movidos = 0

    for archivo in os.listdir(ruta_directorio):
        ruta_completa = os.path.join(ruta_directorio, archivo)
        if os.path.isfile(ruta_completa):
            _, extension = os.path.splitext(archivo)
            extension = extension.lower()
            
            carpeta_destino = 'Otros'

            for categoria, extensiones in categorias.items():
                if extension in extensiones:
                    carpeta_destino = categoria
                    break
            subcarpeta = ""

            if carpeta_destino in ['Imagenes', 'Videos']:
                subcarpeta = obtener_subcarpeta_fecha(ruta_completa)
            elif carpeta_destino in ['Documentos', 'Audio', 'Comprimidos', 'Instaladores', 'Scripts']:
                subcarpeta = obtener_subcarpeta_alfabetica(archivo)
            
            if subcarpeta:
                ruta_carpeta_destino = os.path.join(ruta_directorio, carpeta_destino, subcarpeta)
            else:
                ruta_carpeta_destino = os.path.join(ruta_directorio, carpeta_destino)
            
            if not os.path.exists(ruta_carpeta_destino):
                os.makedirs(ruta_carpeta_destino)
            
            ruta_final = os.path.join(ruta_carpeta_destino, archivo)
            shutil.move(ruta_completa, ruta_final)
            
            ruta_relativa = os.path.join(carpeta_destino, subcarpeta) if subcarpeta else carpeta_destino
            print(f"Movido: {archivo} -> {ruta_relativa}/")
            archivos_movidos += 1

    print(f"\n¡Organización completada! Se movieron {archivos_movidos} archivos.")

if __name__ == "__main__":
    ruta_a_organizar = r"C:\Users\valen\OneDrive\Desktop\Mis proyectos\prueba" 
    
    print("Iniciando el script organizador...")
    organizar_archivos(ruta_a_organizar)
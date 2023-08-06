import os
import shutil
import sys

def buscar_y_eliminar_varias_carpetas(nombres_carpetas, ruta_inicio=None):
    if ruta_inicio is None:
        ruta_inicio = os.path.expanduser("~")
    try:
        for entrada in os.scandir(ruta_inicio):
            if entrada.is_dir() and entrada.name in nombres_carpetas:
                carpeta_encontrada = entrada.path
                print(f"Encontrada la carpeta '{entrada.name}' en: {carpeta_encontrada}")
                eliminar_carpeta(carpeta_encontrada)

        # Recorrer las subcarpetas
        for entrada in os.scandir(ruta_inicio):
            if entrada.is_dir():
                buscar_y_eliminar_varias_carpetas(nombres_carpetas, entrada.path)

    except PermissionError as e:
        print(f"Error de permisos al acceder a la carpeta: {e}")

def eliminar_carpeta(ruta_carpeta):
    try:
        shutil.rmtree(ruta_carpeta)
        print(f"Carpeta eliminada: {ruta_carpeta}")
    except Exception as e:
        print(f"Error al eliminar la carpeta: {e}")

if __name__ == "__main__":
    nombres_carpetas_a_eliminar = ["carpeta1", "carpeta2", ]  # Lista con los nombres de las carpetas a eliminar.
    buscar_y_eliminar_varias_carpetas(nombres_carpetas_a_eliminar)

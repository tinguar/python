import re

def limpiar_documento(nombre_archivo):
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Utilizamos una expresión regular para encontrar y eliminar los bloques nameTranslations
    contenido_limpiado = re.sub(r'\s*nameTranslations\s*:\s*{[^}]*},?', '', contenido)

    # Escribimos el contenido limpiado de vuelta al archivo
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido_limpiado)

# Nombre del archivo que deseas limpiar (en la misma carpeta del script)
archivo_a_limpiar = 'country.txt'

# Llamamos a la función para limpiar el archivo
limpiar_documento(archivo_a_limpiar)

print("El documento ha sido limpiado exitosamente.")

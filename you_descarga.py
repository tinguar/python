import os
from pytube import YouTube

def obtener_ruta_escritorio():
    desktop_path = os.path.expanduser("~/Desktop")
    if not os.path.exists(desktop_path):
        desktop_path = os.path.expanduser("~/Escritorio")
    return desktop_path

def crear_carpeta_descargas():
    ruta_carpeta = os.path.join(obtener_ruta_escritorio(), "descargas_tinguar")
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)
    return ruta_carpeta

def descargar_video(url):
    try:
        youtube = YouTube(url)
        video = youtube.streams.get_highest_resolution()

        ruta_carpeta = crear_carpeta_descargas()
        ruta_guardado = os.path.join(ruta_carpeta, "video.mp4")
        video.download(output_path=ruta_guardado)
        print("Descarga de video completada. Guardado en:", ruta_guardado)
    except Exception as e:
        print("Error:", e)

def descargar_audio(url):
    try:
        youtube = YouTube(url)
        audio = youtube.streams.filter(only_audio=True).first()

        ruta_carpeta = crear_carpeta_descargas()
        ruta_guardado = os.path.join(ruta_carpeta, "audio.mp3")
        audio.download(output_path=ruta_guardado)
        print("Descarga de audio completada. Guardado en:", ruta_guardado)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    print("Menú:")
    print("1. Descargar video")
    print("2. Descargar audio")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        url = input("Ingresa la URL del video de YouTube: ")
        descargar_video(url)
    elif opcion == "2":
        url = input("Ingresa la URL del video de YouTube: ")
        descargar_audio(url)
    else:
        print("Opción no válida.")
import requests

# Lista de URLs a verificar
urls = [
    "https://tinguar.com/",
    "https://gabrielcodigo.com/",
]

# Función para verificar si una URL está activa o no
def verificar_estado(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return str(e)  # Devuelve el mensaje de error como cadena

# Verificar el estado de cada URL en la lista
for url in urls:
    resultado = verificar_estado(url)
    if resultado is True:
        print(f"{url} está activo")
    else:
        print(f"{url} no está activo. Error: {resultado}")

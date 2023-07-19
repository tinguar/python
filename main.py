# from corazon import corazon
from contra import generar_contrasena


def main():
    # corazon()
    longitud_contrasena = 5 # Cambia esta variable para ajustar la longitud de la contraseña generada
    contrasena_generada = generar_contrasena(longitud_contrasena)
    print("Contraseña generada:", contrasena_generada)

if __name__ == "__main__":
    main()
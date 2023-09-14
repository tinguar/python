import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

def generar_varias_contrasenas(cantidad, longitud):
    contrasenas = [generar_contrasena(longitud) for _ in range(cantidad)]
    return contrasenas

def main():
    while True:
        print("Menú:")
        print("1. Crear una contraseña")
        print("2. Crear varias contraseñas con la misma longitud")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                longitud = int(input("Ingresa la longitud de la contraseña: "))
                if longitud <= 0:
                    print("La longitud debe ser un número positivo.")
                else:
                    contrasena_generada = generar_contrasena(longitud)
                    print("Contraseña generada:", contrasena_generada)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "2":
            try:
                cantidad = int(input("Ingresa la cantidad de contraseñas: "))
                longitud = int(input("Ingresa la longitud de las contraseñas: "))
                if cantidad <= 0 or longitud <= 0:
                    print("La cantidad y la longitud deben ser números positivos.")
                else:
                    contrasenas_generadas = generar_varias_contrasenas(cantidad, longitud)
                    print("Contraseñas generadas:")
                    for contrasena in contrasenas_generadas:
                        print(contrasena)
            except ValueError:
                print("Por favor, ingresa números válidos.")
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del menú.")

if __name__ == "__main__":
    main()



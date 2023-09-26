def resolver_laberinto(laberinto, inicio, final):
    if encontrar_camino(laberinto, inicio, final):
        print("Se encontró un camino:")
        imprimir_laberinto(laberinto)
    else:
        print("No se encontró un camino.")

def encontrar_camino(laberinto, posicion, final):
    fila, columna = posicion

    if posicion == final:
        return True

    if (
        fila < 0
        or fila >= len(laberinto)
        or columna < 0
        or columna >= len(laberinto[0])
        or laberinto[fila][columna] == 1
    ):
        return False

    laberinto[fila][columna] = 1

    # Intentar moverse hacia arriba, abajo, izquierda y derecha
    if (
        encontrar_camino(laberinto, (fila - 1, columna), final)
        or encontrar_camino(laberinto, (fila + 1, columna), final)
        or encontrar_camino(laberinto, (fila, columna - 1), final)
        or encontrar_camino(laberinto, (fila, columna + 1), final)
    ):
        return True

    return False

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        print(" ".join(map(str, fila)))

laberinto = [
    [0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1]
]

inicio = (0, 0)
final = (1, 4)

resolver_laberinto(laberinto, inicio, final)

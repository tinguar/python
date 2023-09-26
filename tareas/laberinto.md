**README - Resolución de Laberinto con Backtracking**

Realizado en Python resuelve un laberinto utilizando la técnica de "vuelta atrás" o backtracking. 

**Objetivo:**

El objetivo es encontrar un camino desde una posición de inicio hasta una posición final en un laberinto representado por una matriz.

**Funciones Principales:**

1. `resolver_laberinto(laberinto, inicio, final)`: Esta función principal recibe el laberinto, la posición de inicio y la posición final como argumentos. Primero, verifica si hay un camino desde la posición de inicio hasta la posición final utilizando la función `encontrar_camino`. Luego, imprime el resultado.

2. `encontrar_camino(laberinto, posicion, final)`: Esta función es la encargada de explorar el laberinto y encontrar un camino desde la posición de inicio hasta la posición final. Utiliza la técnica de "vuelta atrás" o backtracking para explorar diferentes caminos. Devuelve `True` si se encuentra un camino y `False` si no se encuentra ninguno.

   - `laberinto`: La matriz que representa el laberinto.
   - `posicion`: La posición actual en el laberinto.
   - `final`: La posición final a la que se desea llegar.

**Detalles de Implementación:**

- La función `encontrar_camino` explora el laberinto desde la posición actual. Si la posición actual es igual a la posición final, se devuelve `True` para indicar que se ha encontrado un camino.
- Se verifica si la posición actual está dentro de los límites del laberinto y si la casilla no está marcada como obstáculo (valor 1 en la matriz).
- La función marca la casilla actual como visitada (asigna 1) y luego intenta moverse hacia arriba, abajo, izquierda y derecha de manera recursiva para buscar el camino.
- Si se encuentra un camino en alguna dirección, se devuelve `True`. Si no se encuentra en ninguna dirección, la función retrocede (backtrack) marcando la casilla actual como no visitada y devuelve `False`.

**Ejemplo de Uso:**

- En el ejemplo proporcionado, se crea un laberinto representado por una matriz bidimensional.
- El punto de inicio es (0, 0), y el punto final es (1, 4).
- La función `resolver_laberinto` se llama con estos parámetros y muestra si se encontró un camino y cómo se ve el laberinto con el camino marcado si se encontró uno.

**Notas Adicionales:**

- Puedes personalizar el laberinto y los puntos de inicio y final para probar diferentes configuraciones.

**Explicación Corta:**

- Este código resuelve un laberinto representado como una matriz. Comienza en una posición de inicio y busca un camino hacia una posición final. Utiliza una técnica llamada "vuelta atrás" para explorar las diferentes rutas. Si encuentra un camino, muestra el laberinto con el camino marcado; de lo contrario, informa que no se encontró un camino. La resolución se logra a través de una función recursiva llamada `encontrar_camino` que se llama a sí misma para explorar las rutas.

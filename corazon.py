import turtle

# Configuración inicial
turtle.speed(0)
turtle.bgcolor('black')

# Cambiar el título de la ventana
turtle.title("Mi Aplicación de Corazón")

# Ajuste de posición inicial para centrar el corazón
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()

# Dibujo del corazón
turtle.fillcolor('red')
turtle.begin_fill()
turtle.left(140)
turtle.forward(180)
turtle.circle(-90, 200)  # Corrección: Cambié el 180 a -90
turtle.setheading(60)
turtle.circle(-90, 200)
turtle.forward(180)
turtle.end_fill()

# Ocultar la tortuga al finalizar
turtle.hideturtle()

# Mantener la ventana abierta
turtle.done()

import turtle as t

t.speed(100)
t.bgcolor("white")

t.penup()
t.goto(0,-100)
t.pendown()
t.pensize(10)
t.color("green")
t.setheading(270)
t.forward(200)

def petalos():
    t.begin_fill()
    t.color("yellow")
    t.circle(100,60)
    t.left(120)
    t.circle(100,60)
    t.left(120)
    t.end_fill()

t.penup()
t.goto(0,-50)
t.pendown()

for _ in range(18):
    petalos()
    t.right(20)

t.penup()
t.goto(-10,-50)
t.pendown()
t.begin_fill()
t.color("orange")
t.circle(10)
t.end_fill()

t.hideturtle()
t.done()
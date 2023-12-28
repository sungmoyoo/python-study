import turtle
t = turtle.Turtle()
t.shape("turtle")

t.pensize(20)
t.speed(0)

t.up()
t.goto(-300,200)
t.down()

for i in range(5):
    t.color("brown")
    t.fd(600)
    t.right(90)
    t.fd(30)
    t.right(90)
    t.fd(600)
    t.left(90)
    t.fd(30)
    t.left(90)

turtle.done()
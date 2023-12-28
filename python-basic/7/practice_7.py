#거북이 경주 게임1
'''
import random
import turtle
t1= turtle.Turtle()
t1.shape("turtle")

t2 = turtle.Turtle()
t2.shape("turtle")

t1.shapesize(3)
t1.pensize(5)
t2.shapesize(3)
t2.pensize(5)

t1.up()
t1.goto(300,300)
t1.write("Goal")
t1.down()
t1.goto(300,-300)

t1.up()
t1.goto(-300,-100)
t1.down()


t2.up()
t2.goto(-300,100)
t2.down()

t1.color("pink")
t2.color("blue")
t1.speed(1)
t2.speed(1)

while True:
    d1 = random.randint(1,60)
    d2 = random.randint(1,60)
    
    t1.fd(d1)
    t2.fd(d2)

    p1 = t1.xcor()
    p2 = t2.xcor()

    if p1 > 310:
        print("Pink win")
        turtle.write("Pink Win", move=False, align ="left", font=("Arial", 50, "normal"))
        break
        
    elif p2 > 310:
        print("Blue win")
        turtle.write("Blue Win", move=False, align ="left", font=("Arial", 50, "normal"))
        break

turtle.done
'''

#거북이 경주2
'''
import random
import turtle

screen = turtle.Screen()
image1 = "rabbit.gif"
image2 = "turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1= turtle.Turtle()
t1.shape(image1)
t1.pensize(5)

t1.up()
t1.goto(300,300)
t1.write("Goal")
t1.down()
t1.goto(300,-300)

t1.up()
t1.goto(-300,0)
t1.down()

t2= turtle.Turtle()
t2.shape(image2)
t2.pensize(5)
t2.up()
t2.goto(-300,-200)

t1.down()
t2.down()
t1.speed(1)
t2.speed(1)

for i in range(100):
    d1 = random.randint(1,60)
    d2 = random.randint(1,60)

    t1.fd(d1)
    t2.fd(d2)

    p1 = t1.xcor()
    p2 = t2.xcor()

    if p1 > 300:
        print("Rabbit Win")
        t1.write("Rabbit Win", move=True, align ="left", font=("Arial", 20, "normal"))
        break
        
    elif p2 > 300:
        print("Turtle Win")
        t2.write("Turtle Win", move=True, align ="left", font=("Arial", 20, "normal"))
        break
    
turtle.done()
'''

#애니메이션 만들기
'''
import random
import turtle

t = turtle.Turtle()

t.speed(0.5)
t.pensize(5)
t.goto(0,0)
while True:
    for i in range(30):
        t.circle(1+5*i)
        t.color((random.random(),random.random(),random.random()))
        t.goto(i*20,0)
    t.clear()

turtle.done()
'''

#앵그리 터틀 게임
'''
import turtle
import math
import random

player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()
screen.bgcolor("black")
screen.setup(800,600)

player.color("yellow")
player.up()
player.goto(-300,0)
player.down()

velocity = 70
player.left(45)


def turnleft():
    player.left(5)

def turnright():
    player.right(5)

def turnup():
    global velocity
    velocity += 10

def turndown():
    global velocity
    velocity -= 10


def fire():
    x = -300
    y = 0
    player.color(random.random(),random.random(),random.random())
    player.goto(x,y)
    angle = player.heading()
    vx = velocity * math.cos(angle * 3.14 / 180.0)
    vy = velocity * math.sin(angle * 3.14 / 180.0)

    while player.ycor() >= 0 :
        vx = vx
        vy = vy - 10
        x = x + vx
        y = y + vy

        player.goto(x,y)
        player.stamp()

screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(turnup,"Up")
screen.onkeypress(turndown,"Down")
screen.onkeypress(fire,"space")

screen.listen()
turtle.mainloop()
'''

#공 애니메이션
import turtle
import time

width, height = 600, 700 #게임 보드의 크기
gravity = 0.05 #중력
x,y = 0, height/2 #공의 위치
vx, vy = 0.25, 1 #공의 속도
coef_res = 0.90 #반발 계수

screen = turtle.Screen()
screen.setup(width+100, height+100)
screen.tracer(0) #수동 화면 업데이트 설정

ball = turtle.Turtle
ball.color("orange","black")
ball.shape("circle")
ball.up()
ball.goto(x,y)
ball.down()

while True:
    x = x + vx
    y = y + vy
    ball.goto(x,y)
    vy = vy - gravity

    if y < -height/2:
        vy = -vy * coef_res
        ball.sety(-height/2)

    if x> width /2 or x < -width /2:
        vx = -vx
        
    screen.update()
        






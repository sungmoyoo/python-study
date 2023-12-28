#과자 먹기 게임 업그레이드
import turtle
import random
import time

score = 0
myList = []

start_time = time.time()

screen = turtle.Screen()
screen.tracer(0)
screen.addshape("dog.gif")

player = turtle.Turtle()
player.shape("dog.gif")
player.up()
player.goto(-200,200)
player.down()
player.goto(200,200)
player.goto(200,-200)
player.goto(-200,-200)
player.goto(-200,200)

player.up()
player.goto(0,0)

display = turtle.Turtle()
display.hideturtle()
display.penup()
display.goto(-210,200)
display.write(f"score={score}", font=('Arial',20,"italic"))

for i in range(10):
    cookie = turtle.Turtle()
    cookie.shape("circle")
    cookie.penup()

    x = random.randint(-180,180)
    y = random.randint(-180,180)

    cookie.goto(x,y)

    myList.append(cookie)

def moveRight():
    player.setheading(0)
    player.forward(10)

def moveLeft():
    player.setheading(180)
    player.forward(10)     

def moveUp():
    player.setheading(90)
    player.forward(10)

def moveDown():
    player.setheading(270)
    player.forward(10)

screen.listen()
screen.onkeypress(moveRight,"Right")
screen.onkeypress(moveLeft,"Left")
screen.onkeypress(moveUp,"Up")
screen.onkeypress(moveDown,"Down")

while True:
    for cookie in myList:
        if player.distance(cookie) <30:
            x = random.randint(-180,180)
            y = random.randint(-180,180)
            cookie.goto(x,y)
            score += 1
            display.clear()
            display.write(f"score={score}", font=('Arial',20,"italic"))
    screen.update()

    #종료 및 클리어 시간 추가 
    if score == 10:
        end_time =time.time()
        timer = end_time - start_time
        display.goto(-210,300)
        display.write(f"time: {timer}", font=('Arial',20,"italic"))
        break
    screen.update()

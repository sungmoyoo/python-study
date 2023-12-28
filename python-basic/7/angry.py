import turtle
import math
import random

#배경, 화면 초기 설정
player = turtle.Turtle()
player.shape("turtle")
screen = player.getscreen()
screen.bgcolor("black")
screen.setup(800,600)

#시작 위치, 색 설정
player.color("yellow")
player.up()
player.goto(-300,0)
player.down()

#초기 힘, 각도 설정
velocity = 70
player.left(45)

#각도 조절, 힘 조절 함수 
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

#발사 함수
def fire():
    x = -300
    y = 0
    player.color(random.random(),random.random(),random.random())
    player.goto(x,y)
    angle = player.heading() #초기 각도

    #라디
    vx = velocity * math.cos(angle * 3.14 / 180.0) 
    vy = velocity * math.sin(angle * 3.14 / 180.0)

    #y좌표가 음수가 될 때까지 터틀 이동 반복
    while player.ycor() >= 0 : 
        vx = vx #x좌표는 그대로
        vy = vy - 10 #y좌표는 중력가속도만큼 감소
        x = x + vx #x값 더하기
        y = y + vy #y값 더하기

        player.goto(x,y) #터틀 위치 이
        player.stamp()

#콜백 함수(사용자 입력)
screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(turnup,"Up")
screen.onkeypress(turndown,"Down")
screen.onkeypress(fire,"space")

screen.listen()
turtle.mainloop()

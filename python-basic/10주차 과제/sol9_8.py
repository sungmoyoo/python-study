import turtle
import random

#화면을 설정하고 배경을 검정색으로 바꿈
s = turtle.Screen()
s.bgcolor("black")

t = turtle.Turtle()
t.shape("turtle")

#사용할 색상리스트
colors = ["white", "yellow", "skyblue", "white", "green", "yellow", "white", "skyblue", "orange", "white", "orange", "skyblue", "blue"]

#별 그리기 함수
def draw_star(c, length, x, y):
    #지정된 좌표로 이동
    t.up()  
    t.goto(x, y)  
    t.down()  

    #색상 지정, 색채우기 시작
    t.color(c)  
    t.begin_fill()  

    #별 그리기(일반적인 별모양의 각도가 각각 144와 72임)
    for _ in range(5):
        t.fd(length)
        t.right(144)
        t.fd(length)
        t.left(72)
    t.end_fill()  

#색상리스트값을 하나씩 꺼내어 반복, 위치와 길이를 무작위로 선택
for c in colors:
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    length = random.randint(30, 100)
    
    #별 그리기 함수 호출
    draw_star(c, length, x, y)

turtle.done()
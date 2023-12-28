import turtle
import random

t = turtle.Turtle() 
t.shape("turtle")  

#사용할 색상 리스트
colors = ["yellow", "blue", "green", "yellow", "skyblue", "orange"]  

#도형 그리기 함수
def draw_shape(c, length, sides, x, y):
    #지정된 좌표로 이동
    t.up()  
    t.goto(x, y)  
    t.down()  

    #색상 지정, 색채우기 시작
    t.begin_fill()  
    t.color(c)  

    #도형 그리기(n각형인 것을 활용하여 반복)
    for i in range(sides):
        t.left(360 / sides)  
        t.fd(length)  

    t.end_fill()  # 도형 내부를 색칠하기 종료

#색상리스트값을 하나씩 꺼내어 반복, 좌표와 길이, n각의 값을 무작위로 선택하여 draw_shape함수 호출
for c in colors:
    x = random.randint(-200, 200)  #-200부터 200 사이의 임의의 x 좌표 생성
    y = random.randint(-200, 200)  #-200부터 200 사이의 임의의 y 좌표 생성
    length = random.randint(50, 100)  #50부터 100 사이의 임의의 길이 생성
    sides = random.randint(3, 6)  #3부터 6 사이의 임의의 변 수 생성

    #도형 그리기 함수 호출
    draw_shape(c, length, sides, x, y)  

turtle.done()  # 거북이 그래픽 종료
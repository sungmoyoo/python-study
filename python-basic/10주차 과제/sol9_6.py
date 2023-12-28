import turtle
import random

t = turtle.Turtle()  
t.shape("turtle")  

#사용할 색상 리스트
colors = ["yellow", "red", "purple", "blue"]  

#사각형 그리는 함수
def draw_square(x, y, c):
    #지정된 좌표로 이동
    t.up()  
    t.goto(x, y)  
    t.down()  

    #색상 설정
    t.color(c)  

    #색이 채워지는 사각형 그리기
    t.begin_fill()  
    t.fd(100)  
    t.left(90)  
    t.fd(100)  
    t.left(90)  
    t.fd(100)  
    t.left(90)  
    t.fd(100)  
    t.end_fill()  

#색상리스트값을 하나씩 꺼내어 반복
for c in colors:
    x = random.randint(-100, 100)  # -100부터 100 사이의 임의의 x 좌표 생성
    y = random.randint(-100, 100)  # -100부터 100 사이의 임의의 y 좌표 생성

    #사각형 그리기 함수 호출
    draw_square(x, y, c)  

turtle.done()  
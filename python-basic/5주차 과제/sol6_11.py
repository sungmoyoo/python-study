import turtle
import random
t = turtle.Turtle()
turtle.colormode(255) #색상 랜덤 지정하기 위해 컬러모드를 1.0 실수모드에서 255 정수모드로 변경

t.shape("turtle")

i = 0
for i in range(30):
    color_r = random.randint(0,255) #r 색상값 난수 생성
    color_g = random.randint(0,255) #g 색상값 난수 생성
    color_b = random.randint(0,255) #b 색상값 난수 생성
    
    x = random.randint(-500, 500) #x좌표 난수 생성
    y = random.randint(-500, 500) #y좌표 난수 생성

    size = random.randint(0,300)

    #채우기 색 지정
    t.color(color_r,color_g,color_b) 

    #좌표로 이동
    t.up() 
    t.goto(x,y)
    t.down()
    
    #별 그리기
    t.begin_fill()
    for i in range(5):
        t.fd(size)
        t.right(144)
    t.end_fill()


turtle.done()
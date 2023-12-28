import turtle
t = turtle.Turtle()
t.shape("turtle")

colors = ["red","orange","yellow","green","blue","indigo","violet"] #색상 리스트 지정

t.pensize(20) #펜 사이즈 지정

x = 0 # 초기 x좌표 값 설정
radius = 60 #초기 반지름 값 설정
t.left(90) 

for color in colors: #색상 리스트의 값을 하나씩 반복
    t.up()
    t.goto(x,0)
    t.down()
    
    t.color(color)
    t.circle(radius,180)
    t.left(180)
    
    #반원을 그린 후 반지름과 x좌표를 30씩 증가
    radius = radius + 30 
    x = x + 30

turtle.done()

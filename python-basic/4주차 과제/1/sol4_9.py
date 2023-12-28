#127p 9
#색 리스트 - 3가지 색상을  colors 리스트에 저장
colors = ["yellow","red","blue"] 

#x좌표 리스트 - x1~x3의 값을 x_cord 리스트에 저장
x_cord = [50,100,150]


#y좌표 리스트 - y1~y3의 값을 y_cord 리스트에 저장
y_cord = [50,30,50]


#터틀 그래픽
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.stamp() #거북이 모양 찍기

t.fillcolor(colors[0]) #색 변환
t.goto(x_cord[0],y_cord[0]) #x_cord,y_cord 인덱스 [0], 즉 x1,y1 좌표로 이동
t.stamp() #거북이 모양 찍기

t.fillcolor(colors[1]) #색 변환
t.goto(x_cord[1],y_cord[1]) #x2, y2 좌표로 이동
t.stamp() #거북이 모양 찍기

t.fillcolor(colors[2]) #색 변환
t.goto(x_cord[2],y_cord[2]) #x3, y3 좌표로 이동
t.stamp() #거북이 모양 찍기

turtle.done()

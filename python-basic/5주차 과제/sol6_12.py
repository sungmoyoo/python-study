import math 
import turtle
t = turtle.Turtle()
t.shape("turtle")


for x in range(0,360): #x는 x좌표 그리고 radian 값을 구하는 각도로 사용
    radian = 3.14*x / 180 #radian 값 구하는 공식
    y = math.sin(radian) *100 #sin(): 라디안 값을 사인 함수로 빗변과 높이 길이의 비를 구함
                              #실수이기 때문에 100을 곱하여 이동하였을때 변화를 확인 
    
    t.goto(x,y) #터틀 이동시키며 그래프 그리기
    
turtle.done()


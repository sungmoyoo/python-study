x1 = int(input("Input x1:")) #x1 값 입력받기
x2 = int(input("Input x2:")) #x2 값 입력받기
y1 = int(input("Input y1:")) #y1 값 입력받기
y2 = int(input("Input y2:")) #y2 값 입력받기
length = (((x1 - x2)**2) + ((y1 - y2)**2))**0.5 #점과 점 사이의 거리 구하는 공식

#터틀 그래픽 임포트
import turtle 
t = turtle.Turtle()
t.shape("turtle")

t.up() #그리지 않고 (x1,y1)위치로 이동하기 위해 펜 올리기
t.goto(x1,y1) #점 이동

t.down() #점과 점 직선을 그리기 위해 펜 내리기
t.goto(x2,y2) #(x2,y2)위치로 이동하며 그리기


t.write("length : " + str(length))#앞서 계산한 점과 점 사이 거리를 터틀그래픽 창에 출력






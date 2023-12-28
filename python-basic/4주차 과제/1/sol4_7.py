#126p 7
color_list = [] #색 리스트 생성

#색을 입력받아 color_list에 추가(append)
color = input("Input color #1:")
color_list.append(color)

color = input("Input color #2:")
color_list.append(color)

color = input("Input color #3:")
color_list.append(color)

#터틀그래픽
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.fillcolor(color_list[0]) #color_list 인덱스 0번에 해당하는 색으로 채우기
t.begin_fill() #채우기 시작
t.circle(50) #반지름 50인 원 그리기
t.end_fill() #채우기 끝

t.up() #펜 올리기(이동하면서 선 안그려지게)
t.fd(100) #앞으로 100 이동
t.down() #다시 그리기

t.fillcolor(color_list[1]) #color_list 인덱스 1번에 해당하는 색으로 채우기
t.begin_fill() #채우기 시작
t.circle(50) #반지름 50인 원 그리기
t.end_fill() #채우기 끝

t.up() #펜 올리기(이동하면서 선 안그려지게)
t.fd(100) #앞으로 100 이동
t.down() #다시 그리기

t.fillcolor(color_list[2]) #color_list 인덱스 1번에 해당하는 색으로 채우기
t.begin_fill() #채우기 시작
t.circle(50) #반지름 50인 원 그리기
t.end_fill() #채우기 끝

turtle.done()

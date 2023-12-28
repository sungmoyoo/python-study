import turtle
t = turtle.Turtle()

#2개의 원에 대한 정보 입력받기
big_x1 = int(input("Enter big circle's x1 location: ")) 
big_y1 = int(input("Enter big circle's y1 location: "))
big_radius = int(input("Enter big circle's radius: "))
small_x1 = int(input("Enter small circle's x1 location: "))
small_y1 = int(input("Enter small circle's y1 location: "))
small_radius = int(input("Enter small circle's radius: "))

#터틀그래픽 생성
t.shape("turtle")

#큰원 그리기
t.up()
t.goto(big_x1,big_y1) 
t.down()
t.circle(big_radius)

#작은원 그리기
t.up()
t.goto(small_x1,small_y1)
t.down()
t.circle(small_radius)

turtle.done()

#두 점 사이의 거리 구하는 공식
distance =((big_x1-small_x1)**2 + (big_y1-small_y1)**2)**0.5

#큰 원의 반지름 - 두 점 사이의 거리가 작은원의 반지름보다 크면 작은 원은 큰 원 안에 포함
if big_radius - distance >= small_radius:
    print("작은 원은 큰 원안에 포함됩니다.")
else:
    print("포함x")
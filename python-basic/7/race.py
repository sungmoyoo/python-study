import random
import turtle

#화면 띄우기, 이미지 추가
screen = turtle.Screen()
image1 = "rabbit.gif"
image2 = "turtle.gif"
screen.addshape(image1)
screen.addshape(image2)

t1= turtle.Turtle()
t1.shape(image1)
t1.pensize(5)

#결승선 그리기
t1.up()
t1.goto(300,300)
t1.write("Goal")
t1.down()
t1.goto(300,-300)

# 시작점으로 이동
t1.up()
t1.goto(-300,0)
t1.down()

t2= turtle.Turtle()
t2.shape(image2)
t2.pensize(5)
t2.up()
t2.goto(-300,-200)

#속도 조정
t1.down()
t2.down()
t1.speed(1)
t2.speed(1)

#시작
for i in range(100):
    d1 = random.randint(1,60)
    d2 = random.randint(1,60)

    t1.fd(d1)
    t2.fd(d2)

    #결승선에 도달했을 때 멈추기 위해 x좌표값 p1,p2에 저장
    p1 = t1.xcor()
    p2 = t2.xcor()

    #토끼 혹은 거북이 중 먼저 도착하는 쪽이 이겼다는 메시지를 출력하고 반복문 멈춤
    if p1 > 300:
        print("Rabbit Win")
        t1.write("Rabbit Win", move=True, align ="left", font=("Arial", 20, "normal"))
        break
        
    elif p2 > 300:
        print("Turtle Win")
        t2.write("Turtle Win", move=True, align ="left", font=("Arial", 20, "normal"))
        break
    
turtle.done()

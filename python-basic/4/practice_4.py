#날짜 차이 계산하기
'''
import datetime

x = datetime.datetime(2022,9,1)
y = datetime.datetime(2022,9,18,20,35,3)

d = y-x

print('만난 일:' + str(x))
print('현재:' + str(y))
print('만난 지' + str(d.days) + '일 되었습니다')
'''

#친구 리스트
'''
friend_list = []
for i in range(5):
    friend = input("Friend Name?: ")
    friend_list.append(friend)

print(friend_list)
'''

#터틀그래픽 리스트 활용
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

color_list = ["yellow","red","blue","green"]

for colors in color_list:
    t.fillcolor(colors)
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.fd(50)
'''


#126p 7
'''
color_list = []

color = input("Input color #1:")
color_list.append(color)

color = input("Input color #2:")
color_list.append(color)

color = input("Input color #3:")
color_list.append(color)

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.fillcolor(color_list[0])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.fd(100)
t.down()

t.fillcolor(color_list[1])
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.fd(100)
t.down()

t.fillcolor(color_list[2])
t.begin_fill()
t.circle(50)
t.end_fill()
'''

#127p 9
'''
#색 리스트
colors = [] 
c = input("Input color #1:")
colors.append(c)
c = input("Input color #2:")
colors.append(c)
c = input("Input color #3:")
colors.append(c)

#x좌표 리스트
x_cord = []
x = int(input("input x1 cord:"))
x_cord.append(x)
x = int(input("input x2 cord:"))
x_cord.append(x)
x = int(input("input x3 cord:"))
x_cord.append(x)

#y좌표 리스트
y_cord = []
y = int(input("input y1 cord:"))
y_cord.append(y)
y = int(input("input y2 cord:"))
y_cord.append(y)
y = int(input("input y3 cord:"))
y_cord.append(y)

import turtle
t = turtle.Turtle()
t.shape("turtle")

t.stamp()

t.fillcolor(colors[0])
t.goto(x_cord[0],y_cord[0])
t.stamp()

t.fillcolor(colors[1])
t.goto(x_cord[1],y_cord[1])
t.stamp()

t.fillcolor(colors[2])
t.goto(x_cord[2],y_cord[2])
t.stamp()
'''

#127p 10
'''
import random #임의의 원소를 추출하기 위한 random모듈 임포트
from string import ascii_lowercase #알파벳 소문자 리스트 호출하는 모듈 임포트

list1 = list(ascii_lowercase) #알파벳 소문자를 list1에 저장
list2 = ["0","1","2","3","4","5","6","7","8","9"] #숫자 0~9까지 list2에 저장
plist = list1 + list2 #알파벳 소문자와 한자리 숫자의 리스트를 병합하여 plist에 저장

first = random.choice(plist) #첫번째 패스워드 랜덤 선택
second = random.choice(plist) #두번째 패스워드 랜덤 선택
third = random.choice(plist) #세번째 패스워드 랜덤 선택

password = first + second + third #랜덤 선택된 패스워드 조합

print(password) #결과 출력
'''

# if-else
'''
score = int(input("Score:"))

if score >= 60:
    print("Pass")
else:
    print("Fail")
'''

#블록
'''
score = int(input("Score:"))

if score >= 90:
    print("Pass")
    print("You can receive scholarship")
elif score >= 70:
    print("Pass")

elif score >= 60:
    print("재시험")
else:
    print("Fail")
'''

#136p 터틀그래픽 선택 구조
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.up()
t.goto(100,100)
t.write("여기로 오면 양수입니다")

t.goto(100,0)
t.write("여기로 오면 0입니다")

t.goto(100,-100)
t.write("여기로 오면 음수입니다")

t.goto(0,0)
t.down()

s = turtle.textinput("","숫자를 입력하시오: ")

n = int(s)

if n > 0:
    t.goto(100,100)
if n == 0:
    t.goto(100,0)
if n < 0:
    t.goto(100,-100)

turtle.done()
'''

#거북이 제어하기
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.width(3)
t.shapesize(3,3)

while True:
    command = input("Enter command: ")
    if command == "r":
        t.right(90)
        t.forward(100)
    if command == "l":
        t.left(90)
        t.forward(100)
    if command == "b":
        break

turtle.done()
'''

#윤년 판단
'''
year =  int(input("Enter Year: "))

if (year % 4) == 0 and (year % 100) != 0 or (year % 400) ==0:
    print("Leap Year")
else:
    print("Not Leap Year")
'''

#동전 던지기 게임 (그래픽버전)
import turtle
import random

t = turtle.Turtle()
screen =  turtle.Screen()
image1 = "front.gif"
image2 = "back.gif"
screen.addshape(image1)
screen.addshape(image2)

coin = random.randrange(2)

if coin == 0:
    t.shape(image1)
    t.stamp()
    print("Result: Front")
    
else:
    t.shape(image2)
    t.stamp()
    print("Result: Back")

turtle.done()





























#함수 호출
'''
def print_address(name):
    print("서울 특별시 종로구 1번지")
    print("파이썬 빌딩 7층")
    print(name)

print_address("홍길동")
'''

#값 반환하기
'''
def calculate(radius):
    area = 3.14 * (radius**2)
    return area

x = calculate(5)

print(x)


def calculate(radius):
    area = 3.14 * (radius**2)
    perimeter = 2 * 3.14 * radius
    return area, perimeter

x, y = calculate(5)

print(x, y)
'''

#여러개 인수 전달
'''
def get_sum(start,end):
    sum = 0
    for i in range(start,end):
        sum += i
    return sum
print(get_sum(1,10))
'''

#사각형 그리는 함수
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

def squre(x, y, length, color):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(color)

    t.begin_fill()
    for i in range(4):
        t.fd(length)
        t.left(90)

    t.end_fill()

squre(-200,0,100,"red")
squre(0,0,100,"blue")
squre(200,0,100,"yellow")

turtle.done()
'''

#자음과 모음 개수 카운팅
'''
def countVowel(string):
    count = 0
    for ch in string:
        if ch in ['a','e','i','o','u']:
            count += 1
    return count

s = input("Enter string: ")
n = countVowel(s)

print("Vowels in words: %d" %(n))
'''



#로또 번호 생성함수
'''
import random

def getLotto():
    numbers = []
    while len(numbers) <6:
        n = random.randint(1,45)
        if n not in numbers:
            numbers.append(n)

    Lotto_num = sorted(numbers)
    return Lotto_num

print(getLotto())
'''

#지역변수, 전역변수
''' #x
def caculate_area(radius):
    result = 3.14 * radius**2
    return result

r = float(input("Enter radius of circle: ")) #r은 전역변수
area = caculate_area(r)
print(result)
'''

''' #o
def caculate_area():
    result = 3.14 * r**2
    return result

r = float(input("Enter radius of circle: ")) #r은 전역변수
area = caculate_area()
print(area)
'''



''' #x
def caculate_area(radius):
    area = 3.14 * radius**2
    return 

area = 0
r = float(input("Enter radius of circle: ")) #r은 전역변수
caculate_area(r)
print(area)
'''

''' #o
def caculate_area(radius):
    global area
    area = 3.14 * radius**2
    return 

area = 0
r = float(input("Enter radius of circle: ")) #r은 전역변수
caculate_area(r)
print(area)
'''

#디폴트 인수
'''
def greet(name, msg="how are you?"): #msg에 디폴트 인수를 넣어준 것
    print("Hi! ", name + ', ',msg)

greet("Sam")
'''

#최대값 함수
'''
def getMax(a, b=-10000,c=-10000):
    if (a > b) and (a > c):
        largest = a
    elif (b > a) and (b > c):
        largest = b
    else:
        largest = c
    return largest

print(f"Largerst number of (10,20,50) is {getMax(10,20,50)}")
print(f"Largerst number of (10,20) is {getMax(10,20)}")
print(f"Largerst number of (10) is {getMax(10)}")
'''

#클릭하는 곳에 사각형 그리기
'''
import random
import turtle
t = turtle.Turtle()


def squre(length):
    t.begin_fill()
    for i in range(4):
        t.fd(length)
        t.left(90)

    t.end_fill()


def drawit(x,y):
    t.up()
    t.goto(x,y)
    t.down()
    t.color(random.random(),random.random(),random.random())
    squre(100)

s = turtle.Screen()
s.onclick(drawit)

turtle.done()
'''

#마우스로 그림 그리기
'''
import turtle
t = turtle.Turtle()

def draw(x,y):
    t.goto(x,y)

t.shape("turtle")
t.pensize(10)

s = turtle.Screen()
s.onscreenclick(draw)
s.onkey(t.penup,"Up")
s.onkey(t.pendown,"Down")

s.listen()
'''

#프랙탈 프로그램(순환호출:리커전)
'''
import turtle
def tree(length):
    if length
'''





























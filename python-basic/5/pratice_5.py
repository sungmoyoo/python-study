#elif
'''
num = int(input("Insert Number: "))
if num > 0:
    print("positive")
elif num == 0:
    print("zero")
else:
    print("negative")
'''

#종달쓰
'''
import random
time = random.randint(1,24)
sunny = random.choice([True, False])

print(f"좋은 아침입니다. 현재 시각은 {time}시 입니다.")

if sunny == True:
    print("현재 날씨는 화창합니다")
else:
    print("현재 날씨가 화창하지 않습니다")

if time >= 6 and time <= 9 and sunny:
    print("종달새가 노래를 합니다.")
else:
    print("종달새가 노래를 하지 않습니다.")
'''    

#터틀 도형 그리기
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","Enter type of polygon: ")

if s == "square":
    r = turtle.numinput("","width: ")
    l = turtle.numinput("","height: ")
    
    t.fd(r)
    t.left(90)
    t.fd(l)
    t.left(90)
    t.fd(r)
    t.left(90)
    t.fd(l)

elif s == "triangle":
    l = turtle.numinput("","length: ")

    t.fd(l)
    t.left(120)
    t.fd(l)
    t.left(120)
    t.fd(l)

elif s == "circle":
    p = turtle.numinput("","radius: ")
    t.circle(p)

else:
    pass

turtle.done()
'''

#반복문 기초
'''
sum = 0
for i in [1,2,3,4,5]:
    print(f"Adding {i} on (sum)")
    sum += i
print("result sum: ", sum)
'''

#n각형 그리기
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("","Enter angle: ")

n = int(s)

for i in range(n):
    t.fd(100)
    t.left(360/n)

turtle.done()
'''

#카운트다운 프로그램
'''
import time
import winsound

seconds = int(input("Enter counting number: "))

for i in range(seconds,0,-1):
    print(f"{i} seconds left")
    time.sleep(1)
print("launch")
winsound.Beep(2000,3000)
'''      

#구구단 출력
'''
for i in range(2, 10):
    print("\n")
    print(f"{i} multiplication table")
    for a in range(1,10):
        print(f"{i}*{a}={i*a}")
'''   

#랜덤 터틀
'''
import turtle
import random
t = turtle.Turtle()
t.shape("turtle")

while True: #while 활용
    command = input("Enter command: ")
    angle = random.randint(-180,180)
    length = random.randint(10,100)
    if command == "g":
        t.fd(length)
        t.right(angle)
    else:
        break
turtle.done()

for i in range(30): #for문 활용
    angle = random.randint(-180,180)
    length = random.randint(10,100)

    t.fd(length)
    t.right(angle)


turtle.done()
'''

#팩토리얼
'''
n = int(input("Enter number: "))

fact = 1

for i in range(1, n+1):
    fact = fact * i

print(fact)
'''

#while 로그인
'''
password = ""
while password != "pythonisfun":
    password = input("Enter password: ")
print("login success")
'''

#while counting
'''
count = 1
sum = 0
while count <= 10:
    sum = sum + count
    count += 1
print(sum)
'''

#별
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

i = 0
while i < 5:
    t.fd(150)
    t.right(144)
    i = i + 1

for i in range(5):
    t.fd(150)
    t.right(144)
'''
#숫자 맞추기
'''
import random
guess = 0
count = 0
answer = random.randint(1,100)
a=1
b=99

print("Guess Number (1-99) in 10 times")

while guess != answer:
    guess = int(input("Guess number: "))
    count += 1
    if answer < guess:
        b = guess
        print(f"wrong number,{a}-{b}")  
        
    if answer > guess:
        a = guess
        print(f"wrong number,{a}-{b}")
        
    if count == 10:
        break

if guess == answer:
    print("Congratulation,", "tries: ", count )

else:
    print("You failed, Answer is %d" %(answer))
'''

#산수 문제 발생기
'''
import random
x = random.randint(1,100)
y = random.randint(1,100)

print(x,"+",y,"= ", end = "")
answer = int(input())

if answer == (x+y):
    print("Good job)
'''


























    


#input
'''
x = int(input("Input first number: "))
y = int(input("Input second number: "))

sum = x+y
dif = x-y
mul = x*y
div = x/y

print("x:%d + y:%d = %d" %(x,y,sum))
print("x:%d - y:%d = %d" %(x,y,dif))
print("x:%d * y:%d = %d" %(x,y,mul))
print("x:%d / y:%d = %d" %(x,y,div))


x = input("First  Number : ")
y = input("Second Number : ")

sum1 = int(x)+int(y)
print(sum1)

sum2 = x+y
print(sum2)
'''

# %d, %s, %f
'''
x = 100
y = 200
sum = x + y
print('%d 과 %d 의 합은 %d 입니다' %(x,y,sum))
'''

#turtle cir/변수
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

radius = 50

t.circle(radius)
t.fd(30)
t.circle(radius)
t.fd(30)
t.circle(radius)

turtle.done
'''

#turtle input
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

size = int(input("집의 크기는 얼마로 할까요?"))
t.color("red")
t.begin_fill()
t.left(60)
t.forward(size)
t.right(120)
t.forward(size)
t.right(120)
t.forward(size)
t.end_fill()

t.color("blue")
t.begin_fill()
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.left(90)
t.forward(size)
t.end_fill()

turtle.done()
'''

#turtle 도전문제
'''
import turtle
t = turtle.Turtle()
t.shape("turtle")

t.color("red")
t.begin_fill()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.end_fill()

t.color("blue")
t.begin_fill()
t.right(90)
t.forward(150)
t.left(90)
t.forward(150)
t.left(90)
t.forward(450)
t.left(90)
t.forward(150)
t.left(90)
t.forward(300)
t.end_fill()

t.up()

t.forward(70)
t.left(90)
t.forward(150)
t.down()
t.color("black")
t.begin_fill()
t.circle(50)
t.end_fill()

t.up()
t.left(90)
t.forward(200)
t.right(90)
t.down()
t.color("black")
t.begin_fill()
t.circle(50)
t.end_fill()

turtle.done()
'''

#초단위의 연산자
'''
sec = 1000
min = 1000//60
remainder = 1000%60
print(min, remainder)
'''

#화씨 섭씨 변환
'''
ftemp = int(input("변환할 화씨를 입력하세요: "))
ctemp = (ftemp - 32) * 5/9
print("화씨온도 %d = 섭씨온도 %f" % (ftemp,ctemp))
'''

#n각형 그리기
'''
n = int(input("몇각형을 그리시겠어요?(3-6): "))

import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(n):
    t.forward(100)
    t.left(360//n)

turtle.done()
'''

'''
#자동판매기 시뮬레이션 
cash =  int(input("투입한 돈 :"))
price = 2600
remainder = cash-price
coin500 = remainder//500
coin100 = (remainder%500)//100

print("투입한 돈 :", cash)
print("거스름 돈 :", remainder)
print("500원 동전의 개수 :",coin500)
print("100원 동전의 개수 :",coin100)
'''





































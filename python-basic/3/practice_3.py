'''
import turtle
t = turtle.Turtle()
t.shape("turtle")
'''

#원리금 계산 
'''
money = 1000000
rate = 0.06
n = 5
print(int(money*(1+rate)**n))
'''

#2차 방정식 근 계산하기(ax**2 + b*x + c)
'''
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

r = b**2 - 4*a*c
m = (b**2 - 4*a*c)**0.5

x1 = (((-b) + m)/(2*a))
x2 = (((-b) - m)/(2*a))

print(x1, x2)
'''

#bmi지수
'''
weight = float(input("몸무게 KG 단위로 입력하세요: "))
height = float(input("키를 M단위로 입력하세요: "))

BMI = weight/(height**2)

print("BMI 지수는 %d입니다" %(BMI))
'''

#챗봇
'''
print("안녕하세요")
name = input("이름이 어떻게 되시나요? ")

print("만나서 반갑습니다. %s씨"%(name))
print("이름의 길이는 다음과 같군요:", len(name))

age = int(input("나이는 어떻게 되나요?"))
print("내년이면 %d이 되시는군요"%(age+1))
'''

#f-문자열
'''
product = "coffee"
count = 3
price = 10000
print(f"상품{product} {count}개의 가격은 {count*price}원 입니다")

pi = 3.141592
print(f"원주율={pi:.2f}")
'''

#인덱스
x = input("First Name: ")
y = input("Second Name: ")
z = input("Last Name: ")

initial = x[0] + "." + y[0] + "." + z

print(f"Your initial Name:{initial}")







































      

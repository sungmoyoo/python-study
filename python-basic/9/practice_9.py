#리스트 기초
'''
friends = ['111','222','333','444']
print(friends)

person = ["Hong", 23, 180.9, 70.3]
print(person)

myList = []
myList.append(1)
myList.append('a')
print(myList)

letters = ['a','b','c','d','e','f']
print(letters[0])

numbers = [1,2,3,4,5,6]
print(len(numbers))

s = "hello world!"
print(len(s))

numbers = [1,2,3,4,5,6]
print(6 in numbers)
print(10 in numbers)
print(10 not in numbers)

myList = ['milk','apple','bean','beef']
for item in myList:
    print(item)

for i in range(len(myList)):
    print(myList[i])

myList[1] = 'coffee'
print(myList)

myList.remove('beef')
print(myList)

item = myList.pop(0)
print(item)
print(myList)

myList = ['milk','apple','bean','beef']
i = myList.index('beef')
print(i)

if 'beef' in myList:
    print(myList.index('beef'))

myList = ['milk','apple']
yourList = ['bean','beef']
allList = myList+yourList
print(allList)

print(myList*2)
'''

#리스트로 그래프 그리기1
'''
import matplotlib.pyplot as plt
import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1,10))

plt.plot(numbers)
plt.ylabel('random numbers')
plt.show()
'''

#리스트로 그래프 그리기2
'''
#y = ax2 + bx + c
import matplotlib.pyplot as plt

xlist = []
ylist = []

#계수
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

#x리스트 
for i in range(-100,100):
    xlist.append(i/10)

#y리스트
for x in xlist:
    ylist.append(a*x**2 + b*x + c)

plt.plot(xlist,ylist)
plt.show()
'''

#딕셔너리 기초
'''
dict= {1:1,2:2,3:3} #key값에 숫자형도 가능
print(dict[1])

phone_book = {'a':'1234','b':'1235','c':'1236'}

for key in sorted(phone_book.keys()):
    print(key,phone_book[key])

phone_book.pop('a')
print(phone_book)
'''

#편의점 재고 관리
'''
items = {"coffee": 7, "pen": 3, "cup":2, "milk":1, "coke":4, "book":5}
search = input("Enter name of product: ")
print(items[search])
'''

#영한 사전
'''
english_dict = {}
english_dict["one"] = "하나"
english_dict["two"] = "둘"
english_dict["three"] = "셋"

while True:
    word = input("찾을 단어를 입력하시오: ")
    if word == 'q':
        break
    elif english_dict.get(word) == None:
        print("단어가 없습니다")
    else:    
        print(english_dict[word])
'''

#practice
#1
'''
mylist = []
for i in range(5):
    num = int(input("Enter Number: "))
    mylist.append(num)

s = sum(mylist)

print(s/len(mylist))
'''

#2
'''
import random
count = [0,0,0,0,0,0]
for i in range(1000):
    value = random.randint(0,5)
    count[value] += 1

print("주사위가 1인 경우는 %d번" %(count[0]))
print("주사위가 2인 경우는 %d번" %(count[1]))
print("주사위가 3인 경우는 %d번" %(count[2]))
print("주사위가 4인 경우는 %d번" %(count[3]))
print("주사위가 5인 경우는 %d번" %(count[4]))
print("주사위가 6인 경우는 %d번" %(count[5]))
'''

#3

#tkinter
'''
from tkinter import *
window =Tk()
button = Button(window, text="click")
button.pack()
'''

#버튼,레이블,엔트리 위젯
'''
from tkinter import *

l1 = Label(window, text="화씨")
l1.pack()
e1 = Entry(window)
e1.pack()

l2 = Label(window, text="섭씨")
l2.pack()
e2 = Entry(window)
e2.pack()

b1 = Button(window, text="화씨 -> 섭씨")
b2 = Button(window, text="섭씨 -> 화씨")
b1.pack()
b2.pack()

window.mainloop()
'''

#격자 배치 관리자
'''
from tkinter import *
def process():
    e2.insert(0,"100")

window = Tk()

l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)

e1 = Entry(window)
e2 = Entry(window)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b1 = Button(window, text="화씨 -> 섭씨",command=process)
b2 = Button(window, text="섭씨 -> 화씨")
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)

window.mainloop()
'''

#버튼 이벤트 처리하기
from tkinter import *

def process1():
    temperature = float(e1.get())
    mytemp = (temperature-32)*5/9
    e2.insert(0,str(mytemp))

def process2():
    temperature = float(e2.get())
    mytemp = (temperature*9/5)+32
    e1.insert(0,str(mytemp))

def process3():
    print("hello")
    #e2.insert(0,"100")

window = Tk()

l1 = Label(window, text="화씨",font="helvetica 16 italic")
l2 = Label(window, text="섭씨",font="helvetica 16 italic")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)


e1 = Entry(window,bg="yellow",fg="black")
e2 = Entry(window,bg="yellow",fg="black")
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)


b1 = Button(window, text="°F -> °C",command=process1)
b2 = Button(window, text="°C -> °F",command=process2)
b3 = Button(window, text="ClicK",command=process3)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)
b3.grid(row=2,column=2)

window.mainloop()


#절대 위치 배치 관리자
'''
from tkinter import *

window = Tk()

w = Label(window, text="Box #1", bg="red", fg="white")
w.place(x=0,y=0)
w = Label(window, text="Box #2", bg="green", fg="black")
w.place(x=20,y=20)
w = Label(window, text="Box #3", bg="blue", fg="white")
w.place(x=40,y=40)

window.mainloop()
'''











































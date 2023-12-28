from tkinter import *

window = Tk()  

#사각형 초기 위치값
x1 = 150 
y1 = 100 
x2 = 250  
y2 = 200  

#사각형 이동 함수들
def up():
    global square
    global y1, y2
    canvas.delete(square)  #이전 사각형 삭제
    y1 -= 20  #y 좌표 이동
    y2 -= 20
    square = canvas.create_rectangle(x1, y1, x2, y2, fill="red")  #새로운 사각형 생성

def down():
    global square
    global y1, y2
    canvas.delete(square)  #이전 사각형 삭제
    y1 += 20  #y 좌표 이동
    y2 += 20
    square = canvas.create_rectangle(x1, y1, x2, y2, fill="red")  #새로운 사각형 생성

def left():
    global square
    global x1, x2
    canvas.delete(square)  #이전 사각형 삭제
    x1 -= 20  #x 좌표 이동
    x2 -= 20
    square = canvas.create_rectangle(x1, y1, x2, y2, fill="red")  #새로운 사각형 생성

def right():
    global square
    global x1, x2
    canvas.delete(square)  #이전 사각형 삭제
    x1 += 20  #x 좌표 이동
    x2 += 20
    square = canvas.create_rectangle(x1, y1, x2, y2, fill="red")  #새로운 사각형 생성

#캔버스 생성, 배치, 초기 사각형 생성
canvas = Canvas(window, width=400, height=300, background="white")  
canvas.grid(row=0, column=0, columnspan=4)  
square = canvas.create_rectangle(x1, y1, x2, y2, fill="red")  

#상하좌우 버튼 생성
lb = Button(window, text="<-(left)", command=left)  
rb = Button(window, text="->(right)", command=right)  
ub = Button(window, text="^(up)", command=up)  
db = Button(window, text="v(down)", command=down)  

#버튼 위치 지정
lb.grid(row=1, column=0)  
rb.grid(row=1, column=1)  
ub.grid(row=1, column=2)  
db.grid(row=1, column=3)  

window.mainloop() 
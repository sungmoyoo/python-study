from tkinter import *
window = Tk()

def paint(event):
    #현재 마우스의 현재 위치를 구하여 각 x값, y값에 저장(event.x)
    x1,y1 = (event.x-1),(event.y+1)
    x2,y2 = (event.x-15),(event.y+15)
    canvas.create_oval(x1,y1,x2,y2,fill=mycolor, outline=mycolor) #타원 생성

#색상 변경 함수
def change_red():
    global mycolor
    mycolor = "red"

def change_blue():
    global mycolor
    mycolor = "blue"

#초기 색상 
mycolor = "blue"

#캔버스 생성, 배치
canvas = Canvas(window)
canvas.pack()
#바인드 이벤트 실행,즉 b-motion이 되면, paint 함수 호출
canvas.bind("<B1-Motion>",paint)

#프레임 생성, 배치
frame = Frame(window)
frame.pack(pady=10)

#프레임에 버튼 생성, 배
b1 = Button(frame,text="Red",command=change_red)
b1.pack(side=LEFT, padx=30)
b2 = Button(frame,text="Blue",command=change_blue)
b2.pack(side=LEFT, padx=30)

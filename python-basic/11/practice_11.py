#이미지 표시 프로그램
'''
from tkinter import *
window = Tk()

#이미지를 변경하는 함수
def change_img():
    path = inputBox.get() #입력받은 값 가져오기
    img = PhotoImage(file = path) #파일 불러오기
    imageLabel.configure(image = img) #이미지 수정
    imageLabel.image = img #표시

#초기 이미지 생성, 배치
photo =PhotoImage(file="wl.gif")
imageLabel = Label(window, image=photo)
imageLabel.pack()

#엔트리 생성, 배치
inputBox = Entry(window)
inputBox.pack()

#제출 버튼 생성, 배치
button = Button(window, text='submit', command=change_img)
button.pack()

window.mainloop()
'''


#mypaint1
'''
from tkinter import *
window = Tk()

#그리기 함수
def paint(event):
    x1,y1 = (event.x-1),(event.y+1) #현재 마우스의 현재 위치를 구하여 x1,y1에 저장
    x2,y2 = (event.x+5),(event.y-1) #현재 마우스의 현재 위치를 구하여 x2,y2에 저장
    canvas.create_oval(x1,y1,x2,y2,fill="black") #타원 생성

canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>",paint)

window.mainloop()
'''

#mypaint2
'''
from tkinter import *
window = Tk()

def paint(event):
    x1,y1 = (event.x-1),(event.y+1)
    x2,y2 = (event.x-15),(event.y+15)
    canvas.create_oval(x1,y1,x2,y2,fill=mycolor, outline=mycolor)

def change_red():
    global mycolor
    mycolor = "red"

def change_blue():
    global mycolor
    mycolor = "blue"

mycolor = "blue"

canvas = Canvas(window)
canvas.pack()
canvas.bind("<B1-Motion>",paint)

frame = Frame(window)
frame.pack(pady=10)

b1 = Button(frame,text="Red",command=change_red)
b1.pack(side=LEFT, padx=30)
b2 = Button(frame,text="Blue",command=change_blue)
b2.pack(side=LEFT, padx=30)
'''

#계산기 프로그램
'''
from tkinter import *
window = Tk()

window.title("My Calculator")
display = Entry(window, width=33, bg="yellow")
display.grid(row=0,column=0,columnspan=5)

def click(key):
    if key == "=":
        result = eval(display.get())
        s = str(result)
        display.insert(END,"=" + s)
    elif key == "C":
        display.delete(0,END)
    else:    
        display.insert(END,key)

button_list = [
    '7','8','9','/','C',
    '4','5','6','*',' ',
    '1','2','3','-',' ',
    '0','.','=','+',' ']

row_index = 1
col_index = 0

for button_text in button_list:
    def process(t=button_text):
        click(t)
    Button(window,text=button_text,width=5,command=process).grid(row=row_index,column=col_index)

    col_index += 1
    if col_index > 4:
        row_index += 1
        col_index = 0
'''






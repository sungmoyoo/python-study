from tkinter import *

window = Tk()  

counter = 1  #작업 순번 변수

def add_work():
    global counter
    input_text = entry.get()  #입력된 텍스트 가져오기
    textarea.insert("end", f"[#{counter}]" + input_text + "\n")  #텍스트 영역에 순번과 입력된 텍스트 추가
    entry.delete(0, "end")  #입력 필드 초기화
    counter += 1  #순번 증가

#제목 레이블 생성,배치
title = Label(window, text="할일을 입력하세요")  
title.pack()  

#입력 필드 생성,배치
entry = Entry()  
entry.pack()  

#추가 버튼 생성,배치
input_button = Button(window, text="추가", command=add_work)  
input_button.pack()  

#텍스트 영역 생성,배치
textarea = Text(window, height=5, width=15, font=("Arial", 13)) 
textarea.pack()  

window.mainloop()  
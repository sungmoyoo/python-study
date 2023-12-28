from tkinter import *
import random

answer = random.randint(0, 100)  #0부터 100 사이의 랜덤한 정답 생성

window = Tk()

def process_guess():
    guess = int(e.get())  #입력된 추측 값을 정수로 변환, entry로 입력받은 값은 str타입이기 때문
    if guess == answer:  #정답과 일치하는 경우
        result['text'] = "Correct!"
    elif guess < answer:  #정답보다 작은 경우
        result.config(text="Higher!")
    elif guess > answer:  s#정답보다 큰 경우
        result.config(text="Lower!")

def process_reset():
    global answer
    e.delete(0, "end")  #입력 필드 초기화
    answer = random.randint(0,100)
    result.config(text="")  #결과 레이블 초기화
    
#제목 레이블 생성,배치
l = Label(window, text="Guessing Game")  
l.grid(row=0, column=0, columnspan=2)  

#입력 필드 생성,배치
e = Entry()  
e.grid(row=1, column=0, columnspan=2) 

#guess,reset 버튼 생성, 배치
b1 = Button(window, text="Guess", command=process_guess)  
b2 = Button(window, text="Reset", command=process_reset)  
b1.grid(row=2, column=0)  
b2.grid(row=2, column=1)  

#결과 레이블 생성,배치
result = Label(window, text="")  
result.grid(row=3, column=0, columnspan=2)  

window.mainloop() 

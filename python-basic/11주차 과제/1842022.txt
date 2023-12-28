from tkinter import *
import random

answer = random.randint(0, 100)

window = Tk()

def process_guess():
    global tries
    
    guess = int(In_Value.get())
    
    if guess == answer:
        tries += 1
        Lbl_try['text'] = "시도 횟수: " + str(tries)
        
        Lbl_history['text'] = Lbl_history['text'] + " " +str(guess)
        
        Lbl_result['text'] = "정답입니다!"
        
    elif guess < answer:
        tries += 1
        Lbl_try['text'] = "시도 횟수: " + str(tries)

        Lbl_history['text'] = Lbl_history['text'] + " " +str(guess)
        
        Lbl_result['text'] = "값이 작습니다"
        
    elif guess > answer:
        Lbl_result['text'] = "값이 큽니다"
        tries += 1


        Lbl_history['text'] = Lbl_history['text'] + " " +str(guess)
        
        Lbl_try['text'] = "시도 횟수: " + str(tries)

def process_reset():
    global answer
    In_Value.delete(0, "end")  
    answer = random.randint(0,100) 
    Lbl_result.config(text="")
    Lbl_try.config(text="")
    Lbl_history.config(text="")

Lbl_Msg = Label(window, text="Guessing Number Game",font=(15))  
Lbl_Msg.grid(row=0, column=0, columnspan=2, pady=5)

In_Value = Entry(window,width=15)  
In_Value.grid(row=1, column=0, columnspan=2, pady=5)

Btn_sure = Button(window, text="확인",width=5, command=process_guess)  
Btn_reset = Button(window, text="다시 시작",width=7, command=process_reset)  
Btn_sure.grid(row=2, column=0,pady=5)  
Btn_reset.grid(row=2, column=1,pady=5)  

Lbl_result = Label(window, text="1에서 100사이의 숫자를 맞혀보세요")  
Lbl_result.grid(row=3,column=0,columnspan=2,pady=5)

#시도 횟수
tries = 0
Lbl_try = Label(window,text="시도 횟수: ")
Lbl_try.grid(row=4,column=0)

#입력값 이력
Lbl_history = Label(window,text="입력 내용: ")
Lbl_history.grid(row=5,column=0,pady=5)





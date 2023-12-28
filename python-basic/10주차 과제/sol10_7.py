from tkinter import *
import random

window = Tk()
window.geometry('400x150')

#제목 레이블 생성,배치
title_label = Label(window, text="가위 바위 보 게임", fg="blue") 
title_label.pack()

#프레임 생성, 배치
frame = Frame(window)
frame.pack(pady=10)  #상하 패딩 추가

#가위바위보 선택지리스트를 생성하고 사용자,컴퓨터 점수 초기화
choices = ["rock", "scissors", "paper"]
user_score = 0
computer_score = 0

#메인, 컴퓨터 선택과 플레이어 선택을 비교하는 battle함수로 이어짐
def main_game(choice):
    computer_choice = random.choice(choices) #컴퓨터의 선택값을 choice리스트에서 무작위 선택
    battle(choice, computer_choice) #사용자의 선택과 컴퓨터의 선택 비교하는 함수로 승패 결정

#조건문을 통해 승패를 결정하고 결과 메시지를 출력
def battle(user_choice, computer_choice):
    
    #사용자 점수와 컴퓨터점수를 전역변수로 선언
    global user_score 
    global computer_score
    
    #승/무/패 비교하는 조건문
    if user_choice == computer_choice: #비긴 경우
        result_message.config(text=f"사용자={user_choice}, 컴퓨터={computer_choice} 비겼습니다.", fg="orange")  
    elif (user_choice == "scissors" and computer_choice == "paper") or \
            (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock"): #플레이어가 이긴 경우
        user_score += 1
        result_message.config(text=f"사용자={user_choice}, 컴퓨터={computer_choice} 플레이어 승리!", fg="orange")  
    else: #컴퓨터가 이긴 경우
        computer_score += 1
        result_message.config(text=f"사용자={user_choice}, 컴퓨터={computer_choice} 컴퓨터 승리!", fg="orange")  
    
    update_scores() #점수판 업데이트

#바뀐 점수를 업데이트 하는 함수, config로 텍스트를 변경
def update_scores():
    user_label.config(text=f"사용자 점수: {user_score}")
    computer_label.config(text=f"컴퓨터 점수: {computer_score}")

#바위 선택 버튼
rock_button = Button(frame, text="바위", width=10, command=lambda choice="rock": main_game(choice), bg="orange") 
rock_button.pack(side=LEFT, padx=10)  #좌측 패딩 추가, 간격을 넓히기 위해서

#가위 선택 버튼
scissors_button = Button(frame, text="가위", width=10, command=lambda choice="scissors": main_game(choice), bg="yellow") 
scissors_button.pack(side=LEFT, padx=10)  #좌측 패딩 추가

#보 선택 버튼
paper_button = Button(frame, text="보", width=10, command=lambda choice="paper": main_game(choice), bg="sky blue")
paper_button.pack(side=LEFT)  #좌측 패딩 추가

#유저 점수 레이블 생성,배치
user_label = Label(window, text=f"사용자 점수: {user_score}")
user_label.pack()

#컴퓨터 점수 레이블 생성, 배치
computer_label = Label(window, text=f"컴퓨터 점수: {computer_score}")
computer_label.pack()

#결과메시지 레이블 생성, 배치
result_message = Label(window, text="", fg="orange")  
result_message.pack()

window.mainloop()
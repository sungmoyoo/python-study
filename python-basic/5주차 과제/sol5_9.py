import random

#리스트 활용
winnum = []
usernum = []

for i in range(2): 
    inp = int(input("Enter Lottery number(1 by 1): ")) #반복문을 통해 각 자리 숫자를 하나씩 입력받아 리스트에 젖아
    usernum.append(inp)
    rnd = random.randint(0,9) #0부터 9까지 숫자를 생성하여 winnum에 저장 (2번 반복)
    winnum.append(rnd)

print("winning number is ", winnum) #당첨번호 출력

if winnum[0] == usernum[0] and winnum[1] == usernum[1]: #사용자로부터 입력받은 값의 리스트와 난수로 생성한 값의 리스트가 전부 일치할 경우
    print("Congratulation! you got prize") 
    prizeinfo = input("If you want to know winning amount, please enter yes") #사용자의 입력에 따라 당첨금 출력하는 조건문
    if prizeinfo == "yes": 
        print("The prize money is 1,000,000 won")


elif winnum[0] == usernum[0] or winnum[1] == usernum[1]: #두 값중 하나만 일치한 경우, elif이기 때문에 전부 일치한 경우는 출력되지 않음
    print("Congratulation! you got prize") 
    prizeinfo = input("If you want to know winning amount, please enter yes: ") #위와 동일
    if prizeinfo == "yes":
        print("The prize money is 500,000 won")

else: #아예 당첨되지 않은 경우
    print("your number doesn't match")


#자리수 분리 활용
win = random.randint(0,99) #두자리 수 생성
user_num = int(input("Enter your lottery number: ")) #로또번호 입력

#입력받은 번호와 복권 당첨번호의 자리수 분리
user_digit1 = user_num //10 #10의 자리
user_digit2 = user_num % 10 #1의 자리
win_digit1 = win //10 #10의 자리
win_digit2 = win % 10 #1의 자리

#일치하는 숫자에 따라 prize에 금액을 저장
if user_num == win:
    prize = 1000000
elif user_digit1 == win_digit1 or user_digit2 == win_digit2:
    prize = 500000
else:
    prize = 0

#당첨번호를 출력하고 사용자의 입력에 따라 당첨금액 출력
print("winning number is ", win)
if prize > 0:
    prizeinfo = input("If you want to know winning amount, please enter yes")
    if prizeinfo == "yes": 
        print(f"The prize money is {prize} won")
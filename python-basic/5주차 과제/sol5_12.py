birth =  input("Enter your birth year: ") #출생연도 입력

birth_digit = int(birth[3]) #끝자리 문자열 슬라이싱 하여 정수형으로 변환

#조건과 일치하면 백신 접종이 가능한 요일을 출력
if birth_digit == 0 or birth_digit == 5: 
    print("Monday")

if birth_digit == 1 or birth_digit == 6:
    print("Tuesday")

if birth_digit == 2 or birth_digit == 7:
    print("Wednesday")

if birth_digit == 3 or birth_digit == 8:
    print("Thursday")

if birth_digit == 4 or birth_digit == 9:
    print("Friday")
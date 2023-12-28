#127p 10
import random #임의의 원소를 추출하기 위한 random모듈 임포트
from string import ascii_lowercase #알파벳 소문자 리스트 호출하는 모듈 임포트

list1 = list(ascii_lowercase) #알파벳 소문자를 list1에 저장
list2 = ["0","1","2","3","4","5","6","7","8","9"] #숫자 0~9까지 list2에 저장
plist = list1 + list2 #알파벳 소문자와 한자리 숫자의 리스트를 병합하여 plist에 저장

first = random.choice(plist) #첫번째 패스워드 랜덤 선택
second = random.choice(plist) #두번째 패스워드 랜덤 선택
third = random.choice(plist) #세번째 패스워드 랜덤 선택

password = first + second + third #랜덤 선택된 패스워드 조합

print(password) #결과 출력

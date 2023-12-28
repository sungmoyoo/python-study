number = int(input("Input number: ")) #정수 입력받기

n1 = number % 10 #1의 자리수를 구하기 위해 나머지 연산자 활용 
number = number // 10 # //연산자를 통해 1의 자리수 제거 후 다시 number에 할당

n10 = number % 10 #10의 자리수 구하기, 앞서 1의 자리수가 없어졌기 때문에 1의 자리수가 입력받은 정수값의 10의 자리수임

number = number // 10 #위와 동일한 작업 반복

n100 = number % 10

n1000 = number // 10 # //연산자를 사용하면 1000의 자리수만 남기 때문에 바로 n1000에 저장

n_sum = n1 + n10 + n100 + n1000 #자리수의 합 구하는 식

print("Result :", n_sum) #결과 출력


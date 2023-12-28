#팩토리얼 함수 생성
def factorial(n):
    count = 1 #초기값 설정, 팩토리얼은 항상 1부터 곱함
    for i in range(n+1): #반복문을 통해 n번째 숫자까지 출력하여 곱한 후 count에 저장
        if i > 0: #반복문은 0부터 시작하기 때문에 i>0 조건문을 통해 0 패스
            count = count * i
    return count

n = int(input("Enter number: ")) #값 입력받기

print(f"{n}! =",factorial(n)) #결과 출력
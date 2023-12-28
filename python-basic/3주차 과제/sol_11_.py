import time #time 모듈 임포트

fseconds = time.time() # time.time() :1970년 1월 1일부터 흘러온 초 호출하는 함수(UTC기준)

fminutes = int(fseconds % 3600 //60) #fseconds를 시간(3600)으로 나눈 나머지 초를 분으로 환산

fhours = int(fseconds % 86400 // 3600) #fseconds를 일(86400)으로 나눈 나머지 초를 시로 환산

print(f"Coordinate Universal Time(UTC): {fhours}:{fminutes}") #결과 출력

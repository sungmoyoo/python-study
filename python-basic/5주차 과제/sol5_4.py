score = int(input("Enter your score: ")) #점수 입력


if score >= 90: #90점 이상일 경우
    grade = "A"

elif score >= 80: #80점 이상
    grade = "B"

elif score >= 70: #70점 이상
    grade = "C"

elif score >= 60: #60점 이상
    grade = "D"

else:             #그외
    grade = "F"

#결과 출력
print("Your grade is a(n) {}".format(grade))

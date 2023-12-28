# 성적 입력 함수
def score_input() :
    field = []
    print("-------------------------------")
    print("|        자 료  입 력         |")
    print("_______________________________")
    std_id = input('학번 입력 : ') 
    field.append(std_id)
    std_name = input('이름 입력 : ') 
    field.append(std_name)
    s_attend = int(input('출석 입력 : '))
    field.append(s_attend)
    s_report = int(input('과제 입력 : '))
    field.append(s_report)
    s_mid = int(input('중간 입력 : ')) 
    field.append(s_mid)
    s_last = int(input('기말 입력 : '))
    field.append(s_last)
    return field
    

# 총점계산 함수 : 
def score_process(field) :
    return field[2]+field[3]+field[4]+field[5]

# 평점계산 함수 : 
def score_grade(field) :
    if field[6] >=360 :
        return 'A'
    elif field[6] >=320 :
        return 'B'
    elif field[6] >=280 :
        return 'C'
    elif field[6] >=240 :
        return 'D'
    else:
        return 'F'
    
# 성적 출력 함수 : 
def data_output() :
    print("************************************************************")
    print("학번    이름    출석    과제    중간    기말    총점    평점")
    print("************************************************************")

    for j in range(len(std)):
        for i in range(len(std[j])):
            print(std[j][i],end='\t')
        print()

    print()
    input(" Press any key to continue..... ")
    
def main_menu():
    print("*************************************")
    print("*         메 인     메 뉴           *")
    print("*************************************")
    print()
    print(" 1. 자료 입력")
    print(" 2. 자료 출력")
    print(" 3. 자료 검색")
    print(" 4. 자료 수정")
    print(" 5. 자료 삭제")
    print(" 6. 작업 종료")

def get_job():
    print()
    job_no = int(input(" Select Menu : "))
    return job_no
    

def data_input():
    field = score_input()
    field.append(score_process(field))
    field.append(score_grade(field))
    std.append(field)

def data_search():
    print("-------------------------------")
    print("|        자 료   검 색        |")
    print("_______________________________")
    print()
    std_id = input(" 찾을 학생 학번 : ")
    print("##############################################################")
    print("#학번    이름    출석    과제    중간    기말    총점    평점#")
    print("##############################################################")
    for j in range(len(std)):
        if std_id not in std[j][0]:
                pass
        else:
            for i in range(len(std[j])):
                if std[j][0] == std_id:
                        print(std[j][i],end='\t')
            print()
    
def data_edit():
    print("-------------------------------")
    print("|        자 료   수 정        |")
    print("-------------------------------")
    print()
    std_id = input(" 찾을 학생 학번 : ")
    print("##############################################################")
    print("#학번    이름    출석    과제    중간    기말    총점    평점#")
    print("##############################################################")
    for j in range(len(std)):
        if std_id not in std[j][0]:
                pass
        else:                      
            for i in range(len(std[j])):
                if std[j][0] == std_id:
                        print(std[j][i],end='\t')

            print()
                        
            confirm = input("수정하시겠습니까? (y/n): ")
            if confirm == "y":
                
                edit_info = []
                edit_info.append(std_id)
                rename = input('이름 수정: ')
                edit_info.append(rename)
                rescore_a = int(input('출석 점수 입력: '))
                edit_info.append(rescore_a)
                rescore_r = int(input('과제 점수 입력: '))
                edit_info.append(rescore_r)
                rescore_m = int(input('중간 점수 입력: '))
                edit_info.append(rescore_m)
                rescore_l = int(input('기말 점수 입력: '))
                edit_info.append(rescore_l)
            
                edit_info.append(score_process(edit_info))
                edit_info.append(score_grade(edit_info))
            
                if std[j][0] == std_id:
                    std[j] = edit_info
                

def data_delete():
    print("-------------------------------")
    print("|        자 료   삭 제        |")
    print("-------------------------------")
    print()
    std_id = input(" 찾을 학생 학번 : ")
    for j in range(len(std)):
        if std_id not in std[j][0]:
                pass
        else:                      
            for i in range(len(std[j])):
                if std[j][0] == std_id:
                        print(std[j][i],end='\t')

            print()
                        
            confirm = input("삭제하시겠습니까? (y/n): ")
            if confirm == "y":
                del std[j]

    print()

std = []
work_no = 0

while work_no != 6:
    main_menu()
    work_no = get_job()
    if work_no == 1:
        data_input()
    elif work_no == 2:
        data_output()
    elif work_no == 3:
        data_search()
    elif work_no == 4:
        data_edit()
    elif work_no == 5:
        data_delete()
    elif work_no == 6:
        print("Program End!!!")
        break
        



#성적 입력 함수
def score_input():
    record = []
    print("############################################")
    print("#               자료 입력                  #")
    print("############################################")

    id = input('학번 입력 :')
    record.append(id)
    name = input('이름 입력: ')
    record.append(name)
    score_a = int(input('출석 점수 입력: '))
    record.append(score_a)
    score_r = int(input('과제 점수 입력: '))
    record.append(score_r)
    score_m = int(input('중간 점수 입력: '))
    record.append(score_m)
    score_l = int(input('기말 점수 입력: '))
    record.append(score_l)
    return record

#총점 계산 함수
def score_process(record):
    return record[2]+record[3]+record[4]+record[5]

#평점 계산 함수
def score_grade(record):
    if record[6] >= 90:
        return 'A'
    elif record[6] >= 80:
        return 'B'
    elif record[6] >= 70:
        return 'C'
    elif record[6] >= 60:
        return 'D'
    else:
        return 'F'

#성적 출력 함수
def data_output():
    print("##############################################################")
    print("#학번    이름    출석    과제    중간    기말    총점    평점#")
    print("##############################################################")
    for j in range(len(std)):
        for i in range(len(std[j])):
            print(std[j][i],end='\t')
        print()
                       
    print()
    input("Press any key to continue")

#자료 검색 함수
def data_search():
    search_id = input("검색할 학번 입력: ")
    print("##############################################################")
    print("#학번    이름    출석    과제    중간    기말    총점    평점#")
    print("##############################################################")
    
    for j in range(len(std)):
        if search_id not in std[j][0]:
                pass
        else:
            for i in range(len(std[j])):
                if std[j][0] == search_id:
                        print(std[j][i],end='\t')
        print()
                       
    print()
    input("Press any key to continue")

#자료 수정 함수
def data_edit():
    search_id = input("검색할 학번 입력: ")
    
    for j in range(len(std)):
        if search_id not in std[j][0]:
            print("검색 결과가 없습니다")
        else:
            edit_info = []
            edit_info.append(search_id)
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
            
            if std[j][0] == search_id:
                std[j] = edit_info

            print("수정이 완료되었습니다")
    return std

#자료 삭제 함수
def data_delete():
    search_id = input("검색할 학번 입력: ")
    for j in range(len(std)):
        if search_id not in std[j][0]:
            print("검색 결과가 없습니다")
        else:
            del std[j]
            
    
         
    
 #메인 메뉴
def main_menu():
    print("############################################")
    print("#               메인 메뉴                  #")
    print("############################################")

    print()
    print("1. 자료 입력")
    print("2. 자료 출력")
    print("3. 자료 검색")
    print("4. 자료 수정")
    print("5. 자료 삭제")
    print("6. 작업 종료")

def get_job():
    print()
    job = int(input("Select Menu: "))
    return job

def data_input():
    record = score_input()
    record.append(score_process(record))
    record.append(score_grade(record))
    std.append(record)

std = []
menu_no = 0

while menu_no != 6:
    main_menu()
    menu_no = get_job()
    if menu_no == 1:
        data_input()
    elif menu_no == 2:
        data_output()
    elif menu_no == 3:
        data_search()
    elif menu_no == 4:
        data_edit()
    elif menu_no == 5:
        data_delete()
    
        

#1번 자료 입력 -> data_input()
#2번 자료 출력 -> data_output()
#3번 자료 검색 -> data_search(), ex) 학번:2321000 ==> 결과 or 자료x
#4번 자료 수정 -> data_edit(), ex) 학번:2321000 ==> 이름, 출석, 과제, 중간, 기말
#5번 자료 삭제 -> data_delete() ex) 학번:232100 ==> 출력 후 , 삭제하시겠습니까?
#6번 작업 종료 추가





















    

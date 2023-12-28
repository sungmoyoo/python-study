import turtle
t = turtle.Turtle()
t.shape("turtle")

t.color('red','yellow') #선 색상을 red, 채우기 색상을 yellow로 설정
t.begin_fill()

while True: #무한 루프 반복문
    t.forward(200) 
    t.left(170)

    print(t.pos())      #t.pos():거북이의 위치를 반환하는 함수
    print(abs(t.pos())) #abs(): 절댓값을 반환하는 함수
    
    #결과 출력 시 위치값[t.pos()]과 절댓값[abs(t.pos())]이 다른 이유
    #==> t.pos() 함수는 현재 터틀의 위치를 반환하며, 이 위치는 (x,y) 형태의 튜플로 반환됨. 
    #    abs()함수는 주어진 값의 절댓값을 반환하는 함수인데, 이때 각 원소에 대해 절댓값을 적용하는 것이 아니라
    #    튜플 자체의 절댓값을 적용하기 때문에 해당 튜플의 크기를 반환함. 이 크기는 (x**2 + y**2)**(1/2) 로 계산
    #    따라서, t.pos()함수로 반환된 위치값과 abs(t.pos())로 반환된 값이 완전히 일치하지 않음
    

    if abs(t.pos()) < 1:
        break

t.end_fill()

turtle.done()


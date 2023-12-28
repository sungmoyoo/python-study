import turtle
t= turtle.Turtle()
t.shape("turtle")

#라인 그리는 함수 
def draw_line():
    t.fd(100) 
    t.bk(100)
    
#360/12 = 30, 30씩 회전하며 12번 라인을 그리며 거미줄 모양 작성
for i in range(12):
    draw_line()
    t.lt(30)

turtle.done()


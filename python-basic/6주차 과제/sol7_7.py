import turtle
t= turtle.Turtle()
t.shape("turtle")

#f(x)함수 생성
def f(x):
    y = (x**2 + 1) * 0.01 #x 값에 따른 y값을 f(x)함수로 작성, 값이 많이 커지므로 0.01을 곱하여 그래프 확인

    return y

#그래프 x,y축 작성
t.goto(200,0) 
t.goto(0,0)
t.goto(0,200)
t.goto(0,0)

#0부터 150까지의 (x,y)값을 그래프로 그리기
for x in range(0,150):
    t.color("red")
    t.goto(x, f(x))

turtle.done()
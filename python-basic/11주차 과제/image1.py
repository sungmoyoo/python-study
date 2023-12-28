from tkinter import *
window = Tk()

#이미지를 변경하는 함수
def change_img():
    path = inputBox.get() #입력받은 값 가져오기
    img = PhotoImage(file = path) #파일 불러오기
    imageLabel.configure(image = img) #이미지 수정
    imageLabel.image = img #표시

#초기 이미지 생성, 배치
photo =PhotoImage(file="wl.gif")
imageLabel = Label(window, image=photo)
imageLabel.pack()

#엔트리 생성, 배치
inputBox = Entry(window)
inputBox.pack()

#제출 버튼 생성, 배치
button = Button(window, text='submit', command=change_img)
button.pack()

window.mainloop()

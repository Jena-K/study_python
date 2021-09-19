import tkinter

#창 생성
win = tkinter.Tk()

win.geometry('500x500') # 가로 x 세로 (px)

#타이틀 창 설정
win.title('팀 뽑기!')

#폰트 설정
win.option_add('*font', '맑은고딕 25')

#버튼 생성
btn = tkinter.Button(win, text='Button')

#버튼 크기
btn.config(width=5, height=1)

#버튼 내용
btn.config(text='Hello')

#버튼 기능
def alert():
    print('Button Clicked!')
btn.config(command=alert)

#버튼 배치
btn.pack()

#창 실행
win.mainloop()
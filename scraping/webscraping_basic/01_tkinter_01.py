import tkinter

#창 생성
win = tkinter.Tk()

win.geometry('500x500') # 가로 x 세로 (px)

#타이틀 창 설정
win.title('팀 뽑기!')

#폰트 설정
win.option_add('*font', '맑은고딕 25')

#버튼 생성
btn = tkinter.Button(win, text='버튼')
btn.pack()

#창 실행
win.mainloop()
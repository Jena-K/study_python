import tkinter

def draw():
    #값 가져오기
    data = ent.get()
    #0~3번 문자열 삭제
    ent.delete(0, 3)
    btn.config(text=data)

win = tkinter.Tk()

win.title('Witch one is my team?')
win.geometry('500x500')
win.option_add('*font', '맑은고딕 20')

btn = tkinter.Button(win, text='버튼1')
btn.config(command=draw)
btn.pack()

btn2 = tkinter.Button(win, text='버튼2')
btn2.pack()

ent = tkinter.Entry(win)

def clear(event):
    ent.delete(0, len(ent.get()))

ent.bind('<Button-1>', clear)
ent.pack()
win.mainloop()

'''
#입력 문자 숨기기
ent.config(show='*')

#해당 위치에 문자열 삽입(초기값 설정시에 유용)
ent.insert(0.'temp@temp.com')

#입력창 문자열 삭제(0~3번째문자열 삭제)
ent.delete(0, 3)

#입력창 클릭시 명령
ent.bind('<Button-1>', clear)
'''
import tkinter

win = tkinter.Tk()

def move():
    btn1.pack(side=ent1.get())

win.geometry('500x500')
win.title('Pack')
win.option_add('*Font', '궁서 25')
12
ent1 = tkinter.Entry(win)
ent1.pack(side='top')

btn1 = tkinter.Button(win)
btn1.config(text='button')
btn1.config(command=move)
btn1.pack()

win.mainloop()
'''
##pack
widget.pack(side = top, pady = 20)
widget.pack(side = left, pady = 30)

##grid
widget.grid(column=0, row=2) 

#[2, 0] 위치에서 줄 방향으로 총 2칸이 병합된다
widget.grid(column2, row=0, rowspan=2)

#[0, 2] 위치에서 행 방향으로 총 2칸이 병합된다
widget.grid(column0, row=2, columnspan=2)

##place
#30, 40 위치에 배치
widget.place(x=30, y=40)

#해당 위쳇에 좌측 여백 0.3, 상단 여백 0.4 부여
widget.place(relx=0.3, rely=0.5)
'''
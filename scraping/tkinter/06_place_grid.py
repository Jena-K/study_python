import tkinter

win = tkinter.Tk()



win.geometry('560x500')
win.title('Pack')
win.option_add('*Font', '궁서 25')

col_num = 4
row_num = 3
btn_list = []
for j in range(row_num):
    for i in range(col_num):
        btn =  tkinter.Button(win)
        btn.config(text='({}, {})'.format(i, j))
        btn.grid(column=i, row=j, padx=10, pady=10)
        btn_list.append(btn)

btn = tkinter.Button(win)
btn.config(text='new')
btn.grid(column=3, row=0, rowspan=2)

win.mainloop()

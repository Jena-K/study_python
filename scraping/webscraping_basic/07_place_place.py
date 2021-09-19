import tkinter

win = tkinter.Tk()

win.geometry('560x500')
win.title('place')
win.option_add('*Font', '궁서 25')

xx = 0.5
yy = 0.5

btn = tkinter.Button(win)

btn.config(text='({}, {})'.format(xx, yy))
btn.place(relx=xx, rely=yy)

win.mainloop()

import tkinter
import random
#TK
win = tkinter.Tk()
win.title('AIM_GAME')
win.geometry('700x150')
win.option_add('*Font', '고딕 20')

#Label
lab = tkinter.Label(win)
lab.config(text='Num of Target')
lab.grid(column=0, row=0, padx=20, pady=20)

#Entry
ent = tkinter.Entry(win)
ent.grid(column=1, row=0, padx=20, pady=20)

k = 1
def cc():
    global k
    if k >= num_t:
        btn.destroy()
        lab = tkinter.Label(win)
        lab.config(text='Clear!')
        lab.pack(pady=230)
        return
    btn.destroy()
    k+=1
    ran_btn()

def ran_btn():
    global btn
    btn = tkinter.Button(win)
    btn.config(bg='white', command=cc, text=k, height=1, width=3)
    btn.place(relx=random.random()*0.88, rely=random.random()*0.9)

def btn_f():
    global num_t
    num_t = int(ent.get())
    for wg in win.grid_slaves():
        wg.destroy()
    win.geometry('500x500')
    ran_btn()

btn = tkinter.Button(win)
btn.config(text='Start', command=btn_f)
btn.grid(column=0, row=1, columnspan=2)

win.mainloop()

#pyinstaller --onefile --noconsole 08_aim.py
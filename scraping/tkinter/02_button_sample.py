import tkinter
import random
win = tkinter.Tk()
win.geometry('300x100')
win.title('Witch one is My team?')
win.option_add('*Font', '맑은고딕 20 bold')

def pick():
    team = random.randint(1, 10)
    btn.config(text=team)
    
btn = tkinter.Button(win, text="Draw!")
btn.config(width=5)
btn.config(command=pick)
btn.pack()
win.mainloop()
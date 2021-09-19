import tkinter
from selenium import webdriver


def login():
    url = 'https://logins.daum.net/accounts/signinform.do?url=https%3A%2F%2Fwww.daum.net%2F'
    browser = webdriver.Chrome()
    browser.get(url)

    browser.find_element_by_name('id').send_keys(ent1.get())
    browser.find_element_by_name('pw').send_keys(ent2.get())
    ent1.delete(0, len(ent1.get()))
    ent2.delete(0, len(ent2.get()))
    browser.find_element_by_id('loginBtn').click()

def clear(event):
    if ent1.get() == 'temp@temp.com' :
        ent1.delete(0, len(ent1.get()))

win = tkinter.Tk()

win.title('Witch one is my team?')
win.geometry('600x1000')

lab_lol = tkinter.Label(win)
img = tkinter.PhotoImage(file='C:\\Users\\Jena\\Documents\\vscode\\CodingTest\\study_python\\scraping\\webscraping_basic\\lol_logo.png').subsample(3)
lab_lol.config(image=img)
lab_lol.config(side)
lab_lol.pack()

lab1 = tkinter.Label(win)
lab1.config(text='ID')
lab1.pack()

ent1 = tkinter.Entry(win)
ent1.insert(0, 'temp@temp.com')
ent1.bind('<Button-1>', clear)
ent1.pack()

lab2 = tkinter.Label(win)
lab2.config(text='Password')
lab2.pack()

ent2 = tkinter.Entry(win)
ent2.config(show='*')
ent2.pack()

btn = tkinter.Button(text='Login')
btn.pack()

btn.config(command=login)
win.mainloop()
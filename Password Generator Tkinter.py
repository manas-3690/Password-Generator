from tkinter import *
from tkinter.ttk import Combobox
import random

win = Tk()

def gen():
    global var
    var.set('')
    password = ' '
    length=int(e2.get())
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + lowercase
    mix = '0123456789' + lowercase + uppercase + '!@#$%^&*'

    if cb.get() == 'Low strength':
        for i in range(0,length):
            password = password + random.choice(lowercase)
        var.set(password)

    elif cb.get() == 'Medium strength':
        for i in range(0, length):
            password = password + random.choice(uppercase)
        var.set(password)

    elif cb.get() == 'High strength':
        for i in range(0,length):
            password = password + random.choice(mix)
        var.set(password)



win.title('Password Generator')
win.geometry('600x400')
win.configure(bg='lightblue')

l1 = Label(win, text='Pyhton password generator', font=('arial',28), fg='orange', bg='white')
l1.place(x=60, y=0)

l2 = Label(win, text='Password : ', font=('Arial', 14))
l2.place(x=45,y=90)
var = StringVar("")
e1 = Entry(win, font=('Arial', 14), textvariable=var)
e1.place(x=160, y=90)


l3 = Label(win, text='Length : ', font=("arial", 14))
l3.place(x=45, y=125)
e2 = Entry(win, font=('Arial', 14), width=10)
e2.place(x=160, y=125)


l4 = Label(win, text='Strength : ', font=('Arial', 14))
l4.place(x=45, y=160)
cb = Combobox(win, font=("Arial", 14), width = 15)
cb['values']=('Low strength', 'Medium strength', 'High strength')
cb.current(1)
cb.place(x=160, y= 160)

button = Button(win, text='Generate', font=("arial", 14), fg='red', bg='white', command=gen)
button.place(x=160, y=200)



win.mainloop()
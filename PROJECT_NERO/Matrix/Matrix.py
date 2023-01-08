from tkinter import *
import random
t = Tk()
t.geometry('1924x1086--10+-33')
t.resizable(width=False, height=False)
c = Canvas(t, width=1920, height=1080, bg='black')
c.pack()
a = '01'
h = 0
while True:
    c.delete('t' + str(h))
    for i in range(1, 102):
        r = random.randint(0, 1)
        ct = c.create_text(18.9 * i, h, text=str(a[r]), fill='red', font=('Comic Sans MS', 10), tag='t' + str(h))
        rdm = random.randint(1, 40)
        for j in range(10):
            c.move(ct, 0, rdm)
        c.update()
        h += 15
        if h >= 650:
            h = 0
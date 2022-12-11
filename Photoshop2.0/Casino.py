from tkinter import *
import tkinter.messagebox as box
from random import *

#===================================================
window = Tk()
window.title('Игровой Автомат')
window.geometry('190x110')

#===================================================
frame = Frame(window, bg = 'blue', height = 30, width = 30)
frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 3)

#==================================================
slots1 = ''
slots2 = ''
slots3 = ''

#==================================================
def dialog():
    var = box.askyesno('Message Box', 'Вы готовы к Победе?')
    if var == 1:
        box.showinfo('Yes Box', 'Крутим Барабан!!!')
        slots1 = randint(1,9)
        entry1.insert(0, ' ' + str(slots1))
        slots2 = randint(1,9)
        entry2.insert(0, ' ' + str(slots2))
        slots3 = randint(1,9)
        entry3.insert(0, ' ' + str(slots3))
    else:
        box.showerror ('Попробуйте ещё Раз!', "Проигрыш(((")

    if slots1 == slots2 == slots3:
        box.showinfo("Вы Победили!!!","Победа!!!")
    else:
        box.showinfo ('Попробуйте ещё Раз!',"Проигрыш(((")
#====================================================
btn = Button (frame, text='Старт!', bd = 5, height = 2, width = 21, command=dialog)
btn.grid(row = 1, column = 0, columnspan = 4)

#====================================================
entry1 = Entry(frame, font = 'Arial 36', bg = 'yellow', bd = 5, width = 2)
entry2 = Entry(frame, font = 'Arial 36', bg = 'yellow', bd = 5, width = 2)
entry3 = Entry(frame, font = 'Arial 36', bg = 'yellow', bd = 5, width = 2)

#======================================================
entry1.grid(row = 0, column = 1)
entry2.grid(row = 0, column = 2)
entry3.grid(row = 0, column = 3)

#======================================================
window.mainloop()
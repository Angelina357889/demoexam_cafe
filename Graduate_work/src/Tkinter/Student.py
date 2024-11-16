from tkinter import *

from src.Controllers.UsersControllers import UsersControllers

def edit_s():
    users = UsersControllers()
    users.input(3, 1)
def edit_r():
    users = UsersControllers()
    users.input_r(3, 2)




window = Tk() # вызываем класс Tkiner
window.title('Информационная система "Заявления и справки"')# создаем название окна
window.geometry('800x600')

title = Label(window, text='Информационная система "Заявления и справки" для Студента', font=('Times New Roman', 16 ), anchor='center')
title.grid(column = 0 , row = 0, columnspan = 12,padx = 100) # координаты текста в окне

title = Label(window, text='Выбирите необходимую категорию:', font=('Times New Roman', 14 ))
title.grid(column = 0, row = 2, padx =1, pady = 10) # координаты текста в окне

button_login = Button(window,text='Заявления',
                      height= 4,
                      width=16,
                      background = 'blue',
                      foreground='white',
                      command=edit_s)
button_login.grid(column = 0, row = 3, padx =100, pady = 0)

button_login = Button(window,text='Справки',
                      height= 4,
                      width=16,
                      background = 'blue',
                      foreground='white',
                      command=edit_r)
button_login.grid(column = 1, row = 3, padx =100, pady = 10)

















window.mainloop()# запускаем окно
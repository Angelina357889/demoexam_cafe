from tkinter import *

from src.Controllers.UsersControllers import UsersControllers


#Функция авторизации
def login():
    users = UsersControllers()
    result = users.log_in(log_in.get(),passwd_in.get())

    if result:
        log = UsersControllers.show(log_in.get()).role_id.id
        if log == 1:
            print('Админ')
        elif log == 2:
            print('Сотрудник')
        elif log == 3:
            print('Студент')
        elif log == 4:
            print('Укажите логин или пароль')
    else:
        print('Логин или пароль введени не верно')

def login_a():
    users = UsersControllers()
    result = users.log_in(log_in.get(),passwd_in.get())
    if result:
       print('Абитуриент')

    else:
        print('Логин или пароль введени не верно')

#окна ввода данных

#оформление окна
window = Tk() # вызываем класс Tkiner
window.title('Информационная система "Заявления и справки"')# создаем название окна
window.geometry('800x600')

title = Label(window, text='Привествуем в информационной системе "Заявления и справки"', font=('Times New Roman', 16 ))
title.grid(column = 1, row = 0) # координаты текста в окне

button_login = Button(window,text='Войти',
                      height= 2,
                      width=8,
                      background = 'green',
                      foreground='white',
                      command=login)
button_login.grid(column = 1 , row =7)
utton_login = Button(window,text='Войти как абитуриент',height= 2,
                      width=20,
                      background = 'blue',
                      foreground='white',
                      command=login_a)
utton_login.grid(column = 1 , row =9)


log_title = Label(window, text='Введите логин')
log_title.grid(column= 0, row = 5)
log_in = Entry(window, width=20)
log_in.grid(column =1, row= 5)

passwd_title = Label(window, text='Введите пароль')
passwd_title.grid(column= 0, row = 6)
passwd_in = Entry(window, width=20)
passwd_in.grid(column= 1, row = 6)






window.mainloop()# запускаем окно
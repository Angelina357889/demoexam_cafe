#окно авторизации с помошью библотеки Tkiner
from tkinter import *

from src.Controllers.UsersController import UsersControllers
from src.Models.Users import Users


#функционал
def click_test():
    button_login.configure(text= 'Нажал')
    message.configure(text=log_in.get(), font = (16), foreground='red')
    log_in.select_clear()
#Функция авторизации
def login():
    users = UsersControllers()
    result = users.log_in(log_in.get(),passwd_in.get())
    if result:
        log = UsersControllers.show(log_in.get()).role_id.id
        if log == 1:
            print('Админ')
        elif log == 2:
            print('Повар')
        else:
            print('Официант')
    else:
        print('Логин или пароль введени не верно')
    print(result)
#окна ввода данных

#оформление окна
window = Tk() # вызываем класс Tkiner
window.title('Информационная система КАФЕ')# создаем название окна
window.geometry('800x600')

title = Label(window, text="Привествуем в информационной системе КАФЕ", font=('Times New Roman', 16 ))
title.grid(column = 0, row = 0) # координаты текста в окне

button_login = Button(window,text='Войти',height= 2,width=8,background = 'green', foreground='white', command=login)
button_login.grid(column = 0, row =2)
message = Label(text='!!!!!!!!')
message.grid(column= 0, row = 3)

log_title = Label(window, text='Введите логин')
log_title.grid(column= 0, row = 4)
log_in = Entry(window, width=20)
log_in.grid(column = 1, row= 4)

passwd_title = Label(window, text='Введите пароль')
passwd_title.grid(column= 0, row = 5)
passwd_in = Entry(window, width=30)
passwd_in.grid(column= 0, row = 5)






window.mainloop()# запускаем окно
from tkinter import *


def click_test():
    button_adopted.configure(text='Оплачен', background = 'green')













window_W = Tk()
window_W.title('Панель официанта')
window_W.geometry('800x600')

title_W = Label(window_W, text= 'Панель официанта', font=('Times New Roman', 16 ))
title_W.grid(column = 0, row = 0)

Title_W = Label(window_W, text= 'Список заказов', font=('Times New Roman', 15 ))
Title_W.grid(column = 0, row = 1)

# button_login_w = Button(window_W, )

button_adopted = Button(window_W,text='Принят',
                      height= 2,
                      width=8,
                      background = 'red',
                      foreground='white',
                      command=click_test)
button_adopted.grid(column = 9, row =5)
message = Label(text='')
message.grid(column= 0, row = 4)

table_title = Label(window_W, text='Столик')
table_title.grid(column= 0, row = 5)


guests_title = Label(window_W, text='Количество гостей')
guests_title.grid(column= 1, row = 5)

dishes_title = Label(window_W, text='Блюда')
dishes_title.grid(column= 3, row = 5)

drink_title = Label(window_W, text='Напиток')
drink_title.grid(column= 5, row = 5)

readiness_title = Label(window_W, text='Готовность')
readiness_title.grid(column= 7, row = 5)



window_W.mainloop()# запускаем окно
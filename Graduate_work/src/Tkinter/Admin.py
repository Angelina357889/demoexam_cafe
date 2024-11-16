from tkinter import *

window = Tk() # вызываем класс Tkiner
window.title('Информационная система "Заявления и справки"')# создаем название окна
window.geometry('800x600')

title = Label(window, text='Панель Администратора', font=('Times New Roman', 16 ), anchor='center')
title.grid(column = 0 , row = 0, columnspan = 12,padx = 315) # координаты текста в окне






window.mainloop()# запускаем окно
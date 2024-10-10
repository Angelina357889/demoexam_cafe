from tkinter import *
from src.Controllers.UsersController import *


def dialog_window_update_status(id_login):
    dialog_window = Tk()
    dialog_window.title('Потверждение увольнения')
    dialog_window.geometry('250x250')
panel_admin = Tk()
panel_admin.geometry('1660x800')
panel_admin.title('Панель администратор')

title_window = Label(panel_admin, text='Панель Администратора',
                     font=('Times New Roman',24),
                     anchor='center')
title_window.grid(column = 0, row = 0, columnspan = 12, padx = 650, pady = 10)

# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
title_employee = Label(panel_admin, text='Сотрудники', font=(18))
title_employee.grid(column = 1, row = 1, padx = 10, pady = 10)

user = UsersControllers()

list_users = user.get()
count_row = 2
for row in list_users:
    login_title = Label(panel_admin, text= row.name)
    login_title.grid(column = 0, row = count_row, padx = 1, pady = 1)
    login_role = Label(panel_admin, text=row.role_id.role)
    login_role.grid(column = 1, row = count_row, padx = 0, pady = 1)
    button_login = Button(panel_admin,
                          text='Уволить',
                          height=2,
                          width=8,
                          background='red',
                          foreground='white')
                          # command= dialog_window_update_status(row.id)
    status_title = Label()
    button_login.grid(column = 2, row = count_row, padx = 0, pady = 1)



    count_row +=1
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
title_employee = Label(panel_admin, text='Список заказов', font=(18))
title_employee.grid(column = 4,  row =1, padx = 10, pady = 10)

user = UsersControllers()

list_users = user.get()
count_row = 2
for row in list_users:
    login_title = Label(panel_admin, text= row.name)
    login_title.grid(column = 3, row = count_row, padx = 1, pady = 1)
    login_role = Label(panel_admin, text=row.role_id.role)
    login_role.grid(column = 4, row = count_row, padx = 0, pady = 1)
    button_login = Button(panel_admin,
                          text='Уволить',
                          height=2,
                          width=8,
                          background='red',
                          foreground='white')
                          # command= dialog_window_update_status(row.id)
    status_title = Label()
    button_login.grid(column = 5, row = count_row, padx = 0, pady = 1)



    count_row +=1




panel_admin.mainloop()
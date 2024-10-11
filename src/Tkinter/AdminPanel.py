from tkinter import *
from src.Controllers.OrdersControllr import *
from src.Controllers.UsersController import *

def admin():
    def add_users(login,name,password,role):
        user.add(login,name,password,role)
        panel_admin.after(100,update)

    def update():
        panel_admin.destroy()
        admin()

    def status_false(id):
        button_login.configure(text='Уволен', background='grey')
        user.update_status(id)
        update()

    # def dialog_window_update_status(id_login):
    #     dialog_window = Tk()
    #     dialog_window.title('Потверждение увольнения')
    #     dialog_window.geometry('250x250')
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
    count_row = 3
    for row in list_users:
        if row.status:
            login_title = Label(panel_admin, text="Имя", background='green')
            login_title.grid(column=0, row=2, padx=1, pady=1)
            login_title = Label(panel_admin, text= row.name)
            login_title.grid(column = 0, row = count_row, padx = 1, pady = 1)
            login_title = Label(panel_admin, text="Должность", background='green')
            login_title.grid(column=1, row=2, padx=1, pady=1)
            login_role = Label(panel_admin, text=row.role_id.role)
            login_role.grid(column = 1, row = count_row, padx = 0, pady = 1)
            login_title = Label(panel_admin, text="Статус", background='green')
            login_title.grid(column=2, row=2, padx=1, pady=1)
            button_login = Button(panel_admin,
                              text='Уволить',
                              height=2,
                              width=8,
                              background='red',
                              foreground='white',
                              command= lambda id = row.id: status_false(id))
            status_title = Label()
            button_login.grid(column = 2, row = count_row, padx = 0, pady = 1)

            count_row +=1

    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    title_employee = Label(panel_admin, text='Список заказов', font=(18))
    title_employee.grid(column = 4,  row =1, padx = 10, pady = 10)

    orders = OrdersController()

    list_orders = orders.get()
    count_row1 = 3
    for row in list_orders:
        login_title = Label(panel_admin, text="Столик", background='green')
        login_title.grid(column=3, row=2, padx=1, pady=1)
        login_table_id = Label(panel_admin, text= row.table_id.number)
        login_table_id.grid(column = 3, row = count_row1, padx = 1, pady = 1)
        login_title = Label(panel_admin, text="Количество клиентов", background='green')
        login_title.grid(column=4, row=2, padx=1, pady=1)
        login_count_cliens = Label(panel_admin, text=row.count_cliens)
        login_count_cliens.grid(column = 4, row = count_row1, padx = 0, pady = 1)
        login_title = Label(panel_admin, text="Блюдо", background='green')
        login_title.grid(column=5, row=2, padx=1, pady=1)
        login_food_id = Label(panel_admin, text=row.food_id.name)
        login_food_id.grid(column=5, row=count_row1, padx=0, pady=1)

        status_title = Label()

        count_row1 +=1

    #Добавить пользователя
    input_login = Entry(panel_admin,width=20)
    name_input_login = Label(panel_admin, text="Введите логин")
    name_input_login.grid(column = 8, row = 2)
    input_login.grid(column = 8, row = 3)

    input_name = Entry(panel_admin,width=20)
    name_input_name = Label(panel_admin, text="Введите имя")
    name_input_name.grid(column = 8, row = 4)
    input_name.grid(column = 8, row = 5)

    input_password = Entry(panel_admin,width=20)
    name_input_password = Label(panel_admin, text="Введите пароль")
    name_input_password.grid(column = 8, row = 6)
    input_password.grid(column = 8, row = 7)

    input_role = Entry(panel_admin,width=20)
    name_input_role = Label(panel_admin, text="Введите Должность")
    name_input_role.grid(column = 8, row = 8)
    input_role.grid(column = 8, row = 9)


    button_add_users = Button(panel_admin, text='Добавить пользователя',height=2,width=20,background='green',
                              foreground='white',
                              command=lambda: add_users(input_login.get(),input_name.get(),
                                                        input_password.get(),input_role.get()))
    button_add_users.grid(column = 8, row = 10)

    panel_admin.mainloop()
if __name__ == '__main__':
    admin()
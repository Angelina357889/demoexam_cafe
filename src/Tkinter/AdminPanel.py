from tkinter import *
from tkinter import ttk

from src.Controllers.OrdersControllr import *
from src.Controllers.ShiftsController import ShiftsControllers
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

    def add_shift(data, cook, oficiant1, oficiant2):
        print(data, cook, oficiant1, oficiant2)




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



        count_row1 +=1

    #Добавить пользователя
    name_input_add = Label(panel_admin, text="Добавить пользователя", font=(18))
    name_input_add.grid(column = 6,  row =1, padx = 10, pady = 10)
    input_login = Entry(panel_admin,width=20)
    name_input_login = Label(panel_admin, text="Введите логин")
    name_input_login.grid(column = 6, row = 2)
    input_login.grid(column = 6, row = 3)

    input_name = Entry(panel_admin,width=20)
    name_input_name = Label(panel_admin, text="Введите имя")
    name_input_name.grid(column = 6, row = 4)
    input_name.grid(column = 6, row = 5)

    input_password = Entry(panel_admin,width=20)
    name_input_password = Label(panel_admin, text="Введите пароль")
    name_input_password.grid(column =6, row = 6)
    input_password.grid(column = 6, row = 7)

    input_role = Entry(panel_admin,width=20)
    name_input_role = Label(panel_admin, text="Введите должность")
    name_input_role.grid(column = 6, row = 8)
    input_role.grid(column = 6, row = 9)


    button_add_users = Button(panel_admin, text='Добавить пользователя',height=2,width=20,background='green',
                              foreground='white',
                              command=lambda: add_users(input_login.get(),input_name.get(),
                                                        input_password.get(),input_role.get()))
    button_add_users.grid(column = 6, row = 10)

    # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    title_employee = Label(panel_admin, text='Список смен', font=(18))
    title_employee.grid(column=8, row=1, padx=10, pady=10)

    shif = ShiftsControllers()

    list_shif = shif.get()
    count_row1 = 3
    for row in list_shif:
        title = Label(panel_admin, text="Номер смены", background='green')
        title.grid(column=7, row=2, padx=1, pady=1)
        id = Label(panel_admin, text=row.date)
        id.grid(column=7, row=count_row1, padx=1, pady=1)
        title_p = Label(panel_admin, text="Повар", background='green')
        title_p.grid(column=8, row=2, padx=1, pady=1)
        cook_id = Label(panel_admin, text=row.cook_id.name)
        cook_id.grid(column=8, row=count_row1, padx=0, pady=1)
        login_title = Label(panel_admin, text="Официант", background='green')
        login_title.grid(column=9, row=2, padx=1, pady=1)
        oficiant_1_id = Label(panel_admin, text=row.oficiant_1_id.name)
        oficiant_1_id.grid(column=9, row=count_row1, padx=0, pady=1)
        title_o = Label(panel_admin, text="Официант", background='green')
        title_o.grid(column=10, row=2, padx=1, pady=1)
        oficiant_2_id = Label(panel_admin, text=row.oficiant_2_id.name)
        oficiant_2_id.grid(column=10, row=count_row1, padx=0, pady=1)


        count_row1 += 1

    title_cook = Label(panel_admin, text='Выберите повара')
    title_cook.grid(column = 11, row = 2)

    list_cook = UsersControllers.list_users(2)

    combobox_cook = ttk.Combobox(values=list_cook)
    combobox_cook.grid(column = 11, row = 3)

    date_input = combobox_cook.get()
    cook_input = combobox_cook.get()
    oficiant1_input = combobox_cook.get()
    oficiant2_input = combobox_cook.get()

    add_shift_button = Button(panel_admin, text='Добавить смену',
                              height=2,
                              width=20,
                              background='blue',
                              foreground='white',
                              command= lambda : add_shift(date_input, cook_input, oficiant1_input, oficiant2_input))
    add_shift_button.grid(column = 11, row = 7)


















    panel_admin.mainloop()
if __name__ == '__main__':
    admin()
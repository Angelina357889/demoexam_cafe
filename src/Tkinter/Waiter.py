from tkinter import *

from src.Controllers.OrdersControllr import OrdersController


def waiter():


    def update():
        window_W.destroy()
        waiter()


    def status_false(order_id):
        button_adopted.configure(text='Оплачен', background='grey')
        waiter.update_order_pay(order_id)
        window_W.after(100,update)




    window_W = Tk()
    window_W.title('Панель официанта')
    window_W.geometry('800x600')

    title_W = Label(window_W, text= 'Панель официанта', font=('Times New Roman',24),
                             anchor='center')
    title_W.grid(column = 0, row = 0, columnspan = 12, padx = 260, pady = 10)

    Title_W = Label(window_W, text= 'Список заказов', font=('Times New Roman', 15 ))
    Title_W.grid(column =3, row = 1, padx = 10, pady = 10)

    # button_login_w = Button(window_W, )










    waiter = OrdersController()

    list_users = waiter.get()
    count_row = 6


    for row in list_users:
        if row.status_id:
            table_title = Label(window_W, text='Столик')
            table_title.grid(column= 0, row = 5)
            login_title = Label(window_W, text= row.table_id.number)
            login_title.grid(column = 0, row = count_row, padx = 1, pady = 1)

            guests_title = Label(window_W, text='Количество гостей')
            guests_title.grid(column= 1, row = 5)
            login_count_cliens = Label(window_W, text=row.count_cliens)
            login_count_cliens.grid(column = 1, row = count_row, padx = 0, pady = 1)

            dishes_title = Label(window_W, text='Блюда')
            dishes_title.grid(column= 2, row = 5)
            login_food_id = Label(window_W, text=row.food_id.name)
            login_food_id.grid(column=2, row=count_row, padx=0, pady=1)

            drink_title = Label(window_W, text='Напиток')
            drink_title.grid(column= 3, row = 5)
            login_food_id = Label(window_W, text=row.drink_id.name)
            login_food_id.grid(column=3, row=count_row, padx=0, pady=1)

            readiness_title = Label(window_W, text='Готовность')
            readiness_title.grid(column= 4, row = 5)
            login_food_id = Label(window_W, text=row.status_id.name)
            login_food_id.grid(column=4, row=count_row, padx=0, pady=1)

            button_adopted = Button(window_W,text='Принят',
                                  height= 2,
                                  width=8,
                                  background = 'green',
                                  foreground='white',
                                  command= lambda id = row.id: status_false(id))
            button_adopted.grid(column = 5, row =count_row, padx=0, pady=1)

            count_row +=1










    window_W.mainloop()# запускаем окно

if __name__ == '__main__':
    waiter()
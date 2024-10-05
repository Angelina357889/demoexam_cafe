from src.Models.Orders import *


class OrdersController():
    @classmethod
    def get(cls):
        return Orders.select()

    @classmethod
    def add(self, count_cliens, table_id, drink_id, food_id, shift_id):
        Orders.create(count_cliens = count_cliens, table_id = table_id, drink_id = drink_id, food_id = food_id, shift_id = shift_id, status_id = 1)

    @classmethod
    def show(cls, shift_id):
        return Orders.select().where(Orders.shift_id ==shift_id)


    @classmethod
    def update_order_ready(cls,order_id):
        Orders.update({Orders.status_id: 4}).where(Orders.id == order_id).execute()


    @classmethod
    def update_order_pay(cls, orders_id):
        Orders.update({Orders.status_id: 2}).where(Orders.id == orders_id).execute()


    def update_status(self, orders_id):
        Orders.update({Orders.status_id : 3}).where(Orders.id == orders_id).execute()

if __name__ == '__main__':
    orde = OrdersController()
    for row in orde.get():
        print(row.id, row.count_cliens, row.table_id.number, row.drink_id.name, row.food_id.name, row.shift_id.id, row.status_id.name)
    print('------------------------------------------------')
    for row in orde.show(2):
        print(row.id, row.count_cliens, row.table_id.number, row.drink_id.name, row.food_id.name, row.shift_id.id, row.status_id.name)
    print('------------------------------------------------')
    for row in orde.get():
        print(row.id, row.count_cliens, row.table_id.number, row.drink_id.name, row.food_id.name, row.shift_id.id, row.status_id.name)

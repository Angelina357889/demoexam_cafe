from src.Models.Shifts import *
from src.Controllers.UsersController import UsersControllers

class ShiftsControllers():
    def add(self, datatime, cook, oficiant_1, oficiant_2):
        cook_id = UsersControllers.show(cook)
        oficiant_1_id = UsersControllers.show(oficiant_1)
        oficiant_2_id = UsersControllers.show(oficiant_2)

        Shifts.create(datatime = datatime, cook_id =cook_id.id, oficiant_1_id = oficiant_1_id.id, oficiant_2_id= oficiant_2_id.id)

    def get(self):
        return Shifts.select()



if __name__ == '__main__':
    shift = ShiftsControllers()

    #shift.add('2024-10-04 10:00:00', 'cook_Alexandr', 'waiter_Sergey', 'waiter_Ilya')

    for row in shift.get():
        print(row.id, row.cook_id.login, row.oficiant_1_id.login, row.oficiant_2_id.login)
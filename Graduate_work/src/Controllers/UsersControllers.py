from src.Models.Users import *

class UsersControllers():

    def log_in(self, input_login, input_password):
        if Users.get_or_none(Users.login == input_login, Users.password == input_password):
            return True
        else:
            return False

    def get(self):
        return Users.select().execute()

    def add(self, input_password, input_login, input_name, input_role_id, input_address, input_phone):
        Users.create(login = input_login, password = input_password, name = input_name, role_id = input_role_id, address = input_address,phone=input_phone)


    @classmethod
    def show(cls, login):
        return Users.get(Users.login==login)

    @classmethod
    def show_users(cls, role_id):
        return Users.select().where(Users.role_id == role_id)

    @classmethod
    def list_users(cls,role_id):
        list = []
        for users in UsersControllers.show_users(role_id):
            list.append(users.name)
        return list

if __name__ == '__main__':
    use = UsersControllers()

    for row in use.get():
        print(row.login, row.password)
    use.log_in('3','3')
    # for row in use.get():
    #     print(row.login, row.password)
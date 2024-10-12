from src.Models.Users import *

class UsersControllers():
    def log_in(self, input_login, input_password):
        if Users.get_or_none(Users.login == input_login, Users.password == input_password):
            return True
        else:
            return False

    def get(self):
        return Users.select().execute()

    def add(self, input_password, input_login, input_name, input_role_id):
        Users.create(login = input_login, password = input_password, name = input_name, role_id = input_role_id)

    def update_status(self, id_users):
        Users.update({Users.status : False}).where(Users.id == id_users).execute()

    def update_statys_true(self):
        Users.update({Users.status: True}).execute()
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

    #print(use.log_in('z','z'))
    for row in use.get():
        print(row.login, row.password)
    use.update_statys_true()
    # use.add('Ivan', '1234', 'Ivanov', 1)
    for row in use.get():
        print(row.login, row.password)
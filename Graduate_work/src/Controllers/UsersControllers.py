from src.Models.Document_type import Document_type
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
    def input(cls, role_id,document_type):
        if role_id == 2:  # Check if the role is 'staff'
            if Document_type.document_type == document_type:
                print('вывод заявлений для сотрудника')  # Output for staff
        elif role_id == 3:  # Check if the role is 'student'
            if Document_type.document_type == document_type:
                print('вывод заявлений для студента')  # Output for student
        elif role_id == 4:  # Check if the role is 'applicant'
            if Document_type.document_type == document_type:
                print('вывод заявлений для абитуриента')

    @classmethod
    def input_r(cls, role_id, document_type):
        if role_id == 2:  # Check if the role is 'staff'
            if Document_type.document_type == document_type:
                print('вывод справок для сотрудника')  # Output for staff
        elif role_id == 3:  # Check if the role is 'student'
            if Document_type.document_type == document_type:
                print('вывод справок для студента')  # Output for student
        elif role_id == 4:  # Check if the role is 'applicant'
            if Document_type.document_type == document_type:
                print('вывод справок для абитуриента')

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
    use.show_users('2')
    # for row in use.get():show_users
    #     print(row.login, row.password)
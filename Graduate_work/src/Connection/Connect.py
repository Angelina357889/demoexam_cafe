from peewee import *

connect = MySQLDatabase('PudA1234_graduate',
                         user = 'PudA1234_grad',
                         password='111111',
                         host='10.11.13.118',
                         port = 3306)


if __name__ == '__main__':
    print(connect.connect())
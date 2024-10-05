from peewee import *

connect = MySQLDatabase('PudA1234_cafe_demo',
                         user = 'PudA1234_AdmCafe',
                         password='111',
                         host='10.11.13.118',
                         port = 3306)


if __name__ == '__main__':
    print(connect.connect())
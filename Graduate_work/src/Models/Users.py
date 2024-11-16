from src.Models.Roles import *

class Users(Base):
    id = PrimaryKeyField()
    login = CharField()
    password =CharField()
    name = CharField()
    address = CharField()
    phone = CharField()
    role_id = ForeignKeyField(Roles)

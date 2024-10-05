from src.Models.Roles import *

class Users(Base):
    id = PrimaryKeyField()
    login = CharField()
    password =CharField()
    name = CharField()
    role_id = ForeignKeyField(Roles)
    status = BooleanField(default=1)
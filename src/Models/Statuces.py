from src.Models.Base import *

class Status(Base):
    id = PrimaryKeyField()
    name = CharField()

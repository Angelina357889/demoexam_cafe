from src.Models.Users import *
from src.Models.Statements import *

class Document(Base):
    id = PrimaryKeyField()
    date = DateField()
    user_id = ForeignKeyField(Users)
    statement_id = ForeignKeyField(Statements)

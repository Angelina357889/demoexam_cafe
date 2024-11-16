from src.Models.Document_type import *

class Statements(Base):
    id = PrimaryKeyField()
    name = CharField()
    sample = CharField()
    document_type = ForeignKeyField(Document_type)
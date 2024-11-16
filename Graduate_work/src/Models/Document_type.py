from src.Models.Base import *

class Document_type(Base):
    id = PrimaryKeyField()
    document_type = CharField()